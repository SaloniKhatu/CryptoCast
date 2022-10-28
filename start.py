from PyQt5 import QtCore, QtGui, QtWidgets
from login import Ui_login
from register import Ui_reg

class Ui_start(object):

    def startLogin(self):
        self.window= QtWidgets.QDialog()
        self.ui=Ui_login()
        self.ui.setupUi(self.window)
        self.window.show()

    def startReg(self):
        self.window= QtWidgets.QDialog()
        self.ui=Ui_reg()
        self.ui.setupUi(self.window)
        self.window.show()     

    def setupUi(self, start):
        start.setObjectName("start")
        start.resize(1040, 600)
        self.widget = QtWidgets.QWidget(start)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1040, 600))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-image: url(:/bg/Images/Start.jpeg);}")
        self.widget.setObjectName("widget")
        self.startregbtn = QtWidgets.QPushButton(self.widget, clicked= lambda:self.startReg())
        self.startregbtn.setGeometry(QtCore.QRect(826, 268, 118, 64))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.startregbtn.setFont(font)
        self.startregbtn.setObjectName("startregbtn")
        self.startlogbtn = QtWidgets.QPushButton(self.widget, clicked= lambda:self.startLogin())
        self.startlogbtn.setGeometry(QtCore.QRect(822, 475, 125, 64))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.startlogbtn.setFont(font)
        self.startlogbtn.setObjectName("startlogbtn")    

        self.retranslateUi(start)
        QtCore.QMetaObject.connectSlotsByName(start)   

    def retranslateUi(self, start):
        _translate = QtCore.QCoreApplication.translate
        start.setWindowTitle(_translate("start", "CryptoCast"))
        self.startregbtn.setText(_translate("start", "Register"))
        self.startlogbtn.setText(_translate("start", "Login"))
import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    start = QtWidgets.QDialog()
    ui = Ui_start()
    ui.setupUi(start)
    start.show()
    sys.exit(app.exec_())