import datetime, uuid

from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtGui import QFont, QIcon, QPixmap, QRegion
from PyQt5.QtWidgets import QPushButton, QSizePolicy, QToolButton, QWidget, QLabel, QHBoxLayout


class UtilController:






    def getNow(self):
        return datetime.datetime.now()

    def getUIID(self):
        return str(uuid.uuid4())


class Constant:

    version = 'v0.01(proto)'
    region = 'A-03'

    #region WIDTH/HEIGHT

    piResolutionWidth = 800
    piResolutionHeight = 480

    widgetHeaderHeight = 50

    #endregion



    #region COLORS

    color_wgrBlue_hex = "#092C74;"
    color_wgrBlue_rgba = "rgba(9,44,116);"
    color_wgrBlue_rgba_opacity_6 = "rgba(9,44,116,0.6);"

    color_wgrDarkBlue_hex = "#05215C;"
    color_wgrDarkBlue_rgba = "rgba(5,33,92);"
    color_wgrDarkBlue_rgba_opacity_6 = "rgba(5,33,92,0.6);"

    color_wgrLightBlue_hex = "#0E368B;"
    color_wgrLightBlue_rgba = "rgba(14,54,139);"
    color_wgrLightBlue_rgba_opacity_6 = "rgba(14,54,139,0.6);"

    color_white_rgba_opacity_3 = "rgba(255,255,255,0.3);"
    color_yellow_rgba_opacity_3 = "rgba(255,255,0,0.3);"

    color_success_hex = "#44bd32;"
    color_success_rgba_opacity_10 = "rgba(76, 209, 55,1.0);"

    color_error_hex = "#e84118;"
    color_error_rgba_opacity_10 = "rgba(232, 65, 24,1.0);"

    color_warning_hex = "#fbc531;"
    color_warning_rgba_opacity_10 = "rgba(251, 197, 49,1.0);"

    color_darkgray_hex = "#273c75;"
    color_darkgray_rgba_opacity_10 = "rgba(39, 60, 117,1.0);"

    color_darksmoothgray = "#ced6e0;"
    color_darksmoothgray_rgba_opacity_10 = "rgba(206, 214, 224,1.0);"

    color_smoothgray = "#dfe4ea;"
    color_smoothgray_rgba_opacity_10 = "rgba(223, 228, 234,1.0);"

    #endregion




    #region IMAGES

    logo_nonbg = "asset/img/logo/nonbg_logo.png"
    bg_main_blur = "asset/img/bg/mainbg_blur.png"

    menu_icon_poweroff = "asset/img/icon/menu/poweroff.png"
    menu_icon_star = "asset/img/icon/menu/star.png"
    menu_icon_production = "asset/img/icon/menu/production.png"
    menu_icon_settings = "asset/img/icon/menu/settings.png"

    #endregion


    #region FONT

    font_fontSize10 = QFont()
    font_fontSize10.setPointSize(10)

    font_fontSize15 = QFont()
    font_fontSize15.setPointSize(15)

    font_fontSize20 = QFont()
    font_fontSize20.setPointSize(20)

    #endregion


class WButton(QPushButton):
    def __init__(self, txt):
        super(WButton, self).__init__()
        self.setText(txt)
        self.setFlat(True)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setFont(Constant().font_fontSize20)
        cssList = []
        cssList.append("WButton {")
        cssList.append("margin: 5px;")
        cssList.append("background-color: " + Constant().color_darksmoothgray)
        cssList.append("color: black;")
        cssList.append("border-style: outset;")
        cssList.append("border-color: " + Constant().color_white_rgba_opacity_3)
        cssList.append("border-radius: 3px;")
        cssList.append("border-width: 1px;")
        cssList.append("}")
        cssList.append("WButton:pressed {")
        cssList.append("background-color: " + Constant().color_yellow_rgba_opacity_3)
        cssList.append("color: white;")
        cssList.append("}")
        css = "".join(cssList)
        self.setStyleSheet(css)

class WMenuButton(QToolButton):
    def __init__(self, txt, icon):
        super(WMenuButton, self).__init__()
        self.setText(txt)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setFont(Constant().font_fontSize15)
        self.setIcon((QIcon(QPixmap(icon))))
        self.setIconSize(QSize(50, 50))
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        cssList = []
        cssList.append("WMenuButton {")
        cssList.append("margin: 5px;")
        cssList.append("padding-top: 25px;")
        cssList.append("background-color: " + Constant().color_wgrBlue_rgba_opacity_6)
        cssList.append("color: white;")
        cssList.append("border-style: outset;")
        cssList.append("border-color: " + Constant().color_wgrBlue_rgba_opacity_6)
        cssList.append("border-radius: 10px;")
        cssList.append("border-width: 1px;")
        cssList.append("}")
        cssList.append("WMenuButton:pressed {")
        cssList.append("background-color: " + Constant().color_yellow_rgba_opacity_3)
        cssList.append("color: white;")
        cssList.append("}")
        css = "".join(cssList)
        self.setStyleSheet(css)


class WLed(QPushButton):
    def __init__(self, ledType):
        super(WLed, self).__init__()
        self.setFixedWidth(12)
        self.setFixedHeight(12)
        cssList = []
        cssList.append("WLed {")
        cssList.append("background-color: " + ledType)
        cssList.append("border-style: outset;")
        cssList.append("border-color: black;")
        cssList.append("border-radius: 6px;")
        #cssList.append("border-width: 1px;")
        cssList.append("}")
        css = "".join(cssList)
        self.setStyleSheet(css)


class WLogo(QLabel):
    def __init__(self):
        super(WLogo, self).__init__()

        pixmap = QPixmap(Constant().logo_nonbg)
        self.setPixmap(pixmap)
        self.setFixedWidth(70)
        self.setScaledContents(True)
        self.setAlignment(Qt.AlignCenter)



class WHeader(QHBoxLayout):
    def __init__(self, lblLeft, lblRight):
        super(WHeader, self).__init__()

        labelLeft = QLabel(lblLeft)
        labelLeft.setFont(Constant().font_fontSize20)
        labelLeft.setStyleSheet("color: white;")
        labelLeft.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.addWidget(labelLeft)


        self.addWidget(WLogo())

        labelLeft = QLabel(lblRight)
        labelLeft.setFont(Constant().font_fontSize20)
        labelLeft.setStyleSheet("color: white;")
        labelLeft.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.addWidget(labelLeft)

class WFooter(QHBoxLayout):
    def __init__(self):
        super(WFooter, self).__init__()

        labelLeft = QLabel(Constant().version)
        labelLeft.setFont(Constant().font_fontSize10)
        labelLeft.setStyleSheet("color: white;")
        labelLeft.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.addWidget(labelLeft)

        ledOk = WLed(Constant().color_success_hex)
        self.addWidget(ledOk)

        ledWarning = WLed(Constant().color_warning_hex)
        self.addWidget(ledWarning)

        ledError = WLed(Constant().color_error_hex)
        self.addWidget(ledError)

        ledOff = WLed(Constant().color_darkgray_hex)
        self.addWidget(ledOff)

        labelRight = QLabel('20:57')
        labelRight.setFont(Constant().font_fontSize10)
        labelRight.setStyleSheet("color: white;")
        labelRight.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.addWidget(labelRight)

