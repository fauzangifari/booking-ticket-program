from View import flight_view as fv
from Controller import flight_controller as fc
from Model import mongodb as db


class User:
    def __init__(self):
        self.flight = fc.Flight()
        self.view = fv.LinkedList()
        self.db = db.dataFlight

    def buyTicket(self):
        self.view.display()
        idFlight = input("Masukkan ID Flight: ")
        self.view.search(idFlight)
        if self.view.search(idFlight):
            sumTicket = int(input("Masukkan jumlah tiket: "))
            if sumTicket > 0:
                for d in self.db.find({"idFlight": idFlight}):
                    price = d['price']
                    total = price * sumTicket
                    print("Total harga: ", total)

        else:
            print("Tiket tidak ditemukan")

    def addBalance(self):
        pass

    def checkHistory(self):
        pass

