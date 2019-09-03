import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtGui


class Calculation(QMainWindow):

    def __init__(self):

        super(Calculation, self).__init__()
        self.all = self.b_n = self.sale = self.cost = 0
        self.dima = self.lena = self.admis = self.decommis = 0
        self.setWindowTitle('Зарплата за день')
        self.setFixedSize(500, 300)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.center()
        self.message_box()

    def general_window(self):
        '''
        Draw all graphics
        '''
        menubar = self.menuBar()
        opt_ns_Menu = menubar.addMenu('&Опции')
        get_Action = QAction('&Рассчитать', self)
        get_Action.setShortcut('Ctrl+r')
        null_Action = QAction('&Обнулить', self)
        null_Action.setShortcut('Ctrl+e')
        exit_Action = QAction('&Выход', self)
        exit_Action.setShortcut('Ctrl+Q')
        get_Action.triggered.connect(self.clear_values)
        null_Action.triggered.connect(self.clear_values)
        exit_Action.triggered.connect(self.close)
        opt_ns_Menu.addAction(get_Action)
        opt_ns_Menu.addAction(null_Action)
        opt_ns_Menu.addAction(exit_Action)
        grid_layout = QGridLayout()
        self.central_widget.setLayout(grid_layout)

        self.table_money = QTableWidget()
        self.table_money.setColumnCount(4)
        self.table_money.setRowCount(5)
        self.table_money.setHorizontalHeaderLabels(['1', '2', '3', '4'])

        self.table_money.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
        self.table_money.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.table_money.horizontalHeaderItem(2).setTextAlignment(Qt.AlignHCenter)
        self.table_money.horizontalHeaderItem(3).setTextAlignment(Qt.AlignHCenter)

        self.table_money.setItem(0, 0, QTableWidgetItem("Всего: "))
        self.table_money.setItem(0, 1, QTableWidgetItem(str(self.help_lst[0])))
        self.table_money.setItem(1, 0, QTableWidgetItem("Безнал: "))
        self.table_money.setItem(1, 1, QTableWidgetItem(str(self.help_lst[1])))
        self.table_money.setItem(2, 0, QTableWidgetItem("Скидки: "))
        self.table_money.setItem(2, 1, QTableWidgetItem(str(self.help_lst[2])))
        self.table_money.setItem(3, 0, QTableWidgetItem("Расход: "))
        self.table_money.setItem(3, 1, QTableWidgetItem(str(self.help_lst[3])))
        self.table_money.setItem(4, 0, QTableWidgetItem("Остаток: "))
        self.table_money.setItem(4, 1, QTableWidgetItem(str(self.rest_money)))
        self.table_money.setItem(0, 2, QTableWidgetItem("Зарплата: "))
        self.table_money.setItem(0, 3, QTableWidgetItem(str(self.all_money)))
        self.table_money.setItem(1, 2, QTableWidgetItem("Списать: "))
        self.table_money.setItem(1, 3, QTableWidgetItem(str(self.help_lst[5])))
        self.table_money.setItem(2, 2, QTableWidgetItem("Довоз: "))
        self.table_money.setItem(2, 3, QTableWidgetItem(str(self.help_lst[4])))
        self.table_money.setItem(3, 2, QTableWidgetItem("Лена забрала: "))
        self.table_money.setItem(3, 3, QTableWidgetItem(str(self.help_lst[7])))
        self.table_money.setItem(4, 2, QTableWidgetItem("Дима забрал: "))
        self.table_money.setItem(4, 3, QTableWidgetItem(str(self.help_lst[6])))
        self.table_money.resizeColumnsToContents()
        grid_layout.addWidget(self.table_money, 0, 0)
        self.show()

    def message_box(self):
        '''
        Warning message of notConnection
        '''
        hello = QDialog(self)
        hello.setWindowTitle('Внимание')
        hello.setWindowModality(Qt.WindowModal)
        hello.setFixedSize(550, 320)
        lable_help = QLabel('Заполните пожалуйста', hello)
        lable_help.move(140, 15)
        thanks = QPushButton('Готово', hello)
        thanks.resize(thanks.sizeHint())
        thanks.adjustSize()
        thanks.setGeometry(320, 270, 200, 30)
        thanks.clicked.connect(self.calc_and_printer)

        self.x_line = 110
        self.y_line = 60
        self.line_all_money = QLineEdit(hello)
        self.line_all_money.move(self.x_line, self.y_line)
        self.lable_all_money = QLabel('Всего:', hello)
        self.lable_all_money.move(15, self.y_line)

        self.line_bn = QLineEdit(hello)
        self.line_bn.move(self.x_line, self.y_line+50)
        self.lable_bn = QLabel('Безнал:', hello)
        self.lable_bn.move(15, self.y_line+50)

        self.line_sale = QLineEdit(hello)
        self.line_sale.move(self.x_line, self.y_line+100)
        self.lable_sale = QLabel('Скидки: ', hello)
        self.lable_sale.move(15, self.y_line+100)

        self.line_сosts = QLineEdit(hello)
        self.line_сosts.move(self.x_line, self.y_line+150)
        self.lable_costs = QLabel('Расход: ', hello)
        self.lable_costs.move(15, self.y_line+150)

        self.line_admission = QLineEdit(hello)
        self.line_admission.move(self.x_line + 250, self.y_line)
        self.lable_admission = QLabel('Довоз: ', hello)
        self.lable_admission.move(240, self.y_line)

        self.line_decommissioned = QLineEdit(hello)
        self.line_decommissioned.move(self.x_line+250, self.y_line+50)
        self.lable_decommissioned = QLabel('Списать: ', hello)
        self.lable_decommissioned.move(240, self.y_line+50)

        self.line_dmitriy = QLineEdit(hello)
        self.line_dmitriy.move(self.x_line+250, self.y_line+100)
        self.lable_dmitriy = QLabel('Дима: ', hello)
        self.lable_dmitriy.move(240, self.y_line+100)

        self.line_elena = QLineEdit(hello)
        self.line_elena.move(self.x_line+250, self.y_line+150)
        self.lable_elena = QLabel('Лена: ', hello)
        self.lable_elena.move(240, self.y_line+150)
        self.set_fonts(lable_help, self.lable_all_money,
                       self.lable_bn, self.lable_sale,
                       self.lable_costs, self.lable_admission,
                       self.lable_decommissioned, self.lable_dmitriy,
                       self.lable_elena)
        self.set_lenght_size(self.line_all_money, self.line_bn,
                             self.line_sale, self.line_сosts,
                             self.line_admission, self.line_decommissioned,
                             self.line_dmitriy, self.line_elena)
        thanks.clicked.connect(hello.close)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        hello.exec()

    def set_lenght_size(self, *args):
        for widget in args:
            widget.setMaxLength(14)
            widget.setFixedSize(100, 30)

    def set_fonts(self, *args):
        for label in args:
            label.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Bold))

    def calc_and_printer(self):
        self.value_list = [self.line_all_money, self.line_bn,
                             self.line_sale, self.line_сosts,
                             self.line_admission, self.line_decommissioned,
                             self.line_dmitriy, self.line_elena]
        self.help_lst = [i for i in range(0, len(self.value_list))]
        help_variable = 0
        for data in self.value_list:
            i = data.text()
            if i == '':
                self.help_lst[help_variable] = 0
            else:
                self.help_lst[help_variable] = float(i)
            help_variable += 1
        '''
        Draw values in table
        '''
        self.all_money = 20 + (((self.help_lst[0] - self.help_lst[2]) / 100) * 5)
        self.rest_money = self.help_lst[0] - self.help_lst[1] - self.help_lst[2] - \
                          self.help_lst[3] - self.help_lst[6] - self.help_lst[7] - \
                          self.all_money
        self.general_window()

    def check_n_color(self):
        '''Check and color'''
        pass

    def clear_values(self):
        pass

    def center(self):
        '''
        Center on desktop
        '''
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculation()
    sys.exit(app.exec_())


