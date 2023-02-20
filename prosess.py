from random import randint, random
import os


class Bank:
    def __init__(self, name, type_card, password, id_passport) -> None:
        self.name = name
        self.type_card = type_card
        self.__password = password
        self.__id_passport = id_passport

    def kredit_olish(self, price):
        print(f"{self.name}ning olmoxchi bolgan summasi {price} so'm")
        print("Bizning Islomiy bankimizda creditni foizi yoq....")

    def investitsiya(self, price):
        os.system('cls')
        print(f"{self.name}ining investitsiyasi {price} so'm ")
        print(f"{self.name} investitsiyasi dan xar oy 5% foyda oladi uning oylik foydasi : {price*0.05} so'm ")

    def pul_otkazish(self, country, price, person):
        print(f"{self.name} {country} davlatiga {person} shaxsga {price} so'm pul otkazildi")

    @staticmethod
    def malumot():
        print('''
        Biznnig bankda siz:
         1) 1. Visa card
            2. Uzcard
            3. Humo
            3. Mir
        kartalarini xarid qilishingiz mumkun !
        2) Kredit  olish
        3) Pul otkazish
        4) Pul invistitsiay qlish

        ''')

class Card(Bank):
    def number_card(self):
        num_card = []
        while len(num_card) !=  16:
            num_card.append(str(randint(0,10)))
        num_cardi = "".join(num_card)
        os.system('cls')
        print(f"{self.name} ning cartasini  raqami: {num_cardi[0:4]} {num_cardi[4:8]} {num_cardi[8:12]} {num_cardi[12:16]}")

    def data_card(self):
        a = randint(1,12)
        b = randint(0,30)
        os.system('cls')
        print(f"{self.name}ning kartasini sanasi : {a}/{b}")

    def passworD(self, parol):
        if self.__password ==  parol:
            print(f"ning kartasini  paroli: {self.__password}")
        else:
            print("Siz notogri parol kritingiz! ")

    def __money_card(self, money):
        print(f"{self.name}ning cartasida {money} so'm pul bor")

    def setPassword(self,password):
        self.__password = password


