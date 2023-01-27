from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class ld_data(object):

    def ld_labels(cursor, tableWidget):
        tableWidget.setColumnCount(12)
        row_list = ld_data.load_name_tables(cursor)
        tableWidget.setHorizontalHeaderLabels([x for x in row_list])

    def ld_data_main_window(cursor, tableWidget):
        sql = "SELECT * FROM gui_table"
        cursor.execute(sql)  # type: ignore
        result = cursor.fetchall()  # type: ignore
        row_count = 0
        for row in result:
            list = []
            for elem in row:
                list.append(elem)
            tableWidget.insertRow(row_count)
            for i in range(len(list)):
                item = QtWidgets.QTableWidgetItem()
                item.setData(QtCore.Qt.DisplayRole, list[i])  # type: ignore
                tableWidget.setItem(row_count, i, item)
                tableWidget.resizeColumnToContents(i)
            tableWidget.setItem(row_count, 2, QtWidgets.QTableWidgetItem(str(list[2])))  # type: ignore
            tableWidget.resizeColumnToContents(2)
            tableWidget.setItem(row_count, 7, QtWidgets.QTableWidgetItem(str(list[7])))  # type: ignore
            tableWidget.resizeColumnToContents(7)
        tableWidget.sortItems(0, QtCore.Qt.AscendingOrder)  # type: ignore

    def show_message(message, type):
        msg = QMessageBox()
        msg.setWindowTitle("Помощь")
        msg.setText(message)  # type: ignore
        msg.setIcon(type)  # type: ignore
        msg.exec_()

    def load_name_tables(cursor):
        sql1 = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'gui_table'"
        cursor.execute(sql1)  # type: ignore
        result_header = cursor.fetchall()  # type: ignore
        row_list = []
        for row in result_header:
            for elem in row:
                row_list.append(elem)
        return row_list

    def ld_data_add_window(cursor, tableWidget, column_name):
        sql = "SELECT " + column_name + " FROM gui_table"
        cursor.execute(sql)  # type: ignore
        result = cursor.fetchall()  # type: ignore
        row_count = 0
        list = []
        for row in result:
            list = []
            for elem in row:
                list.append(elem)
            tableWidget.insertRow(row_count)
            if (column_name == 'дата_рождения' or column_name == 'дата_отправления'):
                tableWidget.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(list[0])))  # type: ignore
            else:
                item = QtWidgets.QTableWidgetItem()
                item.setData(QtCore.Qt.DisplayRole, list[0])  # type: ignore
                tableWidget.setItem(row_count, 0, item)
            tableWidget.resizeColumnToContents(0)
        if (column_name == 'id'):
            tableWidget.sortItems(0, QtCore.Qt.AscendingOrder)  # type: ignore
