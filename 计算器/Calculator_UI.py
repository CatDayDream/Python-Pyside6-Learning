# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Calculator.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(325, 344)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 30, 271, 31))
        self.lineEdit.setReadOnly(True)
        self.pushButton_calculate = QPushButton(Form)
        self.pushButton_calculate.setObjectName(u"pushButton_calculate")
        self.pushButton_calculate.setGeometry(QRect(80, 290, 171, 41))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 110, 271, 171))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_1 = QPushButton(self.widget)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.verticalLayout.addWidget(self.pushButton_1)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_7 = QPushButton(self.widget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout.addWidget(self.pushButton_7)

        self.pushButton_0 = QPushButton(self.widget)
        self.pushButton_0.setObjectName(u"pushButton_0")

        self.verticalLayout.addWidget(self.pushButton_0)

        self.pushButton_point = QPushButton(self.widget)
        self.pushButton_point.setObjectName(u"pushButton_point")

        self.verticalLayout.addWidget(self.pushButton_point)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_8 = QPushButton(self.widget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_plus = QPushButton(self.widget)
        self.pushButton_plus.setObjectName(u"pushButton_plus")

        self.verticalLayout_2.addWidget(self.pushButton_plus)

        self.pushButton_substract = QPushButton(self.widget)
        self.pushButton_substract.setObjectName(u"pushButton_substract")

        self.verticalLayout_2.addWidget(self.pushButton_substract)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_3.addWidget(self.pushButton_6)

        self.pushButton_9 = QPushButton(self.widget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_3.addWidget(self.pushButton_9)

        self.pushButton_multipy = QPushButton(self.widget)
        self.pushButton_multipy.setObjectName(u"pushButton_multipy")

        self.verticalLayout_3.addWidget(self.pushButton_multipy)

        self.pushButton_division = QPushButton(self.widget)
        self.pushButton_division.setObjectName(u"pushButton_division")

        self.verticalLayout_3.addWidget(self.pushButton_division)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.widget1 = QWidget(Form)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(30, 60, 271, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_back = QPushButton(self.widget1)
        self.pushButton_back.setObjectName(u"pushButton_back")

        self.horizontalLayout_2.addWidget(self.pushButton_back)

        self.pushButton_clear = QPushButton(self.widget1)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.horizontalLayout_2.addWidget(self.pushButton_clear)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_calculate.setText(QCoreApplication.translate("Form", u"Calculate!", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_point.setText(QCoreApplication.translate("Form", u".", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_plus.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_substract.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_multipy.setText(QCoreApplication.translate("Form", u"x", None))
        self.pushButton_division.setText(QCoreApplication.translate("Form", u"/", None))
        self.pushButton_back.setText(QCoreApplication.translate("Form", u"Backspace", None))
        self.pushButton_clear.setText(QCoreApplication.translate("Form", u"Clear", None))
    # retranslateUi

