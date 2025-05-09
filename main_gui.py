# main_gui.py
import tkinter as tk
from tkinter import filedialog, messagebox
import encryptor
import os

def encrypt_action():
    file = filedialog.askopenfilename()
    if not os.path.exists("secret.key"):
        encryptor.generate_key()
    key = encryptor.load_key()
    try:
        encryptor.encrypt_file(file, key)
        messagebox.showinfo("Success", "✅ File Encrypted Successfully")
    except Exception as e:
        messagebox.showerror("Error", f"❌ {e}")

def decrypt_action():
    file = filedialog.askopenfilename(filetypes=[("Encrypted files", "*.enc")])
    if not os.path.exists("secret.key"):
        messagebox.showerror("Error", "Key not found. Encrypt something first.")
        return
    key = encryptor.load_key()
    try:
        encryptor.decrypt_file(file, key)
        messagebox.showinfo("Success", "✅ File Decrypted Successfully")
    except Exception as e:
        messagebox.showerror("Error", f"❌ {e}")

app = tk.Tk()
app.title("🔐 AES-256 File Encryption Tool")
app.geometry("400x200")

encrypt_btn = tk.Button(app, text="🔒 Encrypt File", command=encrypt_action, width=30)
encrypt_btn.pack(pady=20)

decrypt_btn = tk.Button(app, text="🔓 Decrypt File", command=decrypt_action, width=30)
decrypt_btn.pack(pady=20)

app.mainloop()
