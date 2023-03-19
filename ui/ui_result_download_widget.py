# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'result_download_widget.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTreeWidget, QTreeWidgetItem, QWidget)
import resource_rc

class Ui_ResultDownloadWidget(object):
    def setupUi(self, ResultDownloadWidget):
        if not ResultDownloadWidget.objectName():
            ResultDownloadWidget.setObjectName(u"ResultDownloadWidget")
        ResultDownloadWidget.resize(615, 390)
        ResultDownloadWidget.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.gridLayout = QGridLayout(ResultDownloadWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(ResultDownloadWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"#downloadBtn {\n"
"	background: rgb(26, 115, 232);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 12pt \"PingFang SC\";\n"
"	border: 0px;\n"
"	border-radius: 10%;\n"
"	/*padding-left: 10px;\n"
"	padding-right: 10px;*/\n"
"	\n"
"\n"
"}\n"
"#downloadBtn:focus{\n"
"border-width: 1px;\n"
"	border-color: rgb(100, 100, 100);\n"
"	border-style: solid;\n"
"	border-radius: 10%;\n"
"}\n"
"#downloadBtn:disabled{\n"
"	\n"
"	background-color: rgb(203, 226, 255);\n"
"}\n"
"#downloadBtn:hover {\n"
"	background: rgb(52, 160, 255);\n"
"	font: 700 14pt \"Microsoft YaHei UI\";\n"
"	border: 0px;\n"
"}\n"
"#downloadBtn:pressed{\n"
"\n"
"	background-color: 	rgb(21, 92, 185);\n"
"}\n"
"#refreshBtn{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	border-radius: 10%;\n"
"	font: 12pt \"PingFang SC\";\n"
"}\n"
"#refreshBtn:hover{\n"
"	\n"
"	background-color:rgb(225, 225, 225);\n"
"}\n"
"#refreshBtn:pressed{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"#refreshBtn:disabled{\n"
"	\n"
"	background-color: rgb(240"
                        ", 240, 240);\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 0, 8, 0)
        self.infoLabel = QLabel(self.widget)
        self.infoLabel.setObjectName(u"infoLabel")
        self.infoLabel.setStyleSheet(u"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color: rgb(199, 33, 27);")

        self.horizontalLayout.addWidget(self.infoLabel)

        self.downloadBtn = QPushButton(self.widget)
        self.downloadBtn.setObjectName(u"downloadBtn")
        self.downloadBtn.setEnabled(True)
        self.downloadBtn.setMinimumSize(QSize(131, 41))
        self.downloadBtn.setMaximumSize(QSize(131, 41))
        self.downloadBtn.setStyleSheet(u"font: 700 11pt \"Microsoft YaHei UI\";")
        self.downloadBtn.setCheckable(False)

        self.horizontalLayout.addWidget(self.downloadBtn)

        self.refreshBtn = QPushButton(self.widget)
        self.refreshBtn.setObjectName(u"refreshBtn")
        self.refreshBtn.setMinimumSize(QSize(60, 41))
        self.refreshBtn.setMaximumSize(QSize(60, 41))
        icon = QIcon()
        icon.addFile(u":/icon/icon/refresh-128.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshBtn.setIcon(icon)

        self.horizontalLayout.addWidget(self.refreshBtn)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.dirTreeWidget = QTreeWidget(ResultDownloadWidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(1, u"2");
        __qtreewidgetitem.setText(0, u"1");
        self.dirTreeWidget.setHeaderItem(__qtreewidgetitem)
        self.dirTreeWidget.setObjectName(u"dirTreeWidget")
        self.dirTreeWidget.setMinimumSize(QSize(300, 144))
        self.dirTreeWidget.setMouseTracking(True)
        self.dirTreeWidget.setLayoutDirection(Qt.LeftToRight)
        self.dirTreeWidget.setStyleSheet(u"font: 11pt \"Microsoft YaHei UI\";")
        self.dirTreeWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.dirTreeWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.dirTreeWidget.setAnimated(True)
        self.dirTreeWidget.setWordWrap(True)
        self.dirTreeWidget.setColumnCount(2)
        self.dirTreeWidget.header().setCascadingSectionResizes(True)

        self.gridLayout.addWidget(self.dirTreeWidget, 1, 0, 1, 1)


        self.retranslateUi(ResultDownloadWidget)

        QMetaObject.connectSlotsByName(ResultDownloadWidget)
    # setupUi

    def retranslateUi(self, ResultDownloadWidget):
        ResultDownloadWidget.setWindowTitle(QCoreApplication.translate("ResultDownloadWidget", u"\u8bad\u7ec3\u7ed3\u679c\u4e0b\u8f7d", None))
        self.infoLabel.setText(QCoreApplication.translate("ResultDownloadWidget", u"\u63a5\u6536\u8bad\u7ec3\u7ed3\u679c\u4e2d", None))
        self.downloadBtn.setText(QCoreApplication.translate("ResultDownloadWidget", u"\u4e0b\u8f7d\u9009\u4e2d\u7684\u6587\u4ef6", None))
#if QT_CONFIG(shortcut)
        self.downloadBtn.setShortcut(QCoreApplication.translate("ResultDownloadWidget", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.refreshBtn.setText(QCoreApplication.translate("ResultDownloadWidget", u"\u5237\u65b0", None))
#if QT_CONFIG(shortcut)
        self.refreshBtn.setShortcut(QCoreApplication.translate("ResultDownloadWidget", u"F5", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

