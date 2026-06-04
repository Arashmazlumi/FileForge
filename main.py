import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from moviepy.editor import VideoFileClip
import os

class FileForge:
    def __init__(self, root):
        self.root = root
        root.title("FileForge")
        root.geometry("500x400")
        root.configure(bg='#2b2b2b')
        
        tk.Label(root, text="🔥 FileForge", font=("Arial", 20, "bold"), 
                bg='#2b2b2b', fg='#ff6b35').pack(pady=20)
        
        tk.Label(root, text="Select your file:", bg='#2b2b2b', fg='white').pack()
        self.file_path = tk.StringVar()
        tk.Entry(root, textvariable=self.file_path, width=40).pack(pady=5)
        tk.Button(root, text="Browse", command=self.select_file).pack()
        
        tk.Label(root, text="Convert to:", bg='#2b2b2b', fg='white').pack(pady=10)
        self.convert_type = tk.StringVar(value="jpg")
        
        for text, value in [("JPG", "jpg"), ("PNG", "png"), ("GIF (first 10s)", "gif")]:
            tk.Radiobutton(root, text=text, variable=self.convert_type, 
                          value=value, bg='#2b2b2b', fg='white').pack()
        
        tk.Button(root, text="CONVERT", command=self.convert, 
                 bg='#ff6b35', fg='white', font=("Arial", 12, "bold")).pack(pady=30)
        
        self.status = tk.Label(root, text="Ready", bg='#2b2b2b', fg='gray')
        self.status.pack()
    
    def select_file(self):
        path = filedialog.askopenfilename()
        if path:
            self.file_path.set(path)
            self.status.config(text=f"Selected: {os.path.basename(path)}")
    
    def convert(self):
        input_path = self.file_path.get()
        if not input_path:
            messagebox.showerror("Error", "Select a file first!")
            return
        
        convert_to = self.convert_type.get()
        
        try:
            if convert_to in ["jpg", "png"]:
                img = Image.open(input_path)
                output_path = input_path.rsplit('.', 1)[0] + f".{convert_to}"
                img.save(output_path)
                messagebox.showinfo("Success", f"Saved to: {output_path}")
                self.status.config(text="Done!")
            elif convert_to == "gif":
                clip = VideoFileClip(input_path).subclip(0, 10)
                output_path = input_path.rsplit('.', 1)[0] + ".gif"
                clip.write_gif(output_path, fps=10)
                messagebox.showinfo("Success", f"GIF saved to: {output_path}")
                self.status.config(text="GIF created!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status.config(text="Failed!")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileForge(root)
    root.mainloop()
