# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trans.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(258, 236)
        Form.setStyleSheet(u".QComboBox{\n"
"    border-radius:0%;\n"
"    border:1px solid black;\n"
"}\n"
"\n"
".QLineEdit{\n"
"    border-radius:5%;\n"
"    border:1px solid black;\n"
"}\n"
"\n"
".QComboBox:hover{\n"
"    background-color: rgb(200,255,255);\n"
"}\n"
"\n"
".QLineEdit:hover{\n"
"    background-color: rgb(200,255,255);\n"
"}")
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(40, 30))

        self.gridLayout.addWidget(self.comboBox_2, 4, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.lineEdit_2, 4, 0, 1, 1)

        self.comboBox_1 = QComboBox(Form)
        self.comboBox_1.setObjectName(u"comboBox_1")
        self.comboBox_1.setMinimumSize(QSize(50, 30))
        self.comboBox_1.setMaximumSize(QSize(100, 16777215))
        self.comboBox_1.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.comboBox_1, 3, 1, 1, 1)

        self.lineEdit_1 = QLineEdit(Form)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setMinimumSize(QSize(30, 30))
        self.lineEdit_1.setMaximumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.lineEdit_1, 3, 0, 1, 1)

        self.origin_data_label = QLabel(Form)
        self.origin_data_label.setObjectName(u"origin_data_label")
        self.origin_data_label.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(15)
        font.setItalic(False)
        self.origin_data_label.setFont(font)

        self.gridLayout.addWidget(self.origin_data_label, 0, 0, 1, 1)

        self.trans_data_label = QLabel(Form)
        self.trans_data_label.setObjectName(u"trans_data_label")
        self.trans_data_label.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.trans_data_label.setFont(font1)

        self.gridLayout.addWidget(self.trans_data_label, 1, 0, 1, 1)

        self.data_type_cobo = QComboBox(Form)
        self.data_type_cobo.setObjectName(u"data_type_cobo")

        self.gridLayout.addWidget(self.data_type_cobo, 2, 0, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8fdb\u5236\u8f6c\u6362\u5668", None))
        self.origin_data_label.setText(QCoreApplication.translate("Form", u"0", None))
        self.trans_data_label.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u70b9\u51fb\u8f6c\u6362", None))
    # retranslateUi

