from dataclasses import dataclass

# from cardit import Card
from commodity import Commodity
from connect_db import connection
import datetime


@dataclass
class Table_Between_commodity_cardit:
    id: int
    id_commodity: int
    id_cardit: int
    number_of_commodity: int
    commodity: Commodity

    def insert_tabel_between_commodity_and_card(self):
        cursor = connection.cursor()

        cursor.execute("EXEC insertCommodityToNumberOfCom4 @id_commodity = ? , @id_Cardit = ? , @number = ?",
                       (self.id_commodity, self.id_cardit, self.number_of_commodity))
        cursor.commit()

    def update_table_between_commodity_and_card(self):
        cursor = connection.cursor()

        cursor.execute("EXEC updateCommodityToNumberOfCom4 @id_commodity = ? , @id_Cardit = ? , @number = ? ,@id = ?",
                       (self.id_commodity, self.id_cardit, self.number_of_commodity, self.id))
        cursor.commit()

    @staticmethod
    def find_table_between_commodity(id):
        cursor = connection.cursor()
        cursor.execute('select * from NumberOfCom where id = ?', id)

        for item in cursor.fetchall():
            return Table_Between_commodity_cardit(item[0], item[1], item[2], item[3],
                                                  Commodity.find_commodity_by(item[1]))

    @staticmethod
    def delete_tabel_between_commodity(id):
        cursor = connection.cursor()
        cursor.execute('DELETE from NumberOfCom where id = ?', id)
        cursor.commit()
