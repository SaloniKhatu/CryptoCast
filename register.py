from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from login import Ui_login
import mysql.connector as con
import os

class Ui_reg(object):

    def setupUi(self, reg):
        reg.setObjectName("reg")
        reg.resize(1040, 600)
        self.widget = QtWidgets.QWidget(reg)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1040, 600))
        self.widget.setStyleSheet("QWidget#widget{\n"
"    background-image: url(:/bg/Images/register.jpeg);}")
        self.widget.setObjectName("widget")
        self.name = QtWidgets.QLineEdit(self.widget)
        self.name.setGeometry(QtCore.QRect(241, 226, 290, 52))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.contact = QtWidgets.QLineEdit(self.widget)
        self.contact.setGeometry(QtCore.QRect(238, 393, 290, 52))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.contact.setFont(font)
        self.contact.setObjectName("contact")
        self.email = QtWidgets.QLineEdit(self.widget)
        self.email.setGeometry(QtCore.QRect(727, 230, 290, 52))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.email.setFont(font)
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(729, 393, 290, 53))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.password.setFont(font)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.regbtn = QtWidgets.QPushButton(self.widget)
        self.regbtn.setGeometry(QtCore.QRect(460, 487, 117, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.regbtn.setFont(font)
        self.regbtn.setObjectName("regbtn")       

        self.retranslateUi(reg)
        QtCore.QMetaObject.connectSlotsByName(reg)
        self.regbtn.clicked.connect(self.regdb)  

    def retranslateUi(self, reg):
        _translate = QtCore.QCoreApplication.translate
        reg.setWindowTitle(_translate("reg", "Register"))
        self.regbtn.setText(_translate("reg", "Register"))
    
    def showPop(self):
        msg=QMessageBox()
        msg.setWindowTitle("Oops")
        msg.setText("Invalid Email! Please create a new account!")
        x=msg.exec_()

    def showPop1(self):
        msg=QMessageBox()
        msg.setWindowTitle("Account Created!")
        msg.setText("Congratulations! Your account has been created!")
        x=msg.exec_()
        self.window= QtWidgets.QDialog()
        self.ui=Ui_login()
        self.ui.setupUi(self.window)
        self.window.show() 
    
    def regdb(self):
        nm=self.name.text()
        cntct=self.contact.text()
        em=self.email.text()
        pw=self.password.text()
        if self.name.text()=="" or self.contact.text()=="" or self.email.text()=="" or self.password.text()=="" :
            msg=QMessageBox()
            msg.setWindowTitle("Invalid format!")
            msg.setText("Revise your details!")
            x=msg.exec_()
            os._exit(0)
        db= con.connect(host="localhost", user="root", password="2965", db="cryptoapp")
        cursor=db.cursor()
        cursor.execute("Select * from userinfo where email='"+ em +"'and passw='"+ pw +"'")
        result = cursor.fetchone()

        if result:
            self.showPop()
            
        else:
            cursor.execute("insert into userinfo values ('"+ nm +"', '"+ em +"','"+ cntct +"','"+ pw +"')")
            db.commit()
            self.showPop1()
            
            self.name.setText("")
            self.contact.setText("")
            self.password.setText("")
            self.email.setText("")

import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    reg = QtWidgets.QDialog()
    ui = Ui_reg()
    ui.setupUi(reg)
    reg.show()
    sys.exit(app.exec_())