import psycopg2

class ContactManager:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cur = self.conn.cursor()

    def qoshish(self, name, phone, email):
        query = "INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)"
        self.cur.execute(query, (name, phone, email))
        self.conn.commit()
        print(f"'{name}' kontakt qo‘shildi.")

    def korish(self):
        self.cur.execute("SELECT * FROM contacts ORDER BY id;")
        rows = self.cur.fetchall()
        if rows:
            print("\n Kontaktlar ro‘yxati:")
            for r in rows:
                print(f"{r[0]}. {r[1]} | {r[2]} | {r[3]}")
        else:
            print("Kontaktlar yo‘q.")

    def tahrirlash(self, contact_id, name, phone, email):
        query = "UPDATE contacts SET name=%s, phone=%s, email=%s WHERE id=%s"
        self.cur.execute(query, (name, phone, email, contact_id))
        self.conn.commit()
        print(f"Kontakt ID {contact_id} taxrirlandi.")

    def ochirish(self, contact_id):
        self.cur.execute("DELETE FROM contacts WHERE id=%s", (contact_id,))
        self.conn.commit()
        print(f"Kontakt ID {contact_id} o‘chirildi.")

    def close(self):
        self.cur.close()
        self.conn.close()
