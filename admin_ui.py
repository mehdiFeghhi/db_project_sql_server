from PyQt5 import QtCore, QtGui, QtWidgets

import commodity
from cardit import Card
from category import Category
from customer import Customer
from commodity import Commodity
from lottery_ui import ui_lottery


class Ui_adminWindow(object):
    all_customer = Customer.all_normal()
    all_category = Category.find_all_category()
    commodity_recently = []
    admin_person = None

    def setupUi(self, adminWindow, person_obj: Customer):
        adminWindow.setObjectName("adminWindow")
        adminWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(adminWindow)
        self.admin_person = person_obj
        self.centralwidget.setObjectName("centralwidget")
        self.userCombo = QtWidgets.QComboBox(self.centralwidget)
        self.userCombo.setGeometry(QtCore.QRect(510, 40, 261, 25))
        self.userCombo.setObjectName("userCombo")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 40, 51, 17))
        self.label.setObjectName("label")
        self.cartCombo = QtWidgets.QComboBox(self.centralwidget)
        self.cartCombo.setGeometry(QtCore.QRect(510, 80, 261, 25))
        self.cartCombo.setObjectName("cartCombo")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 80, 51, 17))
        self.label_2.setObjectName("label_2")
        self.itemInfo = QtWidgets.QLabel(self.centralwidget)
        self.itemInfo.setGeometry(QtCore.QRect(510, 110, 261, 91))
        self.itemInfo.setObjectName("itemInfo")
        self.orderCombo = QtWidgets.QComboBox(self.centralwidget)
        self.orderCombo.setGeometry(QtCore.QRect(510, 210, 261, 25))
        self.orderCombo.setObjectName("orderCombo")

        self.orderInfo = QtWidgets.QLabel(self.centralwidget)
        self.orderInfo.setGeometry(QtCore.QRect(510, 250, 261, 101))
        self.orderInfo.setObjectName("orderInfo")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 210, 51, 17))
        self.label_3.setObjectName("label_3")
        self.categoryCombo = QtWidgets.QComboBox(self.centralwidget)
        self.categoryCombo.setGeometry(QtCore.QRect(100, 40, 261, 25))
        self.categoryCombo.setObjectName("categoryCombo")

        self.itemCombo = QtWidgets.QComboBox(self.centralwidget)
        self.itemCombo.setGeometry(QtCore.QRect(100, 80, 261, 25))
        self.itemCombo.setObjectName("itemCombo")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 40, 71, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 80, 71, 17))
        self.label_6.setObjectName("label_6")
        self.itemnameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.itemnameInput.setGeometry(QtCore.QRect(100, 150, 261, 25))
        self.itemnameInput.setObjectName("itemnameInput")
        self.priceInput = QtWidgets.QLineEdit(self.centralwidget)
        self.priceInput.setGeometry(QtCore.QRect(100, 310, 151, 25))
        self.priceInput.setDragEnabled(False)
        self.priceInput.setObjectName("priceInput")
        self.countryInput = QtWidgets.QLineEdit(self.centralwidget)
        self.countryInput.setGeometry(QtCore.QRect(100, 270, 151, 25))
        self.countryInput.setObjectName("countryInput")
        self.prodateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.prodateEdit.setGeometry(QtCore.QRect(100, 190, 110, 26))
        self.prodateEdit.setObjectName("prodateEdit")
        self.expdateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.expdateEdit.setGeometry(QtCore.QRect(100, 230, 110, 26))
        self.expdateEdit.setObjectName("expdateEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 150, 81, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 190, 71, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 230, 71, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 270, 71, 17))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 310, 71, 17))
        self.label_11.setObjectName("label_11")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(100, 370, 89, 25))
        self.addButton.setObjectName("addButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(200, 370, 89, 25))
        self.deleteButton.setObjectName("deleteButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 370, 71, 31))
        self.label_4.setObjectName("label_4")
        self.cnceledorderCombo = QtWidgets.QComboBox(self.centralwidget)
        self.cnceledorderCombo.setGeometry(QtCore.QRect(510, 370, 261, 25))
        self.cnceledorderCombo.setObjectName("cnceledorderCombo")
        self.cnceledorderCombo.addItem("")
        self.cnceledorderCombo.addItem("")
        self.canceledorderInfo = QtWidgets.QLabel(self.centralwidget)
        self.canceledorderInfo.setGeometry(QtCore.QRect(510, 400, 261, 101))
        self.canceledorderInfo.setObjectName("canceledorderInfo")
        self.lotteryButton = QtWidgets.QPushButton(self.centralwidget)
        self.lotteryButton.setGeometry(QtCore.QRect(350, 520, 89, 25))
        self.lotteryButton.setObjectName("lotteryButton")
        adminWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(adminWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        adminWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(adminWindow)
        self.statusbar.setObjectName("statusbar")
        adminWindow.setStatusBar(self.statusbar)

        self.retranslateUi(adminWindow)

        self.itemCombo.activated.connect(lambda: self.update_combox_item())
        self.cartCombo.activated.connect(lambda: self.show_cart_in_prograss_item())
        self.userCombo.activated.connect(lambda: self.user_change_combo())
        self.categoryCombo.activated.connect(lambda: self.update_combox_category())
        self.addButton.clicked.connect(lambda: self.add_update_item())
        self.deleteButton.clicked.connect(lambda: self.delete_item())
        self.lotteryButton.clicked.connect(lambda: self.lottery_button_clicked(adminWindow))
        QtCore.QMetaObject.connectSlotsByName(adminWindow)

    def retranslateUi(self, adminWindow):
        _translate = QtCore.QCoreApplication.translate
        adminWindow.setWindowTitle(_translate("adminWindow", "Admin Panel"))
        if self.all_customer[0] == 'find':
            for person in self.all_customer[1]:
                self.userCombo.addItem(
                    f"{person.user_name} | {person.first_name} {person.last_name} | {person.time_entery.date()}")

        self.label.setText(_translate("adminWindow", "User"))

        user_name = self.userCombo.currentText().split(' |')[0]
        list_of_in_progress_cart = Card.find_in_process_card(user_name, "in_progress")
        try:
            for item in list_of_in_progress_cart:
                for number_of_commodity in item.number_of_commodity:
                    self.cartCombo.addItem(
                        f"{number_of_commodity.id} | {number_of_commodity.commodity.name} | {number_of_commodity.number_of_commodity}")
        except Exception as ex:
            print(ex)

        list_of_all_cart = Card.find_all_card_of(user_name)
        try:
            for item in list_of_all_cart:
                self.orderCombo.addItem(
                    f"{item.id} | {item.total_price_must_give} | {item.flag}")
        except Exception as ex:
            print(ex)

        self.label_2.setText(_translate("adminWindow", "Cart"))
        try:
            id_pro = self.cartCombo.currentText().split(' | ')[1]
            com = Commodity.find_commodity_by(int(id_pro))
            self.itemInfo.setText(_translate("adminWindow", f"{com.name}\n"
                                                            f"{com.create_date}\n"
                                                            f"{com.expire_date}\n"
                                                            f"Made in {com.country}\n"
                                                            f"{com.price} $"))
        except Exception as ex:
            print(ex)

        # self.orderCombo.setItemText(0, _translate("adminWindow", "Order1"))
        # self.orderCombo.setItemText(1, _translate("adminWindow", "Order2"))
        try:
            for item in list_of_all_cart:
                self.orderCombo.addItem(
                    f"{item.id} | {item.total_price_must_give} | {item.flag}")
        except Exception as ex:
            print(ex)

        self.orderInfo.setText(_translate("adminWindow", "Order info\n"
                                                         "bla bla bla"))
        self.label_3.setText(_translate("adminWindow", "Order"))
        for item in self.all_category.keys():
            print(item)
            self.categoryCombo.addItem(item)

        self.itemCombo.addItem("Add New Item")
        print(self.categoryCombo.currentText())
        commodity_recently = Commodity.find_commodities_by(self.all_category.get(self.categoryCombo.currentText()))
        for item in commodity_recently:
            self.itemCombo.addItem(f"{item.id} |{item.name} | {item.price}")

        self.label_5.setText(_translate("adminWindow", "Category"))
        self.label_6.setText(_translate("adminWindow", "Item"))
        self.label_7.setText(_translate("adminWindow", "Item name"))
        self.label_8.setText(_translate("adminWindow", "Prod. date"))
        self.label_9.setText(_translate("adminWindow", "Exp. date"))
        self.label_10.setText(_translate("adminWindow", "Country"))
        self.label_11.setText(_translate("adminWindow", "Price"))
        self.addButton.setText(_translate("adminWindow", "Add/Update"))
        self.deleteButton.setText(_translate("adminWindow", "Delete"))
        self.label_4.setText(_translate("adminWindow", "Canceled\n"
                                                       "Order"))
        list_of_all_cart_cancel = Card.find_in_process_card(user_name, "DEL")
        try:
            for item in list_of_all_cart_cancel:
                self.canceledorderInfo.addItem(
                    f"{item.id} | {item.total_price_must_give} | {item.flag}")

        except Exception as ex:
            print(ex)

        # self.canceledorderInfo.setText(_translate("adminWindow", "Order info\n"
        #                                                          "bla bla bla"))
        self.lotteryButton.setText(_translate("adminWindow", "Lottery"))

    def update_combox_category(self):
        _translate = QtCore.QCoreApplication.translate

        self.itemCombo.clear()
        self.itemCombo.addItem("Add New Item")
        print(self.categoryCombo.currentText())
        self.commodity_recently = Commodity.find_commodities_by(self.all_category.get(self.categoryCombo.currentText()))
        for item in self.commodity_recently:
            self.itemCombo.addItem(f"{item.id} | {item.name} | {item.price}")

    def add_update_item(self):

        category_id = self.all_category.get(self.categoryCombo.currentText())
        expire_date = self.expdateEdit.date().toPyDate()
        create_date = self.prodateEdit.date().toPyDate()
        name = self.itemnameInput.text()
        price = self.priceInput.text()
        country = self.countryInput.text()
        if self.itemCombo.currentText() == 'Add New Item':

            cos = Commodity(1, category_id, create_date, expire_date, name, int(price), 'Have', country)
            print(cos)
            try:
                cos.insert_commodity()
            except Exception as ex:
                print(ex)

        else:
            id_item = self.itemCombo.currentText().split(' |')[0]
            print(id_item)
            try:
                cos = Commodity(int(id_item), category_id, create_date, expire_date, name, int(price), 'Have', country)
                cos.update_commodity()
            except Exception as ex:
                print(ex)

    def delete_item(self):
        category_id = self.all_category.get(self.categoryCombo.currentText())
        expire_date = self.expdateEdit.date().toPyDate()
        create_date = self.prodateEdit.date().toPyDate()
        name = self.itemnameInput.text()
        price = self.priceInput.text()
        country = self.countryInput.text()
        if self.itemCombo.currentText() == 'Add New Item':

            print("I cant delete this item")

        else:
            id_item = self.itemCombo.currentText().split(' |')[0]
            print(id_item)
            try:
                cos = Commodity(int(id_item), category_id, create_date, expire_date, name, int(price), 'Not have',
                                country)
                cos.update_commodity()
            except Exception as ex:
                print(ex)

    def update_combox_item(self):
        if self.itemCombo.currentText() == 'Add New Item':

            self.priceInput.setText("")
            self.itemnameInput.setText("")
            self.countryInput.setText("")

        else:
            id_item = self.itemCombo.currentText().split(' |')[0]
            print(id_item)
            try:
                cos = Commodity.find_commodity_by(id_item)
                self.priceInput.setText(str(cos.price))
                self.itemnameInput.setText(cos.name)
                self.countryInput.setText(cos.country)
                self.prodateEdit.setDate(cos.create_date)
                self.expdateEdit.setDate(cos.expire_date)

            except Exception as ex:
                print(ex)

    def show_cart_in_prograss_item(self):
        _translate = QtCore.QCoreApplication.translate

        try:
            print(self.cartCombo.currentText())
            id_pro = self.cartCombo.currentText().split(' | ')[1]
            com = Commodity.find_commodity_by(int(id_pro))
            self.itemInfo.setText(_translate("adminWindow", f"{com.name}\n"
                                                            f"{com.create_date}\n"
                                                            f"{com.expire_date}\n"
                                                            f"Made in {com.country}\n"
                                                            f"{com.price} $"))
        except Exception as ex:
            print(ex)

    def user_change_combo(self):
        _translate = QtCore.QCoreApplication.translate
        user_name = self.userCombo.currentText().split(' |')[0]
        print(user_name)
        list_of_in_progress_cart = Card.find_in_process_card(user_name, "in_progress")

        try:
            self.cartCombo.clear()
            for item in list_of_in_progress_cart:
                for number_of_commodity in item.number_of_commodity:
                    self.cartCombo.addItem(
                        f"{number_of_commodity.id} | {number_of_commodity.commodity.id} | {number_of_commodity.commodity.name} | {number_of_commodity.number_of_commodity}")

        except Exception as ex:
            self.cartCombo.clear()
            print(ex)
        list_of_all_cart = Card.find_all_card_of(user_name)

        try:
            self.orderCombo.clear()
            for item in list_of_all_cart:
                self.orderCombo.addItem(
                    f"{item.id} | {item.total_price_must_give} | {item.flag}")

        except Exception as ex:
            self.orderCombo.clear()

            print(ex)
        list_of_all_cart_cancel = Card.find_in_process_card(user_name, "DEL")

        try:
            self.cnceledorderCombo.clear()
            for item in list_of_all_cart_cancel:
                self.cnceledorderCombo.addItem(
                    f"{item.id} | {item.total_price_must_give} | {item.flag}")

        except Exception as ex:
            self.cnceledorderCombo.clear()

            print(ex)

    def lottery_button_clicked(self, adminWindow):
        ui_lottery.setupUi(adminWindow, ui, self.admin_person)


ui = Ui_adminWindow()
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    adminWindow = QtWidgets.QMainWindow()
    ui = Ui_adminWindow()
    ui.setupUi(adminWindow)
    adminWindow.show()
    sys.exit(app.exec_())
