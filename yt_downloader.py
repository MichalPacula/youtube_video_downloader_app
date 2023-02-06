from pytube import YouTube
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os


class my_GUI:
    def __init__(self):
        self.first_page_creator()


    def first_page_creator(self):
        #creating window app
        self.root = tk.Tk()
        self.root.title("Youtube video downloader")
        self.root.geometry("500x500")

        #creating frame to pack first 'page' with ability to destroy all of it
        self.first_page = tk.Frame(self.root)

        #showing message for user to know that he needs to pass link
        self.label = tk.Label(self.first_page, text="Hi! Pass your youtube link below.", font=("Arial", 13))
        self.label.pack(padx=10, pady=2)

        #text box for YouTube link
        self.text_box_link = tk.Text(self.first_page, height=1, font=("Arial", 13))
        self.text_box_link.pack(padx=10, pady=2)

        #button to take link from user
        self.button_link = tk.Button(self.first_page, text="Continue", font=("Arial", 13), command=self.take_link)
        self.button_link.pack(padx=10, pady=10)

        #packing first 'page' frame
        self.first_page.pack(padx=10, pady=10)

        self.root.mainloop()

    #this function destroys first page frame and creates second page
    def second_page_creator(self, yt_link):
        #destroying first page
        self.first_page.destroy()

        #creating second page frame
        self.second_page = tk.Frame(self.root)

        #creating button for going back to the first page
        self.back_button = tk.Button(self.second_page, text="Back", font=("Arial", 13), command=self.back_to_first_page)
        self.back_button.pack(padx=10, pady=2)

        #creating text to inform user what to do
        self.label_file_name = tk.Label(self.second_page, text="Enter name for your file.", font=("Arial", 13))
        self.label_file_name.pack(padx=10, pady=2)

        #creating text box for user to input file name
        self.text_box_file_name = tk.Text(self.second_page, height=1, font=("Arial", 13))
        self.text_box_file_name.pack(padx=10, pady=2)

        #creating text to inform user what to do
        self.label_file_name = tk.Label(self.second_page, text="Enter path for your file.", font=("Arial", 13))
        self.label_file_name.pack(padx=10, pady=2)

        #creating text box for user to input path 
        self.text_box_path = tk.Text(self.second_page, height=1, font=("Arial", 13))
        self.text_box_path.pack(padx=10, pady=2)

        #creating button for user to get path
        self.button_path = tk.Button(self.second_page, text="Choose your path", font=("Arial", 13), command=self.take_path)
        self.button_path.pack(padx=10, pady=10)

        #creating radiobuttons for user to get what type of file to download
        self.radio_button_var = tk.IntVar()
        self.video_audio_button = tk.Radiobutton(self.second_page, text="MP4 with audio", variable=self.radio_button_var, value=1)
        self.video_audio_button.pack(padx=10, pady=10)
        self.only_video_button = tk.Radiobutton(self.second_page, text="Only MP4", variable=self.radio_button_var, value=2)
        self.only_video_button.pack(padx=10, pady=10)
        self.only_audio_button = tk.Radiobutton(self.second_page, text="Only MP3", variable=self.radio_button_var, value=3)
        self.only_audio_button.pack(padx=10, pady=10)

        #creating button for user to download the file
        self.button_download = tk.Button(self.second_page, text="Download file", font=("Arial", 13), command=self.download_file)
        self.button_download.pack(padx=10, pady=10)

        #packing second page frame
        self.second_page.pack(padx=10, pady=10)
    
    #this function destroys current window and create new one on the first page
    def back_to_first_page(self):
        self.root.destroy()
        self.first_page_creator()
    
    #this function let user choose path
    def take_path(self):
        file_path = filedialog.askdirectory()
        self.text_box_path.delete('1.0', tk.END)
        self.text_box_path.insert('1.0', file_path)

    #this function takes what is inside the text box for link and check if it is a link and is it correct
    def take_link(self):
        link = self.text_box_link.get('1.0', tk.END)

        #if stripped string in text box is empty, program will show error
        if link.strip() == "":
            messagebox.showinfo(title="Error!", message="You didn't enter a link!")
        else:
            #checking if string in text box is correct YouTube link and if it isn't correct it will show error
            try:
                global yt_link
                yt_link = YouTube(link, use_oauth=False, allow_oauth_cache=True)
                #calling second_page_creator to destroy first page and proceed with the rest of the program
                self.second_page_creator(yt_link)
            except:
                messagebox.showinfo(title="Error!", message="Your YouTube link is wrong! Please try putting diffrent link.")
    
    #this function download file
    def download_file(self):
        #this function takes what is inside the text box for name of file and checks if anything is entered
        if self.text_box_file_name.get('1.0', tk.END).strip() == "":
            messagebox.showinfo(title="Error!", message="You didn't enter a name!")
        else:
            name = self.text_box_file_name.get('1.0', tk.END).strip()

        if self.text_box_path.get('1.0', tk.END).strip() == "":
            messagebox.showinfo(title="Error!", message="You didn't enter path for your file!")
        else:
            path = self.text_box_path.get('1.0', tk.END).strip()

            if self.radio_button_var.get() == 1:
                try:
                    yt_link_streams = yt_link.streams.filter(file_extension="mp4").get_highest_resolution()
                    out_file = yt_link_streams.download(filename=name, output_path=path)
                    proper_file = out_file + ".mp4"
                    os.rename(out_file, proper_file)
                except FileExistsError:
                    messagebox.showinfo(title="Error!", message="You're trying to make file with same name and format! Please change your name or format.")
                except:
                    messagebox.showinfo(title="Error!", message="You didn't enter a correct path for your file!")
            elif self.radio_button_var.get() == 2:
                try:
                    yt_link_streams = yt_link.streams.filter(only_video=True)
                    out_file = yt_link_streams[0].download(filename=name, output_path=path)
                    proper_file = out_file + ".mp4"
                    os.rename(out_file, proper_file)
                except FileExistsError:
                    messagebox.showinfo(title="Error!", message="You're trying to make file with same name and format! Please change your name or format.")
                except:
                    messagebox.showinfo(title="Error!", message="You didn't enter a correct path for your file!")
            else:
                try:
                    yt_link_streams = yt_link.streams.filter(only_audio=True)
                    out_file = yt_link_streams[0].download(filename=name, output_path=path)
                    base, ext = os.path.splitext(out_file)
                    proper_file = base + ".mp3"
                    os.rename(out_file, proper_file)
                except FileExistsError:
                    messagebox.showinfo(title="Error!", message="You're trying to make file with same name and format! Please change your name or format.")
                except:
                    messagebox.showinfo(title="Error!", message="You didn't enter a correct path for your file!")




my_GUI()
