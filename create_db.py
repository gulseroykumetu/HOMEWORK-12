import sqlite3 as sql
import pyAesCrypt

con = sql.connect("hw-12.db")

db = con.cursor()

def table():
    db.execute("CREATE TABLE IF NOT EXISTS ledgertable (AccountName TEXT, AccountNumber INT,Date TEXT,DescriptionOfTheEntry TEXT, PostingReference TEXT,Debit	INT,Credit INT,DebitBalance INT,CreditBalance INT)")
    con.commit()
    con.close()

def enc(filename,password):
    pyAesCrypt.encryptFile(filename, (filename + ".enc"), password)
table()

filename=input("Enter file name (hw-12.db): ")
password=input("Enter password (123): ")

enc(filename,password)
