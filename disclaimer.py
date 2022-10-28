from PyQt5 import QtCore, QtGui, QtWidgets
from graph1 import Ui_graph

class Ui_disc(object):

    def openGraph(self):
        self.window= QtWidgets.QDialog()
        self.ui=Ui_graph()
        self.ui.setupUi(self.window)
        self.window.show()    

    def setupUi(self, disc):
        disc.setObjectName("disc")
        disc.resize(1040, 600)
        self.widget = QtWidgets.QWidget(disc)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1040, 600))
        self.widget.setStyleSheet("QWidget#widget{\n"
"    background-image: url(:/bg/Images/disclaimer.jpeg);}")
        self.widget.setObjectName("widget")
        self.agreeBox = QtWidgets.QCheckBox(self.widget)
        self.agreeBox.setGeometry(QtCore.QRect(210, 460, 101, 31))

        self.agreeBox.stateChanged.connect(self.hidebtn)

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.agreeBox.setFont(font)
        self.agreeBox.setObjectName("agreeBox")
        self.proceedbtn = QtWidgets.QPushButton(self.widget, clicked= lambda:self.openGraph())
        self.proceedbtn.setGeometry(QtCore.QRect(480, 460, 81, 35))

        self.proceedbtn.hide()
        
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.proceedbtn.setFont(font)
        self.proceedbtn.setObjectName("proceedbtn")

        self.retranslateUi(disc)
        QtCore.QMetaObject.connectSlotsByName(disc)

    def retranslateUi(self, disc):
        _translate = QtCore.QCoreApplication.translate
        disc.setWindowTitle(_translate("disc", "Disclaimer"))
        self.agreeBox.setText(_translate("disc", "I agree"))
        self.proceedbtn.setText(_translate("disc", "Proceed"))

    def hidebtn(self, state):
        if self.agreeBox.isChecked() == True:
            self.proceedbtn.show() 
        else:
            self.proceedbtn.hide()

import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    disc = QtWidgets.QDialog()
    ui = Ui_disc()
    ui.setupUi(disc)
    disc.show()
    sys.exit(app.exec_())