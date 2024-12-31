import mysql.connector
from tkinter import *
from tkinter import ttk, font, messagebox
from random import randrange
from datetime import date

"""mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mysql'
)
mycursor = mydb.cursor()

mycursor.execute('CREATE DATABASE IF NOT EXISTS bank')
mycursor.execute('USE bank')
mycursor.execute('CREATE TABLE IF NOT EXISTS bank_master'
                 '(acc_no INT(8) PRIMARY KEY, pin INT(4), first_name VARCHAR(15), last_name VARCHAR(15), balance INT(6), phone_no INT(10))')
mycursor.execute('CREATE TABLE IF NOT EXISTS bank_trans'
                 '(acc_no INT(8), amount INT(6), dot DATE, trans_type CHAR(1), FOREIGN KEY(acc_no) REFERENCES bank_master(acc_no))')
mydb.commit()
"""

def centreWindow(parent):
    w = 800
    h = 600
    sw = parent.winfo_screenwidth()
    sh = parent.winfo_screenheight()
    x = (sw - w) // 2
    y = (sh - h) // 2
    parent.geometry(f'{w}x{h}+{x}+{y}')


window = Tk()
centreWindow(window)
window.title('Sierra Bank Management System')
window.configure(bg='#002441')
window.resizable(width=FALSE, height=FALSE)

# FONTS #

headFont = font.Font(family='Geometos', size=52)
smallHeadFont = font.Font(family='Geometos', size=45)
subHeadFont = font.Font(family='Geometos', size=31)
textFont = font.Font(family='Poppins', size=18)
entryFont = font.Font(family='Poppins', size=14)


# VALIDATOR #
def check_valid_acc(acc_no):
    mycursor.execute('SELECT acc_no FROM bank_master')
    accounts = [account[0] for account in mycursor]
    if acc_no.isdigit() and int(acc_no) not in accounts:
        messagebox.showerror('Error 420', 'Account does not exist')
        return False
    return True


# HOME FRAME #
class HomeFrameClass():

    @staticmethod
    def homeFrameCreator():
        global homeFrame
        homeFrame = Frame(
            window,
            height=600,
            width=800,
            bg="#002441")
        homeFrame.pack()

        titleLabel = Label(
            homeFrame,
            text='SIERRA\nBANK',
            font=headFont,
            justify=LEFT,
            bg='#002441',
            fg='#F3F4EA')
        titleLabel.place(relx=0.035, rely=0.356)

        createAccount = Button(
            homeFrame,
            text='Create an account',
            relief=FLAT,
            bg='#AFCEDA',
            fg='#002441',
            font=textFont,
            anchor=E,
            padx=20,
            borderwidth=0,
            activebackground="#798E96",
            activeforeground="#FFFFFF",
            command=makeAccountFrameClass.accountFrameCreator)

        dispAccount = Button(
            homeFrame,
            relief=FLAT,
            text='Display account',
            bg='#7F9BA8',
            fg='#002441',
            font=textFont,
            anchor=E,
            borderwidth=0,
            activebackground="#5D717A",
            activeforeground="#FFFFFF",
            padx=20,
            command=displayAccountFrameClass.displayAccountFrameCreator)

        makewithdrawal = Button(
            homeFrame,
            relief=FLAT,
            text='Make a withdrawal',
            bg='#76625D',
            fg='#002441',
            font=textFont,
            anchor=E,
            padx=20,
            command=withdrawalFrameClass.withdrawalFrameCreator)

        makeDeposit = Button(
            homeFrame,
            relief=FLAT,
            text='Make a deposit',
            bg='#E2A394',
            fg='#002441',
            font=textFont,
            anchor=E,
            padx=20,
            command=depositFrameClass.depositFrameCreator)

        exitButton = Button(
            homeFrame,
            relief=FLAT,
            text='Exit',
            bg='#F0DFDD',
            fg='#002441',
            font=textFont,
            anchor=E,
            padx=20,
            command=window.destroy)

        homeButtons = [createAccount, dispAccount, makewithdrawal, makeDeposit, exitButton]
        s = 0
        for button in homeButtons:
            button.place(anchor=NE, relx=1, rely=0 + s, width=298, height=120.4)
            s += 0.2

        lineLabel = Label(homeFrame, text='', bg='#EBEBEB')
        lineLabel.place(relx=0.62, rely=0, height=600, width=10)


