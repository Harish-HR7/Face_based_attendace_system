############################################# IMPORTING MODULES
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import Canvas
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import os
from cv2 import cv2
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import yagmail


############################################# FUNCTIONS ################################################

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


##################################################################################

def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200, tick)


###################################################################################

def contact():
    mess._show(title='Contact us', message="Please contact us on : 'hr18@gmail.com' ")


###################################################################################
def Close():
    window.destroy()

###################################################################################
#receiver="Tkinter-1.system@gmail.com"
def sendMail():
    assure_path_exists("/Users/harishreddy/MyFiles/Coursera/Facial Attendance System/Tkinter-1/TrainingImageLabel/")
    exists1 = os.path.isfile("/Users/harishreddy/MyFiles/Coursera/Facial Attendance System/Tkinter-1/TrainingImageLabel/mail.txt")
    if exists1:
        tf = open("/Users/harishreddy/MyFiles/Coursera/Facial Attendance System/Tkinter-1/TrainingImageLabel/mail.txt", "r")
        receiver = tf.read()
    else:
        receiver = tsd.askstring('Attendance receiver','Please enter mail ID of the receiver of attendance report')

        if receiver == None:
            mess._show(title='No Mail Entered', message='Mail not set!! Please try again')
        else:
            tf = open("/Users/harishreddy/MyFiles/Coursera/Facial Attendance System/Tkinter-1/TrainingImageLabel/mail.txt", "a+")
            tf.write(receiver)
            mess._show(title='Mail ID of receiver Registered', message='Receiver mail ID registered successfully!!')

    date = datetime.date.today().strftime("%B %d, %Y")
    path = "/Users/harishreddy/MyFiles/Coursera/Facial Attendance System/Tkinter-1/Attendance_Excel"
    os.chdir(path)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    newest = files[-2]
    filename = newest
    sub = "Attendance Report for " + str(date)
    body='Please find the Attendance report for the day '+date+' of III year IT-A class'
    # mail information
    yag = yagmail.SMTP("myFRASsystem@gmail.com", "admin#007")
    # sent the mail
    yag.send(
        to=receiver,
        subject=sub,  # email subject
        contents=body,  # email body
        attachments=filename  # file attached
    )
    mess._show(title='EMAIL SENT Succesfully', message=date+' Attendance mailed to '+receiver)


###################################################################################
def check_haarcascadefile():
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title='Some file missing', message='Please contact us for help')
        window.destroy()


###################################################################################

def save_pass():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel/psd.txt")
    if exists1:
        tf = open("TrainingImageLabel/psd.txt", "r")
        key = tf.read()
    else:
        master.destroy()
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel/psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    op = (old.get())
    newp = (new.get())
    nnewp = (nnew.get())
    if (op == key):
        if (newp == nnewp):
            txf = open("TrainingImageLabel/psd.txt", "w")
            txf.write(newp)
        else:
            mess._show(title='Error', message='Confirm new password again!!!')
            return
    else:
        mess._show(title='Wrong Password', message='Please enter correct old password.')
        return
    mess._show(title='Password Changed', message='Password changed successfully!!')
    master.destroy()


###################################################################################

def change_pass():
    global master
    master = tk.Tk()
    master.geometry("400x160")
    master.resizable(False, False)
    master.title("Change Password")
    master.configure(background="white")
    lbl4 = tk.Label(master, text='    Enter Old Password', bg='white', font=('times', 12, ' bold '))
    lbl4.place(x=10, y=10)
    global old
    old = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
    old.place(x=180, y=10)
    lbl5 = tk.Label(master, text='   Enter New Password', bg='white', font=('times', 12, ' bold '))
    lbl5.place(x=10, y=45)
    global new
    new = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
    new.place(x=180, y=45)
    lbl6 = tk.Label(master, text='Confirm New Password', bg='white', font=('times', 12, ' bold '))
    lbl6.place(x=10, y=80)
    global nnew
    nnew = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
    nnew.place(x=180, y=80)
    cancel = tk.Button(master, text="Cancel", command=master.destroy, fg="black", bg="red", height=1, width=25,
                       activebackground="white", font=('times', 10, ' bold '))
    cancel.place(x=200, y=120)
    save1 = tk.Button(master, text="Save", command=save_pass, fg="black", bg="#3ece48", height=1, width=25,
                      activebackground="white", font=('times', 10, ' bold '))
    save1.place(x=10, y=120)
    master.mainloop()


