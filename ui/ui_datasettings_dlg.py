# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'datasettings_dlg.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDialog, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_DataSettingDlg(object):
    def setupUi(self, DataSettingDlg):
        if not DataSettingDlg.objectName():
            DataSettingDlg.setObjectName(u"DataSettingDlg")
        DataSettingDlg.resize(366, 162)
        DataSettingDlg.setMinimumSize(QSize(366, 162))
        DataSettingDlg.setStyleSheet(u"  *[text=\"\u786e\u5b9a\"] {\n"
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
        self.verticalLayout = QVBoxLayout(DataSettingDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(DataSettingDlg)
        self.widget.setObjectName(u"widget")
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(10, 10, 8, 0)
        self.Label = QLabel(self.widget)
        self.Label.setObjectName(u"Label")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        self.Label.setFont(font)
        self.Label.setStyleSheet(u"\n"
"font: 700 15pt \"Microsoft YaHei UI\";")
        self.Label.setMargin(0)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.Label)

        self.nameSpaceEdit = QLineEdit(self.widget)
        self.nameSpaceEdit.setObjectName(u"nameSpaceEdit")
        self.nameSpaceEdit.setStyleSheet(u"\n"
"font: 500 15pt \"Microsoft YaHei UI\";")
        self.nameSpaceEdit.setMaxLength(32767)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameSpaceEdit)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"\n"
"font: 700 15pt \"Microsoft YaHei UI\";")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.seqLenSpinBox = QSpinBox(self.widget)
        self.seqLenSpinBox.setObjectName(u"seqLenSpinBox")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seqLenSpinBox.sizePolicy().hasHeightForWidth())
        self.seqLenSpinBox.setSizePolicy(sizePolicy)
        self.seqLenSpinBox.setMaximumSize(QSize(60, 16777215))
        self.seqLenSpinBox.setStyleSheet(u"\n"
"font: 500 15pt \"Microsoft YaHei UI\";")
        self.seqLenSpinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.seqLenSpinBox.setMinimum(2)
        self.seqLenSpinBox.setMaximum(1000)
        self.seqLenSpinBox.setValue(96)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.seqLenSpinBox)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"\n"
"font: 700 15pt \"Microsoft YaHei UI\";")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.predictLenSpinBox = QSpinBox(self.widget)
        self.predictLenSpinBox.setObjectName(u"predictLenSpinBox")
        self.predictLenSpinBox.setMaximumSize(QSize(60, 16777215))
        self.predictLenSpinBox.setStyleSheet(u"\n"
"font: 500 15pt \"Microsoft YaHei UI\";")
        self.predictLenSpinBox.setMinimum(1)
        self.predictLenSpinBox.setMaximum(1000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.predictLenSpinBox)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(DataSettingDlg)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(180, 10, 10, 10)
        self.okButton = QPushButton(self.widget_2)
        self.okButton.setObjectName(u"okButton")

        self.horizontalLayout.addWidget(self.okButton)

        self.cancelButton = QPushButton(self.widget_2)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(DataSettingDlg)

        QMetaObject.connectSlotsByName(DataSettingDlg)
    # setupUi

    def retranslateUi(self, DataSettingDlg):
        DataSettingDlg.setWindowTitle(QCoreApplication.translate("DataSettingDlg", u"\u5149\u4f0f\u9884\u6d4b\u8bbe\u7f6e", None))
        self.Label.setText(QCoreApplication.translate("DataSettingDlg", u"\u547d\u540d\u7a7a\u95f4\uff1a", None))
#if QT_CONFIG(tooltip)
        self.nameSpaceEdit.setToolTip(QCoreApplication.translate("DataSettingDlg", u"<html><head/><body><p>\u7ed9\u4f60\u7684\u6570\u636e\u96c6\u547d\u540d</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.nameSpaceEdit.setInputMask("")
        self.label.setText(QCoreApplication.translate("DataSettingDlg", u"\u8bad\u7ec3\u65f6\u95f4\u5c3a\u5ea6\uff1a", None))
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
        self.label_2.setText(QCoreApplication.translate("DataSettingDlg", u"\u9884\u6d4b\u957f\u5ea6\uff1a", None))
        self.okButton.setText(QCoreApplication.translate("DataSettingDlg", u"\u786e\u5b9a", None))
        self.cancelButton.setText(QCoreApplication.translate("DataSettingDlg", u"\u53d6\u6d88", None))
    # retranslateUi