################################################GRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPE################################################


class makeAccountFrameClass():

    @staticmethod
    def accountFrameCreator():

        homeFrame.pack_forget()

        accountFrame = Frame(
            window,
            height=600,
            width=800,
            bg="#002441")
        accountFrame.pack()

        genericLabel = Label(
            accountFrame,
            text='SIERRA\nBANK',
            font=smallHeadFont,
            justify=LEFT,
            bg='#002441',
            fg='#F3F4EA')
        genericLabel.place(relx=0.035, rely=0.03775)
        subHeadLabel = Label(
            accountFrame,
            text='Create an\naccount',
            font=subHeadFont,
            justify=RIGHT,
            bg='#002441',
            fg='#F3F4EA')
        subHeadLabel.place(relx=0.648, rely=0.03775)
        firstNameLabel = Label(
            accountFrame,
            text='First name',
            font=textFont,
            anchor=E,
            bg='#002441',
            fg='#F3F4EA')
        firstNameLabel.place(relx=0.185, rely=0.346, width=222, height=44)
        lastNameLabel = Label(
            accountFrame,
            text='Last name',
            font=textFont,
            anchor=E,
            bg='#002441',
            fg='#F3F4EA')
        lastNameLabel.place(relx=0.185, rely=0.446, width=222, height=44)
        pinLabel = Label(
            accountFrame,
            text='Create a PIN',
            font=textFont,
            anchor=E,
            bg='#002441',
            fg='#F3F4EA')
        pinLabel.place(relx=0.185, rely=0.546, width=222, height=44)
        phoneNumberLabel = Label(
            accountFrame,
            text='Phone number',
            font=textFont,
            anchor=E,
            bg='#002441',
            fg='#F3F4EA')
        phoneNumberLabel.place(relx=0.185, rely=0.646, width=222, height=44)

        ###

        firstNameEntry = Entry(
            accountFrame,
            relief=FLAT,
            bg='#203657',
            fg='#F3F4EA',
            font=entryFont,
            borderwidth=6)
        lastNameEntry = Entry(
            accountFrame,
            relief=FLAT,
            bg='#203657',
            fg='#F3F4EA',
            font=entryFont,
            borderwidth=6)
        pinEntry = Entry(
            accountFrame,
            relief=FLAT,
            bg='#203657',
            fg='#F3F4EA',
            font=entryFont,
            borderwidth=6)
        phoneNumEntry = Entry(
            accountFrame,
            relief=FLAT,
            bg='#203657',
            fg='#F3F4EA',
            font=entryFont,
            borderwidth=6)

        entryBoxes = [firstNameEntry, lastNameEntry, pinEntry, phoneNumEntry]
        i = 0
        for entryBox in entryBoxes:
            entryBox.place(relx=0.52, rely=0.353 + i, width=222, height=30)
            i += 0.1
        pinEntry.insert(0, str(randrange(1000, 10000)))

        def create_account():
            f_name = firstNameEntry.get()
            l_name = lastNameEntry.get()
            pin = pinEntry.get()
            phone_no = phoneNumEntry.get()

            checks = []
            if not f_name.isalpha():
                checks.append('The first name must only contain alpahbets.')
            if not l_name.isalpha():
                checks.append('The last name must only contain alpahbets.')
            if not phone_no.isdigit():
                checks.append('The mobile number must only contain digits.')
            if not pin.isdigit():
                checks.append('The PIN must only contain digits.')
            if len(pin) != 4:
                checks.append('The PIN must contain exactly 4 digits.')
            if checks:
                err_msg = '\n'.join(checks)
                messagebox.showerror("Invalid Input", err_msg)
                return

            mycursor.execute('SELECT acc_no FROM bank_master')
            accounts = [account[0] for account in mycursor]
            while True:
                acc_no = randrange(10000000, 100000000)
                if acc_no not in accounts:
                    break
            mycursor.execute(f"INSERT INTO bank_master VALUES({acc_no}, {pin}, '{f_name}', '{l_name}', 0, {phone_no})")
            mydb.commit()
            messagebox.showinfo('Your account was succesfully created',
                                f'Your account number is {acc_no}\n.Your PIN is {pin}\n.Please make a note of these.')

        createAccountButton = Button(
            accountFrame,
            text='CREATE',
            relief=FLAT,
            bg='#7F9BA8',
            fg='#F3F4EA',
            anchor=CENTER,
            font=entryFont,
            command=create_account)
        createAccountButton.place(relx=0.38, rely=0.79, width=190, height=42)

        def goBack():
            if accountFrame.winfo_ismapped():
                accountFrame.pack_forget()
            if not homeFrame.winfo_ismapped():
                homeFrame.pack()

        backButton = Button(
            accountFrame,
            text='< Back',
            font=textFont,
            anchor=W,
            relief=FLAT,
            bg='#002441',
            fg='#F3F4EA',
            borderwidth=0,
            activebackground="#002441",
            activeforeground="#203657",
            command=goBack)
        backButton.place(relx=0.02, rely=0.92, height=30)


