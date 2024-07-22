from random import randint
import mysql.connector as m
from datetime import date

# Establish a connection to the MySQL database
mydb = m.connect(host="localhost", user="root", password="root", database="adarshdb")
cur = mydb.cursor()

class main:
    def signup(self, val):
        cur = mydb.cursor()
        try:
            sql = "INSERT INTO password(pin, username) VALUES(%s, %s)"
            cur.execute(sql, val)
            mydb.commit()  # Commit after inserting into the password table
            print("Do you want to fill your parsonal details ? y/n")

            # Ask if user wants to fill personal details
            req = input("Do you want to fill your personal details? (y/n): ").strip().lower()
            if req == "y":
                # Create a new cursor
                cur = mydb.cursor()
                
                # Execute a query to select the pin from the password table
                cur.execute("SELECT pin FROM password")
                pins = cur.fetchall()  # Fetch all the pin values from the query result
                
                # Prompt user for their password
                ans = input("Enter your valid user password => ")

                # Check if the entered password matches any pin in the database
                for pin in pins:
                    if pin[0] == ans:  # Compare the entered password with each pin (pin[0] extracts the value from the tuple)
                        print("Fill your Bank Details")

                        # If the password matches, proceed to collect bank details
                        self.name = input("Enter your name => ")
                        self.dc = date.today()
                        self.ad = input("Enter your valid address => ")
                        self.ph = int(input("Enter your phone no => "))
                        self.dob = input("Enter your date_of_birth => ")
                        self.age = int(input("Enter your age => "))
                        self.amt = float(input("Enter the amount => "))
                        self.bp = input("Enter your user password => ")
                        self.em = input("Enter your valid email ID => ") 

                        # Insert the collected details into the bank table
                        val = [self.name, self.dc, self.ad, self.ph, self.dob, self.age, self.amt, self.bp, self.em]
                        sql = "INSERT INTO bank(name, date_of_creation, address, phone, date_of_birth, age, amount, bp, email) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        cur.execute(sql, val)

                        # Ask the user if they want to generate an ATM card
                        ch = input("Do you want to generate an ATM card y/n? ")
                        if ch.lower() == "y":
                            print("Enter captcha: ", end=" ")
                            a = randint(10, 99)
                            b = randint(0, 9)
                            print(a, "+", b, "=", end=" ")
                            c = int(input())
                            
                            # Verify captcha
                            if a + b == c:
                                cur = mydb.cursor()

                                # Execute query to fetch all pins from the password table
                                cur.execute("SELECT pin FROM password")
                                pins = cur.fetchall()  # Fetch all results at once

                                # Prompt user for their password
                                ans = input("Enter your user password => ")
                                # Validate the entered password
                                for pin in pins:
                                    if pin[0] == ans:  # Correctly comparing the password
                                        print("Generate your ATM Pin")

                                        # Prompt user to create a 4-digit ATM pin
                                        atm_pin = int(input("Create your 4 digit ATM Pin Number => "))
                                        # Prompt user to enter their bank account number
                                        a_pin = input("Enter your Bank Account number => ")
                                        # Insert the new ATM pin and account number into the ATM table
                                        var = [atm_pin, a_pin]
                                        sql = "INSERT INTO ATM(atm_pin, a_pin) VALUES(%s, %s)"
                                        cur.execute(sql, var)

                                        cur.close()
                                        mydb.commit()
                                        print("ATM Pin generated successfully")
                                        break 
                                else:
                                    # This else block executes if the for loop completes without breaking
                                    print("Incorrect user password")
                                    cur.close()
                            else:
                                print("Captcha does not match")
                            # Ensure cursor is closed if not closed within the loop
                            cur.close()
                            mydb.commit()
                        else:
                            print("Operation canceled")
                        break
                else:
                    print("Incorrect Password.......")
            else:
                print("I don't want fill my details")
        finally:
            cur.close()
        
    def creat_acc(self):
        # Create a new cursor
        cur = mydb.cursor()
        
        # Execute a query to select the pin from the password table
        cur.execute("SELECT pin FROM password")
        pins = cur.fetchall()  # Fetch all the pin values from the query result
        
        # Prompt user for their password
        ans = input("Enter your valid user password => ")
        
        # Check if the entered password matches any pin in the database
        for pin in pins:
            if pin[0] == ans:  # Compare the entered password with each pin (pin[0] extracts the value from the tuple)
                print("Fill your Bank Details")

                # If the password matches, proceed to collect bank details
                self.name = input("Enter your name => ")
                self.dc = date.today()
                self.ad = input("Enter your valid address => ")
                self.ph = int(input("Enter your phone no => "))
                self.dob = input("Enter your date_of_birth => ")
                self.age = int(input("Enter your age => "))
                self.amt = float(input("Enter the amount => "))
                self.bp = input("Enter your user password => ")
                self.em = input("Enter your valid email ID => ")
                
                # Insert the collected details into the bank table
                val = [self.name, self.dc, self.ad, self.ph, self.dob, self.age, self.amt, self.bp, self.em]
                sql = "INSERT INTO bank(name, date_of_creation, address, phone, date_of_birth, age, amount, bp, email) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cur.execute(sql, val)
                
                # Ask the user if they want to generate an ATM card
                ch = input("Do you want to generate an ATM card y/n? ")
                if ch.lower() == "y":
                    print("Enter captcha: ", end=" ")
                    a = randint(10, 99)
                    b = randint(0, 9)
                    print(a, "+", b, "=", end=" ")
                    c = int(input())
                    
                    # Verify captcha
                    if a + b == c:
                        cur = mydb.cursor()

                        # Execute query to fetch all pins from the password table
                        cur.execute("SELECT pin FROM password")
                        pins = cur.fetchall()  # Fetch all results at once

                        # Prompt user for their password
                        ans = input("Enter your user password => ")
                        # Validate the entered password
                        for pin in pins:
                            if pin[0] == ans:  # Correctly comparing the password
                                print("Generate your ATM Pin")

                                # Prompt user to create a 4-digit ATM pin
                                atm_pin = int(input("Create your 4 digit ATM Pin Number => "))
                                # Prompt user to enter their bank account number
                                a_pin = input("Enter your Bank Account number => ")
                                # Insert the new ATM pin and account number into the ATM table
                                var = [atm_pin, a_pin]
                                sql = "INSERT INTO ATM(atm_pin, a_pin) VALUES(%s, %s)"
                                cur.execute(sql, var)

                                cur.close()
                                mydb.commit()
                                print("ATM Pin generated successfully")
                                break 
                        else:
                            print("Incorrect user password")
                            cur.close()
                            mydb.commit()
                    else:
                        print("Captcha does not match")
                        cur.close()
                        mydb.commit()
                else:
                    print("ATM card generation cancelled")
                cur.close()
                mydb.commit
            else:
                print("Incorrect Password.......")
                cur.close()

    def kyc(self):
        # Generate and display captcha
        print("Enter captcha: ", end=" ")
        a = randint(10, 99)
        b = randint(0, 9)
        print(a, "+", b, "=", end=" ")
        c = int(input())
    
        # Verify captcha
        if a + b == c:
            cur = mydb.cursor()

            # Execute query to fetch all pins from the password table
            cur.execute("SELECT pin FROM password")
            pins = cur.fetchall()  # Fetch all results at once
            # Prompt user for their password
            ans = input("Enter your user password => ")
            # Validate the entered password
            for pin in pins:
                if pin[0] == ans:  # Correctly comparing the password
                    print("COMPLETE YOUR KYC")

                    # Prompt user to enter PAN number and bank account number
                    pan_no = input("Create your PAN number => ")
                    acc = int(input("Enter your Bank Account number => "))
                    # Insert the PAN number and account number into the KYC table
                    var = [pan_no, acc]
                    sql = "INSERT INTO kyc(pan_no, acc) VALUES(%s, %s)"
                    cur.execute(sql, var)
                    cur.close()
                    mydb.commit()
                    print("KYC completed successfully")
                    break
            else:
                print("Incorrect user password")
                cur.close()
                mydb.commit()
        else:
            print("Captcha does not match")

    def gen_atm_pin(self):
        # Generate and display captcha
        print("Enter captcha: ", end=" ")
        a = randint(10, 99)
        b = randint(0, 9)
        print(a, "+", b, "=", end=" ")
        c = int(input())
        # Verify captcha
        if a + b == c:
            cur = mydb.cursor()

            # Execute query to fetch all pins from the password table
            cur.execute("SELECT pin FROM password")
            pins = cur.fetchall()  # Fetch all results at once

            # Prompt user for their password
            ans = input("Enter your user password => ")

            # Validate the entered password
            for pin in pins:
                if pin[0] == ans:  # Correctly comparing the password
                    print("Generate your ATM Pin")

                    # Prompt user to create a 4-digit ATM pin
                    atm_pin = int(input("Create your 4 digit ATM Pin Number => "))
                    # Prompt user to enter their bank account number
                    a_pin = input("Enter your Bank Account number => ")
                    # Insert the new ATM pin and account number into the ATM table
                    var = [atm_pin, a_pin]
                    sql = "INSERT INTO ATM(atm_pin, a_pin) VALUES(%s, %s)"
                    cur.execute(sql, var)

                    cur.close()
                    mydb.commit()
                    print("ATM Pin generated successfully")
                    break  
            else:
                print("Incorrect user password")
                cur.close()
                mydb.commit()
        else:
            print("captcha does not match")
    
    def deposit(self):
        cur = mydb.cursor()

        # Fetch all ATM pins
        cur.execute("SELECT atm_pin FROM atm")
        pins = cur.fetchall()  # Fetch all ATM pins at once
        ans = int(input("Enter your ATM pin => "))

        # Validate the entered ATM pin
        for pin in pins:
            if pin== (ans,):
                print("Enter captcha: ", end=" ")
                a = randint(10, 99)
                b = randint(0, 9)
                print(f"{a} + {b} = ", end="")
                c = int(input())

                if(a+b==c):
                    tatal_ac=[]

                    cur.execute("SELECT acc_no FROM bank") 
                    for i in cur:
                        tatal_ac.append(i[0])
                    #print(tatal_ac)    
                    myac=int(input("Enter your bank account number =>"))
                    cur.execute("SELECT amount FROM bank where acc_no=%s",(myac,))
                    present_bl=list(cur)[0][0]
                    # print(present_bl)

                    # Check if the account number exists
                    if myac in tatal_ac:
                        amt=float(input("Enter the deposit amount =>"))
                        new_bl=present_bl+amt

                        # Update the new balance in the bank account
                        cur.execute("UPDATE bank SET amount=%s WHERE acc_no=%s",(new_bl,myac))
                        today = date.today().strftime("%Y-%m-%d")
                        print(f"Your account number {myac} is credited for Rs {amt} on {today}")
                        cur.close()
                        mydb.commit()
                        break
                    else:
                        print("account number does not exist")
                else:
                    print("you enter wrong captcha")  
                    cur.close()      
        else:
            print("Incorrect atm pin")
        cur.close()
        mydb.commit()
    
    def withdraw(self):
        cur = mydb.cursor()

        # Fetch all ATM pins
        cur.execute("SELECT atm_pin FROM ATM")
        pinn=cur.fetchall()
        ans = int(input("Enter your ATM pin => "))
         # Validate the entered ATM pin
        for pin in pinn:
            if pin[0] == ans:
                # Generate and display captcha
                print("Enter captcha: ", end=" ")
                a = randint(10, 99)
                b = randint(0, 9)
                print(a, "+" ,b, "=", end=" ")  
                c = int(input())
                # Verify captcha
                if a + b == c:
                    total_ac = []       
                     # Fetch all account numbers
                    cur.execute("SELECT acc_no FROM bank")
                    accs=cur.fetchall()
                    for acno in accs:
                        total_ac.append(acno[0])  
                    myac=int(input("Enter your account number =>"))
                    # Fetch current balance for the entered account number
                    cur.execute("SELECT amount FROM bank WHERE acc_no=%s", (myac,))
                    present_bl=list(cur)[0][0]
                    print(present_bl)

                    if (myac in total_ac):
                        amt=float(input("Enter the withdraw amount =>"))
                        new_bl=present_bl-amt
                        # Update the new balance in the bank account
                        cur.execute("UPDATE bank SET amount=%s WHERE acc_no=%s", (new_bl, myac))
                        today = date.today().strftime("%Y-%m-%d")
                        print(f"Your account number {myac} is debited for Rs {amt} on {today}")
                        cur.close()
                        mydb.commit()
                        break
                    else:
                        print("Account number does not exist")    
                        cur.close()
                        mydb.commit()              
                else:
                    print("you enter wrong captcha")            
        else:
            print("Incorrect atm pin")
        cur.close()
        mydb.commit()

    def fund_transfer(self):
        total_ac = []  # List to store all account numbers

        # Create a cursor object
        cur = mydb.cursor()
        
        # Fetch all account numbers from the bank table
        cur.execute("SELECT acc_no FROM bank")

        for i in cur:
            total_ac.append(i[0])  # Append each account number to the list
        print(total_ac)
        # Prompt user for the source account number
        ac1 = int(input("Enter source account number => "))
        # Fetch the current balance for the source account
        cur.execute("SELECT amount FROM bank WHERE acc_no=%s", (ac1,))
        credit_ac=list(cur)[0][0]
        print(credit_ac)
        # Check if source account exists
        if ac1 in total_ac:
            # Prompt user for the destination account number
            ac2 = int(input("Enter destination account number => "))
            # Fetch the current balance for the destination account
            cur.execute("SELECT amount FROM bank WHERE acc_no=%s", (ac2,))
            debit_ac=list(cur)[0][0]
            print(debit_ac)
            # Check if destination account exists
            if ac2 in total_ac:
                # Prompt user for the amount to transfer
                amt = float(input("Enter the amount for transfer => "))
                old=credit_ac-amt
                new=debit_ac+amt
                # Update the balance for the source account
                cur.execute("UPDATE bank SET amount=%s WHERE acc_no=%s", (old, ac1))
                
                # Update the balance for the destination account
                cur.execute("UPDATE bank SET amount=%s WHERE acc_no=%s", (new, ac2))
                print("Fund transfer successful.")
            else:
                print("Destination account does not exist")
        else:
            print("source account does not exist")
        cur.close()
        mydb.commit()

    def forget(self):
        # Create a cursor object to interact with the database
        cur = mydb.cursor()
        
        # Fetch all pins from the password table
        cur.execute("select pin from password")
        pin = cur.fetchall()
        print(pin)
        
        # Prompt the user to enter their user password
        ans = input("Enter your user password =>")
        
        for i in pin:
            # Check if the entered password matches any pin
            if i == (ans,):
                print("Generate your new ATM Pin")
                
                # Fetch all ATM numbers from the ATM table
                cur.execute("select atm_no from ATM")
                atmno = cur.fetchall()
                
                # Prompt the user to enter their ATM number
                atm_no = int(input("Enter your atm number =>"))
                
                for j in atmno:
                    # Check if the entered ATM number matches any in the database
                    if j[0] == atm_no:
                        # Prompt the user to create a new password
                        new = int(input("Create new password =>"))
                        
                        # Update the ATM pin for the matched ATM number
                        cur.execute("UPDATE ATM SET atm_pin=%s where atm_no=%s", (new, atm_no))
                        print("Your pin is updated")
                        
                        cur.close()
                        mydb.commit()
                        break
                else:
                    print("ATM number is wrong")
                cur.close()
                break
        else:
            print("User password does not match")
        
        cur.close()
        mydb.commit()
 
    def personal(self):
        # Create a cursor object to interact with the database
        cur = mydb.cursor()
        
        # Fetch all pins from the password table
        cur.execute("SELECT pin FROM password")
        pin = cur.fetchall()
        
        # Prompt the user to enter their user password
        ans = input("Enter your user password =>")
        
        for i in pin:
            # Check if the entered password matches any pin
            if i == (ans,):
                # Fetch the bank pin to validate the user
                cur.execute("SELECT bp FROM bank")
                bank_pin = cur.fetchall()
                
                # Validate the bank pin
                if (ans,) in bank_pin:
                    # Fetch user details from the bank table using the entered password
                    sql = "SELECT b.*, a.atm_no, k.pan_no   FROM bank b LEFT JOIN ATM a ON b.acc_no = a.a_pin LEFT JOIN   kyc k ON b.acc_no = k.acc WHERE b.bp = %s;"
                    cur.execute(sql, (ans,))
                    bank_details = cur.fetchall()

                    # Fetch user details from the password table using the entered password
                    sql = "SELECT bank_name FROM password WHERE pin = %s"
                    cur.execute(sql, (ans,))
                    password_details = cur.fetchall()
                    
                    print(password_details,bank_details)
                    break
        else:
            print("User password does not match or bank pin is incorrect")
        
        # Close the cursor
        cur.close()




                # sql="select bank_name,acc_no,name,date_of_creation,address,phone,date_of_birth,age,amount,email,atm_no,pan_no from password,bank,ATM,kyc where pin=%s"

                # v=input("Enter your user password")
                # val=(v,)
                # cur.execute(sql,val)
                # print(list(cur))
                # cur.close()
                # mydb.commit()



