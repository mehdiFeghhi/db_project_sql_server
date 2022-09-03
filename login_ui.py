
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

from customer import Customer
from admin_ui import ui as admin_ui
from select_ui import ui as select_ui


class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(loginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.usernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameInput.setGeometry(QtCore.QRect(180, 210, 113, 25))
        self.usernameInput.setObjectName("usernameInput")
        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(180, 250, 113, 25))
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 210, 81, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 250, 81, 17))
        self.label_2.setObjectName("label_2")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(140, 310, 111, 25))
        self.loginButton.setObjectName("loginButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 220, 81, 17))
        self.label_3.setObjectName("label_3")
        self.passwordInputSignup = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInputSignup.setGeometry(QtCore.QRect(570, 250, 113, 25))
        self.passwordInputSignup.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInputSignup.setObjectName("passwordInputSignup")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(490, 160, 81, 17))
        self.label_4.setObjectName("label_4")
        self.usernameInputSignup = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameInputSignup.setGeometry(QtCore.QRect(570, 220, 113, 25))
        self.usernameInputSignup.setObjectName("usernameInputSignup")
        self.birthdayInput = QtWidgets.QDateEdit(self.centralwidget)
        self.birthdayInput.setGeometry(QtCore.QRect(570, 190, 111, 26))
        self.birthdayInput.setObjectName("birthdayInput")
        self.signupButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.signupButton_2.setGeometry(QtCore.QRect(530, 310, 111, 25))
        self.signupButton_2.setObjectName("signupButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(490, 250, 81, 17))
        self.label_5.setObjectName("label_5")
        self.lastInput = QtWidgets.QLineEdit(self.centralwidget)
        self.lastInput.setGeometry(QtCore.QRect(570, 160, 113, 25))
        self.lastInput.setObjectName("lastInput")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(490, 190, 81, 17))
        self.label_6.setObjectName("label_6")
        self.firstnameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.firstnameInput.setGeometry(QtCore.QRect(570, 130, 113, 25))
        self.firstnameInput.setObjectName("firstnameInput")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(490, 130, 81, 17))
        self.label_7.setObjectName("label_7")
        self.signupMsg = QtWidgets.QLabel(self.centralwidget)
        self.signupMsg.setGeometry(QtCore.QRect(520, 350, 121, 31))
        self.signupMsg.setAlignment(QtCore.Qt.AlignCenter)
        self.signupMsg.setObjectName("signupMsg")
        self.loginMsg = QtWidgets.QLabel(self.centralwidget)
        self.loginMsg.setGeometry(QtCore.QRect(140, 360, 121, 31))
        self.loginMsg.setAlignment(QtCore.Qt.AlignCenter)
        self.loginMsg.setObjectName("loginMsg")
        loginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        loginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loginWindow)
        self.statusbar.setObjectName("statusbar")
        loginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(loginWindow)

        self.loginButton.clicked.connect(lambda: self.login(loginWindow))
        self.signupButton_2.clicked.connect(lambda: self.signup(loginWindow))
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "Login"))
        self.label.setText(_translate("loginWindow", "Username:"))
        self.label_2.setText(_translate("loginWindow", "Password:"))
        self.loginButton.setText(_translate("loginWindow", "Login"))
        self.label_3.setText(_translate("loginWindow", "Username:"))
        self.label_4.setText(_translate("loginWindow", "Last name:"))
        self.signupButton_2.setText(_translate("loginWindow", "Sign up"))
        self.label_5.setText(_translate("loginWindow", "Password:"))
        self.label_6.setText(_translate("loginWindow", "Birthday:"))
        self.label_7.setText(_translate("loginWindow", "First name:"))
        self.signupMsg.setText(_translate("loginWindow", "LOG"))
        self.loginMsg.setText(_translate("loginWindow", "LOG"))

    def login(self, MainWindow):
        user_name = self.usernameInput.text()
        password = self.passwordInput.text()

        res = Customer.find_person_by(user_name, password)
        # print(res)
        if res[0] == "not find":
            self.loginMsg.setText("همچین کاربری وجود ندارد")

        elif res[0] == "find":

            cus = res[1]
            if 'admin' in cus.ctype:
                admin_ui.setupUi(MainWindow, cus)
            elif 'normal' in cus.ctype:
                # print("hi")
                select_ui.setupUi(MainWindow, cus)
            else:
                self.loginMsg.setText(
                    "مشکلاتی در سمت دیتابیس ")
        else:
            self.loginMsg.setText("مشکلاتی از سمت سیستم ")

    def signup(self, loginWindow):

        first_name = self.firstnameInput.text()
        last_name = self.lastInput.text()
        birthday = self.birthdayInput.date().toPyDate()
        userename = self.usernameInputSignup.text()
        password = self.passwordInputSignup.text()
        time_enter = datetime.datetime.now()
        cus = Customer(userename, first_name, last_name, str(password), time_enter, birthday, "normal")
        res = cus.insert_customer()
        self.signupMsg.setText(res)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QMainWindow()
    ui = Ui_loginWindow()
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())
