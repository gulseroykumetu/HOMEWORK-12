import sqlite3 as sql
import datetime
import pyAesCrypt


def dec(filename,password):
    f = filename[:-4]
    pyAesCrypt.decryptFile(filename, f, password)

def enc(filename,password):
    pyAesCrypt.encryptFile(filename, (filename + ".enc"), password)

filename=input("Enter file name (hw-12.db.enc): ")
password=input("Enter password (123): ")

dec(filename,password)


con = sql.connect("hw-12.db")

db = con.cursor()

userResponse = input("Do you want to load an account or open a new one ?\nPress 1 key to load an account.\nPress 2 key to open a new one.\n")
if(userResponse == "1"):
    accountName =  input("Enter the account name: ")
    print()
    db.execute("SELECT * FROM ledgertable where AccountName='{}'".format(accountName))
    rows = db.fetchall()
    if len(rows)==0:
        print("Error: The account does not exist!")
    else:
        for row in rows:
            print("Account Name:", row[0])
            print("Account Number:", row[1])
            print("Date:", row[2])
            print("Description Of The Entry:", row[3])
            print("Posting Reference:", row[4])
            print("Debit:", row[5])
            print("Credit:", row[6])
            print("Debit Balance:", row[7])
            print("Credit Balance:", row[8])
            print()
    con.commit()
    
            
        
elif userResponse == "2":
    newAccountName = input("Enter the new account name:")
    AccountNumber = 12345678
    Date = datetime.date.today()
    DescriptionOfTheEntry = input("Description:")
    PostingReference = input("Posting Reference:")
    Debit = input("Debit:")
    Credit = input("Credit:")
    DebitBalance = input("Debit Balance:")
    CreditBalance = input("Credit Balance:")
    db.execute("INSERT INTO ledgertable (AccountName,AccountNumber,Date,DescriptionOfTheEntry,PostingReference,Debit,Credit,DebitBalance,CreditBalance)  VALUES ('{}', {},'{}','{}','{}', {} , {}, {}, {})".format(newAccountName,AccountNumber,Date,DescriptionOfTheEntry,PostingReference,Debit,Credit,DebitBalance,CreditBalance))
    print("New account is created successfully!")
    con.commit()
con.close()


enc(filename[:-4],password)
