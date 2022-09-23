# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/import.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(825, 726)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.group_deck_import = QtWidgets.QGroupBox(Dialog)
        self.group_deck_import.setTitle("")
        self.group_deck_import.setObjectName("group_deck_import")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.group_deck_import)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.importMessageLayout = QtWidgets.QVBoxLayout()
        self.importMessageLayout.setSpacing(6)
        self.importMessageLayout.setObjectName("importMessageLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.import_message_label = QtWidgets.QLabel(self.group_deck_import)
        self.import_message_label.setObjectName("import_message_label")
        self.verticalLayout_4.addWidget(self.import_message_label)
        self.import_message_textbox = QtWidgets.QTextBrowser(self.group_deck_import)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_message_textbox.sizePolicy().hasHeightForWidth())
        self.import_message_textbox.setSizePolicy(sizePolicy)
        self.import_message_textbox.setObjectName("import_message_textbox")
        self.verticalLayout_4.addWidget(self.import_message_textbox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.cb_tag_cards = QtWidgets.QCheckBox(self.group_deck_import)
        self.cb_tag_cards.setObjectName("cb_tag_cards")
        self.verticalLayout_6.addWidget(self.cb_tag_cards)
        self.textedit_tags = QtWidgets.QLineEdit(self.group_deck_import)
        self.textedit_tags.setObjectName("textedit_tags")
        self.verticalLayout_6.addWidget(self.textedit_tags)
        self.cb_ignore_move_cards = QtWidgets.QCheckBox(self.group_deck_import)
        self.cb_ignore_move_cards.setObjectName("cb_ignore_move_cards")
        self.verticalLayout_6.addWidget(self.cb_ignore_move_cards)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.group_deck_import)
        self.label_2.setEnabled(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.cb_notes = QtWidgets.QCheckBox(self.group_deck_import)
        self.cb_notes.setObjectName("cb_notes")
        self.verticalLayout_7.addWidget(self.cb_notes)
        self.cb_media = QtWidgets.QCheckBox(self.group_deck_import)
        self.cb_media.setObjectName("cb_media")
        self.verticalLayout_7.addWidget(self.cb_media)
        self.verticalLayout_3.addLayout(self.verticalLayout_7)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.importMessageLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.importMessageLayout)
        self.label = QtWidgets.QLabel(self.group_deck_import)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.list_personal_fields = QtWidgets.QListWidget(self.group_deck_import)
        self.list_personal_fields.setObjectName("list_personal_fields")
        self.verticalLayout_5.addWidget(self.list_personal_fields)
        self.verticalLayout_2.addWidget(self.group_deck_import)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CrowdAnki Import Settings"))
        self.import_message_label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Import Message</span></p></body></html>"))
        self.import_message_textbox.setPlaceholderText(_translate("Dialog", "Message from a deck manager about the recent import"))
        self.cb_tag_cards.setText(_translate("Dialog", "Tag Cards"))
        self.textedit_tags.setPlaceholderText(_translate("Dialog", "Tag1, RecentlyImported, Broken"))
        self.cb_ignore_move_cards.setText(_translate("Dialog", "Do Not Move Existing Cards"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Deck Parts to Use</span></p></body></html>"))
        self.cb_notes.setText(_translate("Dialog", "Notes (Cards)"))
        self.cb_media.setText(_translate("Dialog", "Media"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Personal Fields</span> - <span style=\" font-style:italic;\">Fields which will keep their existing values instead of being imported</span></p></body></html>"))