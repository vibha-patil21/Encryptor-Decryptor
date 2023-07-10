import tkinter as tk
from tkinter import filedialog


#start of main porgram
class MainWindow:

        
    # Defining and setting properties of Window 
    def __init__(self, root):
        self.root = root
        self._file_url = tk.StringVar()
        self._secret_key = tk.IntVar()
        self._status = tk.StringVar()
        self._status.set("---")

        self.should_cancel = False
        #heading
        root.title("Encryptor Decryptor")
        root.configure(bg="#eeeeee")

        self.menu_bar = tk.Menu(
            root,
            bg="#eeeeee",
            relief=tk.FLAT
        )
        
        root.configure(
            menu=self.menu_bar
        )

        #entry box 
        self.file_entry_label = tk.Label(
            root,
            text="Enter File Path Or Select File",
            bg="#eeeeee",
            anchor=tk.W
        )

        #size of the label grid
        self.file_entry_label.grid(
            padx=12,
            pady=(8, 0),
            ipadx=0,
            ipady=1,
            row=0,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.file_entry = tk.Entry(
            root,
            textvariable=self._file_url,
            bg="#fff",
            exportselection=0,
            relief=tk.FLAT
        )
        self.file_entry.grid(
            padx=15,
            pady=6,
            ipadx=8,
            ipady=8,
            row=1,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.select_btn = tk.Button(
            root,
            text="SELECT FILE",
            command=self.selectfile_callback,
            width=42,
            bg="#54e54d",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT
        )
        self.select_btn.grid(
            padx=15,
            pady=8,
            ipadx=24,
            ipady=6,
            row=2,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.key_entry_label = tk.Label(
            root,
            text="Enter Secret Key",
            bg="#eeeeee",
            anchor=tk.W
        )
        self.key_entry_label.grid(
            padx=12,
            pady=(8, 0),
            ipadx=0,
            ipady=1,
            row=3,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.key_entry = tk.Entry(
            root,
            textvariable=self._secret_key,
            bg="#fff",
            exportselection=0,
            relief=tk.FLAT
        )
        self.key_entry.grid(
            padx=15,
            pady=6,
            ipadx=8,
            ipady=8,
            row=4,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        #encrpyt button
        self.encrypt_btn = tk.Button(
            root,
            text="ENCRYPT",
            command=self.encrypt_callback,
            bg="#3366ff",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT
        )
        self.encrypt_btn.grid(
            padx=(15, 6),
            pady=8,
            ipadx=24,
            ipady=6,
            row=7,
            column=0,
            columnspan=2,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        #decrypt button
        self.decrypt_btn = tk.Button(
            root,
            text="DECRYPT",
            command=self.decrypt_callback,
            bg="#ff33cc",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT
        )
        self.decrypt_btn.grid(
            padx=(6, 15),
            pady=8,
            ipadx=24,
            ipady=6,
            row=7,
            column=2,
            columnspan=2,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        #reset button
        self.reset_btn = tk.Button(
            root,
            text="RESET",
            command=self.reset_callback,
            bg="#aaaaaa",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT
        )
        self.reset_btn.grid(
            padx=15,
            pady=(4, 12),
            ipadx=24,
            ipady=6,
            row=8,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.status_label = tk.Label(
            root,
            textvariable=self._status,
            bg="#eeeeee",
            anchor=tk.W,
            justify=tk.LEFT,
            relief=tk.FLAT,
            wraplength=350
        )
        self.status_label.grid(
            padx=12,
            pady=(0, 12),
            ipadx=0,
            ipady=1,
            row=9,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        tk.Grid.columnconfigure(root, 0, weight=1)
        tk.Grid.columnconfigure(root, 1, weight=1)
        tk.Grid.columnconfigure(root, 2, weight=1)
        tk.Grid.columnconfigure(root, 3, weight=1)

    def selectfile_callback(self):
        try:
            name = filedialog.askopenfile()
            self._file_url.set(name.name)
        except Exception as e:
            self._status.set(e)
            self.status_label.update()

    #  disable the buttons 
    def freeze_controls(self):
        self.file_entry.configure(state="disabled")
        self.key_entry.configure(state="disabled")
        self.select_btn.configure(state="disabled")
        self.encrypt_btn.configure(state="disabled")
        self.decrypt_btn.configure(state="disabled")
        self.reset_btn.configure(text="CANCEL", command=self.cancel_callback,
            fg="#ed3833", bg="#fafafa")
        self.status_label.update()

    #  Enable the buttons 
    def unfreeze_controls(self):
        self.file_entry.configure(state="normal")
        self.key_entry.configure(state="normal")
        self.select_btn.configure(state="normal")
        self.encrypt_btn.configure(state="normal")
        self.decrypt_btn.configure(state="normal")
        self.reset_btn.configure(text="RESET", command=self.reset_callback,
            fg="#ffffff", bg="#aaaaaa")
        self.status_label.update()

    # Logic for Encryption
    def encrypt_callback(self):
        self.freeze_controls()

        try:
            key= self._secret_key.get()
            self.user_file = self._file_url.get()
            file = open(self.user_file, "rb")
            data=file.read()
            file.close()
            nfile = open(self.user_file, "wb")
            value = bytearray(data)
            for i in range(len(value)):
                value[i]=value[i]^key
            nfile.write(value)
            nfile.close()
            self._status.set("File Encrypted!")
        except Exception as e:
            self._status.set(e)

        self.unfreeze_controls()

    # Logic for decryption
    def decrypt_callback(self):
        self.freeze_controls()

        try:
            key= self._secret_key.get()
            self.user_file = self._file_url.get()
            file = open(self.user_file, "rb")
            data=file.read()
            file.close()
            
            nfile = open(self.user_file, "wb")
            value = bytearray(data)
            
            for i in range(len(value)):
                value[i]=value[i]^key
            nfile.write(value)
            nfile.close()
            self._status.set("File Decrypted!")
            self.should_cancel = False
        except Exception as e:
            self._status.set(e)
        
        self.unfreeze_controls()

    def reset_callback(self):
        self._file_url.set("")
        self._secret_key.set("")
        self._status.set("---")
    
    def cancel_callback(self):
        self.should_cancel = True


if __name__ == "__main__":
    ROOT = tk.Tk()
    MAIN_WINDOW = MainWindow(ROOT)
    ROOT.mainloop()
