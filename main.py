import sqlite3

conToAccounts = sqlite3.connect("accounts.db")

cur = conToAccounts.cursor()