import tkinter
from tkinter import ttk
import rsa
import symmetric_cipher

window = tkinter.Tk() # Creating a window
window.title("RSA Encryption Demonstration") # Rename window
window.geometry("700x500") # Set size of window to 700 by 500
window.resizable(0, 0) # Don't allow window to resize
tab_parent = ttk.Notebook() # Create ttk notebook for tabs

ttk.Style().theme_use("alt") # Set theme to 'alt'
standard_colour = "#D9D9D9" # Define standard_colour to match background colour

tab0 = ttk.Frame(tab_parent) # Create tab 0
tab1 = ttk.Frame(tab_parent) # Create tab 1
tab2 = ttk.Frame(tab_parent) # Create tab 2
tab3 = ttk.Frame(tab_parent) # Create tab 3

tab_parent.add(tab0, text = "Introduction") # Add tab 0 to tab parent and name
tab_parent.add(tab1, text = "RSA Key Generation") # Add tab 1 to tab parent and name
tab_parent.add(tab2, text = "RSA Integer Encryption") # Add tab 2 to tab parent and name
tab_parent.add(tab3, text = "Symmetric String Encryption") # Add tab 3 to tab parent and name

tab_parent.pack(expand=1, fill='both') # Pack tab parent into window

# Tab 0 Introduction

introduction_text = """
Welcome!

This program demonstrates the use of the asymmetric encryption method known as RSA to
send and receive encrypted messages.

How to Use:

Let's say Alice wants to send Bob a message using this program. The process begins with
Bob who would use the 'RSA Key Generation' tab to create a public and private key. Min
and max values can be set to generate two primes, p and q, which would in turn be used to
generate these keys. Both keys contain two integers: n (the product of p and q) and
either e or d (the encryption/decryption constant). The public key can only be used
to encrypt messages whereas the private key can only be used to decrypt messages. Bob
would send Alice a copy of the public key for her to begin encrypting. To copy the
results from this tab to the 'RSA Integer Encryption' tab, press the button located at
the bottom.

Using this next tab, integers less than n, such as an arbitrary key value, can be
encrypted by Alice. This key value could then only be successfully unencrypted by
the owner of the private key, Bob. Alice would then move on to the next tab in order to
use the key to encrypt a string message.

The 'Symmetric String Encryption' tab uses a simple cipher which uses an integer key to
encrypt a string. The arbitrary key chosen by Alice can be used here to encrypt the
message for secure communication. To complete the process on Alice's end, the encrypted
message, along with the encrypted integer key can be sent to Bob.

For Bob to access the message, he would first apply his private key to decrypt the
integer key, and then use this unencrypted key in the 'Symmetric String Encryption' tab
to decrypt the string message and find out what Alice had sent.

Note: the strength of the RSA encryption relies on the difficulty of factoring n, which
is why two prime numbers are used to generate the keys. To see how these keys are
generated, feel free to look at the code in rsa.py (namely the generate_key method)."""

scrollbar = tkinter.Scrollbar(tab0) # Create scrollbar widget
scrollbar.pack(side = tkinter.RIGHT, fill = tkinter.Y) # Pack scrollbar widget
tab0_text = tkinter.Text(tab0, wrap = tkinter.WORD, yscrollcommand = scrollbar.set, width = 91, height = 29, bg = standard_colour, highlightbackground = standard_colour) # Create text widget
tab0_text.pack() # Pack text widget
tab0_text.insert(tkinter.END, introduction_text) # Insert introduction text into text widget
tab0_text.config(state = tkinter.DISABLED) # Configure text widet to be read-only
scrollbar.config(command = tab0_text.yview) # Bind scrollbar to text widget

# Tab 1 RSA Key Generation

tab1_frame1 = tkinter.Frame(tab1, bg = standard_colour) # Create frame 1
tab1_frame2 = tkinter.Frame(tab1, bg = standard_colour) # Create frame 2

tkinter.Label(tab1, text = "Prime Number Generation", bg = standard_colour).pack(pady = (10,0)) # Create prime number generation label widget

