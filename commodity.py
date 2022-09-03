from dataclasses import dataclass
from connect_db import connection
import datetime


@dataclass
class Commodity:
    id: int
    id_catogory: int
    create_date: datetime.date
    expire_date: datetime.date
    name: str
    price: int
    situation: str
    country: str

    def insert_commodity(self):
        cursor = connection.cursor()
        cursor.execute(
            'insert into Commodity(id_catogory,create_date,expire_date,name,price,situation,country) values(?,?,?,?,?,?,?)',
            (self.id_catogory, self.create_date, self.expire_date, self.name, self.price, "Have", self.country)
        )
        connection.commit()

    def update_commodity(self):
        cursor = connection.cursor()
        cursor.execute(
            'update Commodity set id_catogory = ? , create_date = ?, expire_date = ?,name = ? , price = ? , situation = ?, country = ? '
            'where Commodity.id = ?',
            self.id_catogory, self.create_date, self.expire_date, self.name, self.price, self.situation, self.country,
            self.id
        )
        connection.commit()

    @staticmethod
    def find_commodity_by(id):
        cursor = connection.cursor()
        cursor.execute('select * from Commodity where id = ?', id)
        for item in cursor.fetchall():
            return Commodity(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
        return None

    @staticmethod
    def find_commodities_by(id_category):
        cursor = connection.cursor()
        cursor.execute(
            'select * from Commodity where id_catogory = ? and situation = ?', (id_category, "Have")
        )
        list_of_commodities = []
        for item in cursor.fetchall():
            list_of_commodities.append(
                Commodity(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]))

        return list_of_commodities

