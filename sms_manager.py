import psycopg2
from datetime import datetime

class SMSManager:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cur = self.conn.cursor()

    def yuborish(self, sender, receiver, message):
        query = "INSERT INTO sms (sender, receiver, message, date_sent) VALUES (%s, %s, %s, %s)"
        self.cur.execute(query, (sender, receiver, message, datetime.now()))
        self.conn.commit()
        print(f"'{sender}' dan '{receiver}' ga SMS yuborildi.")

    def tarix(self):
        self.cur.execute("SELECT * FROM sms ORDER BY id DESC;")
        rows = self.cur.fetchall()
        if rows:
            print("\nSMS Tarixi:")
            for r in rows:
                print(f"{r[0]}. {r[1]} ➜ {r[2]} | {r[3]} | {r[4]}")
        else:
            print("Yuborilgan smslar yoq ")

    def close(self):
        self.cur.close()
        self.conn.close()
