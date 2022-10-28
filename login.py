from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from disclaimer import Ui_disc
import mysql.connector as con

class Ui_login(object):      

    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(1040, 600)
        self.widget = QtWidgets.QWidget(login)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1040, 600))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.widget.setFont(font)
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-image: url(:/bg/Images/login.jpeg);}")
        self.widget.setObjectName("widget")
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setGeometry(QtCore.QRect(478, 294, 268, 44))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.username.setFont(font)
        self.username.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(480, 384, 268, 44))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.password.setFont(font)
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.loginbtn = QtWidgets.QPushButton(self.widget)
        self.loginbtn.setGeometry(QtCore.QRect(461, 481, 114, 58))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.loginbtn.setFont(font)
        self.loginbtn.setObjectName("loginbtn")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

        self.loginbtn.clicked.connect(self.logdb)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Login"))
        self.loginbtn.setText(_translate("login", "Login"))

    def logPop(self):
        msg=QMessageBox()
        msg.setWindowTitle("Welcome Aboard!")
        msg.setText("Login Successful!")
        x=msg.exec_()
        self.window= QtWidgets.QDialog()
        self.ui=Ui_disc()
        self.ui.setupUi(self.window)
        self.window.show()

    def logPop1(self):
        msg=QMessageBox()
        msg.setWindowTitle("Invalid Credentials")
        msg.setText("Please try again!")
        x=msg.exec_()

    def logdb(self):
        un=self.username.text()
        pw=self.password.text()
        db= con.connect(host="localhost", user="root", password="2965", db="cryptoapp")
        cursor=db.cursor()
        cursor.execute("select * from userinfo where email = '"+ un +"' and passw ='"+ pw +"'")
        result = cursor.fetchone()
        if result:
            self.logPop()
        else:
            self.logPop1()
            self.username.setText("")
            self.password.setText("")

import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QDialog()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())