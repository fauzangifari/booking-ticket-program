from Model import mongodb as db
from View import admin_view
from View import user_view
import main
import pwinput


class User:

    user_session = []

    def __init__(self):
        self.logged_in = False
        self.main = main
        self.username = ""

    def register(self):
        print("----------------------- REGISTRASI ----------------------")
        name = str.capitalize(input("Masukkan username: "))
        if db.dataAcc.find_one({"name": name}):
            print("Username sudah digunakan!")
            return False
        else:
            password = str(pwinput.pwinput("Masukkan password: "))
            saldo = int(input("Masukkan saldo awal: "))
            email = str(input("Masukkan email: "))
            db.dataAcc.insert_one(
                {"name": name, "password": password, "saldo": saldo, "email": email, "privilege": "Reguler",
                 "role": "user"})
            print("\n--------------- DATA TELAH DIKONFRIMASI ---------------")
            print("> Username: ", name)
            print("> Password: ", password)
            print("> Saldo: ", saldo)
            print("> Email: ", email)
            print("---------------------------------------------------------")
            confirm = input("Tekan [ENTER] jika sesuai dengan anda input!")
            if confirm == '':
                print("\nRegistrasi Berhasil!")
                return True
            else:
                return True

    def login(self):
        print("----------------------- LOGIN ---------------------------")
        count = 3
        while count >= 0:
            count -= 1
            name = str.capitalize(input("> Masukkan username anda: "))
            password = str(pwinput.pwinput("> Masukkan password anda: "))
            user = db.dataAcc.find_one({"name": name, "password": password})
            if user and user["name"] == name and user["password"] == password:
                if user:
                    if user.get("role") == "admin":
                        print("Login berhasil!")
                        self.logged_in = True
                        self.username = user["name"]
                        admin_view.AdminView().menuAdmin()
                        return True
                    elif user.get("role") == "user":
                        print("Login berhasil!")
                        self.logged_in = True
                        self.username = user["name"]
                        session_data = {"username": self.username}
                        User.user_session.append(session_data)
                        user_view.UserView().menuUser()
                        return True
            else:
                print('Username atau Password Salah!')
                print('Anda Memiliki', count, 'Kali Percobaan')
                if count == 0:
                    print('Anda telah mencapai batas maksimum percobaan login. Silakan coba lagi nanti.')
                    return False

    def forgot_password(self):
        print("----------------------- LUPA PASSWORD -------------------")
        name = str.capitalize(input("> Masukkan username: "))
        user = db.dataAcc.find_one({"name": name})
        if user:
            new_password = pwinput.pwinput("> Masukkan password baru: ")
            db.dataAcc.update_one({"name": name}, {"$set": {"password": new_password}})
            print("Password berhasil diubah!")
            return True
        else:
            print("Username tidak ditemukan!")
            return False

    def logout(self):
        for session in User.user_session[:]:
            if session["username"] == self.username:
                print(f"User {self.username} berhasil logout")
                User.user_session.clear(session)
                self.logged_in = False
                self.username = ""
        print("Tidak ada user yang login saat ini!")


    def profile(self):
        print("----------------------- PROFILE -------------------------")
        data = User.user_session[0]["username"]
        user = db.dataAcc.find_one({"name": data})
        if user:
            print("Nama: ", user["name"])
            print("Saldo: ", user["saldo"])
            print("Email: ", user["email"])
            print("Privilege: ", user["privilege"])
            print("---------------------------------------------------------")
            confirm = input("Tekan [ENTER] jika ingin kembali ke menu utama!")
            if confirm == '':
                user_view.UserView().menuUser()
            else:
                user_view.UserView().menuUser()
        else:
            print("User tidak ditemukan!")
            return False
