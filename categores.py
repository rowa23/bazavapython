import psycopg2
from datetime import datetime

class Yangiliklar:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cur = self.conn.cursor()

    def add_category(self, title):
        self.cur.execute("INSERT INTO category (title) VALUES (%s)", (title,))
        self.conn.commit()
        print(f"'{title}' kategoriyasi qo‘shildi.")

    def show_categories(self):
        self.cur.execute("SELECT * FROM category ORDER BY id;")
        rows = self.cur.fetchall()
        if rows:
            print("\nKategoriyalar ro‘yxati:")
            for r in rows:
                print(f"{r[0]}. {r[1]}")
        else:
            print(" Hech qanday kategoriya yo‘q.")

    def update_category(self, category_id, new_title):
        self.cur.execute("UPDATE category SET title=%s WHERE id=%s", (new_title, category_id))
        self.conn.commit()
        print(f"Kategoriya ID {category_id} yangilandi.")

    def delete_category(self, category_id):
        self.cur.execute("DELETE FROM category WHERE id=%s", (category_id,))
        self.conn.commit()
        print(f"Kategoriya ID {category_id} va unga tegishli barcha yangiliklar o‘chirildi.")

    def add_news(self, title, category_id, content):
        query = """
            INSERT INTO news (title, category_id, content, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s)
        """
        now = datetime.now()
        self.cur.execute(query, (title, category_id, content, now, now))
        self.conn.commit()
        print(f"'{title}' yangilik qo‘shildi.")

    def show_news(self):
        self.cur.execute("""
            SELECT n.id, n.title, c.title, n.content, n.created_at, n.updated_at
            FROM news n
            LEFT JOIN category c ON n.category_id = c.id
            ORDER BY n.id;
        """)
        rows = self.cur.fetchall()
        if rows:
            print("\nYangiliklar ro‘yxati:")
            for r in rows:
                print(f"{r[0]}. {r[1]} | Kategoriya: {r[2]} | {r[3]}")
                print(f"Yaratilgan: {r[4]} | Tahrirlangan: {r[5]}")
        else:
            print("Hali yangilik yo‘q.")

    def update_news(self, news_id, new_title, new_content, new_category_id):
        now = datetime.now()
        query = """
            UPDATE news
            SET title=%s, content=%s, category_id=%s, updated_at=%s
            WHERE id=%s
        """
        self.cur.execute(query, (new_title, new_content, new_category_id, now, news_id))
        self.conn.commit()
        print(f"Yangilik ID {news_id} yangilandi.")

    def delete_news(self, news_id):
        self.cur.execute("DELETE FROM news WHERE id=%s", (news_id,))
        self.conn.commit()
        print(f"Yangilik ID {news_id} o‘chirildi.")

    def close(self):
        self.cur.close()
        self.conn.close()

def main():
    app = Yangiliklar('news_db', 'postgres', '123')

    while True:
        print("\n===NEWS MANAGER ===")
        print("1. Kategoriya bo‘limi")
        print("2. Yangiliklar bo‘limi")
        print("3. Chiqish")

        tanlov = input("Tanlang: ")

        # CATEGORY MENU
        if tanlov == "1":
            while True:
                print("\n--- CATEGORY MENU ---")
                print("1. Kategoriya qo‘shish")
                print("2. Kategoriyalarni ko‘rish")
                print("3. Kategoriyani tahrirlash")
                print("4. Kategoriyani o‘chirish")
                print("5. Orqaga qaytish")

                c = input("Tanlang: ")

                if c == "1":
                    title = input("Kategoriya nomi: ")
                    app.add_category(title)
                elif c == "2":
                    app.show_categories()
                elif c == "3":
                    app.show_categories()
                    cid = int(input("Kategoriya ID: "))
                    new_title = input("Yangi nom: ")
                    app.update_category(cid, new_title)
                elif c == "4":
                    app.show_categories()
                    cid = int(input("O‘chiriladigan kategoriya ID: "))
                    app.delete_category(cid)
                elif c == "5":
                    break
                else:
                    print("Noto‘g‘ri tanlov!")

        elif tanlov == "2":
            while True:
                print("\n--- NEWS MENU ---")
                print("1. Yangilik qo‘shish")
                print("2. Yangiliklarni ko‘rish")
                print("3. Yangilikni tahrirlash")
                print("4. Yangilikni o‘chirish")
                print("5. Chiqish")

                n = input("Tanlang: ")

                if n == "1":
                    title = input("Sarlavha: ")
                    app.show_categories()
                    cid = int(input("Kategoriya ID: "))
                    content = input("Kontent: ")
                    app.add_news(title, cid, content)
                elif n == "2":
                    app.show_news()
                elif n == "3":
                    app.show_news()
                    nid = int(input("news ID: "))
                    new_title = input("sarlavha nomi")
                    new_content = input("kontent nomi ")
                    app.show_categories()
                    new_cat = int(input("Yangi kategoriya ID: "))
                    app.update_news(nid, new_title, new_content, new_cat)
                elif n == "4":
                    app.show_news()
                    nid = int(input("O‘chiriladigan yangilik ID: "))
                    app.delete_news(nid)
                elif n == "5":
                    break
                else:
                    print("Noto‘g‘ri tanlov!")

        elif tanlov == "3":
            app.close()
            print("Dastur yakunlandi.")
            break
        else:
            print("Noto‘g‘ri tanlov!")

if __name__ == "__main__":
    main()
