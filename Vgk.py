# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\mathe\OneDrive\Área de Trabalho\orangotango.mp3\python\vgk\gui\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def start_service():
    try:
        subprocess.run(r'cd c:\windows\system32 && sc start vgk', check=True, shell=True)
        messagebox.showinfo("Sucesso", "Serviço vgk iniciado com sucesso!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Erro", "Falha ao iniciar o serviço vgk.")

def stop_service():
    try:
        subprocess.run(r'cd c:\windows\system32 && sc stop vgk', check=True, shell=True)
        messagebox.showinfo("Sucesso", "Serviço vgk parado com sucesso!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Erro", "Falha ao parar o serviço vgk.")

window = Tk()
window.title("Controle do Serviço vgk")
window.geometry("850x480")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=480,
    width=850,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

# Define image_1.png as the background
background_image = PhotoImage(file=relative_to_assets("image_1.png"))
canvas.create_image(
    0, 0,
    image=background_image,
    anchor="nw"
)

canvas.create_text(
    292.0,
    38.0,
    anchor="nw",
    text="Vanguard Inicializer",
    fill="#FFFFFF",
    font=("AllertaStencil Regular", 48 * -1)
)

# Add image_2.png to the left side of the buttons
image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
canvas.create_image(
    420.0,  # Ajuste a posição x conforme necessário
    220.0,  # Ajuste a posição y conforme necessário
    image=image_image_2,
    anchor="e"
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=stop_service,  # Invertido para parar o serviço
    relief="flat"
)
button_1.place(
    x=508.0,
    y=255.0,
    width=95.0,
    height=32.0
)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=start_service, 
    relief="flat"
)
button_2.place(
    x=508.0,
    y=193.0,
    width=95.0,
    height=32.0
)

canvas.create_text(
    752.0,
    452.0,
    anchor="nw",
    text="SUPORT",
    fill="#304FFE",
    font=("OpenSansItalic Light", 12 * -1)
)

window.resizable(False, False)
window.mainloop()
