import tkinter as tk
from tkinter import messagebox
import webbrowser
from PIL import Image, ImageTk  # PIL modülünü yükleyin

def check_credentials():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if entered_username == "admin" and entered_password == "12345":
        welcome_label.config(text=f"Hoş Geldiniz, {entered_username}!")
        open_link_button.pack()  # Doğru giriş yapıldığında link butonunu göster
    else:
        messagebox.showerror("Hata", "Geçersiz Kullanıcı Adı veya Şifre!")
        open_link_button.pack_forget()  # Hatalı giriş durumunda link butonunu gizle

def open_link():
    webbrowser.open("https://mervesoftware.free.nf/")

root = tk.Tk()
root.title("Login")

# Pencere boyutunu 400x400 olarak ayarla
root.geometry("400x400")

# Beyaz arkaplan rengi
root.configure(bg="white")

# Hoşgeldiniz mesajı ve giriş alanlarını içeren bir çerçeve oluştur
frame = tk.Frame(root, bg="white")  # Çerçeve arkaplan rengi
frame.pack(pady=10)

# Hoşgeldiniz mesajını içeren etiket
welcome_label = tk.Label(frame, text="Hoş Geldiniz!", font=("Helvetica", 16), bg="white")
welcome_label.pack(pady=10)

# Kullanıcı adı alanı
username_label = tk.Label(frame, text="Kullanıcı Adı:", bg="white")
username_label.pack()
username_entry = tk.Entry(frame)
username_entry.pack()

# Şifre alanı
password_label = tk.Label(frame, text="Şifre:", bg="white")
password_label.pack()
password_entry = tk.Entry(frame, show="*")
password_entry.pack()

# Giriş yap butonu
login_button = tk.Button(frame, text="Giriş Yap", command=check_credentials)
login_button.pack(pady=10)
# Linke git butonunu başlangıçta gizle
open_link_button = tk.Button(root, text="Linke Git", command=open_link)
open_link_button.pack_forget()

# Resim dosyasının yolu
image_path = "/home/merve/PycharmProjects/pythonProject/icon2.png"
# Resmi yükleyip boyutlandırarak göster
original_image = Image.open(image_path)
resized_image = original_image.resize((100, 100), Image.LANCZOS)
image = ImageTk.PhotoImage(resized_image)
image_label = tk.Label(frame, image=image, bg="white")
image_label.pack()


root.mainloop()