# Create an instance of the Main class
call = main()

# Display main menu options
print("1. LOG IN\n2. SIGN UP")
ans = int(input("Enter your choice? "))

if ans == 1:
    # Display options after logging in
    while True:
        print("1. CREATE ACCOUNT\n2. KYC\n3. GENERATE ATM PIN\n4. DEPOSIT\n5. WITHDRAW\n6. FUND TRANSFER\n7. FORGET PASSWORD\n8. DISPLAY USER DETAILS\n9. Exit")
        choice = int(input("Choose the number: "))
    
        # Call appropriate method based on user choice
        if choice == 1:
            call.creat_acc()
        elif choice == 2:
            call.kyc()
        elif choice == 3:
            call.gen_atm_pin()
        elif choice == 4:
            call.deposit()
        elif choice == 5:
            call.withdraw()
        elif choice == 6:
            call.fund_transfer()
        elif choice == 7:
            call.forget()
        elif choice == 8:
            call.personal()
        elif choice == 9:
            break
    
elif ans == 2:
    # Handle signup process
    print("Signup Your Bank Account")
    pin = input("CREATE YOUR USER PASSWORD => ")
    username = input("CREATE YOUR USERNAME => ")
    val = (pin, username)
    call.signup(val)

else:
    print("Invalid choice. Please enter 1 or 2.")

# Close the cursor and commit changes to the database
cur.close()
mydb.commit()