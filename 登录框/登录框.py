from PySide6.QtWidgets import QApplication, QWidget
from login import Ui_Form


class MyWindow(QWidget, Ui_Form):  # 多继承
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.loginfuc)  # pushButton对象，信号为点击click，连接至loginfuc函数

    def loginfuc(self):
        # 获取账号
        account = self.lineEdit.text()  # 输入框对象名为lineEdit，获取输入文本
        # 获取密码
        password = self.lineEdit_2.text()  # 输入框对象名为lineEdit_2，获取输入文本

        if account == '123' and password == '123':
            print('登陆成功')
        else:
            print('登陆失败')


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
