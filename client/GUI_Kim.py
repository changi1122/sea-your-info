import tkinter as tk
import GUI_get_posts as Gposts
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
        global font_radiobuttontext
        font_radiobuttontext = tkfont.Font(family='Helvetica', size=12)
        global font_hypertext
        font_hypertext = tkfont.Font(size=10, underline=True)
        global font_Cheack_B
        font_Cheack_B = tkfont.Font(size=11, weight="bold", family='Helvetica')

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
                StartPage, Make_User_page, Find_User_Info, main, Change_User_Info, Mk_U_Suss, ch_U_Suss, Find_ID, Find_PW):
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
        # 맨 위의 Sea Your Info 들어가는 부분
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        # label.pack(side="top", fill="x", pady=10)
        label.place(x=100, y=35)

        image_mainlogo = PhotoImage(file='imagefile/logo2_color.gif')
        label_defaultlogo = Label(image=image_mainlogo, borderwidth=0)
        label_defaultlogo.image = image_mainlogo
        label_defaultlogo.place(x=20, y=20)

        # OP_bar 추가
        image_bar = PhotoImage(file='imagefile/OP_bar.png')
        label_defaultlogo = Label(image=image_bar)
        label_defaultlogo.image = image_bar
        label_defaultlogo.place(x=-10, y=100)

        def clickMe():
            # 아무것도 입력하지 않았을때 오류 발생문 필요

            messagebox.showinfo("Button CLicked", str1.get())
            messagebox.showinfo("Button CLicked", str2.get())
            controller.show_frame("main")

        # 첫 화면 텍스트 부분
        label4 = tk.Label(self,
                          text="  정보바다에 오신 것을 환영합니다.\n\n정보바다에서는 여러분들의 학업 증진을 위하여\n 학교의 공지사항 정보들을 알려드리고 있습니다.\n\n회원가입과 로그인을 통하여 자세히 알아보세요.\n\n\nWelcome to Sea-Your-Info!\n\nSea-Your-Info will let you know all of the\nimportant school notice.\nIt will save your precious time.\n\nFor more information, do not hesitate to\njoin our free membership!\n\n",
                          font=font_startpageinfo, background='white')
        label4.place(x=440, y=160)

        # 텍스트 옆에 들어가는 로고 이미지 부분
        image_logo = PhotoImage(file='imagefile/logo2_color.gif')
        mainlogo = Label(self, image=image_logo, borderwidth=0)  # borderwidth가 여백을 제거해준다. 꿀팁
        mainlogo.image = image_logo
        mainlogo.place(x=445, y=140)

        label3 = tk.Label(self, text="Login", font=controller.title_font, background='white')
        label3.place(x=40, y=135)


        str1 = StringVar()
        LabelWidget1 = tk.Label(self, text="E-mail", background='white', font=font_logintext)
        LabelWidget1.place(x=40, y=240)
        display1 = tk.Entry(self, width=20, textvariable=str1)
        display1.place(x=115, y=245)

        str2 = StringVar()
        LabelWidget3 = tk.Label(self, text="PW", background='white', font=font_logintext)
        LabelWidget3.place(x=40, y=280)
        display3 = tk.Entry(self, width=20, textvariable=str2)
        display3.place(x=115, y=285)

        log_B = PhotoImage(file='imagefile/OP_button3.png')

        button1 = Button(self, text="처음 오셨나요?", command=lambda: controller.show_frame("Make_User_page"),
                         background='white', borderwidth=0, font=font_hypertext, fg="#0000FF")
        button2 = Button(self, text="아이디와 비밀번호를 잊어버리셨나요?", command=lambda: controller.show_frame("Find_User_Info"),
                         background='white', borderwidth=0, font=font_hypertext, fg="#0000FF")
        button3 = Button(self, borderwidth=3,relief="flat",background='white', command=clickMe, padx=10, pady=10, image=log_B)
        button3.image = log_B # 이미지 안될 때는 이렇게 재정의 해줘야 함

        button1.place(x=40, y=570)
        button2.place(x=40, y=590)
        button3.place(x=115, y=380)


