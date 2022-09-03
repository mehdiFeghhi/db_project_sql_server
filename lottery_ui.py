# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lottery.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from customer import Customer


class Ui_lotteryWindow(object):

    list_of_all_old_customer = []
    def setupUi(self, lotteryWindow, ui, person):
        lotteryWindow.setObjectName("lotteryWindow")
        lotteryWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(lotteryWindow)
        self.centralwidget.setObjectName("centralwidget")
        try:
            self.list_of_all_old_customer = Customer.see_people_who_buy_more_than_one_year()
        except Exception as ex:
            print(ex)

        self.userCombo = QtWidgets.QComboBox(self.centralwidget)
        self.userCombo.setGeometry(QtCore.QRect(260, 130, 261, 25))
        self.userCombo.setObjectName("userCombo")
        # self.userCombo.addItem("")
        # self.userCombo.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 100, 111, 17))
        self.label.setObjectName("label")
        self.randomButton = QtWidgets.QPushButton(self.centralwidget)
        self.randomButton.setGeometry(QtCore.QRect(430, 100, 89, 25))
        self.randomButton.setObjectName("randomButton")
        self.userInfo = QtWidgets.QLabel(self.centralwidget)
        self.userInfo.setGeometry(QtCore.QRect(260, 180, 261, 91))
        self.userInfo.setObjectName("userInfo")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(340, 360, 89, 25))
        self.backButton.setObjectName("backButton")
        lotteryWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(lotteryWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        lotteryWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(lotteryWindow)
        self.statusbar.setObjectName("statusbar")
        lotteryWindow.setStatusBar(self.statusbar)
        self.comback_ui = ui
        self.person = person
        self.retranslateUi(lotteryWindow)
        self.backButton.clicked.connect(lambda: self.comback_ui.setupUi(lotteryWindow, self.person))
        self.randomButton.clicked.connect(lambda: self.random_clicked_button())
        QtCore.QMetaObject.connectSlotsByName(lotteryWindow)

    def retranslateUi(self, lotteryWindow):
        _translate = QtCore.QCoreApplication.translate
        lotteryWindow.setWindowTitle(_translate("lotteryWindow", "Lottery"))

        try:
            for item in self.list_of_all_old_customer:

                self.userCombo.addItem(f"{item.first_name} {item.last_name} | {item.time_entery.date()}")

            person_first = self.list_of_all_old_customer[0]
            self.userInfo.setText(_translate("lotteryWindow", f"{person_first.first_name} {person_first.last_name}\n"
                                                              f"Date of birth: {person_first.birthday}\n"
                                                              f"Registery date: {person_first.time_entery.date()}"))
        except Exception as ex:
            print(ex)

        self.label.setText(_translate("lotteryWindow", "Eligible Users"))
        self.randomButton.setText(_translate("lotteryWindow", "Random"))

        self.backButton.setText(_translate("lotteryWindow", "Back"))

    def chang_user_combo(self):
        _translate = QtCore.QCoreApplication.translate

        item_chose = self.userCombo.currentIndex()
        person = self.list_of_all_old_customer[item_chose]
        self.userInfo.setText(_translate("lotteryWindow", f"{person.first_name} {person.last_name}\n"
                                                          f"Date of birth: {person.birthday}\n"
                                                          f"Registery date: {person.time_entery.date()}"))

    def random_clicked_button(self):
        _translate = QtCore.QCoreApplication.translate

        person = Customer.lottery_for_people_that_buy_more_than_one_year()
        self.userInfo.setText(_translate("lotteryWindow", f"Winner: \n"
                                                          f"{person.first_name} {person.last_name}\n"
                                                          f"Date of birth: {person.birthday}\n"
                                                          f"Registery date: {person.time_entery.date()}"))

ui_lottery = Ui_lotteryWindow()
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    lotteryWindow = QtWidgets.QMainWindow()
    ui = Ui_lotteryWindow()
    ui.setupUi(lotteryWindow)
    lotteryWindow.show()
    sys.exit(app.exec_())