#####################################################################################

def psw():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel/psd.txt")
    if exists1:
        tf = open("TrainingImageLabel/psd.txt", "r")
        key = tf.read()
    else:
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel/psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered', message='New password registered successfully!!')



    password = tsd.askstring('Password', 'Enter Password', show='*')
    if (password == key):
        TrainImages()
    elif (password == None):
        pass
    else:
        mess._show(title='Wrong Password', message='You have entered wrong password')


######################################################################################

def clear():
    txt.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)


def clear2():
    txt2.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)


#######################################################################################

def TakeImages():
    check_haarcascadefile()
    columns = ['SERIAL NO.', 'ID', 'NAME']
    assure_path_exists("StudentDetails/")
    assure_path_exists("TrainingImage/")
    serial = 0
    exists = os.path.isfile("StudentDetails/StudentDetails.csv")
    if exists:
        with open("StudentDetails/StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                serial = serial + 1
        csvFile1.close()
    else:
        with open("StudentDetails/StudentDetails.csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)
            serial = 1
        csvFile1.close()
    Id = (txt.get())
    name = (txt2.get())
    if ((name.isalpha()) or (' ' in name)):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage/ " + str(serial)+"."+ Id + '.' + str(sampleNum) + ".jpg",
                            gray[y:y + h, x:x + w])
                # display the frame
                cv2.imshow('Taking Images', img)
            # wait for 100 miliseconds
            if cv2.waitKey(5) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum > 100:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Taken for ID : " + Id
        row = [serial, Id, name]
        with open('StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message1.configure(text=res)
    else:
        if (name.isalpha() == False):
            res = "Enter Correct name"
            message.configure(text=res)


########################################################################################

def TrainImages():
    check_haarcascadefile()
    assure_path_exists("TrainingImageLabel/")
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, ID = getImagesAndLabels("TrainingImage")
    try:
        recognizer.train(faces, np.array(ID))
    except:
        mess._show(title='No Registrations', message='Please Register someone first!!!')
        return

    recognizer.save("TrainingImageLabel/Trainner.yml")
    res = "Profile Saved Successfully"
    message1.configure(text=res)
    message.configure(text='Registrated Users  : ' + str(ID[0]))
    #message.configure(text='Registered Users  : ' + str(current_serial_no))



############################################################################################3

def getImagesAndLabels(path):
    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empty face list
    faces = []
    # create empty ID list a Current Serial No.
    Ids = []
    #current_serial_no=0;

    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        if imagePath == 'TrainingImage/.DS_Store':
            continue
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image
        ID = int(os.path.split(imagePath)[-1].split(".")[0])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(ID)
    #current_serial_no=int(os.path.split(imagePaths[0])[-1].split(".")[0])
    return faces, Ids


###########################################################################################

def TrackImages():
    check_haarcascadefile()
    assure_path_exists("Attendance/")
    assure_path_exists("StudentDetails/")
    for k in tv.get_children():
        tv.delete(k)
    msg = ''
    i = 0
    j = 0
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    exists3 = os.path.isfile("TrainingImageLabel/Trainner.yml")
    if exists3:
        recognizer.read("TrainingImageLabel/Trainner.yml")
    else:
        mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
        return
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);

    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    exists1 = os.path.isfile("StudentDetails/StudentDetails.csv")
    if exists1:
        df = pd.read_csv("StudentDetails/StudentDetails.csv")
    else:
        mess._show(title='Details Missing', message='Students details are missing, please check!')
        cam.release()
        cv2.destroyAllWindows()
        window.destroy()
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                ID = str(ID)
                ID = ID[2:-2]
                bb = str(aa)
                bb = bb[2:-2]
                attendance = [ID, bb, str(date), str(timeStamp)]

            else:
                ID = bb= 'Unknown'

            try:
                cv2.putText(im, ID+" : "+bb, (x, y + h), font, 1, (255, 255, 255), 2)
            except:
                ID='Unknown'
                cv2.putText(im, ID + " : " + bb, (x, y + h), font, 1, (255, 255, 255), 2)

        cv2.imshow('Taking Attendance', im)
        if cv2.waitKey(1) == ord('q'):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    exists = os.path.isfile("Attendance/Attendance_" + date + ".csv")
    if exists:
        with open("Attendance/Attendance_" + date + ".csv", 'a+') as csvFile1:
            try:
                writer = csv.writer(csvFile1)
                writer.writerow(attendance)
            except:
                attendance = ['NO ONE', 'NO ONE', str(date), str(datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S'))]

        csvFile1.close()
    else:
        with open("Attendance/Attendance_" + date + ".csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(col_names)
            writer.writerow(attendance)
        csvFile1.close()

    #After Taking attendance showing the details row by row on Treeview

    with open("Attendance/Attendance_" + date + ".csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for lines in reader1:
            i = i + 1
            if (i > 1):
                iidd = str(lines[0])
                tv.insert('', 0, text=iidd, values=(str(lines[1]), str(lines[2]), str(lines[3])))
                # print(iidd)
                # print(lines)

    # Reading the csv file to a DF
    df_new = pd.read_csv("Attendance/Attendance_" + date + ".csv")

    #print(df_new)
    # saving xlsx file
    xls = pd.ExcelWriter('Attendance_Excel/Attendance_' + date + '.xlsx')
    df_new.to_excel(xls, index=False)

    #print(df_new)
    xls.save()
    csvFile1.close()
    cam.release()
    cv2.destroyAllWindows()


######################################## USED STUFFS ############################################

global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day, month, year = date.split("-")

mont = {'01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
        }

######################################## GUI FRONT-END ###########################################


window = tk.Tk()
window.geometry("1280x720")
window.resizable(True, False)
window.title("Attendance System")

Img = cv2.imread("./src/images/19604.png")
cv2.imwrite("./src/images/19604.png",Img)
bg = PhotoImage(file = "./src/images/19604.png")
canvas1 = Canvas( window, width = 1280,height = 720)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg,anchor = "nw")

#window.configure(background='#262523')

## FRAME 1
frame1 = tk.Frame(window)
img = ImageTk.PhotoImage(Image.open("./src/images/f1.png").resize((499, 552), Image.ANTIALIAS))
lbl = tk.Label(frame1, image=img)
lbl.img = img
lbl.place(relwidth=1.0, relheight=1.0, anchor='nw')
frame1.place(relx=0.07, rely=0.17, relwidth=0.39, relheight=0.80)

## FRAME2
frame2 = tk.Frame(window)
img2 = ImageTk.PhotoImage(Image.open("./src/images/f1.png").resize((485, 552), Image.ANTIALIAS))
lbl2 = tk.Label(frame2, image=img2)
lbl2.img2 = img2
lbl2.place(relwidth=1.0, relheight=1.0, anchor='nw')
frame2.place(relx=0.55, rely=0.17, relwidth=0.38, relheight=0.80)

message3 = tk.Label(window, text="Face Recognition Based Attendance System", fg="white", bg='black', width=37,
                    height=1, font=('Anurati', 32))
message3.place(relx=0.2, rely=0.03)

frame3 = tk.Frame(window, bg="#c4c6ce")
frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)

frame4 = tk.Frame(window, bg="#c4c6ce")
frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)

datef = tk.Label(frame4, text=day + "-" + mont[month] + "-" + year + "   |  ", fg="#0066CC",bg='black', width=55,
                 height=1, font=('Neuropolitical', 18))
datef.pack(fill='both', expand=1)

clock = tk.Label(frame3, fg="#0066CC",bg='black', width=55, height=1, font=('Neuropolitical', 18))
clock.pack(fill='both', expand=1)
tick()

head2 = tk.Label(frame2, text="                     New Registrations Here                      ", fg="black",
                 bg="#3ece48", font=('Neuropolitical', 16,))
head2.grid(row=0, column=0)

head1 = tk.Label(frame1, text="                          Registered Users                            ", fg="black",
                 bg="#3ece48", font=('Neuropolitical', 16,))
head1.place(x=0, y=0)

lbl = tk.Label(frame2, text="Enter ID", width=15, height=1, fg="black", bg="#0066CC", font=('Neuropolitical', 14,))
lbl.place(x=80, y=55)

txt = tk.Entry(frame2, width=32, fg="black", font=('Neuropolitical', 12))
txt.place(x=30, y=88)

lbl2 = tk.Label(frame2, text="Enter Name", width=14, fg="black", bg="#0066CC", font=('Neuropolitical', 15))
lbl2.place(x=80, y=140)

txt2 = tk.Entry(frame2, width=32, fg="black", font=('Neuropolitical', 12))
txt2.place(x=30, y=173)

message1 = tk.Label(frame2, text="1) Take Images  >>>  2) Save Profile", bg="#0066CC", fg="black", width=35, height=1,
                    activebackground="yellow", font=('Neuropolitical', 14))
message1.place(x=13, y=230)

##REGISTERD USERS LABEL
message = tk.Label(frame2, text="", bg="#0066CC", fg="black", width=24, height=1, activebackground="yellow",
                   font=('Neuropolitical', 18))
message.place(x=30, y=450)

lbl3 = tk.Label(frame1, text="Attendance", width=15, fg="black", bg="#0066CC", height=1, font=('Neuropolitical', 17))
lbl3.place(x=120, y=115)

res = -1
exists = os.path.isfile("StudentDetails/StudentDetails.csv")
exists2=os.path.isfile("TrainingImageLabel/Trainner.yml")
if exists2 and exists:
    with open("StudentDetails/StudentDetails.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for l in reader1:
            res = res + 1
    #res = (res // 2) - 1
    csvFile1.close()
elif exists:
    with open("StudentDetails/StudentDetails.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for l in reader1:
            res = res + 1
    res=res-1
    csvFile1.close()

else:
    res = 0
message.configure(text='Registered Users  : ' + str(res))

##################### MENUBAR #################################

menubar = tk.Menu(window, relief='ridge')
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='Change Password', command=change_pass)
filemenu.add_command(label='Contact Us', command=contact)
filemenu.add_command(label='Exit', command=Close)
menubar.add_cascade(label='Help', font=('Neuropolitical', 20, ' bold '), menu=filemenu)

################## TREEVIEW ATTENDANCE TABLE ####################

tv = ttk.Treeview(frame1, height=13, columns=('name', 'date', 'time'))
tv.column('#0', width=100)
tv.column('name', width=130)
tv.column('date', width=123)
tv.column('time', width=110)
tv.grid(row=2, column=0, padx=(10, 0), pady=(150, 0), columnspan=4)
tv.heading('#0', text='ID')
tv.heading('name', text='NAME')
tv.heading('date', text='DATE')
tv.heading('time', text='TIME')

###################### SCROLLBAR ################################

scroll = ttk.Scrollbar(frame1, orient='vertical', command=tv.yview)
scroll.grid(row=2, column=4, padx=(0, 100), pady=(150, 0), sticky='ns')
tv.configure(yscrollcommand=scroll.set)

###################### BUTTONS ##################################

clearButton = tk.Button(frame2, text="Clear", command=clear, fg="#009900", bg="#00CC00", width=7,height=1,
                        activebackground="white", font=('Neuropolitical', 10))
clearButton.place(relx=0.82, y=91)
clearButton2 = tk.Button(frame2, text="Clear", command=clear2, fg="#009900", bg="#ea2a2a", width=7,height=1,
                         activebackground="white", font=('Neuropolitical', 10))
clearButton2.place(relx=0.82, y=176)
takeImg = tk.Button(frame2, text="Take Images", command=TakeImages, fg="#009900", bg="#00CC00", width=25, height=1,
                    activebackground="#00CC00", font=('Neuropolitical', 14))
takeImg.place(x=85, y=300)
trainImg = tk.Button(frame2, text="Save Profile", command=psw, fg="#009900", bg="#00CC00", width=25, height=1,
                     activebackground="white", font=('Neuropolitical', 14))
trainImg.place(x=85, y=380)
trackImg = tk.Button(frame1, text="Take Attendance", command=TrackImages, fg="#009900", bg="#00CC00", width=25, height=1,
                     activebackground="#00CC00", font=('Neuropolitical', 14))
trackImg.place(x=85, y=50)

sendEmail = tk.Button(frame1, text="Auto Mail of Attendance", command=sendMail, fg="#009900", bg="#00CC00", width=25, height=1,
                     activebackground="#00CC00", font=('Neuropolitical', 14))
sendEmail.place(x=85, y=80)

quitWindow = tk.Button(frame1, text="Quit", command=Close, fg="red", bg="red", width=25, height=1,
                       font=('Neuropolitical', 14))
quitWindow.place(x=85, y=450)

##################### END ######################################

window.configure(menu=menubar)
window.mainloop()

####################################################################################################
