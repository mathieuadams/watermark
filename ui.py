from tkinter import *
from PIL import Image, ImageTk
from watermark import AddWaterMark
from watermark import *
THEME_COLOR = "#375362"
class AddWaterMarkUI():
    def __init__(self):
        self.window = Tk()
        self.window.title("Watermark")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=4, column=0, columnspan=2, pady=10)

        self.text_entry_label = Label(text="Add Watermark to your picture")
        self.text_entry_label.grid(row=0, column=0, columnspan=2)

        self.input_path_entry = Entry(width=21)
        self.input_path_entry.grid(row=1, column=0)

        self.output_path_entry = Entry(width=21)
        self.output_path_entry.grid(row=2, column=0)

        self.Overlay_text_entry = Entry(width=21)
        self.Overlay_text_entry.grid(row=3, column=0)

        self.add_img_btn = Button(text="Add Image", width=13, command=self.show_image)
        self.add_img_btn.grid(row=1, column=2)

        self.save_btn = Button(text="Save Image", width=13, command=self.save_image)
        self.save_btn.grid(row=2, column=2)

        self.add_overlay_btn = Button(text="Add WaterMark", width=13, command=self.addwatermark)
        self.add_overlay_btn.grid(row=3, column=2)
        self.tk_img = None
        self.watermark = None
        self.window.mainloop()

    def show_image(self):
        input_path = self.input_path_entry.get()
        if input_path:
            try:
                img = Image.open(input_path)
                img = img.resize((300,250))
                self.tk_img = ImageTk.PhotoImage(img)
                self.canvas.create_image(0,0, anchor="nw", image=self.tk_img)
            except Exception as e:
                print(f"Error loading image: {e}")


    def addwatermark(self):
        watermark_text = self.Overlay_text_entry.get()
        input_image = self.input_path_entry.get()
        if watermark_text:
            self.watermark = AddWaterMark(input_image)
            self.watermark.add_watermark_overlay(watermark_text)
            display_image = self.watermark.watermarked_image.convert('RGB')
            display_image = display_image.resize((300,250))
            self.tk_img = ImageTk.PhotoImage(display_image)
            self.canvas.create_image(0, 0, anchor="nw", image=self.tk_img)

    def save_image(self):
        output_path = self.output_path_entry.get()

        # if not output_path:
        #     print("⚠️ Output path is empty.")
        #     return
        #
        # if not hasattr(self, 'watermark'):
        #     print("⚠️ No watermark has been created yet. Click 'Add WaterMark' first.")
        #     return

        try:
            self.watermark.watermarked_image.convert("RGB").save(output_path)
            print(f"✅ Image saved successfully at: {output_path}")
        except Exception as e:
            print(f"❌ Error saving image: {e}")
