import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import requests
from io import BytesIO

def get_new_fox():
    url = "https://randomfox.ca/floof/"
    response = requests.get(url).json()
    img_url = response["image"]
    img_data = requests.get(img_url).content
    img = Image.open(BytesIO(img_data))
    img = img.resize((400, 300))
    img_tk = ImageTk.PhotoImage(img)
    label.config(image=img_tk)
    label.image = img_tk

root = tk.Tk()
root.title("Лисички")

label = Label(root)
label.pack()

btn = Button(root, text="Новая лисичка", command=get_new_fox)
btn.pack()

get_new_fox()

root.mainloop()
