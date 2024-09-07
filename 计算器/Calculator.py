from PySide6.QtWidgets import QApplication, QWidget
from Calculator_UI import Ui_Form


class MyWindow(QWidget, Ui_Form):  # 多继承
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()  # 装订附加代码
        self.result = ''  # result初始化

    def bind(self):
        self.pushButton_0.clicked.connect(lambda: self.addnumber('0'))
        self.pushButton_1.clicked.connect(lambda: self.addnumber('1'))
        self.pushButton_2.clicked.connect(lambda: self.addnumber('2'))
        self.pushButton_3.clicked.connect(lambda: self.addnumber('3'))
        self.pushButton_4.clicked.connect(lambda: self.addnumber('4'))
        self.pushButton_5.clicked.connect(lambda: self.addnumber('5'))
        self.pushButton_6.clicked.connect(lambda: self.addnumber('6'))
        self.pushButton_7.clicked.connect(lambda: self.addnumber('7'))
        self.pushButton_8.clicked.connect(lambda: self.addnumber('8'))
        self.pushButton_9.clicked.connect(lambda: self.addnumber('9'))
        self.pushButton_plus.clicked.connect(lambda: self.addnumber('+'))
        self.pushButton_substract.clicked.connect(lambda: self.addnumber('-'))
        self.pushButton_multipy.clicked.connect(lambda: self.addnumber('*'))
        self.pushButton_division.clicked.connect(lambda: self.addnumber('/'))
        self.pushButton_point.clicked.connect(lambda: self.addnumber('.'))
        self.pushButton_calculate.clicked.connect(self.equal)
        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_back.clicked.connect(self.back)

    def addnumber(self, number):
        self.lineEdit.clear()
        self.result += number
        self.lineEdit.setText(self.result)

    def equal(self):
        self.numberResult = eval(self.result)
        self.lineEdit.setText(str(self.numberResult))

    def clear(self):
        self.result = ''
        self.lineEdit.clear()

    def back(self):
        self.result = self.result[:-1]
        self.lineEdit.setText(self.result)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
