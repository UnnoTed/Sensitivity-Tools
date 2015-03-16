# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/history_window.ui'
#
# Created: Mon Mar 16 12:20:47 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_HistoryForm(object):
    def setupUi(self, HistoryForm):
        HistoryForm.setObjectName(_fromUtf8("HistoryForm"))
        HistoryForm.resize(420, 430)
        HistoryForm.setStyleSheet(_fromUtf8("color: #333;"))
        self.verticalLayout = QtGui.QVBoxLayout(HistoryForm)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.history_view = QtWebKit.QWebView(HistoryForm)
        self.history_view.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.history_view.setObjectName(_fromUtf8("history_view"))
        self.horizontalLayout.addWidget(self.history_view)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(HistoryForm)
        QtCore.QMetaObject.connectSlotsByName(HistoryForm)

    def retranslateUi(self, HistoryForm):
        HistoryForm.setWindowTitle(_translate("HistoryForm", "Sensitivity Tools", None))

from PyQt4 import QtWebKit
