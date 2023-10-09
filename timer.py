from tkinter import *
import time
import pygame
import threading

# Initialize pygame
pygame.mixer.init()

root = Tk()
root.geometry('400x300')
root.resizable(0, 0)
root.config(bg='#35455D')
root.title('Countdown Clock And Timer')
Label(root, text='Countdown Clock and Timer', font='Georgia', bg='#BFD1DF').pack()
Label(root, font='Georgia', text='Time:', bg='#BFD1DF').place(x=40, y=70)

def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    curr_time.config(text=clock_time)
    curr_time.after(1000, clock)

curr_time = Label(root, font='Georgia', text='', fg='black', bg='#BFD1DF')
curr_time.place(x=190, y=70)
clock()
sec = StringVar()
Entry(root, textvariable=sec, width=2, font='Georgia').place(x=250, y=155)
sec.set('00')

mins = StringVar()
Entry(root, textvariable=mins, width=2, font='Georgia').place(x=225, y=155)
mins.set('00')

hrs = StringVar()
Entry(root, textvariable=hrs, width=2, font='Georgia').place(x=200, y=155)
hrs.set('00')

def play_sound():
    try:
        pygame.mixer.music.load('Beep.mp3')  
        pygame.mixer.music.play() 
    except pygame.error as e:
        print("Error playing sound:", str(e))


def countdown():
    times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
    while times > -1:
        minute, second = (times // 60, times % 60)
        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)
      
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)
   
        root.update()
        time.sleep(1)

        if times == 0:
            threading.Thread(target=play_sound).start() 
            sec.set('00')
            mins.set('00')
            hrs.set('00') 
        times -= 1

Label(root, font='Georgia', text='Timer:', bg='#BFD1DF').place(x=40, y=150)
Button(root, text='START', bd='5', command=lambda: [countdown()], bg='antique white', font='#BFD1DF').place(x=150, y=210)
 
root.mainloop()



