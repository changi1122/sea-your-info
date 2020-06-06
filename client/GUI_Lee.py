import tkinter as tk
import GUI_get_posts as Gposts
import Create_User
import Login
import Find_User
import Update_User
import Getalluser
from tkinter import ttk
from tkinter import font as tkfont
from tkinter import *
from tkinter import messagebox
import webbrowser

UserInfo = []
User_token = []


class Apps(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=30, weight="bold", slant="italic")
        global font_logintext
        font_logintext = tkfont.Font(family='Helvetica', size=15)
        global font_startpageinfo
        font_startpageinfo = tkfont.Font(family='여기어때 잘난체 OTF', size=18)
        # 여기어때 잘난체 OTF 다른 컴퓨터에서도 잘 작동하는지 확인 필요
        # 없다면 폰트 파일 공유해야할듯
        global FB
        FB = tkfont.Font(family='Helvetica', size=10)
        global font_hypertext
        font_hypertext = tkfont.Font(size=10, underline=True)
        global font_Cheack_B
        font_Cheack_B = tkfont.Font(size=11, weight="bold", family='Helvetica')
        global font_listbox_content
        font_listbox_content = tkfont.Font(size=13, family='휴먼모음T')
        global font_radiobutton
        font_radiobutton = tkfont.Font(size=12, family='바른고딕', weight="bold")

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
                Find_PW, SuperPage, SuperShowUserINFO, SuperChangeListINFO):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


# 시작 페이지
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
            global User_token
            user_ID = str1.get()
            user_PW = str2.get()
            display1.delete(0, tk.END)
            display3.delete(0, tk.END)
            Lg = Login.Login(user_ID, user_PW)
            Lg.Check(User_token)
            print(User_token)
            if User_token[0] == 1:
                controller.show_frame("SuperPage")
            elif User_token[1] == 200:
                controller.show_frame("main")
            else:
                txt = ""
                for i in range(2, len(User_token)):
                    txt += User_token[i] + '\n'
                User_token = []
                messagebox.showwarning("Error", txt)

        # 비밀번호 별표로 안보이게 가리는 부분
        def toggle_password():
            if checkbutton.var.get():
                display3['show'] = "•"
            else:
                display3['show'] = ""

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
        LabelWidget1 = tk.Label(self, text="ID", background='white', font=font_logintext)
        LabelWidget1.place(x=40, y=240)
        display1 = tk.Entry(self, width=20, textvariable=str1)
        display1.place(x=115, y=245)

        str2 = StringVar()
        LabelWidget3 = tk.Label(self, text="PW", background='white', font=font_logintext)
        LabelWidget3.place(x=40, y=280)
        # bullet = "\u2022"
        # display3 = tk.Entry(self, width=20, textvariable=str2, show=bullet)
        # bullet = "\u2022"
        display3 = tk.Entry(self, width=20, textvariable=str2)
        display3.place(x=115, y=285)

        # 비밀번호 보이게 할 것인지 여부
        display3.default_show_val = display3['show']
        display3['show'] = "•"
        checkbutton = tk.Checkbutton(self, text="Hide password", onvalue=True, offvalue=False, command=toggle_password,
                                     background='white')
        checkbutton.var = tk.BooleanVar(value=True)
        checkbutton['variable'] = checkbutton.var
        checkbutton.place(x=150, y=310)

        log_B = PhotoImage(file='imagefile/OP_button3.png')

        button1 = Button(self, text="처음 오셨나요?", command=lambda: controller.show_frame("Make_User_page"),
                         background='white', borderwidth=0, font=font_hypertext, fg="#0000FF")
        button2 = Button(self, text="아이디와 비밀번호를 잊어버리셨나요?", command=lambda: controller.show_frame("Find_User_Info"),
                         background='white', borderwidth=0, font=font_hypertext, fg="#0000FF")
        button3 = Button(self, borderwidth=3, relief="flat", background='white', command=clickMe, padx=10, pady=10,
                         image=log_B)
        button3.image = log_B  # 이미지 안될 때는 이렇게 재정의 해줘야 함

        # 엔터 누르면 main프레임으로 넘어가는 것 구현
        def onReturn(event):
            value = display1.get()
            clickMe()

        display1.bind("<Return>", onReturn)
        display3.bind("<Return>", onReturn)

        button1.place(x=40, y=570)
        button2.place(x=40, y=590)
        button3.place(x=115, y=380)


