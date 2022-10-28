from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
import os

from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler

class Ui_G2(object):
    def setupUi(self, G2):
        G2.setObjectName("G2")
        G2.resize(1040, 630)
        self.widget = QtWidgets.QWidget(G2)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1040, 630))
        self.widget.setStyleSheet("QWidget#widget{background-image: url(:/bg/Images/graphpg2.jpeg);}")
        self.widget.setObjectName("widget")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(120, 270, 130, 31))
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
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 410, 110, 31))
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
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(130, 480, 110, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 530, 110, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{rgb(170, 0, 0)}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(G2)
        self.pushButton.pressed.connect(self.storeval)
        self.pushButton.pressed.connect(self.showgraph)
        self.pushButton_2.pressed.connect(self.cwin)
        QtCore.QMetaObject.connectSlotsByName(G2)

    def retranslateUi(self, G2):
        _translate = QtCore.QCoreApplication.translate
        G2.setWindowTitle(_translate("G2", "CryptoCast"))
        self.comboBox.setItemText(0, _translate("G2", "BTC"))
        self.comboBox.setItemText(1, _translate("G2", "DOGE"))
        self.comboBox.setItemText(2, _translate("G2", "LTC"))
        self.comboBox.setItemText(3, _translate("G2", "CRV"))
        self.comboBox.setItemText(4, _translate("G2", "HNT"))
        self.comboBox.setItemText(5, _translate("G2", "ETH"))
        self.comboBox.setItemText(6, _translate("G2", "HBAR"))
        self.comboBox.setItemText(7, _translate("G2", "DASH"))
        self.comboBox.setItemText(8, _translate("G2", "MANA"))
        self.comboBox.setItemText(9, _translate("G2", "DOT"))
        self.comboBox_2.setItemText(0, _translate("G2", "2016"))
        self.comboBox_2.setItemText(1, _translate("G2", "2017"))
        self.comboBox_2.setItemText(2, _translate("G2", "2018"))
        self.comboBox_2.setItemText(3, _translate("G2", "2019"))
        self.comboBox_2.setItemText(4, _translate("G2", "2020"))
        self.comboBox_2.setItemText(5, _translate("G2", "2021"))
        self.pushButton.setText(_translate("G2", "Generate"))
        self.pushButton_2.setText(_translate("G2", "Logout"))

    def cwin(self):
        msg=QMessageBox()
        msg.setWindowTitle("Thank you!")
        msg.setText("You will be logged out now!")
        x=msg.exec_()
        os._exit(0)
        
    def storeval(self):
        self.crypval = self.comboBox.currentText()
        self.id1=self.comboBox_2.currentText()
        self.d1=int(self.id1)

    def showgraph(self):
        crypto_currency = self.crypval
        against_currency = 'INR'

        start = dt.datetime(self.d1, 1, 1)
        end = dt.datetime.now()

        data = web.DataReader(f'{crypto_currency}-{against_currency}', 'yahoo', start, end)

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
        test_end = dt.datetime.now()

        test_data = web.DataReader(f'{crypto_currency}-{against_currency}', 'yahoo', test_start, test_end)
        actual_prices = test_data['Close'].values

        total_dataset = pd.concat((data['Close'], test_data['Close']), axis=0)

        model_inputs = total_dataset[len(total_dataset)-len(test_data)-prediction_days:].values
        model_inputs = model_inputs.reshape(-1, 1)
        model_inputs = scaler.fit_transform(model_inputs)

        x_test = []

        for x in range(prediction_days, len(model_inputs)):
            x_test.append(model_inputs[x-prediction_days: x, 0])

        x_test = np.array(x_test)
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

        prediction_prices = model.predict(x_test)
        prediction_prices = scaler.inverse_transform(prediction_prices)

        plt.figure(figsize=(5,3))
        mngr=plt.get_current_fig_manager()
        mngr.window.setGeometry(750,420,550,395)
        plt.plot(actual_prices, color='red', label='Actual Prices')
        plt.plot(prediction_prices, color='blue', label='Predicted Prices')
        plt.title(f'{crypto_currency} Price Prediction')
        plt.xlabel('Time (in Days)')
        plt.ylabel('Price (in Rupees)')
        plt.legend(loc='upper left')
        plt.show()



import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    G2 = QtWidgets.QDialog()
    ui = Ui_G2()
    ui.setupUi(G2)
    G2.show()
    sys.exit(app.exec_())
