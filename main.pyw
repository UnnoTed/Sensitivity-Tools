"""
Sensitivity Tools

Developed by sk1LLb0X

Version 0.1
"""

import os, sys, math, random, platform, ctypes
from subprocess import call, Popen, PIPE

import warnings
warnings.simplefilter('ignore')

from PyQt4.QtCore import pyqtSignature, QString, Qt, QVariant, SIGNAL, SLOT
from PyQt4.QtGui import *
from PyQt4 import Qt
from ui_main_window import Ui_Form

""" some useful stuff """

# return window's sensitivity multiplier
def winSens(val):
  sens = [0.0625, 0.0125, 0.25, 0.5, 0.75, 1, 1.5, 2, 2.5, 3, 3.5]
  return sens[(val - 1)]
#END: winSens

# will transform numbers like: 10.93 to 10.9 or 29.68 to 29.7
def roundSens(sens):
  s = math.fabs(sens)
  factor = math.pow(10, 1)

  return (sens < 0 and -1 or 1) * round(s * factor) / factor
#END: roundSens

def zoomSens(sens, ratio):
  return roundSens((sens / (ratio * 100)) * 100)
#END: zoomSens

def mouseDPI(mouse):
  # 0 = Logitech
  # 1 = Razer
  # 2 = Zowie

  dpiList = []
  i = 400

  if mouse == 0: # logitech
    while i != 4050:
      dpiList.extend([i])
      i += 50
  elif mouse == 1: # razer
    while i != 6500:
      dpiList.extend([i])
      i += 100
  elif mouse == 2: # zowie
    dpiList = [450, 1150, 2300]

  return dpiList
#END: mouseDPI

# sensitivity modes: low, medium, high (cm/360)
modes = [
  [45, 22], # 0 -> low
  [22, 14], # 1 -> medium
  [14, 3],  # 2 -> high
  [45, 3]   # 3 -> random
]
#END: modes

def randomSens(dpi, mode, mouse):
  # get the dpi list
  dpilist = mouseDPI(mouse)

  # choose a random dpi from the list
  if dpi == 0:
    dpi = dpilist[random.randint(0, len(dpilist) - 1)]

  sens = 0

  while True:
    # random number between 0 and 20 (who is going to use more than 20 sens? max i've used was 15)
    r = round(random.uniform(0, 20), 2)

    # calculate the cm/360
    calc = (360 / (0.022 * dpi * r)) * 2.54

    # if the generated cm/360 is between the max and minimum cm/360 of the sensitivity mode it'll break the loop
    if calc < modes[mode][0] and calc > modes[mode][1]:
      sens = r
      break
  #END: while

  return {'dpi': dpi, 'sens': sens}
#END: randomSens

""" main class """

