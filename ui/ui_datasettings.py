# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'datasettings.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractSpinBox, QApplication, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_DataSettingDlg(object):
    def setupUi(self, DataSettingDlg):
        if not DataSettingDlg.objectName():
            DataSettingDlg.setObjectName(u"DataSettingDlg")
        DataSettingDlg.resize(344, 161)
        font = QFont()
        font.setPointSize(12)
        DataSettingDlg.setFont(font)
        DataSettingDlg.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(DataSettingDlg)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.predictLenSqinBox = QSpinBox(DataSettingDlg)
        self.predictLenSqinBox.setObjectName(u"predictLenSqinBox")
        self.predictLenSqinBox.setMaximumSize(QSize(60, 16777215))
        self.predictLenSqinBox.setStyleSheet(u"font: 500 15pt \"PingFang SC\";")
        self.predictLenSqinBox.setMinimum(1)
        self.predictLenSqinBox.setMaximum(1000)

        self.gridLayout.addWidget(self.predictLenSqinBox, 2, 3, 1, 1)

        self.nameSpaceEdit = QLineEdit(DataSettingDlg)
        self.nameSpaceEdit.setObjectName(u"nameSpaceEdit")
        self.nameSpaceEdit.setStyleSheet(u"font: 500 15pt \"PingFang SC\";")
        self.nameSpaceEdit.setMaxLength(32767)

        self.gridLayout.addWidget(self.nameSpaceEdit, 0, 3, 1, 1)

        self.label_2 = QLabel(DataSettingDlg)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 500 15pt \"PingFang SC\";")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.Label = QLabel(DataSettingDlg)
        self.Label.setObjectName(u"Label")
        self.Label.setStyleSheet(u"font: 500 15pt \"PingFang SC\";")

        self.gridLayout.addWidget(self.Label, 0, 0, 1, 1)

        self.seqLenSpinBox = QSpinBox(DataSettingDlg)
        self.seqLenSpinBox.setObjectName(u"seqLenSpinBox")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seqLenSpinBox.sizePolicy().hasHeightForWidth())
        self.seqLenSpinBox.setSizePolicy(sizePolicy)
        self.seqLenSpinBox.setMaximumSize(QSize(60, 16777215))
        self.seqLenSpinBox.setStyleSheet(u"font: 500 15pt \"PingFang SC\";")
        self.seqLenSpinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.seqLenSpinBox.setMinimum(2)
        self.seqLenSpinBox.setMaximum(1000)
        self.seqLenSpinBox.setValue(96)

        self.gridLayout.addWidget(self.seqLenSpinBox, 1, 3, 1, 1)

        self.label = QLabel(DataSettingDlg)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 500 15pt \"PingFang SC\";")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.okCancelBtnBox = QDialogButtonBox(DataSettingDlg)
        self.okCancelBtnBox.setObjectName(u"okCancelBtnBox")
        self.okCancelBtnBox.setStyleSheet(u" *[text=\"\u786e\u5b9a\"] {\n"
"	background: rgb(26, 115, 232);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 12pt \"PingFang SC\";\n"
"	border: 0px;\n"
"	border-radius: 10%;\n"
"	padding-left: 25px;\n"
"	padding-right: 25px;\n"
"	border-width: 1px;\n"
"	border-color: rgb(100, 100, 100);\n"
"	border-style: solid;\n"
"	border-radius: 10%;\n"
"}\n"
"\n"
"*[text=\"\u786e\u5b9a\"]:hover {\n"
"	background: rgb(52, 160, 255);\n"
"	font: 12pt \"PingFang SC\";\n"
"	border: 0px;\n"
"	border-radius: 10%;\n"
"}\n"
"\n"
" *[text=\"\u53d6\u6d88\"] {\n"
"	background: rgb(229, 229, 229);\n"
"	font: 12pt \"PingFang SC\";\n"
"	border-width: 1px;\n"
"	border-color: rgb(100, 100, 100);\n"
"	border-style: solid;\n"
"	border-radius: 10%;\n"
"	padding-left: 25px;\n"
"	padding-right: 25px;\n"
"}\n"
"\n"
" *[text=\"\u53d6\u6d88\"]:hover {\n"
"	background:rgb(255, 255, 255);\n"
"	font: 12pt \"PingFang SC\";\n"
"	border-style: solid;	\n"
"}")
        self.okCancelBtnBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.okCancelBtnBox.setCenterButtons(False)

        self.gridLayout.addWidget(self.okCancelBtnBox, 3, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        QWidget.setTabOrder(self.nameSpaceEdit, self.seqLenSpinBox)
        QWidget.setTabOrder(self.seqLenSpinBox, self.predictLenSqinBox)

        self.retranslateUi(DataSettingDlg)

        QMetaObject.connectSlotsByName(DataSettingDlg)
    # setupUi

    def retranslateUi(self, DataSettingDlg):
        DataSettingDlg.setWindowTitle(QCoreApplication.translate("DataSettingDlg", u"\u5149\u4f0f\u9884\u6d4b\u8bad\u7ec3\u4fe1\u606f", None))
#if QT_CONFIG(tooltip)
        self.nameSpaceEdit.setToolTip(QCoreApplication.translate("DataSettingDlg", u"<html><head/><body><p>\u7ed9\u4f60\u7684\u6570\u636e\u96c6\u547d\u540d</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.nameSpaceEdit.setInputMask("")
        self.label_2.setText(QCoreApplication.translate("DataSettingDlg", u"\u9884\u6d4b\u957f\u5ea6\uff1a", None))
        self.Label.setText(QCoreApplication.translate("DataSettingDlg", u"\u547d\u540d\u7a7a\u95f4\uff1a", None))
#if QT_CONFIG(tooltip)
        self.seqLenSpinBox.setToolTip(QCoreApplication.translate("DataSettingDlg", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'PingFang SC'; font-size:15pt; font-weight:500; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5c3d\u91cf\u662f2\u7684\u500d\u6570</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("DataSettingDlg", u"\u8bad\u7ec3\u65f6\u95f4\u5c3a\u5ea6\uff1a", None))
    # retranslateUi