tkinter.Label(tab1_frame1, text = "Min", bg = standard_colour).grid(row = 0, column = 0) # Create min label widget
tab1_entry1 = tkinter.Entry(tab1_frame1, width = 10, highlightbackground = standard_colour) # Create min entry widget
tab1_entry1.grid(row = 0, column = 1) # Place min entry widget in grid
tkinter.Label(tab1_frame1, text = "Max", bg = standard_colour).grid(row = 0, column = 2) # Create max label widget
tab1_entry2 = tkinter.Entry(tab1_frame1, width = 10, highlightbackground = standard_colour) # Create max entry widget
tab1_entry2.grid(row = 0, column = 3) # Place max entry widget in grid

def generate_keys():
    # Generates primes p and q, and uses values to generate public and private RSA keys
    tab1_text1.delete('1.0',tkinter.END)
    tab1_text2.delete('1.0',tkinter.END)
    tab1_text3.delete('1.0',tkinter.END)
    tab1_text4.delete('1.0',tkinter.END)
    tab1_text5.delete('1.0',tkinter.END)
    tab1_text6.delete('1.0',tkinter.END)
    p = rsa.random_prime(int(tab1_entry1.get()),int(tab1_entry2.get()))
    q = rsa.random_prime(int(tab1_entry1.get()),int(tab1_entry2.get()))
    tab1_text1.insert(tkinter.END,p)
    tab1_text2.insert(tkinter.END,q)
    public_key, private_key = rsa.generate_key(p,q)
    n, e, d = public_key[0], public_key[1], private_key[1]
    tab1_text3.insert(tkinter.END,n)
    tab1_text4.insert(tkinter.END,e)
    tab1_text5.insert(tkinter.END,n)
    tab1_text6.insert(tkinter.END,d)

tkinter.Button(tab1_frame1, text = "Generate", command = generate_keys, highlightbackground = standard_colour).grid(row = 0, column = 4) # Create generate button to call generate_keys() method

tab1_frame1.pack(pady = (5,5)) # Pack frame 1

tkinter.Label(tab1_frame2, text = "Primes:", bg = standard_colour).grid(row = 0, column = 0) # Create primes label widget
tkinter.Label(tab1_frame2, text = "P", bg = standard_colour).grid(row = 0, column = 1) # Create p label widget
tab1_text1 = tkinter.Text(tab1_frame2, height = 1, width = 10, highlightbackground = standard_colour) # Create text widget
tab1_text1.grid(row = 0, column = 2) # Place text widget in grid
tkinter.Label(tab1_frame2, text = "Q", bg = standard_colour).grid(row = 0, column = 3) # Create q label widget
tab1_text2 = tkinter.Text(tab1_frame2, height = 1, width = 10, highlightbackground = standard_colour) # Create text widget
tab1_text2.grid(row = 0, column = 4) # Place text widget in grid

tkinter.Label(tab1_frame2, text = "Public Key:", bg = standard_colour).grid(row = 1, column = 0) # Create public key label widget
tkinter.Label(tab1_frame2, text = "N", bg = standard_colour).grid(row = 1, column = 1) # Create n label widget
tab1_text3 = tkinter.Text(tab1_frame2, height = 1, width = 10, highlightbackground = standard_colour) # Create text widget
tab1_text3.grid(row = 1, column = 2) # Place text widget in grid
tkinter.Label(tab1_frame2, text = "E", bg = standard_colour).grid(row = 1, column = 3) # Create e label widget
tab1_text4 = tkinter.Text(tab1_frame2, height = 1, width = 10, highlightbackground = standard_colour) # Create text widget
tab1_text4.grid(row = 1, column = 4) # Place text widget in grid

tkinter.Label(tab1_frame2, text = "Private Key:", bg = standard_colour).grid(row = 2, column = 0) # Create private key label widget
tkinter.Label(tab1_frame2, text = "N", bg = standard_colour).grid(row = 2, column = 1) # Create n label widget
tab1_text5 = tkinter.Text(tab1_frame2, height = 1, width = 10, highlightbackground = standard_colour) # Create text widget
tab1_text5.grid(row = 2, column = 2) # Place text widget in grid
tkinter.Label(tab1_frame2, text = "D", bg = standard_colour).grid(row = 2, column = 3) # Create d label widget
tab1_text6 = tkinter.Text(tab1_frame2, height = 1, width = 10, highlightbackground = standard_colour) # Create text widget
tab1_text6.grid(row = 2, column = 4) # Place text widget in grid

tab1_frame2.pack(pady = (5,5)) # Pack frame 2

