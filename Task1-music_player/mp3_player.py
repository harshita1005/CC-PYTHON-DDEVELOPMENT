                            
from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer
import os

mixer.init()

def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    song_name.set(songs_list.get(ACTIVE))

    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()

def stop_song(status: StringVar):
    mixer.music.stop()

def load(listbox):
    os.chdir(filedialog.askdirectory(title='Browse songs'))

    tracks = os.listdir()

    for track in tracks:
        listbox.insert(END, track)

def pause_song(status: StringVar):
    mixer.music.pause()

def resume_song(status: StringVar):
    mixer.music.unpause()

root = Tk()
root.geometry("850x360")
root.title("Mp3 Music Player")

root.resizable(0, 0)

song_frame = LabelFrame(root, text='Current Song', width=400, height=400)
song_frame.place(x=0, y=0)


frameCnt = 30
frames = [PhotoImage(file='aa1.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)
label = Label(song_frame)
label.place(x=0, y=0)
root.after(0, update, 0)

button_frame = LabelFrame(root, text='Control Buttons',width=400, height=250)
button_frame.place(x=0, y=220)
button_frame['background']='#D3D3D3'

listbox_frame = LabelFrame(root, text='Playlist')
listbox_frame.place(x=400, y=0, height=410, width=600)
listbox_frame['background']='#D3D3D3'
current_song = StringVar(root, value='<Not selected>')

song_status = StringVar(root, value='<Not Available>')

playlist = Listbox(listbox_frame, font=(
    'Times new roman', 11))

scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)

playlist.config(yscrollcommand=scroll_bar.set)

scroll_bar.config(command=playlist.yview)

playlist.pack(fill=BOTH, padx=5, pady=5)

Label(song_frame, text='Currently \n Playing Song:', 
      font=('Times', 10, 'bold')).place(x=10, y=10)

song_lbl = Label(song_frame, textvariable=current_song,bg='white',
                  font=("Times", 10), width=40)
song_lbl.place(x=100, y=17.5)

pause_btn = Button(button_frame, text='Pause',   width=7,
                   command=lambda: pause_song(song_status))
pause_btn.place(x=195, y=10)

stop_btn = Button(button_frame, text='Stop',  width=7,
                  command=lambda: stop_song(song_status))
stop_btn.place(x=105, y=10)

play_btn = Button(button_frame, text='Play',  width=7,
                  command=lambda: play_song(current_song, playlist, song_status))
play_btn.place(x=15, y=10)

resume_btn = Button(button_frame, text='Resume',  width=7,
                    command=lambda: resume_song(song_status))
resume_btn.place(x=285, y=10)

load_btn = Button(button_frame, text='Browse Music',  width=35,
                  command=lambda: load(playlist))
load_btn.place(x=60, y=60)

root.update()
root.mainloop()
