import math

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, \
    QLineEdit, QPushButton
from faker import Faker


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.page_count = 0
        self.page_size = 10
        self.resize(600, 400)
        self.fake = Faker(locale='zh_CN')
        self.data = [[self.fake.name(), self.fake.address(), self.fake.email()]]
        for count in range(50):
            self.data.append([self.fake.name(), self.fake.address(), self.fake.email()])
        print(self.data)

        self.lineSearch = QLineEdit()
        self.buttonSearch = QPushButton()
        self.TableWidget = QTableWidget()
        self.TableWidget.setRowCount(50)
        self.TableWidget.setColumnCount(3)
        self.TableWidget.setHorizontalHeaderLabels(["一", "二", "三"])
        self.TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.TableWidget.setSortingEnabled(True)

        for row_index, row in enumerate(self.data):
            for column_index, item in enumerate(row):
                self.TableWidget.setItem(row_index, column_index, QTableWidgetItem(item))

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.TableWidget)
        self.mainLayout.addWidget(self.lineSearch)
        self.mainLayout.addWidget(self.buttonSearch)
        self.buttonSearch.setText("搜索")
        self.setLayout(self.mainLayout)
        self.bind()

    def bind(self):
        # 点击单元格信号
        self.TableWidget.cellClicked.connect(lambda: print("选中单元格"))
        # 点击元素信号，输出
        self.TableWidget.itemClicked.connect(lambda: print(self.TableWidget.selectedItems()))
        self.buttonSearch.clicked.connect(self.search)

    def show_data(self):
        pass

    def init_table(self):
        self.page_count = math.ceil(len(self.data) / self.page_size)

    def search(self):
        search_context = self.lineSearch.text()
        result = self.TableWidget.findItems(search_context, Qt.MatchFlag.MatchContains)
        for row_index, row in enumerate(self.data):
            for column_index, item in enumerate(row):
                self.TableWidget.item(row_index, column_index).setBackground(Qt.GlobalColor.white)

        for item in result:
            item.setBackground(Qt.GlobalColor.red)
            print(f"搜索到了第{item.row()}行,第{item.column()}列")

        self.TableWidget.scrollToItem(result[0], QTableWidget.ScrollHint.PositionAtTop)


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
