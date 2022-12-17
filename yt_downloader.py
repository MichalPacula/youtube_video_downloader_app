from pytube import YouTube
import tkinter as tk
from tkinter import messagebox


class my_GUI:

    def __init__(self):
        #creating window app
        self.root = tk.Tk()

        #showing message for user to know that he needs to pass link
        self.label = tk.Label(self.root, text="Hi! Pass your youtube link below.", font=("Arial", 13))
        self.label.pack(padx=10, pady=2)

        #text box for YouTube link
        self.text_box = tk.Text(self.root, height=1, font=("Arial", 13))
        self.text_box.pack(padx=10, pady=2)

        #button to take link from user
        self.button_link = tk.Button(self.root, text="Continue", font=("Arial", 13), command=self.take_link)
        self.button_link.pack(padx=10, pady=10)

        self.root.mainloop()

    #this function takes what is inside of the text box and check if it is a link and is it correct
    def take_link(self):
        link = self.text_box.get('1.0', tk.END)

        #if stripped string in text box is empty, program will show error
        if link.strip() == "":
            messagebox.showinfo(title="Error!", message="You didn't enter a link!")
        else:
            #checking if string in text box is correct YouTube link and if it isn't correct it will show error
            try:
                yt_link = YouTube(link, use_oauth=False, allow_oauth_cache=True)
            except:
                messagebox.showinfo(title="Error!", message="Your YouTube link is wrong! Please try putting diffrent link.")


my_GUI()