class main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        # 맨 위에 Sea your Info 가 보이는 부분
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)
        global frame_department_notice
        global frame_school_notice

        # 좌측 상단 user_image(USER라고 크게 적혀져있고 파란색 원 있는 부분) 출력 부분
        image_user = PhotoImage(file="imagefile/user_image.gif")
        user_image = Label(self, image=image_user, borderwidth=0)
        user_image.image = image_user
        user_image.place(x=25, y=120)

        # 좌측 상단 user_image 바로 오른 쪽에 있는 로그아웃과 회원정보 수정 버튼 부분
        button1 = tk.Button(self, text="로그아웃", command=lambda: controller.show_frame("StartPage"), borderwidth=0, background='white', font=font_hypertext, fg="#0000FF")
        button1.place(x=145, y=160)
        button2 = tk.Button(self, text="회원정보 수정", command=lambda: controller.show_frame("Change_User_Info"), borderwidth=0, background='white', font=font_hypertext, fg="#0000FF")
        button2.place(x=145, y=185)

        # 라디오 버튼 들어가는 부분, Radiobutton에 command추가 해야 한다.
        radio_scholar = Radiobutton(self, text="장학금", background='white', value=1, font=font_radiobuttontext)
        radio_scholar.place(x=30, y=290)

        radio_job = Radiobutton(self, text="학내 행사", background='white', value=2, font=font_radiobuttontext)
        radio_job.place(x=130, y=290)

        radio_event = Radiobutton(self, text="취업", background='white', value=3, font=font_radiobuttontext)
        radio_event.place(x=230, y=290)

        radio_text1 = Radiobutton(self, text="txt1", background='white', value=4, font=font_radiobuttontext)
        radio_text1.place(x=30, y=360)

        radio_text2 = Radiobutton(self, text="txt2", background='white', value=5, font=font_radiobuttontext)
        radio_text2.place(x=130, y=360)

        radio_text3 = Radiobutton(self, text="txt3", background='white', value=6, font=font_radiobuttontext)
        radio_text3.place(x=230, y=360)

        radio_text4 = Radiobutton(self, text="txt4", background='white', value=7, font=font_radiobuttontext)
        radio_text4.place(x=30, y=430)

        radio_text5 = Radiobutton(self, text="txt5", background='white', value=8, font=font_radiobuttontext)
        radio_text5.place(x=130, y=430)

        radio_text6 = Radiobutton(self, text="txt6", background='white', value=9, font=font_radiobuttontext)
        radio_text6.place(x=230, y=430)

        radio_text7 = Radiobutton(self, text="txt7", background='white', value=10, font=font_radiobuttontext)
        radio_text7.place(x=30, y=500)

        radio_text8 = Radiobutton(self, text="txt8", background='white', value=11, font=font_radiobuttontext)
        radio_text8.place(x=130, y=500)

        radio_text9 = Radiobutton(self, text="txt9", background='white', value=12, font=font_radiobuttontext)
        radio_text9.place(x=230, y=500)

        # 탭 부분 - notebook 이용하면 됨
        notebook_main = ttk.Notebook(self, width=670, height=470, padding=10)
        notebook_main.place(x=330, y=115)

        # 탭 부분 중에서 각 프레임 설정 부분
        # 첫 번째 프레임 설정 부분

        frame_department_notice = Frame(self)
        notebook_main.add(frame_department_notice, text="  학과 공지  ")
        label_frame1_1 = Label(frame_department_notice, text="소프트웨어학과 최우수 학과 선정")
        label_frame1_1.place(x=20, y=20)

        # 두 번째 프레임 설정 부분
        frame_school_notice = Frame(self)
        notebook_main.add(frame_school_notice, text="  학교 공지  ")
        label_sn_1 = Label(frame_school_notice, text="충북대학교 등록금 전액 환불 추진")
        label_sn_1.place(x=20, y=20)

        # DB에서 가져온 data를 학교 공지사항, sw 공지사항 별로 저장할 함수

        button = tk.Button(self, borderwidth=3, relief="flat", text="  Enter  ", fg="white",
                           background="#00b0f0", font=font_Cheack_B, command=Show_data)
        button.place(x=230, y=560)

# NoteBook에 Enter 클릭시 data 출력 부분
def Show_data():
    global frame_department_notice
    global frame_school_notice
    a = []
    Gposts.test(a)
    scrollbar=tk.Scrollbar(frame_department_notice)
    scrollbar.pack(side="right", fill ="y")
    listbox=tk.Listbox(frame_department_notice, yscrollcommand=scrollbar.set,width=660, height=460)

    txt=""
    for i in range(0, len(a), 4):
        for k in range(i,i+4):
            txt+=" "+str(a[k])
        listbox.insert(i, txt)
        txt=""
    listbox.pack()

    scrollbar["command"]=listbox.yview


class Make_User_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')

        def clickMe():
            messagebox.showinfo("Button CLicked", str1.get())
            messagebox.showinfo("Button CLicked", str2.get())
            messagebox.showinfo("Button CLicked", str3.get())
            controller.show_frame("Mk_U_Suss")
        # 회원가입 뒤 배경 추가
        image_user = PhotoImage(file="imagefile/OP_make_user.png")
        user_image = Label(self, image=image_user, borderwidth=0)
        user_image.image = image_user
        user_image.place(x=230, y=120)

        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        #label2 = tk.Label(self, text="Sing Up", background='white', font=font_startpageinfo)
        label2 = tk.Label(self, text="회원가입", background='white', font=font_startpageinfo)
        label2.place(x=375, y=230)

        str1 = StringVar()
        LabelWidget1 = tk.Label(self, text="E-mail", background='white', font=font_radiobuttontext)
        LabelWidget1.place(x=375, y=290)
        display1 = tk.Entry(self, width=20, textvariable=str1)
        display1.place(x=475, y=290)

        str2 = StringVar()
        LabelWidget2 = tk.Label(self, text="Name", background='white', font=font_radiobuttontext)
        LabelWidget2.place(x=375, y=360)
        display2 = tk.Entry(self, width=20, textvariable=str2)
        display2.place(x=475, y=360)

        str3 = StringVar()
        LabelWidget3 = tk.Label(self, text="Password", background='white', font=font_radiobuttontext)
        Label_PW_Rool=tk.Label(self, text="Make sure it's at least 15 characters OR \nat lest 8 characters including a number", background="white")
        LabelWidget3.place(x=375, y=430)
        Label_PW_Rool.place(x=475, y=450)
        display3 = tk.Entry(self, width=20, textvariable=str3)
        display3.place(x=475, y=430)


        button = tk.Button(self, borderwidth=3,relief="flat", text="Sing up for Sea Your Info", command=clickMe, fg="white", background="#00b0f0", font=font_Cheack_B)
        button.place(x=475, y=560)



