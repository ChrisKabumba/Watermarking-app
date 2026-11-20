import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageFile
import os

im: ImageFile

def open_file():
    with filedialog.askopenfile('rb', title='select file') as file:
        try:
            im = Image.open(file)

            tk_im = tk.PhotoImage(file=file.name)     
            canvas.create_image(0, 0, image=tk_im)

            watermark = Image.open(os.getcwd() + '\\assets\\watermark.png')

            box = (
                int(im.size[0]/2 - watermark.size[0]/2),
                int(im.size[1]/2 - watermark.size[1]/2),
                int(im.size[0]/2 + watermark.size[0]/2),
                int(im.size[1]/2 + watermark.size[1]/2),
            )

            im.paste(watermark, box, mask=Image.new('RGBA', watermark.size, (0, 0, 0, 128)))

            try:
                save_file_path = filedialog.asksaveasfilename(
                    defaultextension='png', 
                    title='Select a name',
                    filetypes=[
                        ('PNG files', '*.png')
                    ]
                )

                im.save(save_file_path, 'png')

                im.show()
            except Exception as e:
                print(e)
        except OSError:
            pass


window = tk.Tk()
window.title("Watermark App")
window.minsize(1080, 700)

text_label = tk.Label(text="Watermark", font=("Arial", 24, "bold"))
text_label.grid(column=0, row=0, columnspan=2)

open_file_btn = tk.Button(text="Open file", command=open_file)
open_file_btn.grid(column=0, row=1, columnspan=2)

canvas = tk.Canvas(width=1080, height=700)
canvas.grid(column=0, row=2, columnspan=2)

window.mainloop()