# 슈퍼유저 관련 페이지
class SuperPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')

        # 맨 위에 Sea your Info 가 보이는 부분
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)
        global frame_department_notice
        global frame_school_notice
        global type_list
        type_list = []
        # 좌측 상단 user_image(USER라고 크게 적혀져있고 파란색 원 있는 부분) 출력 부분
        image_user = PhotoImage(file="imagefile/user_image.gif")
        user_image = Label(self, image=image_user, borderwidth=0)
        user_image.image = image_user
        user_image.place(x=25, y=120)

        def Logout():  # 로그인 했을때 listbox에 남아있는 ID, PW기록 지우기
            global User_token
            if listbox.size() != 0:
                listbox.delete(0, listbox.size())

            if listbox2.size() != 0:
                listbox2.delete(0, listbox2.size())
            User_token = []  # 유저 정보 저장하는 리스트 초기화
            controller.show_frame("StartPage")

        # 좌측 상단 user_image 바로 오른 쪽에 있는 로그아웃과 회원정보 수정 버튼 부분
        button1 = tk.Button(self, text="로그아웃", command=Logout, borderwidth=0,
                            background='white', font=font_hypertext, fg="#0000FF")
        button1.place(x=145, y=160)
        button2 = tk.Button(self, text="회원정보 관리", command=lambda: controller.show_frame("SuperShowUserINFO"),
                            borderwidth=0, background='white', font=font_hypertext, fg="#0000FF")
        # 유저들이 나오는 페이지로 넘어가는 부분
        button2.place(x=145, y=185)
        button3 = tk.Button(self, text="통계랑 보기", command=lambda: controller.show_frame("SuperShowUserINFO"),
                            borderwidth=0, background='white', font=font_hypertext, fg="#0000FF")
        button3.place(x=145, y=210)
        #TODO 통계량 보기 부분 프레임 추가해야함

        # 라디오 버튼은 사용자가 한개만 선택 가능, 체크박스는 여러게 선택 가능
        self.var0 = IntVar()
        radio_scholar = Checkbutton(self, text="장학금", background='white', font=FB, onvalue=1,
                                    variable=self.var0, command=self.convert)
        # font_radiobutton == FB로, Make_List==M_L로 변경
        radio_scholar.place(x=30, y=290)

        self.var1 = IntVar()
        radio_job = Checkbutton(self, text="대회", background='white', font=FB, onvalue=2, variable=self.var1,
                                command=self.convert)
        radio_job.place(x=130, y=290)

        self.var2 = IntVar()
        radio_event = Checkbutton(self, text="교환학생", background='white', font=FB, onvalue=3, variable=self.var2,
                                  command=self.convert)
        radio_event.place(x=230, y=290)

        self.var3 = IntVar()
        radio_text1 = Checkbutton(self, text="계절수업", background='white', font=FB, onvalue=4, variable=self.var3,
                                  command=self.convert)
        radio_text1.place(x=30, y=360)

        self.var4 = IntVar()
        radio_text2 = Checkbutton(self, text="등록금", background='white', font=FB, onvalue=5, variable=self.var4,
                                  command=self.convert)
        radio_text2.place(x=130, y=360)

        self.var5 = IntVar()
        radio_text3 = Checkbutton(self, text="신입생", background='white', font=FB, onvalue=6, variable=self.var5,
                                  command=self.convert)
        radio_text3.place(x=230, y=360)

        self.var6 = IntVar()
        radio_text4 = Checkbutton(self, text="외국어", background='white', font=FB, onvalue=7,
                                  variable=self.var6, command=self.convert)
        radio_text4.place(x=30, y=430)

        self.var7 = IntVar()
        radio_text5 = Checkbutton(self, text="인턴쉽,채용", background='white', font=FB, onvalue=8,
                                  variable=self.var7, command=self.convert)
        radio_text5.place(x=130, y=430)

        self.var8 = IntVar()
        radio_text6 = Checkbutton(self, text="특강", background='white', font=FB, onvalue=9,
                                  variable=self.var8, command=self.convert)
        radio_text6.place(x=230, y=430)

        self.var9 = IntVar()
        radio_text7 = Checkbutton(self, text="캡스톤", background='white', font=FB, onvalue=10,
                                  variable=self.var9, command=self.convert)
        radio_text7.place(x=30, y=500)

        self.var10 = IntVar()
        radio_text8 = Checkbutton(self, text="이외", background='white', font=FB, onvalue=11,
                                  variable=self.var10, command=self.convert)
        radio_text8.place(x=130, y=500)

        self.var11 = IntVar()
        radio_text9 = Checkbutton(self, text="모두보기", background='white', font=FB, onvalue=12,
                                  variable=self.var11, command=self.convert)
        radio_text9.place(x=230, y=500)

        # 탭 부분 - notebook 이용하면 됨
        notebook_main = ttk.Notebook(self, width=670, height=470, padding=10)
        notebook_main.place(x=330, y=115)

        # 탭 부분 중에서 각 프레임 설정 부분
        # 첫 번째 프레임 설정 부분

        frame_department_notice = Frame(self)
        notebook_main.add(frame_department_notice, text="  학과 공지  ")

        # 두 번째 프레임 설정 부분
        frame_school_notice = Frame(self)
        notebook_main.add(frame_school_notice, text="  학교 공지  ")

        # Updated upstream
        scrollbar = tk.Scrollbar(frame_school_notice)
        scrollbar.pack(side="right", fill="y")
        listbox = tk.Listbox(frame_school_notice, yscrollcommand=scrollbar.set, width=660, height=460,
                             font=font_listbox_content)

        scrollbar2 = tk.Scrollbar(frame_department_notice)
        scrollbar2.pack(side="right", fill="y")
        listbox2 = tk.Listbox(frame_department_notice, yscrollcommand=scrollbar2.set, width=660, height=460,
                              selectmode="extended", font=font_listbox_content)

        def Show_data():
            global type_list
            global url_list, url_list_sw
            # 리스트 박스 1,2에 문자열이 있을 경우 이전 data 삭제
            if listbox.size() != 0:
                listbox.delete(0, listbox.size())

            if listbox2.size() != 0:
                listbox2.delete(0, listbox2.size())

            print(listbox.size())
            global a
            a = []
            global b
            b = []
            Gposts.Get_Department(a)
            Gposts.Get_SW(b)
            # Stashed changes

            txt = ""
            txt_sw = ""
            url_list = []
            url_list_sw = []
            j = 0
            print("-----------")
            print(a)
            print(b)
            print(type_list)
            print("-----------")

            arr1 = []
            arr2 = []
            listbox_order = int(len(a) / 5) + 1

            global cnt
            cnt = 0
            for i in range(0, len(a), 5):
                if a[i + 4] in type_list:
                    cnt += 1

            for i in range(0, len(a), 5):
                # Updated upstream
                if a[i + 4] in type_list:
                    for k in range(i, i + 4):
                        if k % 5 == 3:
                            url_list.append(a[k])
                        elif k % 5 == 0:
                            if cnt - j < 10:  # 이 조건문은 숫자 앞에 0을 붙여 주기 위한 조건문이다.
                                txt += " " + "0" + "0"
                            elif cnt - j < 100:
                                txt += " 0"
                            else:
                                txt += " "
                            # if j < 9:
                            #     txt += " " + "0"
                            # else:
                            #     txt += " "
                            # txt += str(j + 1) + " | "
                            # txt += str(listbox_order - (j + 1)) + " | " #<=안되면 이부분 다시 주석 해제할것 improtatn
                            txt += str(cnt - j) + " | "
                            # listbox_order += 1
                        elif k % 5 != 2:
                            txt += " " + str(a[k]) + " | "
                        else:
                            txt += " " + str(a[k][0:10])
                    # Stashed changes
                    # listbox.insert(j, txt)
                    arr1.append(txt)  # 이 부분에서 listbox에 바로 넣지 않고
                    # arr1에 넣는다. arr1에 넣어서 아래 for문에서 최신 날짜부터 뒤집어서 출력하기 위해서
                    j += 1
                    txt = ""

            for i in range(len(arr1) - 1, -1, -1):
                listbox.insert(j, arr1[i])
                j += 1

            # 여기서부터 b 배열
            global cnt2
            cnt2 = 0
            for i in range(0, len(b), 5):
                if b[i + 4] in type_list:
                    cnt2 += 1

            listbox_order = int(len(b) / 5) + 1
            j = 0
            for i in range(0, len(b), 5):
                # Updated upstream
                if b[i + 4] in type_list:
                    for k in range(i, i + 4):
                        if k % 5 == 3:
                            url_list_sw.append(b[k])
                        elif k % 5 == 0:
                            # if listbox_order - (j + 1) < 10:
                            if cnt2 - j < 10:
                                txt_sw += " " + "0" + "0"
                            # elif listbox_order - (j + 1) < 100:
                            elif cnt2 - j < 100:
                                txt_sw += " 0"
                            else:
                                txt_sw += " "

                            # if j < 9:
                            #     txt_sw += " " + "0"
                            # else:
                            #     txt_sw += " "
                            # txt_sw += str(j + 1) + " | "
                            # txt_sw += str(listbox_order - (j + 1)) + " | "

                            txt_sw += str(cnt2 - j) + " | "
                        elif k % 5 != 2:
                            txt_sw += " " + str(b[k]) + " | "

                        else:
                            txt_sw += " " + str(b[k][0:10])
                    # Stashed changes
                    # listbox2.insert(j, txt_sw)
                    arr2.append(txt_sw)
                    j += 1
                    txt_sw = ""

            j = 0
            for i in range(len(arr2) - 1, -1, -1):
                listbox2.insert(j, arr2[i])
                j += 1

            listbox.pack()
            listbox2.pack()
            print(url_list)
            print(url_list_sw)

            listbox.bind("<Double-Button>", lambda event: openweb(listbox.curselection(), 1))  # 더블클릭 감지하는 코드
            listbox2.bind("<Double-Button>", lambda event: openweb(listbox2.curselection(), 2))

            scrollbar["command"] = listbox.yview
            scrollbar["command"] = listbox2.yview

        # url_list에 DB에서 가져온 순서대로 append후, listbox.curselection()이 클릭한 위치의 정보를 튜플로 반환하므로, 그에 첫번째 인덱스인 0,1,2,와 같은 값만 받아 그에 해당하는 URL을 리스트에서 찾아 여는 방식

        def openweb(Data, sep):
            # 이부분에 스토리 보드와 같이 정보수정으로 넘어가는 페이지 구현 필요
            global url_list, url_list_sw
            url = Data[0]
            if sep == 1:
                # url = int(len(a) / 5) - 1 - url
                url = cnt - 1 - url
            else:
                # url = int(len(b) / 5) - 1 - url
                url = cnt2 - 1 - url

            controller.show_frame("SuperChangeListINFO")

        def Delet_data():
            listbox.pack()
            listbox2.pack()
            Show_data()

        # Stashed changes
        # DB에서 가져온 data를 학교 공지사항, sw 공지사항 별로 저장할 함수

        button = tk.Button(self, borderwidth=3, relief="flat", text="  Enter  ", fg="white",
                           background="#00b0f0", font=font_Cheack_B, command=Delet_data)
        button.place(x=230, y=560)

    # cheack box 버튼을 통해 버튼이 선택되면 해당값 -1 의 인덱스 값에 해당하는 문자열 저장
    def convert(self):
        global type_list
        title = ["scholarship", "contest", "exchange", "vacation", "tuition", "freshman",
                 "foreign", "job", "lecture", "capstone", "other"]

        type_list = []
        if self.var0.get() == 1:
            type_list.append(title[self.var0.get() - 1])
        if self.var1.get() == 2:
            type_list.append(title[self.var1.get() - 1])
        if self.var2.get() == 3:
            type_list.append(title[self.var2.get() - 1])
        if self.var3.get() == 4:
            type_list.append(title[self.var3.get() - 1])
        if self.var4.get() == 5:
            type_list.append(title[self.var4.get() - 1])
        if self.var5.get() == 6:
            type_list.append(title[self.var5.get() - 1])
        if self.var6.get() == 7:
            type_list.append(title[self.var6.get() - 1])
        if self.var7.get() == 8:
            type_list.append(title[self.var7.get() - 1])
        if self.var8.get() == 9:
            type_list.append(title[self.var8.get() - 1])
        if self.var9.get() == 10:
            type_list.append(title[self.var9.get() - 1])
        if self.var10.get() == 11:
            type_list.append(title[self.var10.get() - 1])
        if self.var11.get() == 12:
            for i in range(0, 11):
                type_list.append(title[i])

        print(type_list)


