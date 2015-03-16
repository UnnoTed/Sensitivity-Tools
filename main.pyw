"""
Sensitivity Tools

Developed by sk1LLb0X

Version 0.4
"""

import os, sys, math, random, platform, ctypes, json, datetime, webbrowser, time, threading

import warnings
warnings.simplefilter('ignore')

from PyQt4.QtCore import pyqtSignature, QString, Qt, QVariant, SIGNAL, SLOT, QDate
from PyQt4.QtGui import *
from PyQt4 import Qt

from ui_main_window import Ui_Form
from ui_history_window import Ui_HistoryForm

SKILL_URL = "http://github.com/sk1LLb0X"
VERSION = "0.4"

HISTORY_HTML = ""
HISTORY_CSS = ""

try:
  with open ("history.html", "r") as file:
    HISTORY_HTML = file.read()
except IOError:
  print "Missing history.html"

try:
  with open ("history.css", "r") as file:
    HISTORY_CSS = file.read()
except IOError:
  print "Missing history.css"

""" Config """

cfg = {}
try:
  with open("config.json") as file:
    cfg = json.load(file)
except IOError:
  with open("config.json", "w") as file:
    file.write("{}")
    file.close()
    cfg = {}

def saveConfig():
  with open("config.json", "w") as file:
    json.dump(cfg, file, indent = 2, sort_keys = True)

""" History """

history = {}
try:
  with open("history.json") as file:
    history = json.load(file)
except IOError:
  with open("history.json", "w") as file:
    file.write("{}")
    file.close()
    history = {}

def saveHistory():
  with open("history.json", "w") as file:
    json.dump(history, file, indent = 2, sort_keys = True)

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

if cfg.get("win_sens", None) == None:
  cfg["win_sens"] = 6
  saveConfig()

if cfg.get("m_yaw", None) == None:
  cfg["m_yaw"] = 0.022
  saveConfig()

# sensitivity modes: low, medium, high (cm/360)
# random sensitivity settings
if cfg.get("random", None) == None:
  cfg["random"] = {
    "low" : {
      "min" : 45,
      "max" : 22
    },

    "medium" : {
      "min" : 22,
      "max" : 14
    },

    "high" : {
      "min" : 14,
      "max" : 3
    },

    "all" : {
      "min" : 45,
      "max" : 3
    }
  }
  saveConfig()
#END: random sensitivity settings


def randomSensMode(index):
  if index == 0:
    return "low"
  elif index == 1:
    return "medium"
  elif index == 2:
    return "high"
  else:
    return "all"

def randomSens(dpi, mode, mouse):
  # get the dpi list
  dpilist = mouseDPI(mouse)

  # choose a random dpi from the list
  if dpi == 0:
    dpi = dpilist[random.randint(0, len(dpilist) - 1)]

  sens = 0

  while True:
    r = round(random.uniform(0, 200), 2)

    # calculate the cm/360
    calc = 1

    try:
      calc = (360 / (cfg["m_yaw"] * dpi * r)) * 2.54
    except ZeroDivisionError:
      calc = 1

    # if the generated cm/360 is between the max and minimum cm/360 of the sensitivity mode it'll break the loop
    if calc < cfg["random"][randomSensMode(mode)]["min"] and calc > cfg["random"][randomSensMode(mode)]["max"]:
      sens = r
      break
  #END: while

  return {'dpi': dpi, 'sens': sens}
#END: randomSens

def twoChar(number):
  if number > 0 and number < 10:
    return "0" + str(number)
  else:
    return number

class HistoryWindow(QWidget, Ui_HistoryForm):
  def __init__(self, parent = None):
    QWidget.__init__(self, parent)
    self.setupUi(self)
    self.resize(430, 430)

""" main class """

