from dataclasses import dataclass

from commodity import Commodity
from connect_db import connection
import datetime

from number_of_commodity import Table_Between_commodity_cardit


@dataclass
class Card:
    id_customer: str
    date_accept: datetime.date
    flag: str
    total_price_must_give: str
    id: int
    number_of_commodity: list

    def insert_card(self):
        cursor = connection.cursor()
        cursor.execute(
            'insert into CardIt(id_customer,flage) values(?,?)', (self.id_customer, self.flag)
        )
        connection.commit()

    def update_card(self):
        cursor = connection.cursor()
        if self.date_accept != "" and self.flag != "":
            cursor.execute(
                'update CardIt set date_accept = ? , flage = ? where id = ?', (self.date_accept, self.flag, self.id)
            )
        elif self.date_accept != "":
            cursor.execute(
                'update CardIt set date_accept = ? where id = ?', self.date_accept, self.id
            )
        elif self.flag != "":
            cursor.execute(
                'update CardIt set flage = ? where id = ?', self.flag, self.id
            )
        else:
            return

        cursor.commit()

    @staticmethod
    def find_all_card_of(customer_id):
        cursor = connection.cursor()
        cursor.execute('select * from CardIt where id_customer = ?', customer_id)
        list_of_card_of_customer = []

        for item in cursor.fetchall():
            list_of_card_of_customer.append(
                Card.find_all_number_commodity_by(Card(item[0], item[1], item[2], item[3], item[4], [])))
        return list_of_card_of_customer

    @staticmethod
    def find_card(id):
        cursor = connection.cursor()
        cursor.execute('select * from CardIt where id = ?', id)

        if cursor.rowcount == 0:
            return None
        for item in cursor.fetchall():
            return Card.find_all_number_commodity_by(Card(item[0], item[1], item[2], item[3], item[4], []))

    @staticmethod
    def find_in_process_card(id_customer, flag):
        cursor = connection.cursor()
        cursor.execute('select * from CardIt where id_customer = ? and flage = ?', id_customer, flag)
        if cursor.rowcount == 0:
            return None
        list_item = []
        res = cursor.fetchall()
        # print()
        for item in res:
            # print(item[4])
            list_item.append(Card.find_all_number_commodity_by(Card(item[0], item[1], item[2], item[3], item[4], [])))

        return list_item

    @staticmethod
    def find_all_number_commodity_by(card):
        cursor = connection.cursor()
        cursor.execute(
            'select NumberOfCom.id_commodity,NumberOfCom.id,NumberOfCom.id_cardit,NumberOfCom.number_of_commodity,'
            'Commodity.id,Commodity.id_catogory,Commodity.create_date,'
            '       Commodity.expire_date,Commodity.name,Commodity.price,Commodity.situation,Commodity.country from NumberOfCom '
            'INNER JOIN Commodity on Commodity.id = NumberOfCom.id_commodity '
            'where id_cardit = ?', int(card.id)
        )
        card_find = card
        for item in cursor.fetchall():

            table_Between_commodity_cardit = Table_Between_commodity_cardit(item[1], item[0],
                                                                            item[2], item[3],
                                                                            Commodity(item[4], item[5], item[6],
                                                                                      item[7], item[8], item[9],
                                                                                      item[10], item[11]))
            card_find.number_of_commodity.append(table_Between_commodity_cardit)
        return card_find
