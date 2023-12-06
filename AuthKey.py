import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def check_key():
    entered_key = entry.get()
    correct_key = "123erLlopQWOiZI9"

    if entered_key == correct_key:
        messagebox.showinfo("Success", "Correct Key! Starting MyApp.exe")
        # Spusti aplikáciu MyApp.exe
        # Tu môžete pridať kód na spustenie vášho programu

        # Zavrie okno
        root.destroy()
    else:
        label_result.config(text="Incorrect Key!", fg="red")
        label_try_again.config(text="Please try again.")

# Vytvoriť hlavné okno
root = tk.Tk()
root.title("MyApp Authenticator")

# Nastaviť veľkosť okna
width, height = 600, 300
root.geometry(f"{width}x{height}")

# Načítať a prispôsobiť tapetu
image = Image.open("Photo.jpg")
image = image.resize((width, height), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Vytvoriť vstupné pole a nadpis
entry = tk.Entry(root, font=("Helvetica", 14))
entry.place(relx=0.5, rely=0.4, anchor="center")

label = tk.Label(root, text="Type Auth Key", font=("Helvetica", 16))
label.place(relx=0.5, rely=0.35, anchor="center")

# Vytvoriť tlačidlo na overenie kľúča
button = tk.Button(root, text="Verify Key", command=check_key)
button.place(relx=0.5, rely=0.5, anchor="center")

# Vytvoriť štítky pre výsledok overenia kľúča
label_result = tk.Label(root, text="", font=("Helvetica", 16))
label_result.place(relx=0.5, rely=0.6, anchor="center")

label_try_again = tk.Label(root, text="", font=("Helvetica", 14))
label_try_again.place(relx=0.5, rely=0.65, anchor="center")

# Spustiť hlavnú slučku
root.mainloop()
