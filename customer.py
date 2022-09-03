from dataclasses import dataclass
import datetime

from connect_db import connection
import random


@dataclass
class Customer:
    user_name: str
    first_name: str
    last_name: str
    password: str
    time_entery: datetime.datetime
    birthday: datetime.date
    ctype: str

    def insert_customer(self):
        cursor = connection.cursor()
        try:
            cursor.execute(
                'insert into Customer(user_name,first_name,last_name,password,time_entery,birthday_day,birthday_month,birthday_year,ctype)'
                'values(?,?,?,?,CURRENT_TIMESTAMP,?,?,?,?)',
                (self.user_name, self.first_name, self.last_name, self.password.encode('ascii'),
                 self.birthday.day, self.birthday.month, self.birthday.year, self.ctype))
            connection.commit()
            return "با موفقیت انجام شد"
        except Exception as ex:
            print(ex)
            print(type(self.password))
            return "خطایی در سیستم"

    def update_customer(self):
        cursor = connection.cursor()
        if self.password != "":
            cursor.execute(
                'update Customer set first_name = ? , last_name = ?, time_entery = ?, password = ?,'
                'birthday_day = ?, birthday_month = ?, birthday_year = ? where user_name = ?',
                (self.first_name, self.last_name, self.time_entery, self.password,
                 self.birthday.day, self.birthday.month, self.birthday.year, self.user_name)
            )
        else:
            cursor.execute('update Customer set first_name = ? , last_name = ?, time_entery = ?'
                           'birthday_day = ?, birthday_month = ?, birthday_year = ? where user_name = ?',
                           (self.first_name, self.last_name, self.time_entery,
                            self.birthday.day, self.birthday.month, self.birthday.year, self.user_name))
        connection.commit()

    @staticmethod
    def see_people_who_buy_more_than_one_year():
        cursor = connection.cursor()
        today = datetime.date.today()
        cursor.execute('select * from Customer C where DATEDIFF(year ,C.time_entery,?) > 1 and ctype = ?', (today,"normal"))
        list_of_user = []
        for item in cursor.fetchall():
            list_of_user.append(
                Customer(item[0], item[1], item[2], "", item[4], datetime.date(item[7], item[6], item[5]), item[8]))
        return list_of_user

    @staticmethod
    def lottery_for_people_that_buy_more_than_one_year():

        list_of_people = Customer.see_people_who_buy_more_than_one_year()

        return random.choice(list_of_people)

    @staticmethod
    def find_person_by(user_name, password:str):

        cursor = connection.cursor()
        cursor.execute("EXEC find_person_by_username_and_pass4 @username = ? ,  @password = ?", (user_name, password.encode('ascii')))
        if cursor.rowcount == 0:
            return "not find", None
        try:
            res = cursor.fetchall()
            item = res[0]
            print(item)
            cus = Customer(item[0], item[1], item[2], "", item[3], datetime.date(item[6], item[5], item[4]),
                           item[7])
            return "find", cus
        except Exception as ex:
            print(ex)

    @staticmethod
    def find_person(username):
        cursor = connection.cursor()
        cursor.execute('select * from Customer where user_name = ?', username)
        if cursor.rowcount == 0:
            return "not find", None
        for item in cursor:
            return "find", Customer(item[0], item[1], item[2], "", item[4], datetime.date(item[7],item[6],item[5]),
                                    item[8])

    @staticmethod
    def all_normal():
        cursor = connection.cursor()
        cursor.execute('select * from Customer where ctype = ?',"normal")
        if cursor.rowcount == 0:
            return "not find", None
        try:
            res = cursor.fetchall()
            # print(res)
            list_person = []
            for item in res:
                 list_person.append(Customer(item[0], item[1], item[2], "", item[4], datetime.date(item[7], item[6], item[5]),
                                        item[8]))
            # print(list_person)
            return "find", list_person
        except Exception as ex:
            print(ex)


