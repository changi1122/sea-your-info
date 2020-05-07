import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from tkinter import *
from tkinter import messagebox


class Apps(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=30, weight="bold", slant="italic")
        global font_logintext
        font_logintext = tkfont.Font(family='Helvetica', size=15)
        global font_startpageinfo
        font_startpageinfo = tkfont.Font(family='Helvetica', size=18)

        self.title("Sea Your Info")
        self.geometry('1050x650')
        self.resizable(False, False)
        self.configure(background='white')
        self.iconbitmap(r'imagefile\sea_your_info.ico')
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (
                StartPage, Make_User_page, Find_User_Info, main, Change_User_Info, Mk_U_Suss, ch_U_Suss, Find_ID,
                Find_PW):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        #label.pack(side="top", fill="x", pady=10)
        label.place(x=100,y=35)

        image_mainlogo = PhotoImage(file='imagefile/logo2_color.gif')
        label_defaultlogo=Label(image=image_mainlogo, borderwidth=0)
        label_defaultlogo.image = image_mainlogo
        label_defaultlogo.place(x=20, y=20)

        def clickMe():
            # 아무것도 입력하지 않았을때 오류 발생문 필요

            messagebox.showinfo("Button CLicked", str1.get())
            messagebox.showinfo("Button CLicked", str2.get())
            controller.show_frame("main")



        #첫 화면 텍스트 부분
        label4 = tk.Label(self,
                          text="\t정보바다에 오신 것을 환영합니다.\n\n정보바다에서는 여러분들의 학업 증진을 위하여\n 학교의 공지사항 정보들을 알려드리고 있습니다.\n\n회원가입과 로그인을 통하여 자세히 알아보세요.\n\n\nWelcome to Sea-Your-Info!\n\nSea-Your-Info will let you know all of the\nimportant school notice.\nIt will save your precious time.\n\nFor more information, do not hesitate to\njoin our free membership!\n\n",
                          font=font_startpageinfo, background='white')
        label4.place(x=380, y=180)

        #텍스트 옆에 들어가는 로고 이미지 부분
        image_logo = PhotoImage(file='imagefile/logo2_wb.gif')
        mainlogo = Label(self, image=image_logo, borderwidth=0)#borderwidth가 여백을 제거해준다. 꿀팁
        mainlogo.image = image_logo
        mainlogo.place(x=415, y=145)

        label3 = tk.Label(self, text="Login", font=controller.title_font, background='white')
        label3.place(x=40, y=135)
        # label3.place(x=500, y=700)

        str1 = StringVar()
        LabelWidget1 = tk.Label(self, text="E-mail", background='white', font=font_logintext)
        # LabelWidget1.pack(side=LEFT)
        LabelWidget1.place(x=40, y=240)
        display1 = tk.Entry(self, width=20, textvariable=str1)
        # display1.pack(side=RIGHT)
        display1.place(x=115, y=245)

        str2 = StringVar()
        LabelWidget3 = tk.Label(self, text="PW", background='white', font=font_logintext)
        # LabelWidget3.pack(side=LEFT)
        LabelWidget3.place(x=40, y=280)
        display3 = tk.Entry(self, width=20, textvariable=str2)
        # display3.pack(side=RIGHT)
        display3.place(x=115, y=285)

        image_loginbutton = PhotoImage(file='imagefile/loginbutton.gif')

        button1 = Button(self, text="처음 오셨나요?", command=lambda: controller.show_frame("Make_User_page"),
                         background='white')
        button2 = Button(self, text="아이디와 비밀번호를 잊어버리셨나요?", command=lambda: controller.show_frame("Find_User_Info"),
                         background='white')
        button3 = Button(self, command=clickMe, background='white', image=image_loginbutton)
        button3.image = image_loginbutton#이미지 안될 때는 이렇게 재정의 해줘야 함

        button1.place(x=40, y=555)
        button2.place(x=40, y=590)
        button3.place(x=115, y=380)


