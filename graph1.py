from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as web
import datetime as dt

from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
from graph2 import Ui_G2


class Ui_graph(object):

    def finp(self):
        self.window= QtWidgets.QDialog()
        self.ui=Ui_G2()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, graph):
        graph.setObjectName("graph")
        graph.resize(1040, 630)
        self.widget = QtWidgets.QWidget(graph)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1040, 630))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-image:url(:/bg/Images/graphpg1.jpeg);}")
        self.widget.setObjectName("widget")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(120, 250, 130, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.graphbtn = QtWidgets.QPushButton(self.widget)
        self.graphbtn.setGeometry(QtCore.QRect(122, 450, 115, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.graphbtn.setFont(font)
        self.graphbtn.setObjectName("graphbtn")

        self.nextbtn = QtWidgets.QPushButton(self.widget ,clicked= lambda:self.finp())
        self.nextbtn.setGeometry(QtCore.QRect(98, 500, 190, 34))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.nextbtn.setFont(font)
        self.nextbtn.setObjectName("nextbtn")

        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 300, 130, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3.setGeometry(QtCore.QRect(100, 400, 85, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.widget)
        self.comboBox_4.setGeometry(QtCore.QRect(190, 400, 85, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")

        self.graphbtn.pressed.connect(self.storeval)
        self.graphbtn.pressed.connect(self.cryp1)
        self.graphbtn.pressed.connect(self.cryp2)

        self.retranslateUi(graph)
        QtCore.QMetaObject.connectSlotsByName(graph)

    def retranslateUi(self, graph):
        _translate = QtCore.QCoreApplication.translate
        graph.setWindowTitle(_translate("graph", "Comparision"))
        self.comboBox.setItemText(0, _translate("graph", "BTC"))
        self.comboBox.setItemText(1, _translate("graph", "DOGE"))
        self.comboBox.setItemText(2, _translate("graph", "LTC"))
        self.comboBox.setItemText(3, _translate("graph", "CRV"))
        self.comboBox.setItemText(4, _translate("graph", "HNT"))
        self.graphbtn.setText(_translate("graph", "Generate"))
        self.nextbtn.setText(_translate("graph", "Prediction Page"))
        self.comboBox_2.setItemText(0, _translate("graph", "ETH"))
        self.comboBox_2.setItemText(1, _translate("graph", "HBAR"))
        self.comboBox_2.setItemText(2, _translate("graph", "DASH"))
        self.comboBox_2.setItemText(3, _translate("graph", "MANA"))
        self.comboBox_2.setItemText(4, _translate("graph", "DOT"))
        self.comboBox_3.setItemText(0, _translate("graph", "2016"))
        self.comboBox_3.setItemText(1, _translate("graph", "2017"))
        self.comboBox_3.setItemText(2, _translate("graph", "2018"))
        self.comboBox_3.setItemText(3, _translate("graph", "2019"))
        self.comboBox_3.setItemText(4, _translate("graph", "2020"))
        self.comboBox_3.setItemText(5, _translate("graph", "2021"))
        self.comboBox_4.setItemText(0, _translate("graph", "2017"))
        self.comboBox_4.setItemText(1, _translate("graph", "2018"))
        self.comboBox_4.setItemText(2, _translate("graph", "2019"))
        self.comboBox_4.setItemText(3, _translate("graph", "2020"))
        self.comboBox_4.setItemText(4, _translate("graph", "2021"))
        self.comboBox_4.setItemText(5, _translate("graph", "2022"))

    def storeval(self):
        self.crypval = self.comboBox.currentText()
        self.crypval2 = self.comboBox_2.currentText()
        self.id1=self.comboBox_3.currentText()
        self.id2=self.comboBox_4.currentText()     
        self.d1=int(self.id1)
        self.d2=int(self.id2)

    def cryp1(self):
        self.crypto_currency = self.crypval
        against_currency = 'INR'

        start = dt.datetime(self.d1, 1, 1)
        end = dt.datetime(self.d2, 1, 1)

        data = web.DataReader(f'{self.crypto_currency}-{against_currency}', 'yahoo', start, end)

        # Preparing Data
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))

        prediction_days = 60

        x_train, y_train = [], []

        for x in range(prediction_days, len(scaled_data)):
            x_train.append(scaled_data[x-prediction_days:x, 0])
            y_train.append(scaled_data[x, 0])

        x_train, y_train = np.array(x_train), np.array(y_train)
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

        # Create Neural Network

        model=keras.models.load_model('complete_model/')

        # Testing The Model

        test_start = dt.datetime(self.d1, 1, 1)
        test_end = dt.datetime(self.d2, 1, 1)

        test_data = web.DataReader(f'{self.crypto_currency}-{against_currency}', 'yahoo', test_start, test_end)
        self.actual_prices = test_data['Close'].values

    def cryp2(self):
        self.crypto_currency2 = self.crypval2
        against_currency = 'INR'

        start = dt.datetime(self.d1, 1, 1)
        end = dt.datetime(self.d2, 1, 1)

        data = web.DataReader(f'{self.crypto_currency2}-{against_currency}', 'yahoo', start, end)

        # Preparing Data
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))

        prediction_days = 60

        x_train, y_train = [], []

        for x in range(prediction_days, len(scaled_data)):
            x_train.append(scaled_data[x-prediction_days:x, 0])
            y_train.append(scaled_data[x, 0])

        x_train, y_train = np.array(x_train), np.array(y_train)
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

        # Create Neural Network

        model=keras.models.load_model('complete_model/')

        # Testing The Model

        test_start = dt.datetime(self.d1, 1, 1)
        test_end = dt.datetime(self.d2, 1, 1)

        test_data = web.DataReader(f'{self.crypto_currency2}-{against_currency}', 'yahoo', test_start, test_end)
        self.actual_prices2 = test_data['Close'].values

        plt.figure(figsize=(5,3))
        mngr=plt.get_current_fig_manager()
        mngr.window.setGeometry(750,420,550,395)
        plt.plot(self.actual_prices, color='blue', label= f' {self.crypto_currency} Actual Prices ')
        plt.plot(self.actual_prices2, color='red', label=f' {self.crypto_currency2} Actual Prices')
        plt.title(f'{self.crypto_currency}'' vs 'f'{self.crypto_currency2} Price Comparision')
        plt.xlabel('Time (in Days)')
        plt.ylabel('Price (in Rupees)')
        plt.legend(loc='upper left')
        plt.show()

import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    graph = QtWidgets.QDialog()
    ui = Ui_graph()
    ui.setupUi(graph)
    graph.show()
    sys.exit(app.exec_())