################################################GRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPE################################################


class displayAccountFrameClass():

    @staticmethod
    def displayAccountFrameCreator():

        homeFrame.pack_forget()

        displayAccountFrame = Frame(
            window,
            height=600,
            width=800,
            bg="#002441")
        displayAccountFrame.pack()
        genericLabel = Label(
            displayAccountFrame,
            text='SIERRA\nBANK',
            font=smallHeadFont,
            justify=LEFT,
            bg='#002441',
            fg='#F3F4EA')
        genericLabel.place(relx=0.035, rely=0.03775)
        subHeadLabel = Label(
            displayAccountFrame,
            text='Display Your\naccount',
            font=subHeadFont,
            justify=RIGHT,
            bg='#002441',
            fg='#F3F4EA')
        subHeadLabel.place(relx=0.56, rely=0.03775)
        accountNumberLabel = Label(
            displayAccountFrame,
            text='Account number',
            font=textFont,
            anchor=E,
            bg='#002441',
            fg='#F3F4EA')
        accountNumberLabel.place(relx=0.185, rely=0.346, width=222, height=44)
        fullNameLabel = Label(
            displayAccountFrame,
            text='Full name',
            font=textFont,
            anchor=E,
            bg='#002441',
            fg='#F3F4EA')
        fullNameLabel.place(relx=0.185, rely=0.446, width=222, height=44)
        balanceLabel = Label(
            displayAccountFrame,
            text='Balance',
            font=textFont,
            anchor=E,
            bg='#002441',
            fg='#F3F4EA')
        balanceLabel.place(relx=0.185, rely=0.546, width=222, height=44)
        phoneNumberLabel = Label(
            displayAccountFrame,
            text='Phone number',
            font=textFont,
            anchor=E,
            bg='#002441',
            fg='#F3F4EA')
        phoneNumberLabel.place(relx=0.185, rely=0.646, width=222, height=44)

        ###

        accNumEntry = Entry(
            displayAccountFrame,
            relief=FLAT,
            bg='#203657',
            fg='#F3F4EA',
            font=entryFont,
            borderwidth=6)
        accNumEntry.place(relx=0.52, rely=0.353, width=222, height=30)

        fullNameDisplayLabel = Label(
            displayAccountFrame,
            text='',
            font=textFont,
            anchor=W,
            bg='#002441',
            fg='#F3F4EA')
        fullNameDisplayLabel.place(relx=0.525, rely=0.446, height=44)

        balanceDisplayLabel = Label(
            displayAccountFrame,
            text='',
            font=textFont,
            anchor=W,
            bg='#002441',
            fg='#F3F4EA')
        balanceDisplayLabel.place(relx=0.525, rely=0.546, height=44)

        phoneNumDisplayLabel = Label(
            displayAccountFrame,
            text='',
            font=textFont,
            anchor=W,
            bg='#002441',
            fg='#F3F4EA')
        phoneNumDisplayLabel.place(relx=0.525, rely=0.646, height=44)

        def show_details():
            acc_no = accNumEntry.get()

            if not check_valid_acc(acc_no):
                return
            checks = []
            if not acc_no.isdigit():
                checks.append('The account number must only contain digits.')
            if len(acc_no) != 8:
                checks.append('The account number must contain exactly 8 digits.')
            if checks:
                err_msg = '\n'.join(checks)
                messagebox.showerror("Invalid Input", err_msg)
                return

            mycursor.execute(
                f"SELECT CONCAT(first_name, ' ', last_name), balance, phone_no from bank_master where acc_no = {acc_no}")
            full_name, balance, phone_no = mycursor.fetchone()
            fullNameDisplayLabel.config(text=full_name)
            balanceDisplayLabel.config(text=balance)
            phoneNumDisplayLabel.config(text=phone_no)

        getInfoButton = Button(
            displayAccountFrame,
            text='FETCH',
            relief=FLAT,
            bg='#7F9BA8',
            fg='#F3F4EA',
            anchor=CENTER,
            font=entryFont,
            command=show_details)
        getInfoButton.place(relx=0.38, rely=0.79, width=190, height=42)

        def goBack():
            if displayAccountFrame.winfo_ismapped():
                displayAccountFrame.pack_forget()
            if not homeFrame.winfo_ismapped():
                homeFrame.pack()

        backButton = Button(
            displayAccountFrame,
            text='< Back',
            font=textFont,
            anchor=W,
            relief=FLAT,
            bg='#002441',
            fg='#F3F4EA',
            borderwidth=0,
            activebackground="#002441",
            activeforeground="#203657",
            command=goBack)
        backButton.place(relx=0.02, rely=0.92, height=30)


