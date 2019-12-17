import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem
from design import Ui_MainWindow
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


class myWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, flags=None, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)
        if flags is None:
            flags = []
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.mainTable.setColumnCount(5)
        self.ui.mainTable.setHorizontalHeaderLabels(('Месяц 2019 года', 'Количество заболевших', 'Количество людей с осложнениями',
                                                     'Число летальных исходов', 'Среднее время выздоровления'))
        self.ui.createTable.clicked.connect(self.createTable)
        self.ui.deathRadio.toggled.connect(self.radioToggled)
        self.ui.sickRadio.toggled.connect(self.radioToggled)
        self.ui.timeRadio.toggled.connect(self.radioToggled)
        self.ui.createGraph.clicked.connect(self.createGraph)
        self.ui.fluCheck.toggled.connect(self.checkToggled)
        self.ui.ariCheck.toggled.connect(self.checkToggled)
        self.ui.anginaCheck.toggled.connect(self.checkToggled)
        self.ui.createCircle.clicked.connect(self.createCircle)
        self.ui.createIllnessCircle.clicked.connect(self.createIllnessCircle)

    radio = ''
    activeIlls = []

    def setIllnesses(self, id, bool):
        self.illnesses[id][1] = bool

    def createTable(self):
        self.ui.mainTable.clear()
        self.ui.mainTable.setRowCount(12)
        flu = pd.read_excel('../test.xlsx', sheet_name=str(self.ui.illnesCombo.currentText()))
        array = flu.as_matrix()
        row = 0
        for tup in array:
            col = 0
            for item in tup:
                cellInfo = QTableWidgetItem(str(item))
                cellInfo.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.mainTable.setItem(row, col, cellInfo)
                col += 1
            row += 1
        self.ui.mainTable.setHorizontalHeaderLabels(
            ('Месяц 2019 года', 'Количество заболевших', 'Количество людей с осложнениями',
             'Число летальных исходов', 'Среднее время выздоровления'))
    def radioToggled(self):
        radioButton = self.sender()
        if(radioButton.isChecked()):
            self.radio = radioButton.text()
            self.ui.createGraph.setEnabled(True)

    def checkToggled(self):
        checkButton = self.sender()
        if(checkButton.isChecked()):
            self.activeIlls.append(checkButton.text())
        else:
            self.activeIlls.remove(checkButton.text())

    def createGraph(self):
        flu = (pd.read_excel('../test.xlsx', sheet_name='Грипп')).as_matrix()
        ari = (pd.read_excel('../test.xlsx', sheet_name='ОРЗ')).as_matrix()
        angina = (pd.read_excel('../test.xlsx', sheet_name='Ангина')).as_matrix()
        index = 1
        if self.radio == 'Длительность лечения':
            index = 4
        elif self.radio == 'Количество заболевших':
            index = 1
        elif self.radio == 'Количество смертельных исходов':
            index = 3
        months = []
        fluParams = []
        ariParams = []
        anginaParams = []
        for item in flu:
            months.append(item[0])
            fluParams.append(item[index])
        for item in ari:
            ariParams.append(item[index])
        for item in angina:
            anginaParams.append(item[index])
        trace_flu = go.Scatter(
            x = months,
            y = fluParams,
            mode = 'lines',
            name = 'Грипп'
        )
        trace_ari = go.Scatter(
            x = months,
            y = ariParams,
            mode = 'lines',
            name = 'ОРЗ'
        )
        trace_angina = go.Scatter(
            x = months,
            y = anginaParams,
            mode = 'lines',
            name = 'Ангина'
        )
        layout = go.Layout (
            title = self.radio
        )
        data = []
        if 'Грипп' in self.activeIlls:
            data.append(trace_flu)
        if 'ОРЗ' in self.activeIlls:
            data.append(trace_ari)
        if 'Ангина' in self.activeIlls:
            data.append(trace_angina)
        fig = go.Figure(data = data, layout = layout)
        fig.write_html('first_figure.html', auto_open=True)
    def createCircle(self):
        flu = (pd.read_excel('../test.xlsx', sheet_name='Грипп')).as_matrix()
        ari = (pd.read_excel('../test.xlsx', sheet_name='ОРЗ')).as_matrix()
        angina = (pd.read_excel('../test.xlsx', sheet_name='Ангина')).as_matrix()
        data = []
        names = ['Грипп', 'Ангина', 'ОРЗ']
        sum = 0
        for item in flu:
            sum += item[3]
        data.append(sum)
        sum = 0
        for item in angina:
            sum += item[3]
        data.append(sum)
        sum = 0
        for item in ari:
            sum += item[3]
        data.append(sum)
        fig = px.pie(values=data, names=names, title='Общая статистика смертности')
        fig.write_html('first_figure.html', auto_open=True)
    def createIllnessCircle(self):
        ill = str(self.ui.paramsCombo.currentText())
        index = 0
        if ill == 'Смертность':
            index = 3
        elif ill == 'Заболевания':
            index = 1
        elif ill == 'Осложнения':
            index = 2
        file = (pd.read_excel('../test.xlsx', sheet_name=str(self.ui.circleCombo.currentText()))).as_matrix()
        months = []
        data = []
        for item in file:
            months.append(item[0])
            data.append(item[index])
        fig = px.pie(values = data, names = months, title = 'Статистика болезни ' + str(self.ui.circleCombo.currentText()) +
                     ' по параметру ' + str(self.ui.paramsCombo.currentText()))
        fig.write_html('first_figure.html', auto_open=True)

app = QtWidgets.QApplication([])
win = myWindow()
win.show()

sys.exit(app.exec())
