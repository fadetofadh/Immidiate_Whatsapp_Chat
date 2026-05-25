import tkinter as tk
from tkinter import messagebox
import webbrowser

def open_whatsapp():
    phone_number = entry.get().strip()

    # Validate the phone number (basic validation)
    phone= ''.join(filter(str.isdigit, phone_number))  # Remove non-digit characters

    # Convert 08 to 628 if the number starts with 08
    if phone_number.startswith('08'):
        phone = '62' + phone[1:]
    
    if not phone.startswith('62'):
        messagebox.showerror("Invalid Number", "Please enter a valid Indonesian phone number starting with 08 or 62.")
        return
    
    url = f"https://wa.me/{phone}"

    try:
        webbrowser.open(url)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open WhatsApp: {e}")
    
    root.quit()  # Close the main loop
    root.destroy()  # Close the app after opening WhatsApp
   
root = tk.Tk()
vcmd = (root.register(lambda P: str.isdigit(P) or P == ""), '%P')
root.title("WA Chat")

# Center window app based on display
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 230
window_height = 150

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.attributes("-toolwindow", True)  # Remove minimize and maximize buttons

label = tk.Label(root, text="Enter the phone number\n(starting with 08 or 62):", wraplength=200)
label.pack(pady=10)

entry = tk.Entry(root, width=30, justify='center', validate='key', validatecommand=vcmd)
entry.pack(pady=5)
entry.focus()  # Set focus to the entry widget

button = tk.Button(root, text="Open WhatsApp", command=open_whatsapp)
button.pack(pady=10)

root.bind('<Return>', lambda event: open_whatsapp())  # Bind Enter key to the function
root.mainloop()