
from bus import Bus
from seat import Seat


class Operation:


      bus_list: list[Bus] = [Bus("1", "From Gaza to Hebron"), Bus("2", "From Rafah to Jabalya"),
                                   Bus("3", "From Hefa to Akka")]


      seat_list: list[Seat] = [Seat(bus_id="1", seat_id=1, seat_locate="Right at First row", avilability=True),
                                     Seat(bus_id="1", seat_id=2, seat_locate="Left at First row", avilability=False),
                                     Seat(bus_id="1", seat_id=3, seat_locate="Right at Second row", avilability=False),
                                     Seat(bus_id="1", seat_id=4, seat_locate="Left at Second row", avilability=True),
                                     Seat(bus_id="1", seat_id=5, seat_locate="Mid at Third row", avilability=True),

                                     Seat(bus_id="2", seat_id=1, seat_locate="Right at First row", avilability=False),
                                     Seat(bus_id="2", seat_id=2, seat_locate="Left at First row", avilability=True),
                                     Seat(bus_id="2", seat_id=3, seat_locate="Right at Second row", avilability=True),
                                     Seat(bus_id="2", seat_id=4, seat_locate="Left at Second row", avilability=False),
                                     Seat(bus_id="2", seat_id=5, seat_locate="Mid at Third row", avilability=True),

                                     Seat(bus_id="3", seat_id=1, seat_locate="Right at First row", avilability=True),
                                     Seat(bus_id="3", seat_id=2, seat_locate="Left at First row", avilability=True),
                                     Seat(bus_id="3", seat_id=3, seat_locate="Right at Second row", avilability=True),
                                     Seat(bus_id="3", seat_id=4, seat_locate="Left at Second row", avilability=True),
                                     Seat(bus_id="3", seat_id=5, seat_locate="Mid at Third row", avilability=False),
                                     ]

      def showbuses(self):
          for i in self.bus_list:
              print(i.getbusid(),i.getbuslocate())

      def oper1(self,user_choice):
          for x in self.bus_list:
              if user_choice==x.getbusid():
                  for z in self.seat_list:
                      if user_choice==z.getbusid():
                         print(z.getseat_id(),"-",z.getseat_locate(),"**",z.getavilability(),"**")

      def oper2(self,book):
          for o in self.seat_list:
              if book==o.getseat_id():
                  o.setavilability(False)
          print("Operation Succfully !!!")

      @staticmethod
      def check_input_empty(*input):
          for item in input:
              if item.isspace() or item == "":
                  print("Empty input")
                  exit()
              else:
                  pass


      def check_bus_wrong(self,user_choice):
          for l in self.bus_list:
              if int(user_choice)==int(l.getbusid()):
                  return True

          else:
                   print("Wrong input")
                   exit()

      def check_seat_wrong(self, book,user_choice):
          for y in self.seat_list:
              if int(book) == int(y.getseat_id()) and y.getavilability()==True and y.getbusid()==user_choice:
                 return True
          else:
                 print( "Seat is boocked ")
                 exit()

      @staticmethod
      def check_input_is_not_digit(*input):
          for item in input:
              if str(item).isdigit() == False:
                  print("Wrong input ,please try again")
                  exit()