class main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.pack(side="top", fill="x", pady=10)
        LabelWidget1 = tk.Label(self, text="Main Page", background='white')
        LabelWidget1.place(x=180, y=180)

        button1 = tk.Button(self, text="로그아웃", command=lambda: controller.show_frame("StartPage"))
        button1.place(x=430, y=350)
        button2 = tk.Button(self, text="회원정보 수정", command=lambda: controller.show_frame("Change_User_Info"))
        button2.place(x=430, y=300)


class Make_User_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')

        def clickMe():
            messagebox.showinfo("Button CLicked", str1.get())
            messagebox.showinfo("Button CLicked", str2.get())
            messagebox.showinfo("Button CLicked", str3.get())
            messagebox.showinfo("Button CLicked", str4.get())
            controller.show_frame("Mk_U_Suss")

        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.pack(side="top", fill="x", pady=10)

        label2 = tk.Label(self, text="회원가입", font=controller.title_font, background='white')
        label2.place(x=140, y=90)

        str1 = StringVar()
        LabelWidget1 = tk.Label(self, text="E-mail", background='white')
        # LabelWidget1.pack(side=LEFT)
        LabelWidget1.place(x=170, y=130)
        display1 = tk.Entry(self, width=20, textvariable=str1)
        # display1.pack(side=RIGHT)
        display1.place(x=270, y=130)

        str2 = StringVar()
        LabelWidget2 = tk.Label(self, text="Name", background='white')
        # LabelWidget2.pack(side=LEFT)
        LabelWidget2.place(x=170, y=180)
        display2 = tk.Entry(self, width=20, textvariable=str2)
        # display2.pack(side=RIGHT)
        display2.place(x=270, y=180)

        str3 = StringVar()
        LabelWidget3 = tk.Label(self, text="PW", background='white')
        # LabelWidget3.pack(side=LEFT)
        LabelWidget3.place(x=170, y=230)
        display3 = tk.Entry(self, width=20, textvariable=str3)
        # display3.pack(side=RIGHT)
        display3.place(x=270, y=230)

        str4 = StringVar()
        LabelWidget3_1 = tk.Label(self, text="PW Check", background='white')
        # LabelWidget3_1.pack(side=LEFT)
        LabelWidget3_1.place(x=170, y=280)
        display3_1 = tk.Entry(self, width=20, textvariable=str4)
        # display3_1.pack(side=RIGHT)
        display3_1.place(x=270, y=280)

        button = tk.Button(self, text="회원가입", command=clickMe)
        button.place(x=420, y=330)


