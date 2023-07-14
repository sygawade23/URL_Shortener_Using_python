import tkinter as tk
import pyshorteners
import webbrowser
import tkinter.messagebox as mbox
import pyperclip

def shorten_url():
    url = url_entry.get()
    s = pyshorteners.Shortener()
    try:
        short_url = s.tinyurl.short(url)
        shortened_label.config(text=short_url)
        mbox.showinfo("Success", "URL shortened successfully!")
    except Exception as embox.showerror("Error", str(e))

def open_shortened_url():
    short_url = shortened_label.cget("text")
    if short_url:
        webbrowser.open(short_url)

def copy_shortened_url():
    short_url = shortened_label.cget("text")
    if short_url:
        pyperclip.copy(short_url)
        mbox.showinfo("Success", "Shortened URL copied to clipboard!")
    else:
        mbox.showwarning("Warning", "No shortened URL available!")

# Create the main window
window = tk.Tk()
window.title("URL Shortener")
window.geometry("1700x1600")
window.configure(bg="#f8f8f8")

# Create the URL input label and entry field
url_label = tk.Label(window, text="Enter URL:", bg="#f8f8f8", fg="#333333", font=("Helvetica", 12))
url_label.pack(pady=10)
url_entry = tk.Entry(window, width=50, font=("Helvetica", 10))
url_entry.pack()

# Create the shorten button
shorten_button = tk.Button(window, text="Shorten URL", command=shorten_url, bg="#4caf50", fg="white", font=("Helvetica", 12), relief="flat")
shorten_button.pack(pady=10)

# Create an image label for additional creativity
image = tk.PhotoImage(file="3.png")
image_label = tk.Label(window, image=image, bg="#f8f8f8")
image_label.pack(pady=10)

# Create the label for the shortened URL
shortened_label = tk.Label(window, text="", bg="#f8f8f8", fg="#333333", font=("Helvetica", 10), wraplength=380)
shortened_label.pack(pady=10)

# Create the button to open the shortened URL
open_button = tk.Button(window, text="Open Shortened URL", command=open_shortened_url, bg="#00ff00", fg="white", font=("Helvetica", 12), relief="flat")
open_button.pack(pady=10)

# Create the button to copy the shortened URL
copy_button = tk.Button(window, text="Copy Shortened URL", command=copy_shortened_url, bg="#0000ff", fg="white", font=("Helvetica", 12), relief="flat")
copy_button.pack(pady=10)

# Run the GUI main loop
window.mainloop()