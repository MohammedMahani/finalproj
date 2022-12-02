from father import Abona

class Seat(Abona):

    def __init__(self, bus_id, seat_id,seat_locate, avilability:bool):
        super().__init__(bus_id=bus_id)

        self.__seat_locate=seat_locate
        self.__avilability=avilability
        self.__seat_id=seat_id

    def getseat_locate(self):
        return self.__seat_locate

    def setseat_locate(self,locate):
        self.__seat_locate=locate

    def getavilability(self):
        return self.__avilability

    def setavilability(self,avilabile):
        self.__avilability=avilabile

    def getseat_id(self):
        return self.__seat_id

    def setseat_id(self,selfid):
        self.__seat_id=selfid



