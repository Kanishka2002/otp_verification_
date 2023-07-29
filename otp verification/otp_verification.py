
import math
import random
import smtplib
from tkinter import *

n = 6     

def generate_OTP():  
    digits = "0123456789"
    OTP = ""        
    for i in range(n):          
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def send_OTP():        
    global x  
    x = generate_OTP()
    server = smtplib.SMTP('smtp.gmail.com', 587)      
    server.starttls()           
    password = 'jelixjrkzyefxviu'
    server.login('kaniskamiss@gmail.com', password)
    otp = x
    subject = 'One Time Passcode'
    msg = 'Subject: {}\n\nHello, Your OTP for verification Process is {}'.format(subject, otp) 
    sender = 'kaniskamiss@gmail.com'
    server.sendmail(sender, Gm_id.get(), msg)
    server.quit()

def verify_OTP():           
    entered_otp = OTP_id.get()
    if entered_otp == x:
        print("OTP Verified")
        show_verification_interface()
    else:
        print("OTP Verification Failed")

def show_verification_interface():
    OVW.destroy()  

    verification_window = Tk()
    verification_window.title("OTP Verification Successful")
    verification_window.geometry("400x200")

    label = Label(verification_window, text="OTP Verification Successful!", font=("Arial", 16, "bold"))
    label.pack(pady=20)


    verification_window.mainloop()

OVW = Tk()              
OVW.title("OTP verification Window")
OVW.geometry("600x500")

label1 = Label(OVW, text="One Time Password", relief="solid", font=("arial", 26, "bold"), fg='black')
label1.pack(fill=BOTH)

Gm_id = StringVar()
Gm_place = Label(OVW, text="Enter your Gmail ID  Here: ", fg="black", font=("Arial", 12, "bold"))
Gm_place.place(x=50, y=100)
Gm_enter = Entry(OVW, textvariable=Gm_id, bg="white", width=30)
Gm_enter.place(x=270, y=103)

submit1 = Button(OVW, text="Send OTP", fg="black", width=10, command=send_OTP)
submit1.place(x=250, y=175)

OTP_id = StringVar()
OTP_place = Label(OVW, text="Enter your OTP  Here: ", fg="black", font=("Arial", 12, "bold"))
OTP_place.place(x=80, y=300)
OTP_enter = Entry(OVW, textvariable=OTP_id, bg="white", width=30)
OTP_enter.place(x=270, y=303)

submit2 = Button(OVW, text="Verify", fg="black", width=10, command=verify_OTP)
submit2.place(x=250, y=375)

OVW.mainloop()