class Change_User_Info(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.pack(side="top", fill="x", pady=10)

        label2 = tk.Label(self, text="회원정보 수정", font=controller.title_font, background='white')
        label2.place(x=140, y=90)

        def clickMe():
            messagebox.showinfo("Button CLicked", str1.get())
            messagebox.showinfo("Button CLicked", str2.get())
            messagebox.showinfo("Button CLicked", str3.get())
            messagebox.showinfo("Button CLicked", str4.get())
            controller.show_frame("ch_U_Suss")

        str1 = StringVar()
        LabelWidget1 = tk.Label(self, text="E-mail", background='white')
        # LabelWidget1.pack(side=LEFT)
        LabelWidget1.place(x=170, y=130)
        display1 = tk.Entry(self, width=20, textvariable=str1)
        # display1.pack(side=RIGHT)
        display1.place(x=270, y=130)

        str2 = StringVar()
        LabelWidget2 = tk.Label(self, text="Name", background='white')
        # LabelWidget2.pack(side=LEFT)
        LabelWidget2.place(x=170, y=180)
        display2 = tk.Entry(self, width=20, textvariable=str2)
        # display2.pack(side=RIGHT)
        display2.place(x=270, y=180)

        str3 = StringVar()
        LabelWidget3 = tk.Label(self, text="PW", background='white')
        # LabelWidget3.pack(side=LEFT)
        LabelWidget3.place(x=170, y=230)
        display3 = tk.Entry(self, width=20, textvariable=str3)
        # display3.pack(side=RIGHT)
        display3.place(x=270, y=230)

        str4 = StringVar()
        LabelWidget3_1 = tk.Label(self, text="PW Check", background='white')
        # LabelWidget3_1.pack(side=LEFT)
        LabelWidget3_1.place(x=170, y=280)
        display3_1 = tk.Entry(self, width=20, textvariable=str4)
        # display3_1.pack(side=RIGHT)
        display3_1.place(x=270, y=280)

        button = tk.Button(self, text="완료", command=clickMe)
        button.place(x=420, y=330)


class Find_User_Info(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.pack(side="top", fill="x", pady=10)

        label2 = tk.Label(self, text="find ID", font=controller.title_font, background='white')
        # label2.pack(side="top", pady=5)
        label2.place(x=120, y=80)

        LabelWidget1 = tk.Label(self, text="E-mail", background='white')
        # LabelWidget1.pack(side=LEFT)
        LabelWidget1.place(x=170, y=120)
        display1 = tk.Entry(self, width=20)
        # display1.pack(side=RIGHT)
        display1.place(x=270, y=120)

        LabelWidget2 = tk.Label(self, text="Name", background='white')
        # LabelWidget1.pack(side=LEFT)
        LabelWidget2.place(x=170, y=150)
        display2 = tk.Entry(self, width=20)
        # display2.pack(side=RIGHT)
        display2.place(x=270, y=150)

        label3 = tk.Label(self, text="find PW", font=controller.title_font, background='white')
        label3.pack(side="top", pady=5)
        label3.place(x=120, y=220)

        LabelWidget3 = tk.Label(self, text="E-mail", background='white')
        # LabelWidget3.pack(side=LEFT)
        LabelWidget3.place(x=170, y=260)
        display3 = tk.Entry(self, width=20)
        # display3.pack(side=RIGHT)
        display3.place(x=270, y=260)

        button1 = tk.Button(self, text="완료", command=lambda: controller.show_frame("Find_ID"))
        # button1.pack()
        button1.place(x=400, y=180)

        button2 = tk.Button(self, text="완료", command=lambda: controller.show_frame("Find_PW"))
        # button2.pack()
        button2.place(x=400, y=290)


class Find_ID(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.pack(side="top", fill="x", pady=10)

        # DB에서 E-Mail 반환후 있으면 이거 없으면 오류 출력
        label2 = tk.Label(self, text="등록하신 아이디는... 입니다.", font=controller.title_font, background='white')
        label2.place(x=200, y=100)

        button1 = tk.Button(self, text="확인", command=lambda: controller.show_frame("StartPage"))
        # button1.pack()
        button1.place(x=450, y=300)


class Find_PW(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.pack(side="top", fill="x", pady=10)

        # DB에서 E-Mail 반환후 있으면 이거 없으면 오류 출력
        label2 = tk.Label(self, text="임시 비밀번호 ... 이 되었습니다.\n 접속후 PW를 변경해 주세요", font=controller.title_font,
                          background='white')
        label2.place(x=200, y=100)

        button1 = tk.Button(self, text="확인", command=lambda: controller.show_frame("StartPage"))
        # button1.pack()
        button1.place(x=450, y=300)


class Mk_U_Suss(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.pack(side="top", fill="x", pady=10)

        label2 = tk.Label(self, text="회원가입에 성공했습니다.", font=controller.title_font, background='white')
        label2.place(x=200, y=100)

        button1 = tk.Button(self, text="돌아가기", command=lambda: controller.show_frame("StartPage"))
        # button1.pack()
        button1.place(x=450, y=300)


class ch_U_Suss(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.pack(side="top", fill="x", pady=10)

        label2 = tk.Label(self, text="회원정보 변경에 성공했습니다.", font=controller.title_font, background='white')
        label2.place(x=200, y=100)

        button1 = tk.Button(self, text="돌아가기", command=lambda: controller.show_frame("main"))
        # button1.pack()
        button1.place(x=450, y=300)


if __name__ == "__main__":
    app = Apps()
    app.mainloop()
