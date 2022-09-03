from dataclasses import dataclass
import datetime

from connect_db import connection


@dataclass
class Category:
    id: int
    name: str

    def insert_category(self):
        cursor = connection.cursor()
        cursor.execute(
            'insert into Category(name ) values (?)', self.name
        )
        connection.commit()

    def update_category(self):
        cursor = connection.cursor()
        cursor.execute(
            'update Category set name = ? where id = ?', self.id
        )
        connection.commit()

    @staticmethod
    def find_all_category():
        cursor = connection.cursor()
        cursor.execute(
            'select * from Category'
        )
        dic_of_category = {}
        res = cursor.fetchall()
        # print(res)
        for item in res:
            dic_of_category[item[1]] = item[0]

        return dic_of_category

    @staticmethod
    def find_category_by(id):
        cursor = connection.cursor()
        cursor.execute(
            'select * from Category where id = ?', id
        )
        for item in cursor:
            return Category(item[0], item[1])

    @staticmethod
    def send_item_to_category_default(list_of_name):
        for name in list_of_name:
            Category(1, name).insert_category()


#Category.send_item_to_category_default(['خوراکی','پوشاک','بهداشتی','کالای خانگی'])