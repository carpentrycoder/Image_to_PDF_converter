import tkinter as tk
from tkinter import filedialog
from reportlab.pdfgen import canvas
from PIL import Image
import os

class imgtopdfconverter:
    def __init__(self, root):
        self.root = root
        self.image_paths = []
        self.output_pdf_name = tk.StringVar()
        self.selected_img_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)

        self.intial_UI()

    def intial_UI(self):
        title_lbl = tk.Label(self.root, text="IMAGE TO PDF CONVERTER", font=('Poppins', 16, "bold"))
        title_lbl.pack(pady=10)
        self.root.configure(bg="#237D87")

        seleimg = tk.Button(self.root, text="Upload images here", command=self.seleimg)
        seleimg.pack(pady=(0, 10))

        self.selected_img_listbox.pack(pady=(0, 10), fill=tk.BOTH, expand=True)

        lbl = tk.Label(self.root, text="Enter pdf name: ")
        lbl.pack()

        pdf_name_entry = tk.Entry(self.root, textvariable=self.output_pdf_name, width=60, justify="center")
        pdf_name_entry.pack()

        convert = tk.Button(self.root, text="Convert", command=self.convert)
        convert.pack(pady=(20, 40))

        window_width = 500
        window_height = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    def seleimg(self):
        self.image_paths = filedialog.askopenfilenames(title="select images", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        self.update_sele_img_listbox()

    def update_sele_img_listbox(self):
        self.selected_img_listbox.delete(0, tk.END)

        for image_path in self.image_paths:
            _, img_name = os.path.split(image_path)
            self.selected_img_listbox.insert(tk.END, img_name)

    def convert(self):
        if not self.image_paths:
            return

        output_pdf_name = self.output_pdf_name.get() + ".pdf" if self.output_pdf_name.get() else "output.pdf"
        pdf = canvas.Canvas(output_pdf_name, pagesize=(612, 792))

        for image_path in self.image_paths:
            photo = Image.open(image_path)
            our_width = 500
            our_height = 720
            scale_fact = min(our_width / photo.width, our_height / photo.height)
            new_width = photo.width * scale_fact
            new_height = photo.height * scale_fact
            x_center = (612 - new_width) / 2
            y_center = (792 - new_height) / 2

            pdf.drawInlineImage(photo, x_center, y_center, width=new_width, height=new_height)
            pdf.showPage()

        pdf.save()


def main():
    root = tk.Tk()
    root.title("IMAGE TO PDF CONVERTER")
    root.geometry("500x600")
    convert = imgtopdfconverter(root)
    root.mainloop()


if __name__ == "__main__":
    main()