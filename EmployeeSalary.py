# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EmployeeSalary.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Pay(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 100, 160, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Salepeople1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Salepeople1.setObjectName("Salepeople1")
        self.verticalLayout.addWidget(self.Salepeople1)
        self.Salepeople2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Salepeople2.setObjectName("Salepeople2")
        self.verticalLayout.addWidget(self.Salepeople2)
        self.Cook1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Cook1.setObjectName("Cook1")
        self.verticalLayout.addWidget(self.Cook1)
        self.Cook2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Cook2.setObjectName("Cook2")
        self.verticalLayout.addWidget(self.Cook2)
        self.DeliveryPeople1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.DeliveryPeople1.setObjectName("DeliveryPeople1")
        self.verticalLayout.addWidget(self.DeliveryPeople1)
        self.DeliveryPeople2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.DeliveryPeople2.setObjectName("DeliveryPeople2")
        self.verticalLayout.addWidget(self.DeliveryPeople2)
        self.ExitButton = QtWidgets.QPushButton(Form)
        self.ExitButton.setGeometry(QtCore.QRect(330, 270, 56, 17))
        self.ExitButton.setObjectName("ExitButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 191, 31))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.ExitButton.clicked.connect(lambda: self.closescr(Form))

    def closescr(self, Form):
            Form.hide()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Salepeople1.setText(_translate("Form", "SalePeople1"))
        self.Salepeople2.setText(_translate("Form", "SalePeople2"))
        self.Cook1.setText(_translate("Form", "Cook1"))
        self.Cook2.setText(_translate("Form", "Cook2"))
        self.DeliveryPeople1.setText(_translate("Form", "DeliveryPeople1"))
        self.DeliveryPeople2.setText(_translate("Form", "DeliveryPeople2"))
        self.ExitButton.setText(_translate("Form", "Exit"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#0410f1;\">Employee salary</span></p></body></html>"))
