balance = 5000

user1 = "priya"
pass1 = "1234"

user2 = "rajnesh"
pass2 = "5678"

user3 = "tushar"
pass3 = "1111"

username = input("Enter Username: ")
password = input("Enter Password: ")

if (username == user1 and password == pass1) or \
   (username == user2 and password == pass2) or \
   (username == user3 and password == pass3):

    print("Login Successful")

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Exit")

        num = int(input("Enter your number: "))

        if num == 1:
            amt = int(input("Enter deposit amount: "))
            balance = balance + amt
            print("Amount Deposited")

        elif num == 2:
            amt = int(input("Enter withdraw amount: "))
            if amt <= balance:
                balance = balance - amt
                print("Amount Withdrawn")
            else:
                print("Insufficient Balance")

        elif num == 3:
            print("Current Balance =", balance)

        elif num == 4:
            print("Thank You!")
            break

        else:
            print("Invalid Choice")

else:
    print("Invalid Username or Password")