# joong
# 슈퍼유저가 회원정보 관리 창을 눌렀을 때 나오는 부분
class SuperShowUserINFO(tk.Frame):  # 스토리 보드상 가입된 유저 목록 출력하는 화면 부분
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        image_user = PhotoImage(file="imagefile/user_image.gif")
        user_image = Label(self, image=image_user, borderwidth=0)
        user_image.image = image_user
        user_image.place(x=25, y=120)

        # 밑에 추가로 구현 필요
        notebook_main = ttk.Notebook(self, width=670, height=470, padding=10)
        notebook_main.place(x=330, y=115)

        userpage = Frame(self)
        notebook_main.add(userpage, text="  유저 정보  ")

        scrollbar = tk.Scrollbar(userpage)
        scrollbar.pack(side="right", fill="y")
        listbox = tk.Listbox(userpage, yscrollcommand=scrollbar.set, width=660, height=460,
                             font=font_listbox_content)

        image_back = PhotoImage(file='imagefile/OP_button3_back.png')
        button_back = tk.Button(self, borderwidth=3, relief="flat", background='white',
                                command=lambda: controller.show_frame("SuperPage"), padx=10, pady=10, image=image_back)
        button_back.image = image_back
        button_back.place(x=25, y=550)

        a = []
        userlist = []
        newuserlist = []
        # print("--------------")
        userlist = Getalluser.Getuser.Getuser(a)
        # print(userlist)
        # print("--------------")
        # for i in range(len(userlist)):
        #     if i % 5 == 0:
        #         print()
        #     print(userlist[i])
        # print(len(userlist))

        k = 0
        subcnt = 0
        for i in range(0, len(userlist), 5):
            string = " " + str(k + 1) + ""
            for j in range(i, i + 5):
                if userlist[j] == "none" or j % 5 == 0:
                    continue
                else:
                    string += " | " + str(userlist[j])
                if userlist[j] == True:#만약 구독을 한 사람이라면 subcnt+=1해준다.
                    subcnt += 1
                # newuserlist.append(userlist[j])
            newuserlist.append(string)
            print(newuserlist[k])
            listbox.insert(k, newuserlist[k])
            k += 1
        category = "CATEGORY => number | ID | E-Mail | Subscribed or not"
        listbox.insert(0, category)
        listbox.pack()

        registered = tk.Label(self, text="총 가입인원 수 : " + str(k), font=font_startpageinfo, background='white')
        registered.place(x=30, y=400)
        subscribed = tk.Label(self, text="총 구독자 수 : " + str(subcnt), font=font_startpageinfo, background='white')
        subscribed.place(x=30, y=440)

        # button1 = Button(self, text="type별 검색 통계량 보기", command=lambda: controller.show_frame("Make_User_page"),
        #                  # TODO 이거 make user page로 넘어가면 안되고 통계량 보는 새로운 frame만들어줘야한다.
        #                  background='white', borderwidth=0, font=font_hypertext, fg="#0000FF")
        #button1.place(x=30, y=280)


