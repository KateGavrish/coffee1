import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1281, 799)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(15, 10, 1251, 661))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(800, 711, 113, 21))
        self.pushButton.setObjectName("pushButton")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(20, 710, 113, 21))
        self.name.setObjectName("name")
        self.fry = QtWidgets.QLineEdit(self.centralwidget)
        self.fry.setGeometry(QtCore.QRect(150, 710, 113, 21))
        self.fry.setObjectName("fry")
        self.mol = QtWidgets.QLineEdit(self.centralwidget)
        self.mol.setGeometry(QtCore.QRect(280, 710, 113, 21))
        self.mol.setObjectName("mol")
        self.plot = QtWidgets.QLineEdit(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(410, 710, 113, 21))
        self.plot.setObjectName("plot")
        self.cost = QtWidgets.QLineEdit(self.centralwidget)
        self.cost.setGeometry(QtCore.QRect(540, 710, 113, 21))
        self.cost.setObjectName("cost")
        self.count = QtWidgets.QLineEdit(self.centralwidget)
        self.count.setGeometry(QtCore.QRect(670, 710, 113, 21))
        self.count.setObjectName("count")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 690, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 690, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 690, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 690, 60, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(580, 690, 60, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(680, 690, 121, 16))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "добавить"))
        self.label.setText(_translate("MainWindow", "Название"))
        self.label_2.setText(_translate("MainWindow", "Обжарка"))
        self.label_3.setText(_translate("MainWindow", "Молотый"))
        self.label_4.setText(_translate("MainWindow", "описание"))
        self.label_5.setText(_translate("MainWindow", "цена"))
        self.label_6.setText(_translate("MainWindow", "объем упаковки"))


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("data/coffee.db")
        self.pushButton.clicked.connect(self.add)
        self.printing()

    def printing(self):
        self.cur = self.con.cursor()
        result = self.cur.execute("Select * from Coffee").fetchall()
        self.id = result[-1][0] + 1
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]) - 1)
        self.titles = [description[0] for description in self.cur.description]

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def add(self):
        cost = int(self.cost.text())
        count = int(self.count.text())
        fry = self.fry.text()
        mol = self.mol.text()
        name = self.name.text()
        plot = self.plot.text()

        self.cur.execute(f'''INSERT INTO Coffee VALUES({self.id}, "{name}", "{fry}", 
"{mol}", "{plot}", {cost}, {count})''')
        self.con.commit()
        self.printing()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

