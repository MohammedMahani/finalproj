from father import Abona
from seat import Seat
class Bus(Abona):

     def __init__(self, bus_id, bus_locate):
         super().__init__(bus_id=bus_id)
         self.__bus_locate=bus_locate

     def getbuslocate(self):
         return self.__bus_locate

     def setbuslocate(self,buslocate):
         self.__bus_locate=buslocate