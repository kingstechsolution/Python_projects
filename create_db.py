import sqlite3
def create_db():
    conn=sqlite3.connect(database=r'AppDatabase.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(id CHAR PRIMARY KEY AUTOINCREMENT, name text, email text, gender text, contact text, dob text, doj text, pass text, utype text, address text, salary text)")
    conn.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(InvoiceNo INTEGER PRIMARY KEY AUTOINCREMENT, name text, contact text, description text)")
    conn.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text)")
    conn.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT, category text, supplier text, product text, price text, quantity text, status text)")
    conn.commit()

create_db()