class Change_User_Info(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        def clickMe():
            messagebox.showinfo("Button CLicked", str1.get())
            messagebox.showinfo("Button CLicked", str2.get())
            messagebox.showinfo("Button CLicked", str3.get())
            controller.show_frame("ch_U_Suss")

        image_user = PhotoImage(file="imagefile/OP_make_user.png")
        user_image = Label(self, image=image_user, borderwidth=0)
        user_image.image = image_user
        user_image.place(x=230, y=120)

        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        label2 = tk.Label(self, text="Change User Info", background='white', font=font_startpageinfo)
        label2.place(x=375, y=230)

        str1 = StringVar()
        LabelWidget1 = tk.Label(self, text="E-mail", background='white', font=font_radiobuttontext)
        LabelWidget1.place(x=375, y=290)
        display1 = tk.Entry(self, width=20, textvariable=str1)
        display1.place(x=475, y=290)

        str2 = StringVar()
        LabelWidget2 = tk.Label(self, text="Name", background='white', font=font_radiobuttontext)
        LabelWidget2.place(x=375, y=360)
        display2 = tk.Entry(self, width=20, textvariable=str2)
        display2.place(x=475, y=360)

        str3 = StringVar()
        LabelWidget3 = tk.Label(self, text="Password", background='white', font=font_radiobuttontext)
        Label_PW_Rool = tk.Label(self, text="Make sure it's at least 15 characters OR \nat lest 8 characters including a number", background="white")
        LabelWidget3.place(x=375, y=430)
        Label_PW_Rool.place(x=475, y=450)
        display3 = tk.Entry(self, width=20, textvariable=str3)
        display3.place(x=475, y=430)

        button = tk.Button(self, borderwidth=3, relief="flat", text="\tComplete\t", command=clickMe, fg="white", background="#00b0f0", font=font_Cheack_B)
        button.place(x=475, y=560)


class Find_User_Info(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        image_user = PhotoImage(file="imagefile/KakaoTalk_20200510_195325903.png")
        user_image = Label(self, image=image_user,background="white", borderwidth=0)
        user_image.image = image_user
        user_image.place(x=230, y=120)


        # 아이디 찾기
        display1 = tk.Entry(self, width=20)
        display1.place(x=470, y=232)
        display2 = tk.Entry(self, width=20)
        display2.place(x=470, y=291)

        display3 = tk.Entry(self, width=20)
        display3.place(x=470, y=522)


        button1 = tk.Button(self, text="   Enter   ", command=lambda: controller.show_frame("Find_ID"))
        button1.place(x=720, y=330)
        button2 = tk.Button(self, text="   Enter   ", command=lambda: controller.show_frame("Find_PW"))
        button2.place(x=720, y=567)


class Find_ID(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        # DB에서 E-Mail 반환후 있으면 이거 없으면 오류 출력
        label2 = tk.Label(self, text="등록하신 아이디는... 입니다.", font=controller.title_font, background='white')
        label2.place(x=250, y=300)

        button1 = tk.Button(self, text="    확인    ", command=lambda: controller.show_frame("StartPage"))
        button1.place(x=800, y=500)


class Find_PW(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        # DB에서 E-Mail 반환후 있으면 이거 없으면 오류 출력
        label2 = tk.Label(self, text="임시 비밀번호 ... 이 되었습니다.\n 접속후 PW를 변경해 주세요", font=controller.title_font, background='white')
        label2.place(x=250, y=300)

        button1 = tk.Button(self, text="확인", command=lambda: controller.show_frame("StartPage"))
        button1.place(x=800, y=500)


class Mk_U_Suss(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        # 로그인 성공시 페이지
        image_user = PhotoImage(file="imagefile/Make_User_Successful.png")
        user_image = Label(self, image=image_user,  background="white", borderwidth=0)
        user_image.image = image_user
        user_image.place(x=270, y=130)

        button1 = tk.Button(self, borderwidth=3, relief="flat", text="Move Back", command=lambda: controller.show_frame("StartPage"),fg="white", background="#00b0f0", font=font_Cheack_B)
        button1.place(x=700, y=500)


class ch_U_Suss(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        label2 = tk.Label(self, text="회원정보 변경에 성공했습니다.", font=controller.title_font, background='white')
        label2.place(x=250, y=300)

        button1 = tk.Button(self, text="돌아가기", command=lambda: controller.show_frame("main"))
        button1.place(x=700, y=500)

if __name__ == "__main__":
    app = Apps()
    app.mainloop()
