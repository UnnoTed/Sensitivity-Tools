# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created: Tue Oct 14 16:40:58 2014
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(329, 375)
        Form.setStyleSheet(_fromUtf8("color: #333;"))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.size = QtGui.QWidget()
        self.size.setObjectName(_fromUtf8("size"))
        self.size_calculate = QtGui.QPushButton(self.size)
        self.size_calculate.setGeometry(QtCore.QRect(0, 172, 301, 31))
        self.size_calculate.setObjectName(_fromUtf8("size_calculate"))
        self.label = QtGui.QLabel(self.size)
        self.label.setGeometry(QtCore.QRect(10, 210, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.size_sens = QtGui.QLineEdit(self.size)
        self.size_sens.setGeometry(QtCore.QRect(10, 30, 131, 20))
        self.size_sens.setObjectName(_fromUtf8("size_sens"))
        self.size_dpi = QtGui.QLineEdit(self.size)
        self.size_dpi.setGeometry(QtCore.QRect(180, 30, 113, 20))
        self.size_dpi.setObjectName(_fromUtf8("size_dpi"))
        self.size_win_sens = QtGui.QSlider(self.size)
        self.size_win_sens.setGeometry(QtCore.QRect(10, 90, 131, 19))
        self.size_win_sens.setMinimum(1)
        self.size_win_sens.setMaximum(11)
        self.size_win_sens.setProperty("value", 6)
        self.size_win_sens.setOrientation(QtCore.Qt.Horizontal)
        self.size_win_sens.setObjectName(_fromUtf8("size_win_sens"))
        self.label_2 = QtGui.QLabel(self.size)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.size)
        self.label_3.setGeometry(QtCore.QRect(180, 10, 51, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.size)
        self.label_4.setGeometry(QtCore.QRect(180, 70, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.size_yaw = QtGui.QLineEdit(self.size)
        self.size_yaw.setGeometry(QtCore.QRect(180, 90, 113, 20))
        self.size_yaw.setObjectName(_fromUtf8("size_yaw"))
        self.label_5 = QtGui.QLabel(self.size)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.size_label_win = QtGui.QLabel(self.size)
        self.size_label_win.setGeometry(QtCore.QRect(110, 70, 46, 16))
        self.size_label_win.setObjectName(_fromUtf8("size_label_win"))
        self.label_6 = QtGui.QLabel(self.size)
        self.label_6.setGeometry(QtCore.QRect(10, 230, 46, 13))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.size)
        self.label_7.setGeometry(QtCore.QRect(10, 120, 111, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.size_zoom = QtGui.QLineEdit(self.size)
        self.size_zoom.setGeometry(QtCore.QRect(10, 140, 131, 20))
        self.size_zoom.setObjectName(_fromUtf8("size_zoom"))
        self.label_8 = QtGui.QLabel(self.size)
        self.label_8.setGeometry(QtCore.QRect(10, 260, 71, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.size)
        self.label_9.setGeometry(QtCore.QRect(10, 280, 71, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.size_result_cm = QtGui.QLabel(self.size)
        self.size_result_cm.setGeometry(QtCore.QRect(50, 210, 46, 13))
        self.size_result_cm.setObjectName(_fromUtf8("size_result_cm"))
        self.size_result_in = QtGui.QLabel(self.size)
        self.size_result_in.setGeometry(QtCore.QRect(50, 230, 46, 13))
        self.size_result_in.setObjectName(_fromUtf8("size_result_in"))
        self.size_result_zoom_cm = QtGui.QLabel(self.size)
        self.size_result_zoom_cm.setGeometry(QtCore.QRect(80, 260, 46, 16))
        self.size_result_zoom_cm.setObjectName(_fromUtf8("size_result_zoom_cm"))
        self.size_result_zoom_in = QtGui.QLabel(self.size)
        self.size_result_zoom_in.setGeometry(QtCore.QRect(80, 280, 46, 16))
        self.size_result_zoom_in.setObjectName(_fromUtf8("size_result_zoom_in"))
        self.size_rawinput = QtGui.QCheckBox(self.size)
        self.size_rawinput.setGeometry(QtCore.QRect(180, 140, 81, 17))
        self.size_rawinput.setObjectName(_fromUtf8("size_rawinput"))
        self.line = QtGui.QFrame(self.size)
        self.line.setGeometry(QtCore.QRect(150, 0, 20, 161))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.size_copy = QtGui.QPushButton(self.size)
        self.size_copy.setEnabled(True)
        self.size_copy.setGeometry(QtCore.QRect(220, 280, 75, 23))
        self.size_copy.setObjectName(_fromUtf8("size_copy"))
        self.tabWidget.addTab(self.size, _fromUtf8(""))
        self.random = QtGui.QWidget()
        self.random.setObjectName(_fromUtf8("random"))
        self.label_10 = QtGui.QLabel(self.random)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.random_dpi = QtGui.QLineEdit(self.random)
        self.random_dpi.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.random_dpi.setObjectName(_fromUtf8("random_dpi"))
        self.random_generate = QtGui.QPushButton(self.random)
        self.random_generate.setGeometry(QtCore.QRect(0, 150, 301, 31))
        self.random_generate.setObjectName(_fromUtf8("random_generate"))
        self.label_11 = QtGui.QLabel(self.random)
        self.label_11.setGeometry(QtCore.QRect(10, 240, 71, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.random)
        self.label_12.setGeometry(QtCore.QRect(10, 220, 91, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.random)
        self.label_13.setGeometry(QtCore.QRect(10, 270, 46, 13))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.random)
        self.label_14.setGeometry(QtCore.QRect(10, 290, 46, 13))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.random_slider_type = QtGui.QSlider(self.random)
        self.random_slider_type.setGeometry(QtCore.QRect(140, 30, 160, 19))
        self.random_slider_type.setMinimum(1)
        self.random_slider_type.setMaximum(3)
        self.random_slider_type.setProperty("value", 2)
        self.random_slider_type.setOrientation(QtCore.Qt.Horizontal)
        self.random_slider_type.setObjectName(_fromUtf8("random_slider_type"))
        self.random_check_type = QtGui.QCheckBox(self.random)
        self.random_check_type.setGeometry(QtCore.QRect(140, 10, 51, 17))
        self.random_check_type.setChecked(True)
        self.random_check_type.setObjectName(_fromUtf8("random_check_type"))
        self.random_type = QtGui.QLabel(self.random)
        self.random_type.setGeometry(QtCore.QRect(190, 10, 46, 16))
        self.random_type.setObjectName(_fromUtf8("random_type"))
        self.random_gen_sens = QtGui.QLabel(self.random)
        self.random_gen_sens.setGeometry(QtCore.QRect(100, 220, 46, 16))
        self.random_gen_sens.setObjectName(_fromUtf8("random_gen_sens"))
        self.random_gen_cm = QtGui.QLabel(self.random)
        self.random_gen_cm.setGeometry(QtCore.QRect(50, 270, 46, 13))
        self.random_gen_cm.setObjectName(_fromUtf8("random_gen_cm"))
        self.random_gen_in = QtGui.QLabel(self.random)
        self.random_gen_in.setGeometry(QtCore.QRect(50, 290, 46, 13))
        self.random_gen_in.setObjectName(_fromUtf8("random_gen_in"))
        self.random_gen_dpi = QtGui.QLabel(self.random)
        self.random_gen_dpi.setGeometry(QtCore.QRect(70, 240, 46, 16))
        self.random_gen_dpi.setObjectName(_fromUtf8("random_gen_dpi"))
        self.label_15 = QtGui.QLabel(self.random)
        self.label_15.setGeometry(QtCore.QRect(10, 60, 46, 13))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.random_razer = QtGui.QRadioButton(self.random)
        self.random_razer.setGeometry(QtCore.QRect(10, 100, 291, 17))
        self.random_razer.setObjectName(_fromUtf8("random_razer"))
        self.random_logitech = QtGui.QRadioButton(self.random)
        self.random_logitech.setGeometry(QtCore.QRect(10, 80, 291, 17))
        self.random_logitech.setChecked(True)
        self.random_logitech.setObjectName(_fromUtf8("random_logitech"))
        self.random_zowie = QtGui.QRadioButton(self.random)
        self.random_zowie.setGeometry(QtCore.QRect(10, 120, 291, 17))
        self.random_zowie.setObjectName(_fromUtf8("random_zowie"))
        self.line_2 = QtGui.QFrame(self.random)
        self.line_2.setGeometry(QtCore.QRect(0, 190, 301, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.tabWidget.addTab(self.random, _fromUtf8(""))
        self.convert = QtGui.QWidget()
        self.convert.setObjectName(_fromUtf8("convert"))
        self.convert_dpi = QtGui.QLineEdit(self.convert)
        self.convert_dpi.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.convert_dpi.setObjectName(_fromUtf8("convert_dpi"))
        self.convert_btn = QtGui.QPushButton(self.convert)
        self.convert_btn.setGeometry(QtCore.QRect(180, 160, 111, 41))
        self.convert_btn.setObjectName(_fromUtf8("convert_btn"))
        self.label_16 = QtGui.QLabel(self.convert)
        self.label_16.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.convert_sens = QtGui.QLineEdit(self.convert)
        self.convert_sens.setGeometry(QtCore.QRect(10, 90, 113, 20))
        self.convert_sens.setObjectName(_fromUtf8("convert_sens"))
        self.label_17 = QtGui.QLabel(self.convert)
        self.label_17.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.convert_new_dpi = QtGui.QLineEdit(self.convert)
        self.convert_new_dpi.setGeometry(QtCore.QRect(10, 160, 113, 20))
        self.convert_new_dpi.setObjectName(_fromUtf8("convert_new_dpi"))
        self.label_18 = QtGui.QLabel(self.convert)
        self.label_18.setGeometry(QtCore.QRect(10, 140, 46, 13))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.convert)
        self.label_19.setEnabled(True)
        self.label_19.setGeometry(QtCore.QRect(10, 190, 81, 16))
        self.label_19.setAutoFillBackground(False)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.convert_new_sens = QtGui.QLabel(self.convert)
        self.convert_new_sens.setGeometry(QtCore.QRect(90, 190, 41, 16))
        self.convert_new_sens.setObjectName(_fromUtf8("convert_new_sens"))
        self.convert_all = QtGui.QCheckBox(self.convert)
        self.convert_all.setGeometry(QtCore.QRect(180, 10, 70, 17))
        self.convert_all.setObjectName(_fromUtf8("convert_all"))
        self.convert_razer = QtGui.QRadioButton(self.convert)
        self.convert_razer.setEnabled(False)
        self.convert_razer.setGeometry(QtCore.QRect(180, 70, 121, 41))
        self.convert_razer.setObjectName(_fromUtf8("convert_razer"))
        self.convert_zowie = QtGui.QRadioButton(self.convert)
        self.convert_zowie.setEnabled(False)
        self.convert_zowie.setGeometry(QtCore.QRect(180, 110, 121, 41))
        self.convert_zowie.setObjectName(_fromUtf8("convert_zowie"))
        self.convert_logitech = QtGui.QRadioButton(self.convert)
        self.convert_logitech.setEnabled(False)
        self.convert_logitech.setGeometry(QtCore.QRect(180, 40, 111, 31))
        self.convert_logitech.setChecked(True)
        self.convert_logitech.setObjectName(_fromUtf8("convert_logitech"))
        self.label_20 = QtGui.QLabel(self.convert)
        self.label_20.setGeometry(QtCore.QRect(180, 30, 46, 13))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.convert_list = QtGui.QTextEdit(self.convert)
        self.convert_list.setGeometry(QtCore.QRect(10, 210, 281, 91))
        self.convert_list.setObjectName(_fromUtf8("convert_list"))
        self.tabWidget.addTab(self.convert, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.skillurl = QtGui.QLabel(Form)
        self.skillurl.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.skillurl.setStyleSheet(_fromUtf8("color: rgb(0, 68, 255)"))
        self.skillurl.setTextFormat(QtCore.Qt.AutoText)
        self.skillurl.setAlignment(QtCore.Qt.AlignCenter)
        self.skillurl.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.skillurl.setObjectName(_fromUtf8("skillurl"))
        self.verticalLayout.addWidget(self.skillurl)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Sensitivity Tools", None))
        self.size_calculate.setText(_translate("Form", "Calculate", None))
        self.label.setText(_translate("Form", "cm/360:", None))
        self.label_2.setText(_translate("Form", "Game Sensitivity", None))
        self.label_3.setText(_translate("Form", "Mouse DPI", None))
        self.label_4.setText(_translate("Form", "m_yaw", None))
        self.size_yaw.setText(_translate("Form", "0.022", None))
        self.label_5.setText(_translate("Form", "Windows Sensitivity:", None))
        self.size_label_win.setText(_translate("Form", "6/11", None))
        self.label_6.setText(_translate("Form", "in/360:", None))
        self.label_7.setText(_translate("Form", "zoom_sensitivity_ratio", None))
        self.size_zoom.setText(_translate("Form", "1", None))
        self.label_8.setText(_translate("Form", "zoom cm/360:", None))
        self.label_9.setText(_translate("Form", "zoom in/360:", None))
        self.size_result_cm.setText(_translate("Form", "0", None))
        self.size_result_in.setText(_translate("Form", "0", None))
        self.size_result_zoom_cm.setText(_translate("Form", "0", None))
        self.size_result_zoom_in.setText(_translate("Form", "0", None))
        self.size_rawinput.setToolTip(_translate("Form", "will reset windows sensitivity to 6/11", None))
        self.size_rawinput.setText(_translate("Form", "m_rawinput", None))
        self.size_copy.setText(_translate("Form", "Copy info", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.size), _translate("Form", "size/360", None))
        self.label_10.setText(_translate("Form", "Mouse DPI", None))
        self.random_generate.setText(_translate("Form", "Generate", None))
        self.label_11.setText(_translate("Form", "Mouse DPI:", None))
        self.label_12.setText(_translate("Form", "Game Sensitivity:", None))
        self.label_13.setText(_translate("Form", "cm/360:", None))
        self.label_14.setText(_translate("Form", "in/360:", None))
        self.random_check_type.setText(_translate("Form", "Type:", None))
        self.random_type.setText(_translate("Form", "Medium", None))
        self.random_gen_sens.setText(_translate("Form", "0", None))
        self.random_gen_cm.setText(_translate("Form", "0", None))
        self.random_gen_in.setText(_translate("Form", "0", None))
        self.random_gen_dpi.setText(_translate("Form", "0", None))
        self.label_15.setText(_translate("Form", "Mouse:", None))
        self.random_razer.setText(_translate("Form", "Razer -> 400-6400 DPI", None))
        self.random_logitech.setText(_translate("Form", "Logitech -> 400-4000 DPI", None))
        self.random_zowie.setText(_translate("Form", "Zowie -> 450 or 1150 or 2300 DPI", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.random), _translate("Form", "Random", None))
        self.convert_btn.setText(_translate("Form", "Convert", None))
        self.label_16.setText(_translate("Form", "DPI", None))
        self.label_17.setText(_translate("Form", "Sensitivity", None))
        self.label_18.setText(_translate("Form", "New DPI", None))
        self.label_19.setText(_translate("Form", "New Sensitivity:", None))
        self.convert_new_sens.setText(_translate("Form", "0", None))
        self.convert_all.setToolTip(_translate("Form", "will show a list with all dpi available in certain mouse...", None))
        self.convert_all.setText(_translate("Form", "ALL DPIs", None))
        self.convert_razer.setText(_translate("Form", "Razer\n"
"400-6400 DPI", None))
        self.convert_zowie.setText(_translate("Form", "Zowie -> 450,\n"
"1150 or 2300 DPI", None))
        self.convert_logitech.setText(_translate("Form", "Logitech\n"
"400-4000 DPI", None))
        self.label_20.setText(_translate("Form", "Mouse:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.convert), _translate("Form", "Convert", None))
        self.skillurl.setText(_translate("Form", "http://github.com/sk1LLb0X", None))