class SuperChangeListINFO(tk.Frame):  # 스토리 보드상 리스트의 항복 변경하는 부분
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)
        # 밑에 추가로 구현 필요

        image_back = PhotoImage(file='imagefile/OP_button3_back.png')
        button_back = tk.Button(self, borderwidth=3, relief="flat", background='white',
                                command=lambda: controller.show_frame("SuperPage"), padx=10, pady=10, image=image_back)
        button_back.image = image_back
        button_back.place(x=25, y=550)  # 뒤로가기버튼


# DB쪽 put-post사용해야함, 이거는 제가 구현 할께요 - 김성욱 ( ㅇ우창ㅇ이랑 얘기가 필요해요 )

# 일반 유져 관련 페이지
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
        global type_list
        type_list = []
        # 좌측 상단 user_image(USER라고 크게 적혀져있고 파란색 원 있는 부분) 출력 부분
        image_user = PhotoImage(file="imagefile/user_image.gif")
        user_image = Label(self, image=image_user, borderwidth=0)
        user_image.image = image_user
        user_image.place(x=25, y=120)

        def Logout():  # 로그인 했을때 listbox에 남아있는 ID, PW기록 지우기
            global User_token
            if listbox.size() != 0:
                listbox.delete(0, listbox.size())

            if listbox2.size() != 0:
                listbox2.delete(0, listbox2.size())
            User_token = []  # 유저 정보 저장하는 리스트 초기화
            controller.show_frame("StartPage")

        # 좌측 상단 user_image 바로 오른 쪽에 있는 로그아웃과 회원정보 수정 버튼 부분
        button1 = tk.Button(self, text="로그아웃", command=Logout, borderwidth=0,
                            background='white', font=font_hypertext, fg="#0000FF")
        button1.place(x=145, y=160)
        button2 = tk.Button(self, text="회원정보 수정", command=lambda: controller.show_frame("Change_User_Info"),
                            borderwidth=0, background='white', font=font_hypertext, fg="#0000FF")
        button2.place(x=145, y=185)

        # 라디오 버튼은 사용자가 한개만 선택 가능, 체크박스는 여러게 선택 가능
        self.var0 = IntVar()
        radio_scholar = Checkbutton(self, text="장학금", background='white', font=FB, onvalue=1,
                                    variable=self.var0, command=self.convert)
        # font_radiobutton == FB로, Make_List==M_L로 변경
        radio_scholar.place(x=30, y=290)

        self.var1 = IntVar()
        radio_job = Checkbutton(self, text="대회", background='white', font=FB, onvalue=2, variable=self.var1,
                                command=self.convert)
        radio_job.place(x=130, y=290)

        self.var2 = IntVar()
        radio_event = Checkbutton(self, text="교환학생", background='white', font=FB, onvalue=3, variable=self.var2,
                                  command=self.convert)
        radio_event.place(x=230, y=290)

        self.var3 = IntVar()
        radio_text1 = Checkbutton(self, text="계절수업", background='white', font=FB, onvalue=4, variable=self.var3,
                                  command=self.convert)
        radio_text1.place(x=30, y=360)

        self.var4 = IntVar()
        radio_text2 = Checkbutton(self, text="등록금", background='white', font=FB, onvalue=5, variable=self.var4,
                                  command=self.convert)
        radio_text2.place(x=130, y=360)

        self.var5 = IntVar()
        radio_text3 = Checkbutton(self, text="신입생", background='white', font=FB, onvalue=6, variable=self.var5,
                                  command=self.convert)
        radio_text3.place(x=230, y=360)

        self.var6 = IntVar()
        radio_text4 = Checkbutton(self, text="외국어", background='white', font=FB, onvalue=7,
                                  variable=self.var6, command=self.convert)
        radio_text4.place(x=30, y=430)

        self.var7 = IntVar()
        radio_text5 = Checkbutton(self, text="인턴쉽,채용", background='white', font=FB, onvalue=8,
                                  variable=self.var7, command=self.convert)
        radio_text5.place(x=130, y=430)

        self.var8 = IntVar()
        radio_text6 = Checkbutton(self, text="특강", background='white', font=FB, onvalue=9,
                                  variable=self.var8, command=self.convert)
        radio_text6.place(x=230, y=430)

        self.var9 = IntVar()
        radio_text7 = Checkbutton(self, text="캡스톤", background='white', font=FB, onvalue=10,
                                  variable=self.var9, command=self.convert)
        radio_text7.place(x=30, y=500)

        self.var10 = IntVar()
        radio_text8 = Checkbutton(self, text="이외", background='white', font=FB, onvalue=11,
                                  variable=self.var10, command=self.convert)
        radio_text8.place(x=130, y=500)

        self.var11 = IntVar()
        radio_text9 = Checkbutton(self, text="모두보기", background='white', font=FB, onvalue=12,
                                  variable=self.var11, command=self.convert)
        radio_text9.place(x=230, y=500)

        # 탭 부분 - notebook 이용하면 됨
        notebook_main = ttk.Notebook(self, width=670, height=470, padding=10)
        notebook_main.place(x=330, y=115)

        # 탭 부분 중에서 각 프레임 설정 부분
        # 첫 번째 프레임 설정 부분

        frame_department_notice = Frame(self)
        notebook_main.add(frame_department_notice, text="  학과 공지  ")

        # 두 번째 프레임 설정 부분
        frame_school_notice = Frame(self)
        notebook_main.add(frame_school_notice, text="  학교 공지  ")

        # Updated upstream
        scrollbar = tk.Scrollbar(frame_school_notice)
        scrollbar.pack(side="right", fill="y")
        listbox = tk.Listbox(frame_school_notice, yscrollcommand=scrollbar.set, width=660, height=460,
                             font=font_listbox_content)

        scrollbar2 = tk.Scrollbar(frame_department_notice)
        scrollbar2.pack(side="right", fill="y")
        listbox2 = tk.Listbox(frame_department_notice, yscrollcommand=scrollbar2.set, width=660, height=460,
                              selectmode="extended", font=font_listbox_content)

        def Show_data():
            global type_list
            global url_list, url_list_sw
            # 리스트 박스 1,2에 문자열이 있을 경우 이전 data 삭제
            if listbox.size() != 0:
                listbox.delete(0, listbox.size())

            if listbox2.size() != 0:
                listbox2.delete(0, listbox2.size())

            print(listbox.size())
            global a
            a = []
            global b
            b = []
            Gposts.Get_Department(a)
            Gposts.Get_SW(b)
            # Stashed changes

            txt = ""
            txt_sw = ""
            url_list = []
            url_list_sw = []
            j = 0
            print("-----------")
            print(a)
            print(b)
            print(type_list)
            print("-----------")

            arr1 = []
            arr2 = []
            listbox_order = int(len(a) / 5) + 1

            global cnt
            cnt = 0
            for i in range(0, len(a), 5):
                if a[i + 4] in type_list:
                    cnt += 1

            for i in range(0, len(a), 5):
                # Updated upstream
                if a[i + 4] in type_list:
                    for k in range(i, i + 4):
                        if k % 5 == 3:
                            url_list.append(a[k])
                        elif k % 5 == 0:
                            if cnt - j < 10:  # 이 조건문은 숫자 앞에 0을 붙여 주기 위한 조건문이다.
                                txt += " " + "0" + "0"
                            elif cnt - j < 100:
                                txt += " 0"
                            else:
                                txt += " "
                            # if j < 9:
                            #     txt += " " + "0"
                            # else:
                            #     txt += " "
                            # txt += str(j + 1) + " | "
                            # txt += str(listbox_order - (j + 1)) + " | " #<=안되면 이부분 다시 주석 해제할것 improtatn
                            txt += str(cnt - j) + " | "
                            # listbox_order += 1
                        elif k % 5 != 2:
                            txt += " " + str(a[k]) + " | "
                        else:
                            txt += " " + str(a[k][0:10])
                    # Stashed changes
                    # listbox.insert(j, txt)
                    arr1.append(txt)  # 이 부분에서 listbox에 바로 넣지 않고
                    # arr1에 넣는다. arr1에 넣어서 아래 for문에서 최신 날짜부터 뒤집어서 출력하기 위해서
                    j += 1
                    txt = ""

            for i in range(len(arr1) - 1, -1, -1):
                listbox.insert(j, arr1[i])
                j += 1

            # 여기서부터 b 배열
            global cnt2
            cnt2 = 0
            for i in range(0, len(b), 5):
                if b[i + 4] in type_list:
                    cnt2 += 1

            listbox_order = int(len(b) / 5) + 1
            j = 0
            for i in range(0, len(b), 5):
                # Updated upstream
                if b[i + 4] in type_list:
                    for k in range(i, i + 4):
                        if k % 5 == 3:
                            url_list_sw.append(b[k])
                        elif k % 5 == 0:
                            # if listbox_order - (j + 1) < 10:
                            if cnt2 - j < 10:
                                txt_sw += " " + "0" + "0"
                            # elif listbox_order - (j + 1) < 100:
                            elif cnt2 - j < 100:
                                txt_sw += " 0"
                            else:
                                txt_sw += " "

                            # if j < 9:
                            #     txt_sw += " " + "0"
                            # else:
                            #     txt_sw += " "
                            # txt_sw += str(j + 1) + " | "
                            # txt_sw += str(listbox_order - (j + 1)) + " | "

                            txt_sw += str(cnt2 - j) + " | "
                        elif k % 5 != 2:
                            txt_sw += " " + str(b[k]) + " | "

                        else:
                            txt_sw += " " + str(b[k][0:10])
                    # Stashed changes
                    # listbox2.insert(j, txt_sw)
                    arr2.append(txt_sw)
                    j += 1
                    txt_sw = ""

            j = 0
            for i in range(len(arr2) - 1, -1, -1):
                listbox2.insert(j, arr2[i])
                j += 1

            listbox.pack()
            listbox2.pack()
            print(url_list)
            print(url_list_sw)

            listbox.bind("<Double-Button>", lambda event: openweb(listbox.curselection(), 1))  # 더블클릭 감지하는 코드
            listbox2.bind("<Double-Button>", lambda event: openweb(listbox2.curselection(), 2))

            scrollbar["command"] = listbox.yview
            scrollbar["command"] = listbox2.yview

        # url_list에 DB에서 가져온 순서대로 append후, listbox.curselection()이 클릭한 위치의 정보를 튜플로 반환하므로, 그에 첫번째 인덱스인 0,1,2,와 같은 값만 받아 그에 해당하는 URL을 리스트에서 찾아 여는 방식

        def openweb(Data, sep):
            global url_list, url_list_sw
            url = Data[0]
            if sep == 1:
                # url = int(len(a) / 5) - 1 - url
                url = cnt - 1 - url
                webbrowser.open(url_list[url])
            else:
                # url = int(len(b) / 5) - 1 - url
                url = cnt2 - 1 - url
                webbrowser.open(url_list_sw[url])

            image_back = PhotoImage(file='imagefile/OP_button3_back.png')
            button_back = tk.Button(self, borderwidth=3, relief="flat", background='white',
                                    command=Empty, padx=10, pady=10, image=image_back)
            button_back.image = image_back
            button_back.place(x=170, y=570)

        def Delet_data():
            listbox.pack()
            listbox2.pack()
            Show_data()

        # Stashed changes
        # DB에서 가져온 data를 학교 공지사항, sw 공지사항 별로 저장할 함수

        button = tk.Button(self, borderwidth=3, relief="flat", text="  Enter  ", fg="white",
                           background="#00b0f0", font=font_Cheack_B, command=Delet_data)
        button.place(x=230, y=560)

    # cheack box 버튼을 통해 버튼이 선택되면 해당값 -1 의 인덱스 값에 해당하는 문자열 저장
    def convert(self):
        global type_list
        title = ["scholarship", "contest", "exchange", "vacation", "tuition", "freshman",
                 "foreign", "job", "lecture", "capstone", "other"]

        type_list = []
        if self.var0.get() == 1:
            type_list.append(title[self.var0.get() - 1])
        if self.var1.get() == 2:
            type_list.append(title[self.var1.get() - 1])
        if self.var2.get() == 3:
            type_list.append(title[self.var2.get() - 1])
        if self.var3.get() == 4:
            type_list.append(title[self.var3.get() - 1])
        if self.var4.get() == 5:
            type_list.append(title[self.var4.get() - 1])
        if self.var5.get() == 6:
            type_list.append(title[self.var5.get() - 1])
        if self.var6.get() == 7:
            type_list.append(title[self.var6.get() - 1])
        if self.var7.get() == 8:
            type_list.append(title[self.var7.get() - 1])
        if self.var8.get() == 9:
            type_list.append(title[self.var8.get() - 1])
        if self.var9.get() == 10:
            type_list.append(title[self.var9.get() - 1])
        if self.var10.get() == 11:
            type_list.append(title[self.var10.get() - 1])
        if self.var11.get() == 12:
            for i in range(0, 11):
                type_list.append(title[i])

        print(type_list)


