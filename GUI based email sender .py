import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import smtplib
import ssl
import csv
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email():
    name = entry_name.get()
    content = text_content.get("1.0", tk.END).strip()

    if not name or not content:
        messagebox.showerror("Error", "Please enter both name and email content.")
        return

    email_to = fetch_email_by_name(name)

    if email_to:
        try:
            smtp_port = 587  
            smtp_server = "smtp.gmail.com" 
            sender_email = "testmailmehul@gmail.com"  
            sender_password = "bwptdfcskbqmiszt"  

            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls(context=context)
                server.login(sender_email, sender_password)

                # Attach document if selected
                attachment_path = entry_attachment.get()
                if attachment_path:
                    msg = MIMEMultipart()
                    msg.attach(MIMEText(content, "plain"))

                    with open(attachment_path, 'rb') as attachment:
                        base_name = os.path.basename(attachment_path)
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition', f'attachment; filename={base_name}')
                        msg.attach(part)

                    server.sendmail(sender_email, email_to, msg.as_bytes())
                else:
                    # Send email without attachment
                    server.sendmail(sender_email, email_to, content)
                
                messagebox.showinfo("Success", f"Email successfully sent to {name}")
        except Exception as e:
            messagebox.showerror("Error", f"Error sending email: {str(e)}")
    else:
        messagebox.showerror("Error", f"Email not found for {name}. Add it to the CSV file.")


def fetch_email_by_name(name):
    with open('emails.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Name'] == name:
                return row['Email']
    return None

def add_to_csv():
    name = entry_name.get()
    email = entry_email.get()

    if not name or not email:
        messagebox.showerror("Error", "Please enter both name and email.")
        return

    with open('emails.csv', 'a', newline='') as csvfile:
        fieldnames = ['Name', 'Email']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write data to CSV file
        writer.writerow({'Name': name, 'Email': email})
    
    messagebox.showinfo("Success", f"Information for {name} added to the CSV file.")

def update_csv():
    old_name = entry_name.get()
    new_name = entry_updated_name.get()
    email = entry_email.get()

    if not old_name or not new_name or not email:
        messagebox.showerror("Error", "Please enter both old and new names, and email.")
        return

    updated_rows = []
    with open('emails.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Name'] == old_name:
                row['Name'] = new_name
                row['Email'] = email
            updated_rows.append(row)

    with open('emails.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Email']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write updated data to CSV file
        writer.writeheader()
        writer.writerows(updated_rows)
    
    messagebox.showinfo("Success", f"Information for {old_name} updated in the CSV file.")

def display_existing_emails():
    existing_emails = []
    with open('emails.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            existing_emails.append((row['Name'], row['Email']))

    display_window = tk.Toplevel(root)
    display_window.title("Existing Emails")

    tree = ttk.Treeview(display_window, columns=('Name', 'Email'), show='headings')
    tree.heading('Name', text='Name')
    tree.heading('Email', text='Email')

    for email in existing_emails:
        tree.insert('', tk.END, values=email)

    tree.pack(expand=True, fill='both')

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")])
    entry_attachment.delete(0, tk.END)
    entry_attachment.insert(0, file_path)

# GUI setup
root = tk.Tk()
root.title("Email Sender")
root.geometry("600x500")

# Name input
label_name = tk.Label(root, text="Recipient Name:")
label_name.pack(pady=10)

entry_name = tk.Entry(root)
entry_name.pack(pady=10)

# Updated Name input
label_updated_name = tk.Label(root, text="Updated Name:")
label_updated_name.pack(pady=10)

entry_updated_name = tk.Entry(root)
entry_updated_name.pack(pady=10)

# Email input
label_email = tk.Label(root, text="Recipient Email:")
label_email.pack(pady=10)

entry_email = tk.Entry(root)
entry_email.pack(pady=10)

# Email content input
label_content = tk.Label(root, text="Email Content:")
label_content.pack(pady=10)

text_content = tk.Text(root, height=5, width=30)
text_content.pack(pady=10)

# Attachment input
label_attachment = tk.Label(root, text="Attachment:")
label_attachment.pack(pady=10)

entry_attachment = tk.Entry(root)
entry_attachment.pack(pady=10)

button_browse = tk.Button(root, text="Browse", command=browse_file)
button_browse.pack(pady=10)

# Send button
button_send = tk.Button(root, text="Send Email", command=send_email)
button_send.pack(pady=10)

# Add to CSV button
button_add_to_csv = tk.Button(root, text="Add to CSV", command=add_to_csv)
button_add_to_csv.pack(pady=10)

# Update CSV button
button_update_csv = tk.Button(root, text="Update CSV", command=update_csv)
button_update_csv.pack(pady=10)

# Display Existing Emails button
button_display_emails = tk.Button(root, text="Display Existing Emails", command=display_existing_emails)
button_display_emails.pack(pady=10)

# Run the GUI
root.mainloop()
