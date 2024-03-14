import tkinter as tk
from urllib.parse import quote, unquote
import pyperclip  # Import the pyperclip library

def encode_url():
    url = entry.get()
    encoded_url = quote(url, safe='')
    output.delete(1.0, tk.END)
    output.insert(tk.END, encoded_url)

def decode_url():
    url = entry.get()
    decoded_url = unquote(url)
    output.delete(1.0, tk.END)
    output.insert(tk.END, decoded_url)

def copy_to_clipboard():
    text_to_copy = output.get(1.0, tk.END).strip()  # Get text from output and strip trailing newline
    pyperclip.copy(text_to_copy)  # Copy text to clipboard

app = tk.Tk()
app.title('URL Encoder/Decoder')

# Input field
entry_label = tk.Label(app, text="Enter URL:")
entry_label.pack()
entry = tk.Entry(app, width=50)
entry.pack()

# Encode button
encode_button = tk.Button(app, text="Encode", command=encode_url)
encode_button.pack()

# Decode button
decode_button = tk.Button(app, text="Decode", command=decode_url)
decode_button.pack()

# Output field
output_label = tk.Label(app, text="Result:")
output_label.pack()
output = tk.Text(app, height=4, width=50)
output.pack()

# Copy to Clipboard button
copy_button = tk.Button(app, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

app.mainloop()
