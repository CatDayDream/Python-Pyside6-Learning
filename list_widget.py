import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QPushButton, QLineEdit,\
    QLabel, QStyle
from faker import Faker
import os


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.info = ""
        self.fake = Faker(locale='zh_CN')
        # 添加控件
        self.lb = QLabel()
        self.listWidget = QListWidget()
        self.addButton = QPushButton()
        self.lineEdit = QLineEdit()
        # label中添加icon
        self.lb.setPixmap(self.style().standardPixmap(QStyle.StandardPixmap.SP_DialogOkButton))
        # 按钮中添加icon
        self.addButton.setIcon(QIcon(os.path.join(icon_dir, "print.ico")))
        # 列表中添加和插入元素
        self.listWidget.addItems(["Plan1", "Plan2"])
        self.listWidget.insertItems(1, ['6', '8'])
        # 添加上下文菜单
        self.deleteItem = QAction("删除")
        self.listWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.listWidget.addAction(self.deleteItem)
        # 设定列表元素选中状态
        self.listWidget.item(0).setCheckState(Qt.CheckState(False))
        # 添加控件到布局
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.listWidget)
        self.mainLayout.addWidget(self.lineEdit)
        self.mainLayout.addWidget(self.addButton)
        self.mainLayout.addWidget(self.lb)
        self.setLayout(self.mainLayout)
        self.bind()

    def bind(self):
        self.lineEdit.textChanged.connect(self.get_current_text)
        self.addButton.clicked.connect(lambda: self.listWidget.addItem(self.info))
        self.deleteItem.triggered.connect(lambda: self.listWidget.takeItem(self.listWidget.currentRow()))
        self.listWidget.itemChanged.connect(lambda: print(self.listWidget.currentItem().checkState()))
        self.listWidget.currentItemChanged.connect(self.output_current_item)

    def get_current_text(self):
        self.info = self.lineEdit.text()
        # 排序
        self.listWidget.sortItems(Qt.SortOrder.AscendingOrder)

    def output_current_item(self):
        print(self.listWidget.currentItem().text())


if __name__ == "__main__":
    root_dir = os.path.dirname(sys.argv[0])
    icon_dir = os.path.join(root_dir, 'icon')
    print(icon_dir)
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
