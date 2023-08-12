import sys
import datetime


# Here is a design function just to simply print out the Design
def design():
    print("======================")


# This function will check if the rooms are available or not
def checkavailable(x):
    if x == 1:
        num_lines = sum(1 for line in open('apart_a.txt'))
        if num_lines > 40:
            available = 'no'
        else:
            available = 'yes'
    # Here is the instruction is bit different to type a because type a is all single room while type b is not
    # So the instruction will count depending whether the room booked is Master or Single
    if x == 2:
        with open('apart_b.txt', 'r') as f:
            contents = f.read()
            count = contents.count("Master")
            scount = contents.count("Single")
            if count == 20:
                available = 'm.full'
            elif scount == 40:
                available = 's.full'
            else:
                available = 'yes'

    return available


# This function contains the Fees for Type A
def feesa():

    design()
    fees = 400

    return fees


# This function is for registering the student into the system also requesting the student to enter their information
# Also requesting the student to enter Type A information and whether they want internet or not
def booka():
    now = str(datetime.date.today())
    five_months = str(datetime.date.today() + datetime.timedelta(5 * 365 / 12))
    design()
    info = []
    student_info = []

    name = str(input("Enter your name :"))
    info.append(name)
    tpnum = str(input("Enter your TPNumber :"))
    info.append(tpnum)
    nation = str(input("Nationality :"))
    info.append(nation)
    age = str(input("Age :"))
    info.append(age)
    status = 'in'
    info.append(status)

#    Calling check available function to get the return value whether it is available or not
    total_rooms = checkavailable(1)

#   Here is the process where the program will request for the input of the user
    design()
    if total_rooms == 'yes':
        print("Type A is still available for booking")
        design()
        option = str(input("Yes\tNo\nWant a Single Room :"))
        if option.lower() == 'yes':
            tipe = 'Single'
            choice = str(input("Yes\tNo\nDo you want Internet Subscription :"))
            if choice.lower() == 'yes':
                fees = feesa()
                fees = fees + 50
            elif choice.lower() == 'no':
                fees = feesa()

        elif option.lower() == 'no':
            menu()
        else:
            print("Please enter yes or no")
            savedata(1)
    else:
        design()
        print("Sorry all rooms in Type A is occupied")
        shift = str(input("Yes\tNo\nDo you want to shift to B or exit :"))
        if shift.lower() == 'yes':
            savedata(2)
        elif shift.lower() == 'no':
            out()
        else:
            out()

    # continuation of appending in the information
    money = str(fees + 100)


#--------------------------------------------------------------------------#
    # This is payment for booka
    pay = str(input("Pay full or Partial :"))
    if pay == 'full':
        fees = fees + 100
        must_pay = str(fees)
        print("Please pay this amount which is including the deposit =", fees)

    elif pay == 'partial':
        temp = fees
        temp = temp * 0.5
        fees_a = temp + 100
        print("Please pay this amount or more which is including the deposit =", fees_a)
        paying = float(input("How much you want to pay :"))
        if paying < fees_a:
            print("This is not acceptable\n"
                  "Please re-enter your booking details again because it is less than the actual fees")
            savedata(1)
        if paying > fees + 100:
            print("This is not acceptable\n"
                  "Please re-enter your booking details again because it is more than the actual fees")
            savedata(1)

        must_pay = str(paying)

    print("This is the Day of you booked :", now)
    design()
    print("This the day you should check out :", five_months)
    info.append(tipe)
    info.append(pay)
    info.append(money)
    info.append(must_pay)
    info.append(now)
    info.append(five_months)
    student_info.append(info)

    return student_info


# Here is the function for the fees in block b
def feesb():

    design()
    fees = 300

    return fees


# This function is for registering the student into the system also requesting the student to enter their information
# Also requesting the student to enter Type B information and whether they want internet or not
# Almost everything in Bookb is similar to Booka
def bookb():

    now = str(datetime.date.today())
    five_months = str(datetime.date.today() + datetime.timedelta(5 * 365 / 12))
    design()
    info = []
    student_info = []

    name = str(input("Enter your name :"))
    info.append(name)
    tpnum = str(input("Enter your TPNumber :"))
    info.append(tpnum)
    nation = str(input("Nationality :"))
    info.append(nation)
    age = str(input("Age :"))
    info.append(age)
    status = 'in'
    info.append(status)

    total_rooms = checkavailable(2)

    design()
    if total_rooms == 'yes':
        print("Type B is still available for booking")
        design()
        option = str(input("Single\tMaster\nWant a Single Room or Master Room :"))
        if option.lower() == 'single':
            tipe = 'Single'
            if total_rooms == 's.full':
                print("Sorry Single is full please book other than Single")
                savedata(2)
            choice = str(input("Yes\tNo\nDo you want Internet Subscription :"))
            if choice.lower() == 'yes':
                fees = feesb()
                fees = fees + 40
            elif choice.lower() == 'no':
                fees = feesb()
        elif option.lower() == 'master':
            tipe = 'Master'
            if total_rooms == 'm.full':
                print("Sorry Master is full please book other than Master")
                savedata(2)
            choice = str(input("Yes\tNo\nDo you want Internet Subscription :"))
            if choice.lower() == 'yes':
                fees = feesb()
                fees = fees + 240
            elif choice.lower() == 'no':
                fees = feesb()
                fees = fees + 200
        else:
            design()
            print("Please enter single or master: ")
            savedata(2)
    else:
        design()
        print("Sorry all rooms in Type B is occupied")
        shift = str(input("Yes\tNo\nDo you want to shift to A or exit :"))
        if shift.lower() == 'yes':
            savedata(1)
        elif shift.lower() == 'no':
            out()
        else:
            out()

    money = str(fees + 100)

    # This is payment for bookb
    pay = str(input("Pay full or Partial :"))
    if pay == 'full':
        fees = fees + 100
        must_pay = str(fees)
        print("Please pay this amount which is including the deposit =", fees)

    elif pay == 'partial':
        temp = fees
        temp = temp * 0.5
        fees_b = temp + 100
        print("Please pay this amount or more which is including the deposit =", fees_b)
        paying = float(input("How much you want to pay :"))
        if paying < fees_b:
            design()
            print("This is not acceptable\n"
                  "Please re-enter your booking details again because it is less than the actual fees")
            savedata(2)
        if paying > fees + 100:
            design()
            print("This is not acceptable\n"
                  "Please re-enter your booking details again because it is more than the actual fees")
            savedata(1)

        must_pay = str(paying)

    print("This is the Day of you booked :", now)
    design()
    print("This the day you should check out :", five_months)
    info.append(tipe)
    info.append(pay)
    info.append(money)
    info.append(must_pay)
    info.append(now)
    info.append(five_months)
    student_info.append(info)

    return student_info


