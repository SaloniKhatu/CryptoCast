from PyQt5 import QtCore, QtGui, QtWidgets
import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt

from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential

class Ui_graph(object):
    def setupUi(self, graph):
        graph.setObjectName("graph")
        graph.resize(1040, 600)
        self.widget = QtWidgets.QWidget(graph)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1040, 600))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-image: url(:/bg/graph.jpeg);}")
        self.widget.setObjectName("widget")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(90, 120, 130, 31))
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
        self.graphbtn.setGeometry(QtCore.QRect(95, 440, 110, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.graphbtn.setFont(font)
        self.graphbtn.setObjectName("graphbtn")

        

        self.retranslateUi(graph)
        QtCore.QMetaObject.connectSlotsByName(graph)
        self.graphbtn.pressed.connect(self.storeval)
        self.graphbtn.pressed.connect(self.showgraph)


    def retranslateUi(self, graph):
        _translate = QtCore.QCoreApplication.translate
        graph.setWindowTitle(_translate("graph", "CryptoCast"))
        self.comboBox.setItemText(0, _translate("graph", "BTC"))
        self.comboBox.setItemText(1, _translate("graph", "ETH"))
        self.comboBox.setItemText(2, _translate("graph", "LTC"))
        self.comboBox.setItemText(3, _translate("graph", "DOGE"))
        self.comboBox.setItemText(4, _translate("graph", "XRP"))
        self.graphbtn.setText(_translate("graph", "Generate"))
        

    def storeval(self):
        self.crypval = self.comboBox.currentText()
        print(self.crypval)
        self.d1= 2019
        self.d2= 2021
        

    def showgraph(self):
        crypto_currency = self.crypval
        against_currency = 'INR'

        start = dt.datetime(self.d1, 1, 1)
        end = dt.datetime(self.d2, 1, 1)

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
        
        """model = Sequential()

        model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
        model.add(Dropout(0.2))
        model.add(LSTM(units=50, return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(units=50))
        model.add(Dropout(0.2))
        model.add(Dense(units=1))
        model.compile(optimizer='Adam', loss='mean_squared_error')
        model.fit(x_train, y_train, epochs=25, batch_size=32) """

    # Testing The Model

        test_start = dt.datetime(2020, 1, 1)
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

        plt.plot(actual_prices, color='red', label='Actual Prices')
        plt.plot(prediction_prices, color='blue', label='Predicted Prices')
        plt.title(f'{crypto_currency} Price Prediction')
        plt.xlabel('time')
        plt.ylabel('price')
        plt.legend(loc='upper left')
        plt.show()

    # Predict Next Day

        real_data = [model_inputs[len(model_inputs)+1-prediction_days: len(model_inputs)+1, 0]]
        real_data = np.array(real_data)
        real_data = np.reshape(real_data, (real_data.shape[0], real_data.shape[1], 1))

        prediction = model.predict(real_data)
        prediction = scaler.inverse_transform(prediction)
        print()


import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    graph = QtWidgets.QDialog()
    ui = Ui_graph()
    ui.setupUi(graph)
    graph.show()
    sys.exit(app.exec_())