################################################GRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPE################################################


class withdrawalFrameClass():

    @staticmethod
    def withdrawalFrameCreator():

        homeFrame.pack_forget()

        withdrawalFrame = Frame(
            window,
            height=600,
            width=800,
            bg="#002441")
        withdrawalFrame.pack()

        genericLabel = Label(
            withdrawalFrame,
            text='SIERRA\nBANK',
            font=smallHeadFont,
            justify=LEFT,
            bg='#002441',
            fg='#F3F4EA')
        genericLabel.place(relx=0.035, rely=0.03775)

        subHeadLabel = Label(
            withdrawalFrame,
            text='Make a\nwithdrawal',
            font=subHeadFont,
            justify=RIGHT,
            bg='#002441',
            fg='#F3F4EA')
        subHeadLabel.place(relx=0.59, rely=0.03775)

        accountNumberLabel = Label(
            withdrawalFrame,
            text='Account number',
            font=textFont,
            anchor=E,
            bg='#002441',
            fg='#F3F4EA')
        accountNumberLabel.place(relx=0.185, rely=0.4, width=222, height=44)

        PINLabel = Label(
            withdrawalFrame,
            text='PIN',
            font=textFont,
            anchor=E,
            bg='#002441',
            fg='#F3F4EA')
        PINLabel.place(relx=0.185, rely=0.5, width=222, height=44)

        amountLabel = Label(
            withdrawalFrame,
            text='Amount',
            font=textFont,
            anchor=E,
            bg='#002441',
            fg='#F3F4EA')
        amountLabel.place(relx=0.185, rely=0.6, width=222, height=44)

        accNumEntry = Entry(
            withdrawalFrame,
            relief=FLAT,
            bg='#203657',
            fg='#F3F4EA',
            font=entryFont,
            borderwidth=6)
        accNumEntry.place(relx=0.52, rely=0.409, width=222, height=30)

        PINEntry = Entry(
            withdrawalFrame,
            relief=FLAT,
            bg='#203657',
            fg='#F3F4EA',
            font=entryFont,
            borderwidth=6)
        PINEntry.place(relx=0.52, rely=0.509, width=222, height=30)

        amountEntry = Entry(
            withdrawalFrame,
            relief=FLAT,
            bg='#203657',
            fg='#F3F4EA',
            font=entryFont,
            borderwidth=6)
        amountEntry.place(relx=0.52, rely=0.609, width=222, height=30)

        def withdraw():
            acc_no = accNumEntry.get()
            pin = PINEntry.get()
            amount = amountEntry.get()

            if not check_valid_acc(acc_no):
                return

            checks = []
            if not acc_no.isdigit():
                checks.append('The account number must only contain digits.')
            if not amount.isdigit():
                checks.append('The amount must only contain digits.')
            if not pin.isdigit():
                checks.append('The PIN must only contain digits.')
            if len(acc_no) != 8:
                checks.append('The account number must contain exactly 8 digits.')
            if len(pin) != 4:
                checks.append('The PIN must contain exactly 4 digits.')
            if checks:
                err_msg = '\n'.join(checks)
                messagebox.showerror("Invalid Input", err_msg)
                return

            mycursor.execute(f'SELECT balance FROM bank_master WHERE acc_no = {acc_no}')
            if amount > mycursor.fetchone()[0]:
                messagebox.showerror('Error', 'Insufficient funds.')
                return

            mycursor.execute(f'UPDATE bank_master SET balance = balance - {amount} where acc_no = {acc_no}')
            mycursor.execute(f"INSERT INTO bank_trans VALUES({acc_no}, {amount}, '{date.today()}', 'W')")
            mycursor.execute(f'SELECT balance FROM bank_master where acc_no = {acc_no}')
            balance = mycursor.fetchone()[0]
            mydb.commit()
            messagebox.showinfo('Successful withdrawal',
                                f'{amount} dollars were withdrawn from your account.\nNew balance : {balance}')

        withdrawButton = Button(
            withdrawalFrame,
            text='WITHDRAW',
            relief=FLAT,
            bg='#7F9BA8',
            fg='#F3F4EA',
            anchor=CENTER,
            font=entryFont,
            command=withdraw)
        withdrawButton.place(relx=0.38, rely=0.76, width=190, height=42)

        def goBack():
            if withdrawalFrame.winfo_ismapped():
                withdrawalFrame.pack_forget()
            if not homeFrame.winfo_ismapped():
                homeFrame.pack()

        backButton = Button(
            withdrawalFrame,
            text='< Back',
            font=textFont,
            anchor=W,
            relief=FLAT,
            bg='#002441',
            fg='#F3F4EA',
            borderwidth=0,
            activebackground="#002441",
            activeforeground="#203657",
            command=goBack)
        backButton.place(relx=0.02, rely=0.92, height=30)