def copy_keys():
    # Copys n, e and d values from tab 1 to tab 2
    n = tab1_text3.get("1.0",'end-1c')
    e = tab1_text4.get("1.0",'end-1c')
    d = tab1_text6.get("1.0",'end-1c')
    tab2_entry1.delete(0,tkinter.END)
    tab2_entry1.insert(0,str(n))
    tab2_entry2.delete(0,tkinter.END)
    tab2_entry2.insert(0,str(e))
    tab2_entry4.delete(0,tkinter.END)
    tab2_entry4.insert(0,str(n))
    tab2_entry5.delete(0,tkinter.END)
    tab2_entry5.insert(0,str(d))


tkinter.Button(tab1, text = "Copy Results to RSA Encryption Tab", command = copy_keys, highlightbackground = standard_colour).pack(pady = (20)) # Create  button to call copy_keys() method

# Tab 2 RSA Integer Encryption

tab2_frame1 = tkinter.Frame(tab2, bg = standard_colour) # Create frame 1
tab2_frame2 = tkinter.Frame(tab2, bg = standard_colour) # Create frame 2
tab2_frame3 = tkinter.Frame(tab2, bg = standard_colour) # Create frame 3
tab2_frame4 = tkinter.Frame(tab2, bg = standard_colour) # Create frame 4

tkinter.Label(tab2, text = "Encryption", bg = standard_colour).pack(pady = (10,0)) # Create encryption label widget

tkinter.Label(tab2_frame1, text = "Public Key:", bg = standard_colour).grid(row = 0, column = 0) # Create public key label widget
tkinter.Label(tab2_frame1, text = "N", bg = standard_colour).grid(row = 0, column = 1) # Create n label widget
tab2_entry1 = tkinter.Entry(tab2_frame1, width = 10, highlightbackground = standard_colour) # Create n entry widget
tab2_entry1.grid(row = 0, column = 2) # Place n entry widget in grid
tkinter.Label(tab2_frame1, text = "E", bg = standard_colour).grid(row = 0, column = 3) # Create e label widget
tab2_entry2 = tkinter.Entry(tab2_frame1, width = 10, highlightbackground = standard_colour) # Create e entry widget
tab2_entry2.grid(row = 0, column = 4) # Place e entry widget in grid

tab2_frame1.pack(pady = (5,5)) # Pack frame 1

tkinter.Label(tab2_frame2, text = "Int Message", bg = standard_colour).grid(row = 0, column = 0) # Create int message label widget
tab2_entry3 = tkinter.Entry(tab2_frame2, width = 10, highlightbackground = standard_colour) # Create int message entry widget
tab2_entry3.grid(row = 0, column = 1) # Place int message entry widget in grid

def tab2_encrypt():
    # Encrypts message from tab 2 int message entry using tab 2 key entry, and places in tab 2 text widget
    tab2_text1.delete('1.0',tkinter.END)
    n = int(tab2_entry1.get())
    e = int(tab2_entry2.get())
    m = int(tab2_entry3.get())
    public_key = [n,e]
    c = rsa.encrypt(m,public_key)
    tab2_text1.insert(tkinter.END,c)

tkinter.Button(tab2_frame2, text = "Encrypt", command = tab2_encrypt, bg = standard_colour, highlightbackground = standard_colour).grid(row = 0, column = 2) # Create encrypt button to call tab2_encrypt() method
tab2_text1 = tkinter.Text(tab2_frame2, height = 1, width = 10, highlightbackground = standard_colour) # Create text widget
tab2_text1.grid(row = 0, column = 3) # Place text widget in grid

tab2_frame2.pack() # Pack frame 2

tkinter.Label(tab2, text = "Decryption", bg = standard_colour).pack(pady = (20,0)) # Create decryption label widget

tkinter.Label(tab2_frame3, text = "Private Key:", bg = standard_colour).grid(row = 0, column = 0) # Create private key label widget
tkinter.Label(tab2_frame3, text = "N", bg = standard_colour).grid(row = 0, column = 1) # Create n label widget
tab2_entry4 = tkinter.Entry(tab2_frame3, width = 10, highlightbackground = standard_colour) # Create n entry widget
tab2_entry4.grid(row = 0, column = 2) # Place n entry widget in grid
tkinter.Label(tab2_frame3, text = "D", bg = standard_colour).grid(row = 0, column = 3) # Create d label widget
tab2_entry5 = tkinter.Entry(tab2_frame3, width = 10, highlightbackground = standard_colour) # Create d entry widget
tab2_entry5.grid(row = 0, column = 4) # Place d entry widget in grid