class MainWindow(QWidget, Ui_Form):

  def __init__(self, parent = None):
    QWidget.__init__(self, parent)
    self.setupUi(self)
    self.calculateSens()
    self.winSlider()
    self.genSens()
    self.Convert()
    self.setFixedSize(329, 375)

  """ TAB: size/360 """

  ###########################
  #### RAWINPUT CHECKBOX ####
  ###########################

  def winSlider(self):
    self.size_win_sens.valueChanged.connect(self.onWinSlide)

  def onWinSlide(self, val):
    self.size_label_win.setText(str(val) + '/11')

  #############################
  #### WINDOWS SENS SLIDER ####
  #############################

  def winSlider(self):
    self.size_win_sens.valueChanged.connect(self.onWinSlide)

  def onWinSlide(self, val):
    self.size_label_win.setText(str(val) + '/11')

  ###################
  #### CALCULATE ####
  ###################

  # on click the button: "Calculate" of the tab: size/360
  def calculateSens(self):
    self.size_calculate.clicked.connect(self.onCalculate)
    self.size_copy.clicked.connect(self.onCopyInfo)

  def onCopyInfo(self):
    cm = str(self.size_result_cm.text())

    dpi = str(self.size_dpi.text())
    win = str(self.size_win_sens.value())

    inch = str(self.size_result_in.text())
    sens = str(self.size_sens.text())

    zoom = str(self.size_zoom.text())
    zoom_cm = str(self.size_result_zoom_cm.text())
    zoom_in = str(self.size_result_zoom_in.text())

    rawinput = str((self.size_rawinput.isChecked() and 1 or 0))

    text = """-- Info --
DPI: %s
Sensitivity: %s

-- Other --
m_rawinput: %s
Windows Sensitivity: %s/11

-- Size --
cm/360: %s
in/360: %s

-- Zoom --
zoom_sensitivity_ratio: %s
zoom cm/360: %s
zoom in/360: %s
    """ % (dpi, sens, rawinput, win, cm, inch, zoom, zoom_cm, zoom_in)

    # from https://github.com/asweigart/pyperclip
    text = str(text)
    GMEM_DDESHARE = 0x2000
    ctypes.windll.user32.OpenClipboard(0)
    ctypes.windll.user32.EmptyClipboard()
    try:
        # works on Python 2 (bytes() only takes one argument)
        hCd = ctypes.windll.kernel32.GlobalAlloc(GMEM_DDESHARE, len(bytes(text))+1)
    except TypeError:
        # works on Python 3 (bytes() requires an encoding)
        hCd = ctypes.windll.kernel32.GlobalAlloc(GMEM_DDESHARE, len(bytes(text, 'ascii'))+1)
    pchData = ctypes.windll.kernel32.GlobalLock(hCd)
    try:
        # works on Python 2 (bytes() only takes one argument)
        ctypes.cdll.msvcrt.strcpy(ctypes.c_char_p(pchData), bytes(text))
    except TypeError:
        # works on Python 3 (bytes() requires an encoding)
        ctypes.cdll.msvcrt.strcpy(ctypes.c_char_p(pchData), bytes(text, 'ascii'))
    ctypes.windll.kernel32.GlobalUnlock(hCd)
    ctypes.windll.user32.SetClipboardData(1, hCd)
    ctypes.windll.user32.CloseClipboard()

  # ^ callback
  def onCalculate(self):
    if len(self.size_dpi.text()) == 0 or len(self.size_sens.text()) == 0:
      return

    # m_yaw
    yaw = float(self.size_yaw.text())

    # mouse dpi
    dpi = int(self.size_dpi.text())
    if dpi == 0:
      dpi = 400

    # sensitivity
    sens = float(self.size_sens.text())
    if sens == 0:
      sens = 0.1

    # zoom_sensitivity_ratio
    zoom = float(self.size_zoom.text())

    # return window's sens multiplier
    # if rawinput == 1: return 6 else: return slider's value
    win = winSens(self.size_rawinput.isChecked() and 6 or self.size_win_sens.value())

    # inch/360
    size = (360 / (yaw * dpi * win * sens))

    # final result
    cm   = roundSens(size * 2.54) # 2.54 == inch size
    inch = roundSens(size)

    # shows result for "cm" and "in" /360
    self.size_result_cm.setText(str(cm)) # cm
    self.size_result_in.setText(str(inch)) # in

    # shows result for zoom's "cm" and "in" /360
    self.size_result_zoom_cm.setText(str(zoomSens(cm, zoom))) # cm
    self.size_result_zoom_in.setText(str(zoomSens(inch, zoom))) # in
  #END: onCalculate

  """ END: TAB: size/360 """

  """ TAB: Random """

  ##############################
  #### GENERATE SENSITIVITY ####
  ##############################

    # on click the button: "Generate" of the tab: Random
  def genSens(self):
    self.random_generate.clicked.connect(self.onGen)
    self.random_slider_type.valueChanged.connect(self.onTypeSlide)
  #END: genSens

  def getMouse(self):
    if self.random_logitech.isChecked():
      return 0
    elif self.random_razer.isChecked():
      return 1
    elif self.random_zowie.isChecked():
      return 2
  #END: getMouse

  def onTypeSlide(self):
    modes = ['Low', 'Medium', 'High']
    # set the text to one of these ^
    self.random_type.setText(modes[self.random_slider_type.value() - 1])
  #END: onTypeSlide

  # ^ callback
  def onGen(self):

    mouse = self.getMouse()

    # mouse dpi
    dpi = int(len(self.random_dpi.text()) > 0 and self.random_dpi.text() or 0)

    # if a type is not set, the sensitivity type (low, high...) will be random
    mode = 0
    if self.random_check_type.isChecked():
      mode = self.random_slider_type.value() - 1
    else:
      mode = 3

    # get random dpi and sensitivity
    r = randomSens(dpi, mode, mouse)

    dpi = r['dpi']
    sens = r['sens']

    # inch/360
    size = (360 / (0.022 * dpi * sens))

    # final result
    cm   = roundSens(size * 2.54) # 2.54 == inch size
    inch = roundSens(size)

    # shows result for "cm" and "in" /360
    self.random_gen_sens.setText(str(sens))
    self.random_gen_dpi.setText(str(dpi))
    self.random_gen_cm.setText(str(cm)) # cm
    self.random_gen_in.setText(str(inch)) # in
  #END: onCalculate

  """ END: TAB: Random """

  """ TAB: Convert """

  ##################
  #### ALL DPIs ####
  ##################

  def AllDPI(self):
    self.convert_all.clicked.connect(self.onAllDPI)
  #END: AllDPI

  def onAllDPI(self):
    if self.convert_all.isChecked():
      self.convert_logitech.setEnabled(True)
      self.convert_razer.setEnabled(True)
      self.convert_zowie.setEnabled(True)
      self.convert_new_sens.hide()
      self.convert_list.show()
      self.label_19.hide()
    else: # not checked
      self.convert_logitech.setEnabled(False)
      self.convert_razer.setEnabled(False)
      self.convert_zowie.setEnabled(False)
      self.convert_new_sens.show()
      self.convert_list.hide()
      self.label_19.show()
  #END: onAllDPI

  def AllDPIMouse(self):
    if self.convert_logitech.isChecked():
      return mouseDPI(0)
    elif self.convert_razer.isChecked():
      return mouseDPI(1)
    elif self.convert_zowie.isChecked():
      return mouseDPI(2)
  #END: AllDPIMouse

  #############################
  #### CONVERT SENSITIVITY ####
  #############################

  def Convert(self):
    self.convert_btn.clicked.connect(self.onConvert)
    self.convert_list.hide()
    self.AllDPI()
  #END: Convert

  def onConvert(self):
    if len(self.convert_dpi.text()) == 0 or len(self.convert_sens.text()) == 0:
      return

    dpi = int(self.convert_dpi.text())
    sens = float(self.convert_sens.text())

    # current sensitivity's in/360
    calc = (360 / (0.022 * dpi * sens))

    if self.convert_all.isChecked():
      # get the dpi list for the mouse
      dpiList = self.AllDPIMouse()
      listText = ''

      for d in dpiList:
        raw = 360 / calc
        newSens = round(raw / d / 0.022, 2)
        listText += "DPI: " + str(d) + "\nSensitivity: " + str(newSens) + "\n\n"

      # set the label with the sens list
      self.convert_list.setText(str(listText))
    else:
      newDPI = int(len(self.convert_new_dpi.text()) > 0 and self.convert_new_dpi.text() or 400)
      raw = 360 / calc
      newSens = round(raw / newDPI / 0.022, 2)
      # set the label with the new sens
      self.convert_new_sens.setText(str(newSens))

  #END: onConvert


  """ END: TAB: Convert """

#END: class: MainWindow

if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())

