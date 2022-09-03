
from PyQt5 import QtCore, QtGui, QtWidgets

from cardit import Card
from commodity import Commodity
from customer import Customer
from number_of_commodity import Table_Between_commodity_cardit


class Ui_cartWindow(object):
    person = None
    card = None
    number_want = 0
    id_item = 0
    come_back_ui = None

    def setupUi(self, cartWindow, person: Customer, card_in_progress: Card, come_back_ui):
        cartWindow.setObjectName("cartWindow")
        cartWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(cartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.person = person
        self.card = card_in_progress
        self.come_back_ui = come_back_ui
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 140, 67, 17))
        self.label.setObjectName("label")
        self.cartCombo = QtWidgets.QComboBox(self.centralwidget)
        self.cartCombo.setGeometry(QtCore.QRect(240, 160, 251, 25))
        self.cartCombo.setObjectName("cartCombo")
        # self.cartCombo.addItem("")
        # self.cartCombo.addItem("")
        # self.cartCombo.addItem("")
        # self.cartCombo.addItem("")
        self.countSpin = QtWidgets.QSpinBox(self.centralwidget)
        self.countSpin.setGeometry(QtCore.QRect(500, 160, 48, 26))
        self.countSpin.setProperty("value", 3)
        self.countSpin.setObjectName("countSpin")
        self.userInfo = QtWidgets.QLabel(self.centralwidget)
        self.userInfo.setGeometry(QtCore.QRect(10, 10, 201, 91))
        self.userInfo.setObjectName("userInfo")
        self.buyButton = QtWidgets.QPushButton(self.centralwidget)
        self.buyButton.setGeometry(QtCore.QRect(330, 300, 89, 25))
        self.buyButton.setObjectName("buyButton")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(10, 510, 89, 25))
        self.clearButton.setObjectName("clearButton")
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        self.editButton.setGeometry(QtCore.QRect(330, 340, 89, 25))
        self.editButton.setObjectName("editButton")
        cartWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(cartWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        cartWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(cartWindow)
        self.statusbar.setObjectName("statusbar")
        cartWindow.setStatusBar(self.statusbar)

        self.retranslateUi(cartWindow)

        self.cartCombo.activated.connect(lambda: self.update_combox_item())
        self.buyButton.clicked.connect(lambda: self.buy_button_clicked(cartWindow))
        self.editButton.clicked.connect(lambda: self.edit_button_clicked(cartWindow))
        self.clearButton.clicked.connect(lambda: self.clearButton_clicked(cartWindow))
        self.countSpin.valueChanged.connect(lambda: self.change_count_spin())
        QtCore.QMetaObject.connectSlotsByName(cartWindow)

    def retranslateUi(self, cartWindow):
        _translate = QtCore.QCoreApplication.translate
        cartWindow.setWindowTitle(_translate("cartWindow", "Shop"))
        self.label.setText(_translate("cartWindow", "Cart"))


        if self.card.number_of_commodity is not None:
            for item in self.card.number_of_commodity:
                self.cartCombo.addItem(f"{item.commodity.name} | {item.commodity.price} | {item.number_of_commodity}")

            look_head_number_have = self.card.number_of_commodity[0].number_of_commodity
            self.countSpin.setValue(look_head_number_have)
            self.number_want = look_head_number_have
            self.id_item = self.card.number_of_commodity[0].commodity.id

        self.userInfo.setText(_translate("cartWindow", f"{self.person.first_name} {self.person.last_name}\n"
                                                       f"Date of birth: {self.person.birthday}\n"
                                                       f"Registery date: {self.person.time_entery.date()}\n"
                                                       f"total_amunt_of_card: {self.card.total_price_must_give}"))
        self.buyButton.setText(_translate("cartWindow", "Buy"))
        self.clearButton.setText(_translate("cartWindow", "Clear Cart"))
        self.editButton.setText(_translate("cartWindow", "Edit"))

    def update_combox_item(self):
        _translate = QtCore.QCoreApplication.translate

        try:
            number_in_combo_box = self.cartCombo.currentIndex()
            self.update_caridit()
            self.id_item = self.card.number_of_commodity[number_in_combo_box].commodity.id
            self.number_want = self.card.number_of_commodity[number_in_combo_box].number_of_commodity
        except Exception as ex:
            print(ex)
        self.countSpin.setValue(self.number_want)
        self.userInfo.setText(_translate("cartWindow", f"{self.person.first_name} {self.person.last_name}\n"
                                                       f"Date of birth: {self.person.birthday}\n"
                                                       f"Registery date: {self.person.time_entery.date()}\n"
                                                       f"total_amunt_of_card: {self.card.total_price_must_give}"))
    def change_count_spin(self):
        self.number_want = self.countSpin.value()
        # print(self.number_want)


    def update_caridit(self):
        find = False
        print(self.number_want)
        if self.number_want > 0 and (self.card is None):
            print("hey go1")
            try:
                create_card = Card(self.person.user_name, "", "in_progress", "", 1, [])
                create_card.insert_card()
                self.card = Card.find_in_process_card(self.person.user_name, "in_progress")[0]
                table_between = Table_Between_commodity_cardit(1, int(self.id_item), self.card.id, self.number_want,
                                                               Commodity.find_commodity_by(self.id_item))
                table_between.insert_tabel_between_commodity_and_card()
                find = True

            except Exception as ex:
                print(ex)

        elif self.card is not None:

            print("hey go2")

            for item in self.card.number_of_commodity:
                if int(item.id_commodity) == int(self.id_item):
                    print("offfff")
                    if int(item.number_of_commodity) == int(self.number_want):
                        find = True
                        break
                    else:
                        if int(self.number_want) > 0:
                            print("must be here")
                            table_between = Table_Between_commodity_cardit.find_table_between_commodity(item.id)
                            table_between.number_of_commodity = self.number_want
                            table_between.update_table_between_commodity_and_card()
                        else:
                            Table_Between_commodity_cardit.delete_tabel_between_commodity(item.id)
                        find = True
                        break
        print(find)
        print(self.number_want)
        if not find and self.number_want > 0:
            print("hey go3")

            # card = self.all_item_of_in_process_card[0]
            table_between = Table_Between_commodity_cardit(1, int(self.id_item), self.card.id, self.number_want,
                                                           Commodity.find_commodity_by(self.id_item))
            table_between.insert_tabel_between_commodity_and_card()

        else:
            print("hey go4")

        list_all_card_in_prograss = Card.find_in_process_card(self.person.user_name, "in_progress")
        if list_all_card_in_prograss is not None and len(list_all_card_in_prograss) > 0:
            self.card = Card.find_in_process_card(self.person.user_name, "in_progress")[0]

    def buy_button_clicked(self, card_window):

        self.update_caridit()
        self.card.flag = "END"
        self.card.update_card()
        self.come_back_ui.setupUi(card_window, self.person)

    def edit_button_clicked(self, card_window):

        self.update_caridit()
        self.come_back_ui.setupUi(card_window, self.person)


    def clearButton_clicked(self, card_window):

        self.update_caridit()

        self.card.flag = "DEL"
        self.card.update_card()
        self.come_back_ui.setupUi(card_window, self.person)



cart_ui = Ui_cartWindow()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    cartWindow = QtWidgets.QMainWindow()
    ui = Ui_cartWindow()
    ui.setupUi(cartWindow)
    cartWindow.show()
    sys.exit(app.exec_())
