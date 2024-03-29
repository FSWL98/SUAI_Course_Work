# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1356, 848)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupTable = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupTable.setFont(font)
        self.groupTable.setAlignment(QtCore.Qt.AlignCenter)
        self.groupTable.setFlat(False)
        self.groupTable.setCheckable(False)
        self.groupTable.setObjectName("groupTable")
        self.mainTable = QtWidgets.QTableWidget(self.groupTable)
        self.mainTable.setGeometry(QtCore.QRect(320, 30, 961, 231))
        self.mainTable.setObjectName("mainTable")
        self.mainTable.setColumnCount(0)
        self.mainTable.setRowCount(0)
        self.illnesCombo = QtWidgets.QComboBox(self.groupTable)
        self.illnesCombo.setGeometry(QtCore.QRect(50, 130, 221, 31))
        self.illnesCombo.setObjectName("illnesCombo")
        self.illnesCombo.addItem("")
        self.illnesCombo.addItem("")
        self.illnesCombo.addItem("")
        self.createTable = QtWidgets.QPushButton(self.groupTable)
        self.createTable.setGeometry(QtCore.QRect(30, 180, 261, 28))
        self.createTable.setObjectName("createTable")
        self.verticalLayout.addWidget(self.groupTable)
        self.groupCompare = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupCompare.setFont(font)
        self.groupCompare.setAlignment(QtCore.Qt.AlignCenter)
        self.groupCompare.setObjectName("groupCompare")
        self.groupIllness = QtWidgets.QGroupBox(self.groupCompare)
        self.groupIllness.setGeometry(QtCore.QRect(30, 20, 191, 221))
        self.groupIllness.setObjectName("groupIllness")
        self.ariCheck = QtWidgets.QCheckBox(self.groupIllness)
        self.ariCheck.setGeometry(QtCore.QRect(20, 100, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ariCheck.setFont(font)
        self.ariCheck.setObjectName("ariCheck")
        self.anginaCheck = QtWidgets.QCheckBox(self.groupIllness)
        self.anginaCheck.setGeometry(QtCore.QRect(20, 160, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.anginaCheck.setFont(font)
        self.anginaCheck.setObjectName("anginaCheck")
        self.fluCheck = QtWidgets.QCheckBox(self.groupIllness)
        self.fluCheck.setGeometry(QtCore.QRect(20, 40, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.fluCheck.setFont(font)
        self.fluCheck.setObjectName("fluCheck")
        self.groupParams = QtWidgets.QGroupBox(self.groupCompare)
        self.groupParams.setGeometry(QtCore.QRect(270, 20, 351, 221))
        self.groupParams.setObjectName("groupParams")
        self.timeRadio = QtWidgets.QRadioButton(self.groupParams)
        self.timeRadio.setGeometry(QtCore.QRect(20, 40, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.timeRadio.setFont(font)
        self.timeRadio.setObjectName("timeRadio")
        self.sickRadio = QtWidgets.QRadioButton(self.groupParams)
        self.sickRadio.setGeometry(QtCore.QRect(20, 100, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.sickRadio.setFont(font)
        self.sickRadio.setObjectName("sickRadio")
        self.deathRadio = QtWidgets.QRadioButton(self.groupParams)
        self.deathRadio.setGeometry(QtCore.QRect(20, 160, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.deathRadio.setFont(font)
        self.deathRadio.setObjectName("deathRadio")
        self.createGraph = QtWidgets.QPushButton(self.groupCompare)
        self.createGraph.setEnabled(False)
        self.createGraph.setGeometry(QtCore.QRect(700, 120, 251, 31))
        self.createGraph.setObjectName("createGraph")
        self.verticalLayout.addWidget(self.groupCompare)
        self.circleGroup = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.circleGroup.setFont(font)
        self.circleGroup.setAlignment(QtCore.Qt.AlignCenter)
        self.circleGroup.setObjectName("circleGroup")
        self.createCircle = QtWidgets.QPushButton(self.circleGroup)
        self.createCircle.setGeometry(QtCore.QRect(150, 60, 111, 81))
        self.createCircle.setShortcut("")
        self.createCircle.setAutoRepeat(False)
        self.createCircle.setDefault(False)
        self.createCircle.setFlat(False)
        self.createCircle.setObjectName("createCircle")
        self.circleCombo = QtWidgets.QComboBox(self.circleGroup)
        self.circleCombo.setGeometry(QtCore.QRect(610, 80, 181, 31))
        self.circleCombo.setObjectName("circleCombo")
        self.circleCombo.addItem("")
        self.circleCombo.addItem("")
        self.circleCombo.addItem("")
        self.createIllnessCircle = QtWidgets.QPushButton(self.circleGroup)
        self.createIllnessCircle.setGeometry(QtCore.QRect(830, 80, 191, 28))
        self.createIllnessCircle.setObjectName("createIllnessCircle")
        self.paramsCombo = QtWidgets.QComboBox(self.circleGroup)
        self.paramsCombo.setGeometry(QtCore.QRect(610, 160, 181, 31))
        self.paramsCombo.setObjectName("paramsCombo")
        self.paramsCombo.addItem("")
        self.paramsCombo.addItem("")
        self.paramsCombo.addItem("")
        self.verticalLayout.addWidget(self.circleGroup)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupTable.setTitle(_translate("MainWindow", "Таблица"))
        self.illnesCombo.setItemText(0, _translate("MainWindow", "Грипп"))
        self.illnesCombo.setItemText(1, _translate("MainWindow", "ОРЗ"))
        self.illnesCombo.setItemText(2, _translate("MainWindow", "Ангина"))
        self.createTable.setText(_translate("MainWindow", "Построить таблицу"))
        self.groupCompare.setTitle(_translate("MainWindow", "Сравнение"))
        self.groupIllness.setTitle(_translate("MainWindow", "Болезни"))
        self.ariCheck.setText(_translate("MainWindow", "ОРЗ"))
        self.anginaCheck.setText(_translate("MainWindow", "Ангина"))
        self.fluCheck.setText(_translate("MainWindow", "Грипп"))
        self.groupParams.setTitle(_translate("MainWindow", "Параметры"))
        self.timeRadio.setText(_translate("MainWindow", "Длительность лечения"))
        self.sickRadio.setText(_translate("MainWindow", "Количество заболевших"))
        self.deathRadio.setText(_translate("MainWindow", "Количество смертельных исходов"))
        self.createGraph.setText(_translate("MainWindow", "Построить график сравнения"))
        self.circleGroup.setTitle(_translate("MainWindow", "Круговые диаграммы"))
        self.createCircle.setText(_translate("MainWindow", "Общая \n"
"статистика \n"
"смертности"))
        self.circleCombo.setItemText(0, _translate("MainWindow", "Грипп"))
        self.circleCombo.setItemText(1, _translate("MainWindow", "ОРЗ"))
        self.circleCombo.setItemText(2, _translate("MainWindow", "Ангина"))
        self.createIllnessCircle.setText(_translate("MainWindow", "Статистика"))
        self.paramsCombo.setItemText(0, _translate("MainWindow", "Смертность"))
        self.paramsCombo.setItemText(1, _translate("MainWindow", "Заболевания"))
        self.paramsCombo.setItemText(2, _translate("MainWindow", "Осложнения"))
