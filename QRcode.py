                                                       #GENERATING A UNIQUE QR CODE USING PYTHON(Tkinter)#
from resizeimage import resizeimage
from tkinter import*
import qrcode
from PIL import ImageTk, Image
import time
import pyttsx3
logo = Image.open('pesu_image.jpg')


class Qr_Generator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("Qr Generator | Developed By Abhishek")
        self.root.resizable(False, False)

        title = Label(self.root, text="         \tQr Code Generator", font=("times new roman", 40), bg="#053246", fg="violet", anchor="w").place(x=0, y=0, relwidth=1)

        #==========Student Details window=========#
        #==========Variables=======================#
        self.var_stu_code = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_designation = StringVar()

        stu_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        stu_Frame.place(x=50, y=100, width=500, height=380)

        stu_title = Label(stu_Frame, text="Student details", font=("goudy old style", 20), bg="#043256", fg="yellow").place(x=0, y=0, relwidth=1)

        lbl_stu_code = Label(stu_Frame, text="Student srn : ", font=("times new roman", 20, "bold"), bg="white").place(x=20, y=50)
        lbl_stu_name = Label(stu_Frame, text="Name : ", font=("times new roman", 20, "bold"), bg="white").place(x=20, y=100)
        lbl_stu_department = Label(stu_Frame, text="Department : ", font=("times new roman", 20, "bold"), bg="white").place(x=20, y=140)
        lbl_stu_section = Label(stu_Frame, text="Section : ", font=("times new roman", 20, "bold"), bg="white").place(x=20, y=180)

        txt_stu_code = Entry(stu_Frame, textvariable=self.var_stu_code, font=("times new roman", 20), bg="lightyellow").place(x=200, y=60)
        txt_stu_name = Entry(stu_Frame, textvariable=self.var_name, font=("times new roman", 20), bg="lightyellow").place(x=200, y=100)
        txt_stu_department = Entry(stu_Frame, textvariable=self.var_department, font=("times new roman", 20), bg="lightyellow").place(x=200, y=140)
        txt_stu_section = Entry(stu_Frame, textvariable=self.var_designation, font=("times new roman", 20), bg="lightyellow").place(x=200, y=180)

        btn_generate = Button(stu_Frame, text="Qr Generator", command=self.generate, font=("times new romen", 18, "bold"), bg="#2196f3", fg="white").place(x=90, y=250, width=160, height=30)
        btn_clear = Button(stu_Frame, text="Clear", command=self.clear, font=("times new romen", 18, "bold"), bg="#607d8b", fg="white").place(x=300, y=250, width=120, height=30)

        self.msg = ""
        self.lbl_msg = Label(stu_Frame, text=self.msg, font=("times new romaN", 20, "bold"), bg="white", fg="green")
        self.lbl_msg.place(x=0, y=300, relwidth=1)

    # ==========Student Details window========#
        qr_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        qr_Frame.place(x=600, y=100, width=250, height=380)

        stu_title = Label(qr_Frame, text="Student Qr code", font=("goudy old style", 20), bg="#043256", fg="cyan").place(x=0, y=0, relwidth=1)

        self.qr_code = Label(qr_Frame, text="No Qr\nAvailable", font=("times new roman", 20), bg="#3f51b5", fg="white")
        self.qr_code.place(x=35, y=100, width=180, height=180)

        engin = pyttsx3.init()
        engin.say("Hi student, please Enter your following details")
        engin.runAndWait()

    def clear(self):
        self.var_stu_code.set("")
        self.var_name.set("")
        self.var_department.set("")
        self.var_designation.set("")
        self.msg = ""
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image="")

        engin = pyttsx3.init()
        engin.say("clear")
        engin.runAndWait()
        self.msg = "clear"
        self.lbl_msg.config(text=self.msg, fg="black")

    def generate(self):
        if self.var_stu_code.get() == "" or self.var_name.get() == "" or self.var_department.get() == "" or self.var_designation.get() == "":

            engin = pyttsx3.init()
            engin.say("Error!! Error!!")
            engin.runAndWait()

            self.msg = "Error!! Error!!"
            self.lbl_msg.config(text=self.msg, fg="red")
        else:
            global logo
            basic = 40
            width_percentage = (basic/float(logo.size[0]))
            height_size = int((float(logo.size[1])*float(width_percentage)))
            logo = logo.resize((basic, height_size), Image.ANTIALIAS)
            qrc = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=3.8)

            qrc.add_data(f"Student SRN : {self.var_stu_code.get()}\nStudent Name : {self.var_name.get()}\nDestination : {self.var_department.get()}\nDesignation : {self.var_designation.get()}")
            qrc.make()
            gen_img = qrc.make_image(fill_color='#4a7a8c', bg_color="#fff").convert('RGBA')

            position = ((gen_img.size[0] - logo.size[0]) // 2, (gen_img.size[1] - logo.size[1]) // 2)

            gen_img.paste(logo, position)
            gen_img.save(".idea/Stu_"+str(self.var_stu_code.get())+".png")

            #=========Qr code image updating ==============##

            self.im = ImageTk.PhotoImage(file=".idea/Stu_"+str(self.var_stu_code.get())+".png")
            self.qr_code.config(image=self.im)

            #======updating notification=============#

            engin = pyttsx3.init()
            engin.say("Qr code generated successfully!!!,please.... scan...it...,thank..you!!!!!!!!")
            engin.runAndWait()

            self.msg = "Qr code generated successfully!!!"
            self.lbl_msg.config(text=self.msg, fg="green")

root = Tk()
obj = Qr_Generator(root)
root.mainloop()