# Here is the function for the user to checkout and it will replace the data in into out
# and save in the Check_out file as to show that the user have left the apartment
# Also it will delete the data in aparta file and save in check_out file

def checkout(x):
    if x == 1:
        file = open('apart_a.txt', 'r+')
        file1 = open('check_out.txt', 'a')
#       here it will prompt the user to enter the student name or any info to search it and check it out from the
        # original file
        search = str(input('Enter your name to check your info :'))
        for line in file:
            line = line.rstrip()
            if not search.lower() in line.lower():
                continue
            temp = line
            line = line.replace("in", "out", 1)
            print("You have Checked out, this is your info :\n", line)
            for li in line:
                file1.write(li)
            file1.write('\tA')
            file1.write('\n')

        file.close()
        file1.close()

# This is instruction will delete the temp line in file apart_a
        fn = 'apart_a.txt'
        f = open(fn)
        output = []
        stri = temp
        for line in f:
            if not line.startswith(stri):
                output.append(line)
        f.close()
        f = open(fn, 'w')
        f.writelines(output)
        f.close()

    # Here is for the apartb
    elif x == 2:
        file = open('apart_b.txt', 'r+')
        file1 = open('check_out.txt', 'a')

        search = str(input('Enter your name to check your info :'))
        for line in file:
            line = line.rstrip()
            if not search.lower() in line.lower():
                continue
            temp = line
            line = line.replace("in", "out", 1)
            print("You have Checked out, this is your info :\n", line)
            for li in line:
                file1.write(li)
            file1.write('\tB')
            file1.write('\n')
        file.close()
        file1.close()

        # This is instruction will delete the temp line in file apart_b
        fn = 'apart_b.txt'
        f = open(fn)
        output = []
        stri = temp
        for line in f:
            if not line.startswith(stri):
                output.append(line)
        f.close()
        f = open(fn, 'w')
        f.writelines(output)
        f.close()


# This function to save the entered data whether the user want to book type A or B
def savedata(x):
    if x == 1:
        file = open('apart_a.txt', 'a')
        # Here is where the booka will start working
        student_info = booka()

        for info in student_info:
            for inf in info:
                file.write(inf)
                file.write('\t')
            file.write('\n')
        file.close()

    elif x == 2:
        file = open('apart_b.txt', 'a')
        student_info = bookb()

        for info in student_info:
            for inf in info:
                file.write(inf)
                file.write('\t')
            file.write('\n')
        file.close()


# This function is print all of the data in the text file depending on the request whether from A, B or check_out
def printall(x):
    design()
    if x == 1:
        file = open('apart_a.txt', 'r+')
        line = 1
        for line in file:
            print(line)
    if x == 2:
        file = open('apart_b.txt', 'r+')
        line = 1
        for line in file:
            print(line)
    if x == 3:
        file = open('check_out.txt', 'r+')
        line = 1
        for line in file:
            print(line)

    design()


def out():
    design()
    sys.exit("Bye")


# This is the Menu where the user can decide what options would like to perform
def menu():
    print("========= Welcome to APU Apartment System =========")
    design()
    register = str(input("1.Book\n2.Check-out\n3.Print All Info\n4.Exit\nEnter the number you want :"))
    if register == '1':
        design()
        option = str(input("Wanna book type A or B: "))
        if option.lower() == 'a':
            savedata(1)
            design()
        elif option.lower() == 'b':
            savedata(2)
            design()
        else:
            design()
            print("Please enter the correct input")
            menu()

    elif register == '2':
        check_opt = str(input("Wanna check-out type A or B: "))
        if check_opt.lower() == 'a':
            checkout(1)
        elif check_opt.lower() == 'b':
            checkout(2)
        else:
            design()
            print("Please enter the correct input")
            menu()

    elif register == '3':
        toprint = str(input("Which apartment info you want to print A, B or check_out :"))
        if toprint.lower() == 'a':
            printall(1)
        elif toprint.lower() == 'b':
            printall(2)
        elif toprint.lower() == 'check out':
            printall(3)
        else:
            design()
            print("Please enter the correct input")
            menu()

    elif register == '4':
        out()

    else:
        design()
        random = int(input("1.Exit\n2.Try again\nDo you want to exit or try again :"))
        if random == 1:
            out()
        elif random == 2:
            design()
            menu()
        else:
            sys.exit("Error message")


# Here is the loop to keep on saving and requesting the user whether to continue or not
con = True
while con:
    menu()
    start_again = str(input("Yes\t No\nDo you want to start again :"))
    if start_again.lower() == 'yes':
        menu()
    else:
        con = False
        out()
