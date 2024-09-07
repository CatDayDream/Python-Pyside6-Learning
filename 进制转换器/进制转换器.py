from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from trans import Ui_Form


class MyWindow(QWidget, Ui_Form):  # 多继承
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lengthVar = {'厘米': 1, '分米': 10, '米': 100, '千米': 1000}
        self.weightVar = {'克': 1, '斤': 500, '千克': 1000}
        self.TypeDict = {'长度': self.lengthVar, '质量': self.weightVar}

        self.comboBox_1.addItems(self.lengthVar.keys())
        self.comboBox_2.addItems(self.lengthVar.keys())
        self.data_type_cobo.addItems(self.TypeDict.keys())

        self.bind()

    def bind(self):
        self.data_type_cobo.currentTextChanged.connect(self.typeChanged)
        self.pushButton.clicked.connect(self.calculate)

    def calculate(self):
        bigType = self.data_type_cobo.currentText()
        # 获取第一个输入框的值
        value = self.lineEdit_1.text()
        if value == '':
            return

        currentType = self.comboBox_1.currentText()
        transType = self.comboBox_2.currentText()

        standardlization = float(value) * self.TypeDict[bigType][currentType]
        result = standardlization / self.TypeDict[bigType][transType]

        self.origin_data_label.setText(f'{value} {currentType} =')
        self.trans_data_label.setText(f'{result} {transType} ')
        self.lineEdit_2.setText(f'{result} {transType} ')

    def typeChanged(self, text):
        self.comboBox_1.clear()
        self.comboBox_2.clear()

        self.comboBox_1.addItems(self.TypeDict[text].keys())
        self.comboBox_2.addItems(self.TypeDict[text].keys())


if __name__ == '__main__':
    app = QApplication([])  # Qt应用程序
    window = MyWindow()  # 打开窗口
    window.show()  # 显示窗口
    app.exec()  # 执行应用程序