################################################GRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPE################################################


class depositFrameClass():

    @staticmethod
    def depositFrameCreator():

        homeFrame.pack_forget()

        depositFrame = Frame(
            window,
            height=600,
            width=800,
            bg="#002441")
        depositFrame.pack()

        genericLabel = Label(
            depositFrame,
            text='SIERRA\nBANK',
            font=smallHeadFont,
            justify=LEFT,
            bg='#002441',
            fg='#F3F4EA')
        genericLabel.place(relx=0.035, rely=0.03775)

        subHeadLabel = Label(
            depositFrame,
            text='Make a\ndeposit',
            font=subHeadFont,
            justify=RIGHT,
            bg='#002441',
            fg='#F3F4EA')
        subHeadLabel.place(relx=0.72, rely=0.03775)

        accountNumberLabel = Label(
            depositFrame,
            text='Account number',
            font=textFont,
            anchor=E,
            bg='#002441',
            fg='#F3F4EA')
        accountNumberLabel.place(relx=0.185, rely=0.4, width=222, height=44)

        PINLabel = Label(
            depositFrame,
            text='PIN',
            font=textFont,
            anchor=E,
            bg='#002441',
            fg='#F3F4EA')
        PINLabel.place(relx=0.185, rely=0.5, width=222, height=44)

        amountLabel = Label(
            depositFrame,
            text='Amount',
            font=textFont,
            anchor=E,
            bg='#002441',
            fg='#F3F4EA')
        amountLabel.place(relx=0.185, rely=0.6, width=222, height=44)

        accNumEntry = Entry(
            depositFrame,
            relief=FLAT,
            bg='#203657',
            fg='#F3F4EA',
            font=entryFont,
            borderwidth=6)
        accNumEntry.place(relx=0.52, rely=0.409, width=222, height=30)

        PINEntry = Entry(
            depositFrame,
            relief=FLAT,
            bg='#203657',
            fg='#F3F4EA',
            font=entryFont,
            borderwidth=6)
        PINEntry.place(relx=0.52, rely=0.509, width=222, height=30)

        amountEntry = Entry(
            depositFrame,
            relief=FLAT,
            bg='#203657',
            fg='#F3F4EA',
            font=entryFont,
            borderwidth=6)
        amountEntry.place(relx=0.52, rely=0.609, width=222, height=30)

        def deposit():
            acc_no = accNumEntry.get()
            pin = PINEntry.get()
            amount = amountEntry.get()

            if not check_valid_acc(acc_no):
                return

            checks = []
            if not acc_no.isdigit():
                checks.append('The account number must only contain digits.')
            if not amount.isdigit():
                checks.append('The amount must only contain digits.')
            if not pin.isdigit():
                checks.append('The PIN must only contain digits.')
            if len(acc_no) != 8:
                checks.append('The account number must contain exactly 8 digits.')
            if len(pin) != 4:
                checks.append('The PIN must contain exactly 4 digits.')
            if checks:
                err_msg = '\n'.join(checks)
                messagebox.showerror("Invalid Input", err_msg)
                return

            mycursor.execute(f'UPDATE bank_master SET balance = balance + {amount} where acc_no = {acc_no}')
            mycursor.execute(f"INSERT INTO bank_trans VALUES({acc_no}, {amount}, '{date.today()}', 'D')")
            mycursor.execute(f'SELECT balance FROM bank_master where acc_no = {acc_no}')
            balance = mycursor.fetchone()[0]
            mydb.commit()
            messagebox.showinfo('Successful deposit',
                                f'{amount} QR/- was deposited to your account.\nNew balance : {balance}')

        depositButton = Button(
            depositFrame,
            text='DEPOSIT',
            relief=FLAT,
            bg='#7F9BA8',
            fg='#F3F4EA',
            anchor=CENTER,
            font=entryFont,
            command=deposit)
        depositButton.place(relx=0.38, rely=0.76, width=190, height=42)

        def goBack():
            if depositFrame.winfo_ismapped():
                depositFrame.pack_forget()
            if not homeFrame.winfo_ismapped():
                homeFrame.pack()

        backButton = Button(
            depositFrame,
            text='< Back',
            font=textFont,
            anchor=W,
            relief=FLAT,
            bg='#002441',
            fg='#F3F4EA',
            borderwidth=0,
            activebackground="#002441",
            activeforeground="#203657",
            command=goBack)
        backButton.place(relx=0.02, rely=0.92, height=30)


if __name__ == '__main__':
    HomeFrameClass.homeFrameCreator()
    window.mainloop()
