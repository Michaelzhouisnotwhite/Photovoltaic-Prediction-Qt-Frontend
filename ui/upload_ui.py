# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'upload.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
from . import resource_rc

class Ui_UploadMainWindow(object):
    def setupUi(self, UploadMainWindow):
        if not UploadMainWindow.objectName():
            UploadMainWindow.setObjectName(u"UploadMainWindow")
        UploadMainWindow.resize(785, 470)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UploadMainWindow.sizePolicy().hasHeightForWidth())
        UploadMainWindow.setSizePolicy(sizePolicy)
        UploadMainWindow.setMaximumSize(QSize(785, 470))
        UploadMainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(UploadMainWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.baseWidget = QWidget(UploadMainWindow)
        self.baseWidget.setObjectName(u"baseWidget")
        self.baseWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(self.baseWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 4, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(111, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.baseWidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QSize(17, 58))
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_5 = QSpacerItem(141, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.browseComputerBtn = QPushButton(self.widget_2)
        self.browseComputerBtn.setObjectName(u"browseComputerBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.browseComputerBtn.sizePolicy().hasHeightForWidth())
        self.browseComputerBtn.setSizePolicy(sizePolicy1)
        self.browseComputerBtn.setMinimumSize(QSize(183, 39))
        self.browseComputerBtn.setMaximumSize(QSize(183, 39))
        self.browseComputerBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.browseComputerBtn.setStyleSheet(u"background-color: rgb(26, 115, 232);\n"
"font: 14pt \"PingFang SC\";\n"
"font: 14pt \"Alibaba PuHuiTi 2.0 55 Regular\";\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"SimHei\";\n"
"border-width: 2px;\n"
"border-radius: 8px;\n"
"")

        self.horizontalLayout.addWidget(self.browseComputerBtn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)


        self.gridLayout.addWidget(self.widget_2, 2, 1, 2, 1)

        self.uploadStackedWidget = QStackedWidget(self.baseWidget)
        self.uploadStackedWidget.setObjectName(u"uploadStackedWidget")
        self.uploadStackedWidget.setMinimumSize(QSize(500, 0))
        self.uploadStackedWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.uploadStackedWidget.setLayoutDirection(Qt.LeftToRight)
        self.uploadStackedWidget.setStyleSheet(u"QStackedWidget {\n"
"border: 2px dotted rgb(0, 0, 0);\n"
"border-radius: 8px;\n"
"width: 40%;}")
        self.uploadStackedWidget.setFrameShape(QFrame.StyledPanel)
        self.uploadStackedWidget.setFrameShadow(QFrame.Raised)
        self.stackedWidgetPage1 = QWidget()
        self.stackedWidgetPage1.setObjectName(u"stackedWidgetPage1")
        self.verticalLayout_2 = QVBoxLayout(self.stackedWidgetPage1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_5 = QWidget(self.stackedWidgetPage1)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.widget_5.setAcceptDrops(True)
        self.verticalLayout_4 = QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 33, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.chooseFileBtn = QPushButton(self.widget_5)
        self.chooseFileBtn.setObjectName(u"chooseFileBtn")
        self.chooseFileBtn.setAcceptDrops(True)
        self.chooseFileBtn.setStyleSheet(u"border: 0px;\n"
"font: 700 16pt \"Microsoft YaHei UI\";")

        self.verticalLayout_4.addWidget(self.chooseFileBtn)

        self.uploadCsvBtn = QPushButton(self.widget_5)
        self.uploadCsvBtn.setObjectName(u"uploadCsvBtn")
        self.uploadCsvBtn.setAcceptDrops(True)
        self.uploadCsvBtn.setStyleSheet(u"border: 0px;\n"
"font: 10pt \"Microsoft YaHei UI\";")

        self.verticalLayout_4.addWidget(self.uploadCsvBtn)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.uploadStackedWidget.addWidget(self.stackedWidgetPage1)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_3 = QWidget(self.page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setLayoutDirection(Qt.LeftToRight)
        self.widget_3.setAutoFillBackground(False)
        self.widget_3.setStyleSheet(u"border-color: rgba(255, 255, 255, 0);\n"
"")
        self.fileUploadProgressBar = QProgressBar(self.widget_3)
        self.fileUploadProgressBar.setObjectName(u"fileUploadProgressBar")
        self.fileUploadProgressBar.setGeometry(QRect(90, 90, 300, 16))
        self.fileUploadProgressBar.setMinimumSize(QSize(100, 0))
        self.fileUploadProgressBar.setMaximumSize(QSize(300, 20))
        self.fileUploadProgressBar.setStyleSheet(u"\n"
"QProgressBar::chunk{\n"
"	background: rgb(189, 189, 189)\n"
"}")
        self.fileUploadProgressBar.setValue(15)
        self.fileIconWidget = QWidget(self.widget_3)
        self.fileIconWidget.setObjectName(u"fileIconWidget")
        self.fileIconWidget.setGeometry(QRect(140, 10, 71, 71))
        self.fileIconWidget.setStyleSheet(u"border-image: url(:/icon/icon/csv-64.png)")
        self.uploadCompleteLabel = QLabel(self.widget_3)
        self.uploadCompleteLabel.setObjectName(u"uploadCompleteLabel")
        self.uploadCompleteLabel.setGeometry(QRect(230, 50, 141, 31))
        self.uploadCompleteLabel.setStyleSheet(u"font: 14pt \"PingFang SC\";")
        self.fileNameLabel = QLabel(self.widget_3)
        self.fileNameLabel.setObjectName(u"fileNameLabel")
        self.fileNameLabel.setGeometry(QRect(230, 30, 241, 21))
        self.fileNameLabel.setStyleSheet(u"font: 11pt \"PingFang SC\";")

        self.verticalLayout_3.addWidget(self.widget_3)

        self.uploadStackedWidget.addWidget(self.page)

        self.gridLayout.addWidget(self.uploadStackedWidget, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.baseWidget)


        self.retranslateUi(UploadMainWindow)
        self.browseComputerBtn.clicked.connect(UploadMainWindow.browse_computer_btn_clicked)
        self.chooseFileBtn.clicked.connect(self.browseComputerBtn.click)
        self.uploadCsvBtn.clicked.connect(self.browseComputerBtn.click)

        self.uploadStackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(UploadMainWindow)
    # setupUi

    def retranslateUi(self, UploadMainWindow):
        UploadMainWindow.setWindowTitle(QCoreApplication.translate("UploadMainWindow", u"\u4e0a\u4f20\u6587\u4ef6", None))
        self.browseComputerBtn.setText(QCoreApplication.translate("UploadMainWindow", u"\u6d4f\u89c8\u60a8\u7684\u8ba1\u7b97\u673a", None))
        self.chooseFileBtn.setText(QCoreApplication.translate("UploadMainWindow", u"\u9009\u62e9\u60a8\u7684\u6587\u4ef6", None))
        self.uploadCsvBtn.setText(QCoreApplication.translate("UploadMainWindow", u"\u8bf7\u4e0a\u4f20.csv \u6587\u4ef6", None))
        self.uploadCompleteLabel.setText(QCoreApplication.translate("UploadMainWindow", u"\u6587\u4ef6\u4e0a\u4f20\u6210\u529f!", None))
        self.fileNameLabel.setText(QCoreApplication.translate("UploadMainWindow", u"abc.csv", None))
    # retranslateUi