class Make_User_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')

        global display3, checkbutton

        def clickMe():
            string = []
            user_ID = str1.get()
            user_Email = str2.get()
            user_PW = str3.get()
            Mk = Create_User.Make_user(user_ID, user_Email, user_PW)
            Mk.make(string)
            print(string)
            if string[0] == 201:
                display1.delete(0, tk.END)  # 엔트리에 있는 정보 삭제
                display2.delete(0, tk.END)
                display3.delete(0, tk.END)
                controller.show_frame("Mk_U_Suss")
            else:
                txt = ""
                for i in range(1, len(string)):
                    txt += string[i] + '\n'
                messagebox.showwarning(
                    "Error", txt)

        def Error_Messagebox():  # 비밀번호가 조건에 맞지 않을 때 띄우는 에러
            messagebox.showinfo("에러", "ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n| 비밀번호 조건을 다시 확인해 주세요.  |\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

        def Error_Fill():  # 창에 값이 모두 입력되지 않았을 때 띄우는 에러
            messagebox.showinfo("Error", "Please fill out all of the spaces.")

        def button_hit():  # Sign up for SYI 눌렸을 때 반응하는 함수
            # 암호가 조건에 맞는지 확인하는 것
            chk_pw = str3.get()
            chk = True
            sum = 0
            for i in range(len(chk_pw)):
                if 'a' <= chk_pw[i] <= 'z' or 'A' <= chk_pw[i] <= 'Z':  # 암호가 모두 알파벳으로 돼 있다면
                    sum += 1
            if sum is len(chk_pw):
                chk = False  # False로 바꿈
            if len(chk_pw) < 8 or len(chk_pw) >= 15:  # 비밀번호의 길이가 8자 미만이거나 15자 이상이면 안된다.
                chk = False
            if chk is False:
                display3.delete(0, tk.END)
                Error_Messagebox()
            elif chk is True:
                clickMe()

        def on_enter(event):
            label2.configure(text="Make it at least 8 characters.\nMake it at most 15 characters.\nAdd punctuation.")

        def on_leave(event):
            label2.configure(text="")

        # 비밀번호 별표로 안보이게 가리는 부분
        def toggle_password():
            if checkbutton.var.get():
                display3['show'] = "•"
            else:
                display3['show'] = ""

        # 회원가입 뒤 배경 추가
        image_user = PhotoImage(file="imagefile/OP_make_user.png")
        user_image = Label(self, image=image_user, borderwidth=0)
        user_image.image = image_user
        user_image.place(x=230, y=120)

        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        label2 = tk.Label(self, text="회원가입", background='white', font=font_startpageinfo)
        label2.place(x=375, y=230)

        str1 = StringVar()
        LabelWidget1 = tk.Label(self, text="ID(user name)", background='white', font=FB)
        LabelWidget1.place(x=375, y=290)
        display1 = tk.Entry(self, width=20, textvariable=str1)
        display1.place(x=475, y=290)

        str2 = StringVar()
        LabelWidget2 = tk.Label(self, text="E-mail", background='white', font=FB)
        LabelWidget2.place(x=375, y=360)
        display2 = tk.Entry(self, width=20, textvariable=str2)
        display2.place(x=475, y=360)

        str3 = StringVar()
        LabelWidget3 = tk.Label(self, text="Password", background='white', font=FB)
        # Label_PW_Rool = tk.Label(self,
        #                          text="Make sure it's at least 15 characters OR \nat lest 8 characters including a number",
        #                          background="white")
        LabelWidget3.place(x=375, y=430)
        # Label_PW_Rool.place(x=475, y=450)
        display3 = tk.Entry(self, width=20, textvariable=str3)
        display3.place(x=475, y=430)

        # button = tk.Button(self, borderwidth=3, relief="flat", text="Sign up for Sea Your Info",
        #                        command=clickMe,
        #                        fg="white", background="#00b0f0", font=font_Cheack_B)
        # button.place(x=475, y=560)

        # 물음표 이미지 띄우는 부분
        que_image = PhotoImage(file='imagefile/questionmarkimage.gif')
        label_Queimage = tk.Label(self, image=que_image, borderwidth=0)
        label_Queimage.image = que_image
        label_Queimage.place(x=595, y=450)

        label2 = tk.Label(self, text="", width=0, background='white')
        label2.place(x=620, y=450)

        label_Queimage.bind("<Enter>", on_enter)
        label_Queimage.bind("<Leave>", on_leave)

        display3.default_show_val = display3['show']
        display3['show'] = "•"
        checkbutton = tk.Checkbutton(self, text="Hide password", onvalue=True, offvalue=False, command=toggle_password,
                                     background='white')
        checkbutton.var = tk.BooleanVar(value=True)
        checkbutton['variable'] = checkbutton.var
        checkbutton.place(x=620, y=428)

        button = tk.Button(self, borderwidth=3, relief="flat", text="Sign up for Sea Your Info",
                           command=button_hit,
                           fg="white", background="#00b0f0", font=font_Cheack_B)
        button.place(x=475, y=560)

        image_back = PhotoImage(file='imagefile/OP_button3_back.png')
        button_back = tk.Button(self, borderwidth=3, relief="flat", background='white',
                                command=lambda: controller.show_frame("StartPage"), padx=10, pady=10, image=image_back)
        button_back.image = image_back
        button_back.place(x=235, y=550)


class Change_User_Info(tk.Frame):

    def __init__(self, parent, controller):
        global User_token
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        def clickMe():
            message = []
            # messagebox.showinfo("Button CLicked", str1.get())
            # messagebox.showinfo("Button CLicked", str2.get())
            # messagebox.showinfo("Button CLicked", str3.get())
            print(User_token[2])
            CH = Update_User.Update_User(str1.get(), str2.get(), str3.get(), str4.get(), User_token[2])
            CH.UUD_INFO(message)
            print(message)
            display1.delete(0, tk.END)
            display2.delete(0, tk.END)
            display3.delete(0, tk.END)
            display4.delete(0, tk.END)
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
        LabelWidget1 = tk.Label(self, text="ID", background='white', font=FB)
        LabelWidget1.place(x=375, y=290)
        display1 = tk.Entry(self, width=20, textvariable=str1)
        display1.place(x=475, y=290)

        str2 = StringVar()
        LabelWidget2 = tk.Label(self, text="Email", background='white', font=FB)
        LabelWidget2.place(x=375, y=350)
        display2 = tk.Entry(self, width=20, textvariable=str2)
        display2.place(x=475, y=350)

        # 비밀번호 별표로 안보이게 가리는 부분
        def toggle_password():
            if checkbutton1.var.get():
                display3['show'] = "•"
            else:
                display3['show'] = ""

            if checkbutton2.var.get():
                display4['show'] = "•"
            else:
                display4['show'] = ""

        str3 = StringVar()
        LabelWidget3 = tk.Label(self, text="Password", background='white', font=FB)
        LabelWidget3.place(x=375, y=410)
        display3 = tk.Entry(self, width=20, textvariable=str3)
        display3.place(x=475, y=410)
        # 비번 안보이게 하는 부분
        display3.default_show_val = display3['show']
        display3['show'] = "•"
        checkbutton1 = tk.Checkbutton(self, text="Hide password", onvalue=True, offvalue=False, command=toggle_password,
                                      background='white')
        checkbutton1.var = tk.BooleanVar(value=True)
        checkbutton1['variable'] = checkbutton1.var
        checkbutton1.place(x=620, y=405)

        str4 = StringVar()
        LabelWidget4 = tk.Label(self, text="New_Password", background='white', font=FB)
        LabelWidget4.place(x=375, y=470)
        display4 = tk.Entry(self, width=20, textvariable=str4)
        display4.place(x=475, y=470)

        # 비번 안보이게 하는 부분
        display4.default_show_val = display4['show']
        display4['show'] = "•"
        checkbutton2 = tk.Checkbutton(self, text="Hide password", onvalue=True, offvalue=False, command=toggle_password,
                                      background='white')
        checkbutton2.var = tk.BooleanVar(value=True)
        checkbutton2['variable'] = checkbutton2.var
        checkbutton2.place(x=620, y=465)

        def Error_Messagebox():  # 비밀번호가 조건에 맞지 않을 때 띄우는 에러
            messagebox.showinfo("에러", "ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n| 다시 확인해 주세요. |\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")  # 메시지 다시 만들기

        # 비번 조건 확인
        def button_hit():  # Sign up for SYI 눌렸을 때 반응하는 함수
            # 암호가 조건에 맞는지 확인하는 것
            chk_pw = str4.get()
            chk = True
            sum = 0
            for i in range(len(chk_pw)):
                if 'a' <= chk_pw[i] <= 'z' or 'A' <= chk_pw[i] <= 'Z':  # 암호가 모두 알파벳으로 돼 있다면
                    sum += 1
            if sum is len(chk_pw):
                chk = False  # False로 바꿈
            if len(chk_pw) < 8 or len(chk_pw) >= 15:  # 비밀번호의 길이가 8자 미만이거나 15자 이상이면 안된다.
                chk = False
            if chk is False:
                display4.delete(0, tk.END)
                Error_Messagebox()
            elif chk is True:
                clickMe()

        # 물음표 이미지 띄우는 부분
        def on_enter(event):
            label5.configure(text="Make it at least 8 characters.\nMake it at most 15 characters.\nAdd punctuation.")

        def on_leave(event):
            label5.configure(text="")

        que_image = PhotoImage(file='imagefile/questionmarkimage.gif')
        label_Queimage = tk.Label(self, image=que_image, borderwidth=0)
        label_Queimage.image = que_image
        label_Queimage.place(x=600, y=490)

        label5 = tk.Label(self, text="", width=0, background='white')
        label5.place(x=625, y=490)

        label_Queimage.bind("<Enter>", on_enter)
        label_Queimage.bind("<Leave>", on_leave)

        button = tk.Button(self, borderwidth=3, relief="flat", text="\tComplete\t", command=button_hit, fg="white",
                           background="#00b0f0", font=font_Cheack_B)
        button.place(x=475, y=560)

        def Empty():
            global User_token
            User_token = []
            controller.show_frame("main")

        image_back = PhotoImage(file='imagefile/OP_button3_back.png')
        button_back = tk.Button(self, borderwidth=3, relief="flat", background='white',
                                command=Empty, padx=10, pady=10, image=image_back)
        button_back.image = image_back
        button_back.place(x=235, y=550)


class Find_User_Info(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        image_user = PhotoImage(file="imagefile/OP_FIND_PWID2.png")
        user_image = Label(self, image=image_user, background="white", borderwidth=0)
        user_image.image = image_user
        user_image.place(x=230, y=115)

        # 아이디 찾기
        FU_ID_Email = StringVar()
        display1 = tk.Entry(self, width=20, textvariable=FU_ID_Email)
        display1.place(x=470, y=227)
        # 비번 찾기
        FU_PW_ID = StringVar()
        display2 = tk.Entry(self, width=20, textvariable=FU_PW_ID)
        display2.place(x=470, y=457)
        FU_PW_Email = StringVar()
        display3 = tk.Entry(self, width=20, textvariable=FU_PW_Email)
        display3.place(x=470, y=517)

        def Call_OR1():
            Email = FU_ID_Email.get()
            Delet()
            self.onReturn1(Email)

        def Call_OR2():
            ID = FU_PW_ID.get()
            Email = FU_PW_Email.get()
            Delet()
            self.onReturn23(ID, Email)

        button1 = tk.Button(self, text="   Enter   ", command=lambda: Call_OR1())
        button1.place(x=720, y=270)
        button2 = tk.Button(self, text="   Enter   ", command=lambda: Call_OR2())
        button2.place(x=720, y=557)

        def Delet():
            display1.delete(0, tk.END)
            display2.delete(0, tk.END)
            display3.delete(0, tk.END)

        def Empty():
            global UserInfo
            UserInfo = []
            Delet()
            controller.show_frame("StartPage")

        image_back = PhotoImage(file='imagefile/OP_button3_back.png')
        button_back = tk.Button(self, borderwidth=3, relief="flat", background='white',
                                command=Empty, padx=10, pady=10, image=image_back)
        button_back.image = image_back
        button_back.place(x=170, y=570)

        # 아이디찾기 부분에서 enter눌렀을 때 작동해야 하는 함수

        # PW찾기 부분에서 etner눌렀을때 작동해야 하는 함수

    def onReturn23(self, PW_id, PW_Email):
        global UserInfo
        self.controller.show_frame("Find_PW")
        FU_PW = Find_User.Find_User(PW_id, PW_Email)
        FU_PW.find_PW(UserInfo)

        self.controller.show_frame("Find_PW")
        # clickMe() clickme처럼 이곳에 작동해야 하는 함수 추가하면 됨

    def onReturn1(self, ID_Email):
        global UserInfo
        FU_ID = Find_User.Find_User(None, ID_Email)
        FU_ID.find_ID(UserInfo)
        print(1111111111)
        self.controller.show_frame("Find_ID")


class Find_ID(tk.Frame):
    def __init__(self, parent, controller):
        global UserInfo
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')

        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        def Show(event):
            print('event happen')
            if UserInfo:
                print(11111111111)
                print(UserInfo)
                if UserInfo[0] != 'None':
                    print(22222222)
                    label2 = tk.Label(self, text="등록하신 아이디는 %s 입니다." % (UserInfo[0]), font=controller.title_font,
                                      background='white')
                    label2.place(x=250, y=300)
                else:
                    label3 = tk.Label(self, text="   유저가 존제하지 않습니다                       ", font=controller.title_font,
                                      background='white')
                    label3.place(x=250, y=300)

        _widget = tk.LabelFrame(self, bg='white', bd=0)  # 화면에 user의 아이디 혹은 존제하지 않음을 출력하기 위해 사용하는 Event를 사용하기 위해 추가
        _widget.pack(fill=BOTH, expand=1)
        _widget.bind("<Enter>", Show)

        # DB에서 E-Mail 반환후 있으면 이거 없으면 오류 출력

        def Empty():
            global UserInfo
            UserInfo = []
            controller.show_frame("StartPage")

        button1 = tk.Button(self, text="    확인    ", command=Empty)
        button1.place(x=800, y=500)


class Find_PW(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        def Show(event):
            print('event happen')
            if UserInfo:
                print(11111111111)
                print(UserInfo)
                if UserInfo[0] != 'None':
                    print(22222222)
                    label2 = tk.Label(self, text="임시 비밀번호가 발급되었습니다.\n 접속후 PW를 변경해 주세요\n 임시비밀번호 : %s" % (UserInfo[0]),
                                      font=controller.title_font,
                                      background='white')
                    label2.place(x=250, y=300)
                else:
                    label2 = tk.Label(self, text="유저가 존제하지 않습니다", font=controller.title_font,
                                      background='white')
                    label2.place(x=250, y=300)

        _widget = tk.LabelFrame(self, bg='white', bd=0)  # 화면에 user의 아이디 혹은 존제하지 않음을 출력하기 위해 사용하는 Event를 사용하기 위해 추가
        _widget.pack(fill=BOTH, expand=1)
        _widget.bind("<Enter>", Show)

        # DB에서 E-Mail 반환후 있으면 이거 없으면 오류 출력

        def Empty():
            global UserInfo
            UserInfo = []
            controller.show_frame("StartPage")

        # DB에서 E-Mail 반환후 있으면 이거 없으면 오류 출력
        button1 = tk.Button(self, text="    확인     ", command=Empty)
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
        user_image = Label(self, image=image_user, background="white", borderwidth=0)
        user_image.image = image_user
        user_image.place(x=270, y=130)

        button1 = tk.Button(self, borderwidth=3, relief="flat", text="Move Back",
                            command=lambda: controller.show_frame("StartPage"), fg="white", background="#00b0f0",
                            font=font_Cheack_B)
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

        def Empty():
            global User_token
            User_token = []
            controller.show_frame("main")

        button1 = tk.Button(self, text="돌아가기", command=Empty)
        button1.place(x=700, y=500)


if __name__ == "__main__":
    app = Apps()
    app.mainloop()
