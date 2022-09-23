from aqt.qt import (
	Qt,
	QComboBox,
	QTreeView,
	QStandardItem,
	QAbstractScrollArea,
	QHeaderView,
	QSizePolicy,
	QProxyStyle,
	QStyle
)

from anki.hooks import wrap
from anki.utils import ids2str
from anki.collection import _Collection
from anki.stats import CollectionStats
from aqt.stats import DeckStats
from aqt.forms.stats import Ui_Dialog


class TreeComboBox(QComboBox):
	def __init__(self, parent=None):
		super().__init__(parent)

		view = QTreeView()
		self.setView(view)
		view.setHeaderHidden(True)
		view.setRootIsDecorated(False)
		view.setItemsExpandable(False)
		view.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
		view.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
		header = view.header()
		header.setStretchLastSection(False)
		header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

	def sizeHint(self):
		view_size = self.view().sizeHint()
		view_size.setHeight(0)
		return super().sizeHint().expandedTo(view_size)


class HideBranchStyle(QProxyStyle):
	def drawPrimitive(self, element, option, painter, widget):
		option.state &= ~QStyle.StateFlag.State_Children
		super().drawPrimitive(element, option, painter, widget)


def after_setupUi(self, dialog):
	if not hasattr(dialog, 'selectionChanged'):
		return
	self.filter_comboBox = TreeComboBox()
	self.horizontalLayout_2.addWidget(self.filter_comboBox)
	self.tags_comboBox = TreeComboBox()
	self.horizontalLayout_2.addWidget(self.tags_comboBox)

	self.filter_comboBox.addItem('All Card Types')
	item_model = self.filter_comboBox.model()

	models = dialog.mw.col.models.all()
	models.sort(key=lambda x: x['name'])
	for model in models:
		model_id = model['id']
		model_name = model['name']
		note_item = QStandardItem(model_name)
		note_item.setData((model_id, None, model_name, None), Qt.ItemDataRole.UserRole)
		item_model.appendRow(note_item)

		cards = model['tmpls']
		if len(cards) < 2:
			continue

		for card in cards:
			card_name = card['name']
			card_item = QStandardItem(card_name)
			card_item.setData((model_id, card['ord'], model_name, card_name), Qt.ItemDataRole.UserRole)
			note_item.appendRow(card_item)

	self.filter_comboBox.view().expandAll()

	tags_treeview = self.tags_comboBox.view()
	tags_style = HideBranchStyle()
	tags_style.setParent(tags_treeview)
	tags_treeview.setStyle(tags_style)

	self.tags_comboBox.addItem('All Tags')
	tags_model = self.tags_comboBox.model()

	tag_items = {}
	tags = dialog.mw.col.tags.all()
	tags.sort(key=str.casefold)
	for tag in tags:
		path = None
		parent = tags_model
		for part in tag.split('::'):
			path = f'{path}::{part}' if path is not None else part
			tag_item = tag_items.get(path)
			if not tag_item:
				tag_item = QStandardItem(part)
				tag_item.setData(path, Qt.ItemDataRole.UserRole)
				parent.appendRow(tag_item)
				tag_items[path] = tag_item
			parent = tag_item

	tags_treeview.expandAll()

	self.filter_comboBox.currentIndexChanged[int].connect(dialog.selectionChanged)
	self.tags_comboBox.currentIndexChanged[int].connect(dialog.selectionChanged)


def selectionChanged(self, index):
	self.refresh()


def before_refresh(self):
	f = self.form.filter_comboBox.currentData()
	if not f:
		f = (None, None, None, None)
	tag = self.form.tags_comboBox.currentData()
	self.mw.col.filter_stats = (f[0], f[1], tag, f[2], f[3])


def new_stats(self, _old):
	ret = _old(self)
	try:
		ret.filter_stats = self.filter_stats
		self.filter_stats = None
	except AttributeError:
		pass

	return ret


def new_footer(self, _old):
	ret = _old(self)
	filter_stats = getattr(self, 'filter_stats', None)
	if not filter_stats:
		return ret

	tag, model, card = filter_stats[2:]
	br = ret.rfind('<br>')
	return f"{ret[:br]}{''.join(f', {i}' for i in (model, card, tag) if i)}{ret[br:]}"


def filter_conds(self):
	filter_stats = getattr(self, 'filter_stats', None)
	if not filter_stats:
		return

	model_id, card_ord, tag = filter_stats[:3]
	if model_id:
		yield f'nid IN (SELECT id FROM notes WHERE mid = {model_id})'
	if card_ord is not None:
		yield f'ord = {card_ord}'
	if tag is not None:
		tag = tag.replace("'", '').replace('\\', '\\\\').replace('%', '\\%').replace('_', '\\_')
		yield f"nid IN (SELECT id FROM notes WHERE tags LIKE '% {tag} %' ESCAPE '\\' OR tags LIKE '% {tag}::%' ESCAPE '\\')"


def new_limit(self, _old):
	conds = [_old(self)]
	conds += filter_conds(self)
	return ' AND '.join(conds)


def new_revlogLimit(self):
	conds = []
	if not self.wholeCollection:
		conds.append(f'did IN {ids2str(self.col.decks.active())}')

	conds += filter_conds(self)
	if not conds:
		return ''

	return f"cid IN (SELECT id FROM cards WHERE {' AND '.join(conds)})"


Ui_Dialog.setupUi = wrap(Ui_Dialog.setupUi, after_setupUi, pos='after')
DeckStats.selectionChanged = selectionChanged
DeckStats.refresh = wrap(DeckStats.refresh, before_refresh, pos='before')
_Collection.stats = wrap(_Collection.stats, new_stats, pos='around')
CollectionStats.footer = wrap(CollectionStats.footer, new_footer, pos='around')
CollectionStats._limit = wrap(CollectionStats._limit, new_limit, pos='around')
CollectionStats._revlogLimit = new_revlogLimit