tab2_frame3.pack(pady = (5,5)) # Pack frame 3

tkinter.Label(tab2_frame4, text = "Int Message", bg = standard_colour).grid(row = 0, column = 0) # Create int message label widget
tab2_entry6 = tkinter.Entry(tab2_frame4, width = 10, highlightbackground = standard_colour) # Create int message entry widget
tab2_entry6.grid(row = 0, column = 1) # Place int message entry widget in grid

def tab2_decrypt():
    # Decryts message from tab 2 int message entry using tab 2 key entry, and places in tab 2 text widget
    tab2_text2.delete('1.0',tkinter.END)
    n = int(tab2_entry4.get())
    d = int(tab2_entry5.get())
    c = int(tab2_entry6.get())
    private_key = [n,d]
    m = rsa.decrypt(c,private_key)
    tab2_text2.insert(tkinter.END,m)

tkinter.Button(tab2_frame4, text = "Decrypt", command = tab2_decrypt, bg = standard_colour, highlightbackground = standard_colour).grid(row = 0, column = 2) # Create decrypt button to call tab2_decrypt() method
tab2_text2 = tkinter.Text(tab2_frame4, height = 1, width = 10, highlightbackground = standard_colour) # Create text widget
tab2_text2.grid(row = 0, column = 3) # Place text widget in grid

tab2_frame4.pack() # Pack frame 4

# Tab 3 Symmetric String Encryption

tab3_frame = tkinter.Frame(tab3, bg = standard_colour) # Create frame

tkinter.Label(tab3_frame, text = "Key:", bg = standard_colour).grid(row = 0, column = 0, pady = (10,10)) # Create key label widget
tab3_e1 = tkinter.Entry(tab3_frame, width = 46, highlightbackground = standard_colour) # Create key entry widget
tab3_e1.grid(row = 0, column = 1, pady = (10,10)) # Place key entry widget in grid
tkinter.Label(tab3_frame, text = "Message:", bg = standard_colour).grid(row = 1, column = 0) # Create message label widget and place in grid
tab3_e2 = tkinter.Entry(tab3_frame, width = 46, highlightbackground = standard_colour) # Create message entry widget
tab3_e2.grid(row = 1, column = 1, pady = (10,10)) # Place message entry widget in grid

def tab3_encrypt():
    # Encrypts message from tab 3 message entry using tab 3 key entry, and places in tab 3 text widget
    tab3_text.delete('1.0',tkinter.END)
    cipher = symmetric_cipher.encrypt_string(tab3_e2.get(),int(tab3_e1.get()))
    tab3_text.insert(tkinter.END,cipher)

def tab3_decrypt():
    # Decryts message from tab 3 message entry using tab 3 key entry, and places in tab 3 text widget
    tab3_text.delete('1.0',tkinter.END)
    message = symmetric_cipher.decrypt_string(tab3_e2.get(),int(tab3_e1.get()))
    tab3_text.insert(tkinter.END,message)

button_frame = tkinter.Frame(tab3_frame, bg = standard_colour) # Create button frame

tab3_button1 = tkinter.Button(button_frame, text = "Encrypt", command = tab3_encrypt, bg = standard_colour, highlightbackground = standard_colour) # Create encrypt button to call tab3_encrypt() method
tab3_button1.grid(row = 0, column = 0, pady = (0,10)) # Place button widget in grid
tab3_button2 = tkinter.Button(button_frame, text = "Decrypt", command = tab3_decrypt, bg = standard_colour, highlightbackground = standard_colour) # Create decrypt button wiet to call tab3_decrypt() method
tab3_button2.grid(row = 1, column = 0) # Place button widget in grid

button_frame.grid(row = 2, column = 0, pady = (10,10)) # Place button frame in grid

tab3_text = tkinter.Text(tab3_frame, height = 3, width = 60, highlightbackground = standard_colour) # Create text widget
tab3_text.grid(row = 2, column = 1, pady = (10,10)) # Place text widget in grid

tab3_frame.pack(pady = (10,0)) # Pack frame

window.mainloop() # Begin main loop
