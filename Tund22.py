import tkinter as tk
from tkinter import filedialog, messagebox
import smtplib
from email.message import EmailMessage
import ssl
import imghdr
import os
import json

sender_email = ""
sender_password = ""
smtp_server = "smtp.gmail.com"
smtp_port = 587

attachment_path = []
SENT_LOG_FILE = "Tund22_log.json"

themes = {
    "light": {
        "bg": "#3498DB",
        "fg": "white",
        "input_bg": "#FFFFFF",
        "input_fg": "#000000",
        "button_bg": "#2980B9",
        "button_fg": "white",
    },
    "dark": {
        "bg": "#2E2E2E",
        "fg": "#FFFFFF",
        "input_bg": "#3C3C3C", 
        "input_fg": "#FFFFFF",
        "button_bg": "#505050",
        "button_fg": "#FFFFFF",
    }
}

current_theme = "light"

def send_message(message):
    server = None
    try:
        context = ssl.create_default_context()

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls(context=context)

        server.login(sender_email, sender_password)
        server.send_message(message)
        messagebox.showinfo("Info", "Kiri oli saadetud")
        log_sent_email_json(message)
    except:
        messagebox.showerror("Viga", "Tekkis viga!")
    finally:
        if server:
            server.quit()

def delete_all_attachments():
    attachment_path.clear()
    update_attachment_display()

def update_attachment_display():
    if attachment_path:
        filenames = [os.path.basename(path) for path in attachment_path]
        display_text = ", ".join(filenames)
        attachment_label_display.config(text=display_text)
        delete_attachment_button.config(state=tk.NORMAL)
    else:
        attachment_label_display.config(text="")
        delete_attachment_button.config(state=tk.DISABLED)

def select_attachments():
    filenames = filedialog.askopenfilenames(
        initialdir="Downloads",
        title="Vali failid",
        filetypes= (
            ("Kõik failid", "*.*"),
            ("Pildid", "*.jpg *.png *.gif"),
        )
    )
    if filenames:
        attachment_path.extend(filenames)
        update_attachment_display()

def create_and_send_email():
    recipient_string = email_entry.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", "end").strip()

    recipients = []
    d_recipients = recipient_string.split(',')
    for r in d_recipients:
        cleaned_recipient = r.strip()
        if cleaned_recipient:
            recipients.append(cleaned_recipient)

    if not recipients or not subject or not body:
        messagebox.showwarning("Puuduvad andmed", "Palun täitke kõik väljad")
        return

    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject
    msg.set_content(body)

    for attachment in attachment_path:
        try:
            with open(attachment, 'rb') as f:
                file_data = f.read()
                file_name = os.path.basename(attachment)

            image_subtype = imghdr.what(None, file_data)
            msg.add_attachment(file_data, maintype="image", subtype=image_subtype, filename=file_name)
        except:
             messagebox.showerror("Viga", f"Viga pilti lisamisel")
             return

    send_message(msg)

    email_entry.delete(0, tk.END)
    subject_entry.delete(0, tk.END)
    body_text.delete("1.0", tk.END)
    delete_all_attachments()

def log_sent_email_json(message):
    try:
        recipients = message.get_all('To', [])
        subject = message['Subject']
        attached_filenames = [os.path.basename(part.get_filename()) for part in message.walk() if part.get_filename()]

        new_log_entry = {
            "recipients": recipients,
            "subject": subject,
            "attachments": attached_filenames
        }
        all_log_entries = []
        try:
            with open(SENT_LOG_FILE, 'r', encoding='utf-8') as f:
                loaded_data = json.load(f)
                all_log_entries = loaded_data
        except:
                print(f"Viga olemasoleva logifaili lugemisel")
                all_log_entries = []

        all_log_entries.append(new_log_entry)

        try:
            with open(SENT_LOG_FILE, 'w', encoding='utf-8') as f:
                json.dump(all_log_entries, f, indent=4, ensure_ascii=False)
        except:
            print(f"Viga logifaili salvestamisel")

    except Exception as e:
        print(f"Viga saadetud kirja logi töötlemisel: {e}")

def preview_email():
    recipient_string = email_entry.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", "end").strip()
    attached_files = [os.path.basename(path) for path in attachment_path]

    if not recipient_string or not subject or not body:
        messagebox.showwarning("Puuduvad andmed", "Palun täitke kõik väljad et näha eelvaadet.")
        return
    
    preview_window = tk.Toplevel(root) # new, independent top-level window
    preview_window.title("E-kirja eelvaade")
    preview_window.geometry("500x600")
    theme = themes[current_theme]
    preview_window.configure(bg=theme["bg"])
    preview_window.transient(root)

    tk.Label(preview_window, text="Saaja(d):", fg=theme["fg"], bg=theme["bg"], font=("Arial", 10, "bold")).pack(pady=2, padx=10, anchor='w')
    tk.Label(preview_window, text=recipient_string, fg=theme["fg"], bg=theme["bg"], wraplength=480, justify='left').pack(pady=2, padx=10, anchor='w')

    tk.Label(preview_window, text="Teema:", fg=theme["fg"], bg=theme["bg"], font=("Arial", 10, "bold")).pack(pady=2, padx=10, anchor='w')
    tk.Label(preview_window, text=subject, fg=theme["fg"], bg=theme["bg"], wraplength=480, justify='left').pack(pady=2, padx=10, anchor='w')

    tk.Label(preview_window, text="Pildid:", fg=theme["fg"], bg=theme["bg"], font=("Arial", 10, "bold")).pack(pady=2, padx=10, anchor='w')
    attached_text = ", ".join(attached_files) if attached_files else "Puuduvad"
    tk.Label(preview_window, text=attached_text, fg=theme["fg"], bg=theme["bg"], wraplength=480, justify='left').pack(pady=2, padx=10, anchor='w')

    tk.Label(preview_window, text="Kirja sisu:", fg=theme["fg"], bg=theme["bg"], font=("Arial", 10, "bold")).pack(pady=5, padx=10, anchor='w')

    preview_body = tk.Text(preview_window, height=15, width=60, wrap="word", state="normal", font=("Arial", 10),
                           bg=theme["input_bg"], fg=theme["input_fg"], insertbackground=theme["input_fg"]) # Use input_fg for text color
    preview_body.insert("1.0", body)
    preview_body.config(state="disabled")
    preview_body.pack(pady=5, padx=10, expand=True)

    button_frame_preview = tk.Frame(preview_window, bg=theme["bg"])
    button_frame_preview.pack(pady=10)

    send_button_preview = tk.Button(button_frame_preview, text="Saada", command=lambda: [create_and_send_email(), preview_window.destroy()],
                                    bg=theme["button_bg"], fg=theme["button_fg"], font=("Arial", 10, "bold"))
    send_button_preview.grid(row=0, column=0, padx=10)

    cancel_button_preview = tk.Button(button_frame_preview, text="Sulge", command=preview_window.destroy, bg="#E74C3C", fg="white", font=("Arial", 10, "bold"))
    cancel_button_preview.grid(row=0, column=1, padx=10)

