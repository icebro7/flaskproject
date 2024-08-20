import sqlite3

con = sqlite3.connect('empdata.db')
cur = con.cursor()



cur.execute("CREATE TABLE employ(name TEXT,education TEXT,salaryMax Decimal,salaryMin Decimal,companyName TEXT,companyId TEXT,workCity TEXT,empcode Decimal)")
con.commit()
con.close()