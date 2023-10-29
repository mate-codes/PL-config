import tkinter as tk
import os

def shutdown():
    os.system("poweroff")

def restart():
    os.system("reboot")

def cancel():
    root.destroy()

root = tk.Tk()
root.title("System Control")
root.geometry("300x150")
root.resizable(False, False)

# Dark mode colors (darker)
bg_color = "#111111"   # Darker background color
fg_color = "white"     # Text color

root.configure(bg=bg_color)  # Set the background color for the root window

button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack(fill=tk.BOTH, expand=True)

# Configure the buttons with dark mode colors
shutdown_button = tk.Button(button_frame, text="Shutdown", command=shutdown, bg=bg_color, fg=fg_color)
shutdown_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

restart_button = tk.Button(button_frame, text="Restart", command=restart, bg=bg_color, fg=fg_color)
restart_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

cancel_button = tk.Button(root, text="Cancel", command=cancel, bg=bg_color, fg=fg_color)
cancel_button.pack(fill=tk.BOTH, expand=True, pady=10)

root.mainloop()
