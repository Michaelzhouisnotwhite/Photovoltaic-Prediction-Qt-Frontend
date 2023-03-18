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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QSizePolicy,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_ResultDownloadWidget(object):
    def setupUi(self, ResultDownloadWidget):
        if not ResultDownloadWidget.objectName():
            ResultDownloadWidget.setObjectName(u"ResultDownloadWidget")
        ResultDownloadWidget.resize(672, 431)
        ResultDownloadWidget.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.verticalLayout = QVBoxLayout(ResultDownloadWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.treeWidget = QTreeWidget(ResultDownloadWidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(1, u"2");
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMinimumSize(QSize(300, 144))
        self.treeWidget.setMouseTracking(True)
        self.treeWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.treeWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setWordWrap(True)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.header().setCascadingSectionResizes(True)

        self.verticalLayout.addWidget(self.treeWidget)


        self.retranslateUi(ResultDownloadWidget)

        QMetaObject.connectSlotsByName(ResultDownloadWidget)
    # setupUi

    def retranslateUi(self, ResultDownloadWidget):
        ResultDownloadWidget.setWindowTitle(QCoreApplication.translate("ResultDownloadWidget", u"\u8bad\u7ec3\u7ed3\u679c\u4e0b\u8f7d", None))
    # retranslateUi