class MainWindow(QWidget, Ui_Form):

  def __init__(self, parent = None):
    QWidget.__init__(self, parent)
    self.setupUi(self)
    self.calculateSens()
    self.winSlider()
    self.genSens()
    self.Convert()
    self.loadSettings()
    self.loadHistory()
    self.setFixedSize(420, 420)
    self.setWindowTitle('Sensitivity Tools v' + VERSION)

    self.settings_label.setHidden(True)

    self.HistoryWindow = HistoryWindow()

    self.size2sens_btn_inch.clicked.connect(self.size2sens_GenerateFromInch)
    self.size2sens_btn_cm.clicked.connect(self.size2sens_GenerateFromCM)

    self.size2sens_btn_zoom_inch.clicked.connect(self.size2sens_GenerateZoomFromInch)
    self.size2sens_btn_zoom_cm.clicked.connect(self.size2sens_GenerateZoomFromCM)

    self.settings_btn_save.clicked.connect(self.saveSettings)

    self.skillurl.clicked.connect(self.openUrl)

    self.history_calendar.clicked.connect(self.updateHistory)
    self.history_show.clicked.connect(self.showHistory)

    self.tabWidget.currentChanged.connect(self.reloadHistory)

  def reloadHistory(self):
    if self.tabWidget.currentIndex() == 4:
      self.loadHistory()

  def showHistory(self):
    self.HistoryWindow.show()

  def updateHistory(self):
    date = self.history_calendar.selectedDate()
    strDate = "{year}-{month}-{day}".format(year = twoChar(date.year()), month = twoChar(date.month()), day = twoChar(date.day()))

    styles = "<style>%s</style>" % HISTORY_CSS
    sensNumber = 0

    historyModel = HISTORY_HTML

    if history.get(strDate, None):
      sensList = history[strDate]
      historyText = ""

      for i in sensList:
        sDate = datetime.datetime.strptime(i["date"], "%Y-%m-%d %H:%M:%S").date()
        sTime = datetime.datetime.strptime(i["date"], "%Y-%m-%d %H:%M:%S").time()

        sensNumber += 1

        historyText += historyModel.format(
          month = twoChar(sDate.month),
          year = twoChar(sDate.year),
          day = twoChar(sDate.day),

          seconds = twoChar(sTime.second),
          minutes = twoChar(sTime.minute),
          hours = twoChar(sTime.hour),

          sens = str(i["sensitivity"]["sens"]),
          dpi = str(i["sensitivity"]["dpi"]),

          rawinput = str(i["sensitivity"]["rawinput"]),
          yaw = str(i["sensitivity"]["yaw"]),
          win = str(i["sensitivity"]["win"]),

          inch = str(i["sensitivity"]["size"]["inch"]),
          cm = str(i["sensitivity"]["size"]["cm"]),

          zoom_ratio = str(i["sensitivity"]["size"]["zoom"]["ratio"]),
          zoom_inch = str(i["sensitivity"]["size"]["zoom"]["inch"]),
          zoom_cm = str(i["sensitivity"]["size"]["zoom"]["cm"]),

          type = str(i["type"]),

          number = sensNumber
        )

      self.HistoryWindow.history_view.setHtml(styles + historyText)

  def loadHistory(self):
    min = 9999999999999999
    max = 0

    for i in history:
      for j in history[i]:
        if j.get("date", None):
          sDate = int(time.mktime(datetime.datetime.strptime(j["date"], "%Y-%m-%d %H:%M:%S").date().timetuple()))
          if sDate < min:
            min = sDate

          if sDate > max:
            max = sDate
    
    if min != 9999999999999999:
      self.history_calendar.setHidden(False)
      self.history_show.setHidden(False)
      minDate = datetime.datetime.fromtimestamp(min)
      maxDate = datetime.datetime.fromtimestamp(max)

      minCalendar = QDate(minDate.year, minDate.month, minDate.day)
      maxCalendar = QDate(maxDate.year, maxDate.month, maxDate.day)

      self.history_calendar.setDateRange(minCalendar, maxCalendar)
    else:
      self.history_calendar.setHidden(True)
      self.history_show.setHidden(True)

  def openUrl(self):
    webbrowser.open(SKILL_URL, new = 2, autoraise = True)

  def loadSettings(self):
    # low
    self.settings_random_low_min.setText(str(cfg["random"]["low"]["min"]))
    self.settings_random_low_max.setText(str(cfg["random"]["low"]["max"]))

    # medium
    self.settings_random_medium_min.setText(str(cfg["random"]["medium"]["min"]))
    self.settings_random_medium_max.setText(str(cfg["random"]["medium"]["max"]))

    # high
    self.settings_random_high_min.setText(str(cfg["random"]["high"]["min"]))
    self.settings_random_high_max.setText(str(cfg["random"]["high"]["max"]))

    # all
    self.settings_random_all_min.setText(str(cfg["random"]["all"]["min"]))
    self.settings_random_all_max.setText(str(cfg["random"]["all"]["max"]))

    self.size_win_sens.setValue(int(cfg.get("win_sens", 6)))
    self.settings_m_yaw.setText(str(cfg.get("m_yaw", 0.022)))

  def saveSettings(self):
    cfg["random"] = {
      "low" : {
        "min" : int(self.settings_random_low_min.text()),
        "max" : int(self.settings_random_low_max.text())
      },

      "medium" : {
        "min" : int(self.settings_random_medium_min.text()),
        "max" : int(self.settings_random_medium_max.text())
      },

      "high" : {
        "min" : int(self.settings_random_high_min.text()),
        "max" : int(self.settings_random_high_max.text())
      },

      "all" : {
        "min" : int(self.settings_random_all_min.text()),
        "max" : int(self.settings_random_all_max.text())
      }
    }

    # m_yaw
    cfg["m_yaw"] = float(self.settings_m_yaw.text())

    # Windows Sensitivity
    cfg["win_sens"] = int(self.size_win_sens.value())

    saveConfig()

    self.settings_label.setHidden(False)
    threading.Timer(1.5, self.hideSettingsLabel).start()

  def hideSettingsLabel(self):
    self.settings_label.setHidden(True)

  def size2sens_GenerateFromInch(self):
    inch = float(self.size2sens_inch.text() if len(self.size2sens_inch.text()) > 0 else -1)
    dpi = int(self.size2sens_dpi.text() if len(self.size2sens_dpi.text()) > 2 else -1)
    m_yaw = float(cfg["m_yaw"])

    if inch == -1 or dpi == -1:
      return

    raw = 360 / inch
    sens = round(raw / dpi / m_yaw, 2)

    self.size2sens_result_sens.setText(str(sens))
    self.size2sens_result_inch.setText(str(inch))
    self.size2sens_result_cm.setText(str(roundSens(inch * 2.54)))


  def size2sens_GenerateZoomFromInch(self):
    inch = float(self.size2sens_inch.text() if len(self.size2sens_inch.text()) > 0 else -1)
    dpi = int(self.size2sens_dpi.text() if len(self.size2sens_dpi.text()) > 2 else -1)
    m_yaw = float(cfg["m_yaw"])
    sens = float(self.size2sens_sens.text() if len(self.size2sens_sens.text()) > 0 else -1)

    if inch == -1 or dpi == -1 or sens == -1:
      return

    raw = 360 / inch
    sens = round(raw / dpi / m_yaw, 2)

    self.size2sens_result_sens.setText(str(sens))
    self.size2sens_result_inch.setText(str(inch))
    self.size2sens_result_cm.setText(str(roundSens(inch * 2.54)))
    self.size2sens_result_zoom.setText(str(roundSens((sens / (1.1 * 100)) * 100)))

  def size2sens_GenerateFromCM(self):
    cm = float(self.size2sens_cm.text() if len(self.size2sens_cm.text()) > 0 else -1)
    dpi = int(self.size2sens_dpi.text() if len(self.size2sens_dpi.text()) > 2 else -1)
    m_yaw = float(cfg["m_yaw"])

    if cm == -1 or dpi == -1:
      return

    sens = round((360 / (cm / 2.54)) / dpi / m_yaw, 2)

    self.size2sens_result_sens.setText(str(sens))
    self.size2sens_result_inch.setText(str(roundSens((cm / 2.54))))
    self.size2sens_result_cm.setText(str(cm))


  def size2sens_GenerateZoomFromCM(self):
    cm = float(self.size2sens_cm.text() if len(self.size2sens_cm.text()) > 0 else -1)
    dpi = int(self.size2sens_dpi.text() if len(self.size2sens_dpi.text()) > 2 else -1)
    m_yaw = float(cfg["m_yaw"])

    if cm == -1 or dpi == -1:
      return

    sens = round((360 / (cm / 2.54)) / dpi / m_yaw, 2)

    self.size2sens_result_sens.setText(str(sens))
    self.size2sens_result_inch.setText(str(roundSens((cm / 2.54))))
    self.size2sens_result_cm.setText(str(cm))

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
    win = str(cfg["win_sens"])

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
    yaw = float(cfg["m_yaw"])

    # mouse dpi
    dpi = int(self.size_dpi.text())
    if dpi == 0:
      return

    # sensitivity
    sens = float(self.size_sens.text())
    if sens == 0:
      return

    # zoom_sensitivity_ratio
    zoom = float(self.size_zoom.text())

    # return window's sens multiplier
    # if rawinput == 1: return 6 else: return slider's value
    win = (self.size_rawinput.isChecked() and 6 or cfg["win_sens"])

    # inch/360
    size = (360 / (yaw * dpi * winSens(win) * sens))

    # final result
    cm   = roundSens(size * 2.54) # 2.54 == inch size
    inch = roundSens(size)

    # shows result for "cm" and "in" /360
    self.size_result_cm.setText(str(cm)) # cm
    self.size_result_in.setText(str(inch)) # in

    # shows result for zoom's "cm" and "in" /360
    self.size_result_zoom_cm.setText(str(zoomSens(cm, zoom))) # cm
    self.size_result_zoom_in.setText(str(zoomSens(inch, zoom))) # in

    # gets the current date and time
    date = datetime.datetime.now()

    # create a string with date in it: yyyy-mm-dd
    calendarDate = date.strftime("%Y-%m-%d")
    sensDate = date.strftime("%Y-%m-%d %H:%M:%S")

    # dict that will be saved to 
    # history.json when the sensitivity 
    # is generated
    if history.get(calendarDate, None) == None:
      history[calendarDate] = []

    history[calendarDate].append({
      "date" : sensDate,
      "type" : "calculated",
      "sensitivity" : {
        "sens" : float(sens),
        "dpi" : int(dpi),
        "yaw" : float(yaw),
        "win" : int(win),
        "rawinput" : str(self.size_rawinput.isChecked()),
        "size" : {
          "cm" : float(cm),
          "inch" : float(inch),

          "zoom" : {
            "ratio" : int(zoom),
            "cm" : float(zoomSens(cm, zoom)),
            "inch" : float(zoomSens(inch, zoom))
          }
        }
      }
    })
    saveHistory()
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
    size = (360 / (cfg["m_yaw"] * dpi * sens))

    # final result
    cm   = roundSens(size * 2.54) # 2.54 == inch size
    inch = roundSens(size)

    # shows result for "cm" and "in" /360
    self.random_gen_sens.setText(str(sens))
    self.random_gen_dpi.setText(str(dpi))
    self.random_gen_cm.setText(str(cm)) # cm
    self.random_gen_in.setText(str(inch)) # in

    # gets the current date and time
    date = datetime.datetime.now()

    # create a string with date in it: yyyy-mm-dd
    calendarDate = date.strftime("%Y-%m-%d")
    sensDate = date.strftime("%Y-%m-%d %H:%M:%S")

    # dict that will be saved to 
    # history.json when the sensitivity 
    # is generated
    if history.get(calendarDate, None) == None:
      history[calendarDate] = []

    history[calendarDate].append({
      "date" : sensDate,
      "type" : "generated",
      "sensitivity" : {
        "sens" : float(sens),
        "dpi" : int(dpi),
        "yaw" : float(cfg["m_yaw"]),
        "win" : 6,
        "rawinput" : "True",
        "size" : {
          "cm" : float(cm),
          "inch" : float(inch),

          "zoom" : {
            "ratio" : 1,
            "cm" : float(cm),
            "inch" : float(inch)
          }
        }
      }
    })
    saveHistory()
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
    calc = (360 / (cfg["m_yaw"] * dpi * sens))

    if self.convert_all.isChecked():
      # get the dpi list for the mouse
      dpiList = self.AllDPIMouse()
      listText = ''

      for d in dpiList:
        raw = 360 / calc
        newSens = round(raw / d / cfg["m_yaw"], 2)
        listText += "DPI: " + str(d) + "\nSensitivity: " + str(newSens) + "\n\n"

      # set the label with the sens list
      self.convert_list.setText(str(listText))
    else:
      newDPI = int(len(self.convert_new_dpi.text()) > 0 and self.convert_new_dpi.text() or 400)
      raw = 360 / calc
      newSens = round(raw / newDPI / cfg["m_yaw"], 2)
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

