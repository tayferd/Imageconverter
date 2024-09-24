import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image

# List of supported output formats
SUPPORTED_FORMATS = ["jpg", "pdf", "bmp", "gif", "tiff", "webp"]


# Function to handle the image conversion
def convert_image():
    # Ask user to select an image file
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[
            ("All Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff;*.webp"),
            ("PNG files", "*.png"),
            ("JPEG files", "*.jpg;*.jpeg"),
            ("BMP files", "*.bmp"),
            ("GIF files", "*.gif"),
            ("TIFF files", "*.tiff"),
            ("WEBP files", "*.webp")
        ]
    )

    if not file_path:
        return  # Exit if no file is selected

    # Get the selected format from dropdown
    format_selection = format_var.get().lower()

    if format_selection not in SUPPORTED_FORMATS:
        messagebox.showerror("Error", "Unsupported format selected!")
        return

    # Ask user where to save the converted file
    save_path = filedialog.asksaveasfilename(
        defaultextension=f".{format_selection}",
        filetypes=[(f"{format_selection.upper()} files", f"*.{format_selection}")],
        title=f"Save the {format_selection.upper()} file"
    )

    if not save_path:
        return  # Exit if no save path is provided

    try:
        # Open and convert the image to RGB for compatibility
        img = Image.open(file_path)
        img = img.convert("RGB")  # Ensure compatibility for formats like JPEG, PDF
        img.save(save_path, format_selection.upper())
        messagebox.showinfo("Success", f"Image successfully converted to {format_selection.upper()}!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert image: {e}")


# Set up Tkinter window
root = tk.Tk()
root.title("Image Converter")

# Dropdown for selecting format
format_var = tk.StringVar(value="jpg")
format_label = tk.Label(root, text="Select format to convert to:")
format_label.pack(pady=5)

format_dropdown = ttk.Combobox(root, textvariable=format_var, values=SUPPORTED_FORMATS, state="readonly")
format_dropdown.pack(pady=5)

# Create and place the Convert button
convert_button = tk.Button(root, text="Select Image to Convert", command=convert_image)
convert_button.pack(pady=20)

# Start the Tkinter loop
root.geometry("300x200")
root.mainloop()
