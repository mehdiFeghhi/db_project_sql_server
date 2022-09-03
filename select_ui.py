
from PyQt5 import QtCore, QtGui, QtWidgets

from cardit import Card
from cart_ui import cart_ui
from category import Category
from commodity import Commodity
from customer import Customer
from number_of_commodity import Table_Between_commodity_cardit


class Ui_selectWindow(object):
    all_category = Category.find_all_category()
    all_item_of_in_process_card = []
    id_item = 0
    number_want = 0
    person = None

    def setupUi(self, selectWindow, person_obj: Customer):
        selectWindow.setObjectName("selectWindow")
        selectWindow.resize(800, 600)
        self.all_item_of_in_process_card = Card.find_in_process_card(person_obj.user_name, "in_progress")


        self.centralwidget = QtWidgets.QWidget(selectWindow)
        self.person = person_obj
        self.centralwidget.setObjectName("centralwidget")
        self.categoryCombo = QtWidgets.QComboBox(self.centralwidget)
        self.categoryCombo.setGeometry(QtCore.QRect(160, 150, 171, 25))
        self.categoryCombo.setObjectName("categoryCombo")


        self.categoryCombo.setItemText(4, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 120, 67, 17))
        self.label.setObjectName("label")
        self.itemCombo = QtWidgets.QComboBox(self.centralwidget)
        self.itemCombo.setGeometry(QtCore.QRect(340, 150, 261, 25))
        self.itemCombo.setObjectName("itemCombo")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 120, 67, 17))
        self.label_2.setObjectName("label_2")
        self.userInfo = QtWidgets.QLabel(self.centralwidget)
        self.userInfo.setGeometry(QtCore.QRect(10, 0, 201, 91))
        self.userInfo.setObjectName("userInfo")
        self.itemInfo = QtWidgets.QLabel(self.centralwidget)
        self.itemInfo.setGeometry(QtCore.QRect(160, 230, 501, 101))
        self.itemInfo.setObjectName("itemInfo")
        self.countSpin = QtWidgets.QSpinBox(self.centralwidget)
        self.countSpin.setGeometry(QtCore.QRect(610, 150, 48, 26))
        self.countSpin.setObjectName("countSpin")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 340, 141, 25))
        self.pushButton.setObjectName("pushButton")
        selectWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(selectWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        selectWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(selectWindow)
        self.statusbar.setObjectName("statusbar")
        selectWindow.setStatusBar(self.statusbar)


        self.retranslateUi(selectWindow, person_obj)

        self.categoryCombo.activated.connect(lambda: self.update_combox_category())
        self.itemCombo.activated.connect(lambda: self.update_combox_item())
        self.countSpin.valueChanged.connect(lambda: self.change_count_spin())

        self.pushButton.clicked.connect(lambda: self.pushButton_click(selectWindow))

        QtCore.QMetaObject.connectSlotsByName(selectWindow)

    def retranslateUi(self, selectWindow, person):
        _translate = QtCore.QCoreApplication.translate
        selectWindow.setWindowTitle(_translate("selectWindow", "Shop"))

        self.label.setText(_translate("selectWindow", "Category"))

        self.label_2.setText(_translate("selectWindow", "Item"))
        self.userInfo.setText(_translate("selectWindow", f"{person.first_name} {person.last_name}\n"
                                                         f"Date of birth: {person.birthday}\n"
                                                         f"Registery date: {person.time_entery.date()}"))

        for item in self.all_category.keys():
            print(item)
            self.categoryCombo.addItem(item)

        print(self.categoryCombo.currentText())
        commodity_recently = Commodity.find_commodities_by(self.all_category.get(self.categoryCombo.currentText()))
        for item in commodity_recently:
            self.itemCombo.addItem(f"{item.id} |{item.name} | {item.price}")

        id_item = self.itemCombo.currentText().split(' |')[0]
        try:
            com = Commodity.find_commodity_by(id_item)
            self.itemInfo.setText(_translate("selectWindow", f"{com.name}\n"
                                                             f"{com.create_date}\n"
                                                             f"{com.expire_date}\n"
                                                             f"Made in {com.country}\n"
                                                             f"{com.price} $"))
        except Exception as ex:
            print(ex)

        count = 0
        try:
            card = self.all_item_of_in_process_card[0]
            for item in card.number_of_commodity:
                if int(item.id_commodity) == int(id_item):
                    count = item.number_of_commodity
        except Exception as ex:
            print(ex)

        self.countSpin.setValue(count)
        self.id_item = id_item
        self.number_want = count
        self.pushButton.setText(_translate("selectWindow", "Show Cart and Buy"))

    def update_combox_category(self):

        _translate = QtCore.QCoreApplication.translate

        self.commodity_recently = Commodity.find_commodities_by(self.all_category.get(self.categoryCombo.currentText()))
        self.itemCombo.clear()
        for item in self.commodity_recently:

                self.itemCombo.addItem(f"{item.id} | {item.name} | {item.price}")

        id_item = self.itemCombo.currentText().split(' |')[0]
        try:
            self.update_caridit()
            com = Commodity.find_commodity_by(id_item)
            self.itemInfo.setText(_translate("selectWindow", f"{com.name}\n"
                                                             f"{com.create_date}\n"
                                                             f"{com.expire_date}\n"
                                                             f"Made in {com.country}\n"
                                                             f"{com.price} $"))
        except Exception as ex:
            print(ex)

        count = 0
        try:
            card = self.all_item_of_in_process_card[0]
            for item in card.number_of_commodity:
                if int(item.id_commodity) == int(id_item):
                    count = item.number_of_commodity
        except Exception as ex:
            print(ex)

        self.countSpin.setValue(count)
        self.number_want = count
        self.id_item = id_item

    def update_combox_item(self):
        _translate = QtCore.QCoreApplication.translate

        id_item = self.itemCombo.currentText().split(' |')[0]
        try:
            self.update_caridit()
            com = Commodity.find_commodity_by(id_item)
            self.itemInfo.setText(_translate("selectWindow", f"{com.name}\n"
                                                             f"{com.create_date}\n"
                                                             f"{com.expire_date}\n"
                                                             f"Made in {com.country}\n"
                                                             f"{com.price} $"))
        except Exception as ex:
            print(ex)

        id_item = self.itemCombo.currentText().split(' |')[0]

        count = 0
        try:
            card = self.all_item_of_in_process_card[0]
            for item in card.number_of_commodity:
                if int(item.id_commodity) == int(id_item):
                    count = item.number_of_commodity

        except Exception as ex:
            print(ex)
        self.countSpin.setValue(count)
        self.number_want = count
        self.id_item = id_item

    def change_count_spin(self):
        self.number_want = self.countSpin.value()
        # print(self.number_want)

    def update_caridit(self):
        find = False
        print(self.number_want)
        if self.number_want > 0 and (self.all_item_of_in_process_card is None or len(
                self.all_item_of_in_process_card) == 0):
            print("hey go1")
            try:
                create_card = Card(self.person.user_name, "", "in_progress", "", 1, [])
                create_card.insert_card()
                self.all_item_of_in_process_card = Card.find_in_process_card(self.person.user_name, "in_progress")
                card = self.all_item_of_in_process_card[0]
                table_between = Table_Between_commodity_cardit(1, int(self.id_item), card.id, self.number_want,
                                                               Commodity.find_commodity_by(self.id_item))
                table_between.insert_tabel_between_commodity_and_card()
                find = True
            except Exception as ex:
                print(ex)

        elif self.all_item_of_in_process_card is not None and len(self.all_item_of_in_process_card) > 0:

            print("hey go2")

            card = self.all_item_of_in_process_card[0]

            for item in card.number_of_commodity:
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

            card = self.all_item_of_in_process_card[0]
            table_between = Table_Between_commodity_cardit(1, int(self.id_item), card.id, self.number_want,
                                                           Commodity.find_commodity_by(self.id_item))
            table_between.insert_tabel_between_commodity_and_card()

        else:
            print("hey go4")

        self.all_item_of_in_process_card = Card.find_in_process_card(self.person.user_name, "in_progress")

    def pushButton_click(self, selectWindow):

        _translate = QtCore.QCoreApplication.translate

        self.update_caridit()

        if self.all_item_of_in_process_card is None or len(self.all_item_of_in_process_card) == 0:
            print("you don't choss any item")
            self.itemInfo.setText(_translate("selectWindow", "شما آیتمی انتخاب نکردید"))

        else:
            print(self.all_item_of_in_process_card)
            cart_ui.setupUi(selectWindow, self.person, self.all_item_of_in_process_card[0], ui)


ui = Ui_selectWindow()
# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     selectWindow = QtWidgets.QMainWindow()
#     ui = Ui_selectWindow()
#     ui.setupUi(selectWindow)
#     selectWindow.show()
#     sys.exit(app.exec_())
