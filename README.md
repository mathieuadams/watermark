# 📸 Watermark GUI App

A simple and intuitive Python GUI application for adding watermark overlays to your images. Built with `Tkinter` for the interface and `Pillow` for image processing, this tool allows users to preview and save watermarked versions of their images with custom text and stylish diagonal patterns.

---

## 🧩 Features

- ✅ Load and display an image on a canvas  
- ✅ Add a centered text watermark with adjustable size  
- ✅ Overlay diagonal transparent lines for style  
- ✅ Preview the watermarked image in the app  
- ✅ Save the edited image to disk in JPEG or PNG format  

---

## 🛠️ Built With

- **Python 3**
- **Tkinter** – for the user interface
- **Pillow (PIL)** – for image processing

---

## 📁 Project Structure

```
📦 WatermarkApp
├── main.py             # Entry point to launch the GUI
├── ui.py               # Tkinter GUI logic
├── watermark.py        # Watermark logic using Pillow
├── README.md           # You're here!
```

---

## ▶️ How to Run

1. **Install dependencies** (if not already installed):

```bash
pip install pillow
```

2. **Run the application:**

```bash
python main.py
```

3. **Steps inside the app:**
   - Enter the full path or filename of your input image.
   - Enter an output filename (e.g., `output.jpg`).
   - Type your watermark text.
   - Click **Add Image** to view the original.
   - Click **Add WaterMark** to apply your overlay.
   - Click **Save Image** to save the result.

---

## 💡 Example Watermark Output

- Transparent white diagonal stripes.
- Centered watermark text with adjustable font size.
- Subtle and professional design for branding images.

---

## 📌 Notes

- For custom fonts, ensure `arial.ttf` exists on your system. You can replace it with another TTF font if needed.
- Output images are saved in the same directory unless a full path is provided.
- Supported formats: `.jpg`, `.png`, `.jpeg`, `.bmp` (Pillow handles most).

---

## ✨ Future Improvements (Optional Ideas)

- Add drag-and-drop file support.
- Let users choose watermark position or color.
- Enable font size/opacity controls with sliders.
- Use `filedialog.askopenfilename()` and `asksaveasfilename()` for easier file selection.
