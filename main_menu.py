from kontakt_manger import ContactManager
from sms_manager import SMSManager

def contact_menu():
    manager = ContactManager('yusupov_baza', 'yusupov', '123')

    while True:
        print("\n=== CONTACT MANAGER ===")
        print("1. Kontakt qo‘shish")
        print("2. Kontaktlarni ko‘rish")
        print("3. Kontaktni tahrirlash")
        print("4. Kontaktni o‘chirish")
        print("5. Ortga qaytish")

        tanlov = input("Tanlang: ")

        if tanlov == "1":
            name = input("Ism: ")
            phone = input("Telefon: ")
            email = input("Email: ")
            manager.qoshish(name, phone, email)

        elif tanlov == "2":
            manager.korish()

        elif tanlov == "3":
            manager.korish()
            cid = int(input("ID kiriting: "))
            name = input("Yangi ism: ")
            phone = input("Yangi telefon: ")
            email = input("Yangi email: ")
            manager.tahrirlash(cid, name, phone, email)

        elif tanlov == "4":
            manager.korish()
            cid = int(input("ID kiriting: "))
            manager.ochirish(cid)

        elif tanlov == "5":
            manager.close()
            break
        else:
            print("Noto‘g‘ri tanlov.")


def sms_menu():
    sms = SMSManager('yusupov_baza', 'yusupov', '123')

    while True:
        print("\n=== SMS MANAGER ===")
        print("1. SMS yuborish")
        print("2. Tarixni ko‘rish")
        print("3. Ortga qaytish")

        tanlov = input("Tanlang: ")

        if tanlov == "1":
            sender = input("Kimdan: ")
            receiver = input("Kimga: ")
            message = input("Xabar: ")
            sms.yuborish(sender, receiver, message)

        elif tanlov == "2":
            sms.tarix()

        elif tanlov == "3":
            sms.close()
            break
        else:
            print("Noto‘g‘ri tanlov.")


def main():
    while True:
        print("1. Kontakt")
        print("2. SMS")
        print("3. Chiqish")

        tanlov = input("Tanlang: ")

        if tanlov == "1":
            contact_menu()
        elif tanlov == "2":
            sms_menu()
        elif tanlov == "3":
            break
        else:
            print("Noto‘g‘ri tanlov.")

if __name__ == "__main__":
    main()