def apply_theme(theme_name):
    global current_theme
    current_theme = theme_name
    theme = themes[current_theme]

    root.configure(bg=theme["bg"])
    input_frame.configure(bg=theme["bg"])
    button_frame.configure(bg=theme["bg"])

    email_label.config(bg=theme["bg"], fg=theme["fg"])
    subject_label.config(bg=theme["bg"], fg=theme["fg"])
    attachment_label.config(bg=theme["bg"], fg=theme["fg"])
    body_label.config(bg=theme["bg"], fg=theme["fg"]) 

    email_entry.config(bg=theme["input_bg"], fg=theme["input_fg"], insertbackground=theme["fg"])
    subject_entry.config(bg=theme["input_bg"], fg=theme["input_fg"], insertbackground=theme["fg"])

    body_text.config(bg=theme["input_bg"], fg=theme["input_fg"], insertbackground=theme["fg"])

    add_attachment_button.config(bg=theme["button_bg"], fg=theme["button_fg"])
    preview_button.config(bg=theme["button_bg"], fg=theme["button_fg"])
    send_button.config(bg=theme["button_bg"], fg=theme["button_fg"])

    update_attachment_display()

def toggle_theme():
    if current_theme == "light":
        apply_theme("dark")
        theme_button.config(text="Valgus Teema")
    else:
        apply_theme("light")
        theme_button.config(text="Tume Teema")

root = tk.Tk()
root.title("E-kirja saatmine")
root.geometry("400x420")
root.configure(bg="#3498DB")

input_frame = tk.Frame(root, bg="#3498DB")
input_frame.pack(pady=10, fill="x", padx=10)

email_label = tk.Label(input_frame, text="EMAIL:", fg="white", bg="#3498DB", font=("Arial", 12, "bold")) 
email_label.grid(row=0, column=0, sticky="w", padx=5, pady=2)

email_entry = tk.Entry(input_frame, width=40, font=("Arial", 10))
email_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=2)

subject_label = tk.Label(input_frame, text="TEEMA:", fg="white", bg="#3498DB", font=("Arial", 12, "bold")) 
subject_label.grid(row=1, column=0, sticky="w", padx=5, pady=2)

subject_entry = tk.Entry(input_frame, width=40, font=("Arial", 10))
subject_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)

attachment_label = tk.Label(input_frame, text="LISA:", fg="white", bg="#3498DB", font=("Arial", 12, "bold")) 
attachment_label.grid(row=2, column=0, sticky="w", padx=5, pady=2)

attachment_label_display = tk.Label(input_frame, text="", width=30, font=("Arial", 10), anchor="w", bg="white", fg="black") 
attachment_label_display.grid(row=2, column=1, sticky="ew", padx=5, pady=2)

delete_attachment_button = tk.Button(input_frame, text="X", command=delete_all_attachments, bg="#E74C3C", fg="white", font=("Arial", 10, "bold"), state=tk.DISABLED)
delete_attachment_button.grid(row=2, column=2, padx=5, pady=2)

input_frame.grid_columnconfigure(1, weight=1)


body_label = tk.Label(root, text="KIRI:", fg="white", bg="#3498DB", font=("Arial", 12, "bold"))
body_label.pack(pady=5)

body_text = tk.Text(root, width=40, height=8, font=("Arial", 10))
body_text.pack(pady=5)

button_frame = tk.Frame(root, bg="#3498DB")
button_frame.pack(pady=10)

add_attachment_button = tk.Button(button_frame, text="LISA PILDID", command=select_attachments, bg="#2980B9", fg="white", font=("Arial", 12, "bold"))
add_attachment_button.grid(row=0, column=0, padx=5)

preview_button = tk.Button(button_frame, text="EELVAADE", command=preview_email, bg="#2980B9", fg="white", font=("Arial", 12, "bold"))
preview_button.grid(row=0, column=1, padx=5)

send_button = tk.Button(button_frame, text="SAADA", command=create_and_send_email, bg="#2980B9", fg="white", font=("Arial", 12, "bold"))
send_button.grid(row=0, column=2, padx=5)

theme_button = tk.Button(root, text="Teema vahetamine", command=toggle_theme, font=("Arial", 10, "bold"))
theme_button.pack(pady=10)

root.mainloop()
