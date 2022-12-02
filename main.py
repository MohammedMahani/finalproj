from operation import Operation

print("Welcome in your app <3\n-------------------------------------------------------------------")
x=Operation()
x.showbuses()

print("-------------------------------------------------------------------")
user_choice= (input("Enter the bus ID: "))
x.check_input_empty(user_choice)
x.check_input_is_not_digit(user_choice)
x.check_bus_wrong(user_choice)

print("-------------------------------------------------------------------")
print("**-True-** = avilabile\n**-False-** = not avilabile")
print()
x.oper1(user_choice)

print("-------------------------------------------------------------------")
book=(input("Book your seat: "))
x.check_input_empty(book)
x.check_input_is_not_digit(book)
x.check_seat_wrong(book,user_choice)
x.oper2(book)