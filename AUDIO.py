# Hide your secret text in wave audio file.
import os
import wave
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import shutil
import random
import os
import sys
from PIL import Image, ImageTk
window = tk.Tk()
window.title("Audio Steganography System")
window.configure(background="#b0f69f")
window.geometry("1600x850")
img=Image.open("ste.jpg")
img=img.resize((1600,850))
bg=ImageTk.PhotoImage(img)
lmain = Label(window,image=bg)
lmain.place(x=0, y=0)
def exit_win():
    window.destroy()
def encrypt():
##    window1 = tk.Tk()
##    window1.title("Audio Steganography System")
##    window1.geometry("1000x500")
##    window1.configure(background ="darkcyan")
    fileName1 = askopenfilename(initialdir='', title='SELECT AUDIO FOR ENCRYPTION',
                           filetypes=[('audio files', '.wav')])
    lbl=tk.Label(window,text="Enter the text you want hide..",font=("elephant",20,"italic"),bg="black",fg="white")
    lbl.place(x=20,y=420)
    entb_q1=tk.Entry(window,text="",font=("times",14,"italic"),bg="white")
    entb_q1.place(x=540,y=420)
    lbl=tk.Label(window,text="Enter the name of output\n  file in the format (.wav)",font=("elephant",20,"italic"),bg="black",fg="white")
    lbl.place(x=20,y=520)
    enty_q1=tk.Entry(window,text="",font=("times",14,"italic"),bg="white")
    enty_q1.place(x=540,y=520)
    lbl=tk.Label(window,text="Enter the Secret Key",font=("elephant",20,"italic"),bg="black",fg="white")
    lbl.place(x=20,y=620)
    enty_sk=tk.Entry(window,text="",font=("times",14,"italic"),bg="white",show="*")
    enty_sk.place(x=540,y=620)
    def check1():
        global key            
        af=fileName1
        string=entb_q1.get()
        output=enty_q1.get()
        key=enty_sk.get()
        f = open('Key_a.txt' ,'w')
        f.write(key)
        f.close()

##        f = open('Message.txt' ,'w')
##        f.write(input_string)
##        f.close()
##
##        f = open('Video.txt' ,'w')
##        f.write(video_file)
##        f.close()
        
        def cls():
          os.system("clear")
        def help():
          print("Hide Your Secret Message in Audio Wave File")

        def em_audio(af, string, output):
            print ("Done...")
            print ("Please wait...")
            waveaudio = wave.open(af, mode='rb')
            frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
            string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
            bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
            for i, bit in enumerate(bits):
              frame_bytes[i] = (frame_bytes[i] & 254) | bit
            frame_modified = bytes(frame_bytes)
            with wave.open(output, 'wb') as fd:
              fd.setparams(waveaudio.getparams())
              fd.writeframes(frame_modified)
              print('encryption done............')
              lbl_enc=tk.Label(window,text="successfully hidden in "+str(output),font=("elephant",20,"italic"),bg="black",fg="white")
              lbl_enc.place(x=300,y=730)
              
            waveaudio.close()
            print ("Done...")
        cls()
        try:
          em_audio(af, string, output)
        except:
          print ("Something went wrong!! try again")
          quit('')
    lbl=tk.Button(window,text="Submit",font=("times",18,"italic"),command=check1,bg="black",fg="white")
    lbl.place(x=300,y=650)
    lbl=tk.Button(window,text="Close",font=("times",18,"italic"),command=exit_win,bg="black",fg="white")
    lbl.place(x=600,y=650)
    window.mainloop()
def decrypt():
    fileName2 = askopenfilename(initialdir='', title='SELECT AUDIO FOR DECRYPTION ',
                           filetypes=[('audio files', '.wav')])
    def check2():
        af=(fileName2)
        def cls():
           os.system("clear")
        
        def ex_msg(af):

            print ("Please wait...")
            waveaudio = wave.open(af, mode='rb')
            frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
            extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
            string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
            msg = string.split("###")[0]
            print("Your Secret Message is: "+msg)
            waveaudio.close()
            lbl=tk.Label(window,text="your secret message is :  \n "+msg,font=("elephant",20,"italic bold"),bg="black",fg="white")
            lbl.place(x=950,y=650)
        cls()
        try:
          ex_msg(af)
        except:
          print ("Something went wrong!! try again")
          quit('')
    def confirm_pass():
            new_key=new_pass.get()
            f = open('Key_a.txt' ,'r')
            old_key = f.read()
            f.close()
            print("OLD KEY IS === "+str(old_key)+"  ,   \n   NEW KEY IS === "+str(new_key)) 
            if old_key == new_key:
                check2()
            else:
                lbl=tk.Label(window,text="Secret Key Not Mathed",font=("elephant",20,"italic"),bg="black",fg="white")
                lbl.place(x=950,y=650)
    global new_pass
    lbl=tk.Label(window,text="Enter the \n Secret Key",font=("elephant",20,"italic"),bg="black",fg="white")
    lbl.place(x=700,y=400)
    new_pass=tk.Entry(window,text="",font=("times",14,"italic"),bg="white")
    new_pass.place(x=1100,y=400)
    lbl=tk.Button(window,text="submit key",font=("times",20,"italic"),command=confirm_pass,bg="black",fg="white")
    lbl.place(x=1100,y=500)

img2 =Image.open('enc.jpg')
img2=img2.resize((180,180))
bt0 = ImageTk.PhotoImage(img2)
buttono = tk.Button(text="ENCRYPT", command = encrypt,fg="black",bg="black",font=("times",15,"bold"),image = bt0,
    height="180",
    width="180",
    relief = FLAT,
    border = 0,
)
buttono.place(x=450,y=150)

img3 =Image.open('dec.jpg')
img3=img3.resize((180,180))
bt = ImageTk.PhotoImage(img3)


buttonr = tk.Button(text="DECRYPT", command = decrypt,fg="black",bg="black",font=("times",15,"bold"),image = bt,
    height="180",
    width="180",
    relief = FLAT,
    border = 0,
)
buttonr.place(x=950,y=150)
window.mainloop()
