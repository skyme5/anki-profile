# Form implementation generated from reading ui file './addtable.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(441, 396)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QtCore.QSize(175, 16777215))
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 10, 0, 1, 1)
        self.sb_align_H = QtWidgets.QComboBox(Dialog)
        self.sb_align_H.setObjectName("sb_align_H")
        self.gridLayout_2.addWidget(self.sb_align_H, 8, 1, 1, 1)
        self.cb_width = QtWidgets.QCheckBox(Dialog)
        self.cb_width.setText("")
        self.cb_width.setObjectName("cb_width")
        self.gridLayout_2.addWidget(self.cb_width, 3, 1, 1, 1)
        self.cb_save = QtWidgets.QCheckBox(Dialog)
        self.cb_save.setText("")
        self.cb_save.setObjectName("cb_save")
        self.gridLayout_2.addWidget(self.cb_save, 10, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 8, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.sb_styling = QtWidgets.QComboBox(Dialog)
        self.sb_styling.setObjectName("sb_styling")
        self.gridLayout_2.addWidget(self.sb_styling, 7, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 9, 0, 1, 1)
        self.sb_rows = QtWidgets.QSpinBox(Dialog)
        self.sb_rows.setObjectName("sb_rows")
        self.gridLayout_2.addWidget(self.sb_rows, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)
        self.sb_align_V = QtWidgets.QComboBox(Dialog)
        self.sb_align_V.setObjectName("sb_align_V")
        self.gridLayout_2.addWidget(self.sb_align_V, 9, 1, 1, 1)
        self.cb_first = QtWidgets.QCheckBox(Dialog)
        self.cb_first.setText("")
        self.cb_first.setObjectName("cb_first")
        self.gridLayout_2.addWidget(self.cb_first, 4, 1, 1, 1)
        self.sb_columns = QtWidgets.QSpinBox(Dialog)
        self.sb_columns.setObjectName("sb_columns")
        self.gridLayout_2.addWidget(self.sb_columns, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.cb_prefill = QtWidgets.QCheckBox(Dialog)
        self.cb_prefill.setText("")
        self.cb_prefill.setObjectName("cb_prefill")
        self.gridLayout_2.addWidget(self.cb_prefill, 5, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 7, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 6, 0, 1, 1)
        self.cb_center = QtWidgets.QCheckBox(Dialog)
        self.cb_center.setText("")
        self.cb_center.setObjectName("cb_center")
        self.gridLayout_2.addWidget(self.cb_center, 6, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_8.setText(_translate("Dialog", "Save these settings as default for next table"))
        self.label_3.setText(_translate("Dialog", "Number of rows"))
        self.label_5.setText(_translate("Dialog", "Table alignment, horizontal"))
        self.label_2.setText(_translate("Dialog", "Number of columns"))
        self.label_7.setText(_translate("Dialog", "Table alignment, vertical"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Enter table properties:</span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "Fixed Width columns"))
        self.label_4.setText(_translate("Dialog", "prefill fields"))
        self.label_6.setText(_translate("Dialog", "First row is head"))
        self.label_9.setText(_translate("Dialog", "styling"))
        self.label_11.setText(_translate("Dialog", "center table"))
