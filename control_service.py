import subprocess
import tkinter as tk
from tkinter import messagebox

def start_service():
    try:
        subprocess.run(r'cd c:\windows\system32 && sc start vgk', check=True, shell=True)
        messagebox.showinfo("Successo", "Serviço vgk iniciado com sucesso!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Erro", "Falha ao iniciar o serviço vgk.")

def stop_service():
    try:
        subprocess.run(r'cd c:\windows\system32 && sc stop vgk', check=True, shell=True)
        messagebox.showinfo("Successo", "Serviço vgk parado com sucesso!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Erro", "Falha ao parar o serviço vgk.")

root = tk.Tk()
root.title("Controle do Serviço vgk")

start_button = tk.Button(root, text="Executar", command=start_service)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Parar", command=stop_service)
stop_button.pack(pady=10)

root.mainloop()
