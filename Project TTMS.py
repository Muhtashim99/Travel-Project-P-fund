from tkinter import *
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
import webbrowser 

def get_details():
    global username 
    global password 
    username=[]
    password=[] 
    get= username_entry1.get()
    username.append(get)
    pass1= password_entry1.get()
    password.append(pass1)
    print(username)
    print(password) 

def signup1():
    global username_entry1
    global password_entry1
    global signwin
    signwin=Tk()
    signwin.geometry('720x720')
    signwin.title("Signup")
    signwin.config(background="#FAF3E0")

    signup_label = Label(signwin, 
                        text="Sign-Up", 
                        bg='#FAF3E0', 
                        fg="#193452", 
                        font=("Provicali", 50))  
    signup_label.place(x=270,y=50)

    email_label1 =Label(signwin, 
                          text="Email", 
                          bg='#FAF3E0', 
                          fg="#193452", 
                          font=("Provicali", 28))
    email_label1.place(x=20,y=190)

    email_entry1 = Entry(signwin, 
                           font=("Arial", 28))
    email_entry1.place(x=220,y=190)



    username_label1 =Label(signwin, 
                          text="Username", 
                          bg='#FAF3E0', 
                          fg="#193452", 
                          font=("Provicali", 28))
    username_label1.place(x=20,y=290)

    username_entry1 = Entry(signwin, 
                           font=("Arial", 28))
    username_entry1.place(x=220,y=290)

    password_label1 = Label(signwin, 
                           text="Password", 
                           bg='#FAF3E0', 
                           fg="#193452", 
                           font=("Provicali", 28))
    password_label1.place(x=20,y=390)

    password_entry1 = Entry(signwin,
                           show="*", 
                           font=("Arial", 28))
    password_entry1.place(x=220,y=390) 
    signup_button1 = Button(signwin, 
                          text="REGISTER", 
                          font=("lemondays",19),
                          width=10,
                          height=1,
                          bg='#193452',
                          fg="white",
                          activeforeground="white",
                          activebackground="#193452",
                          cursor="hand2",
                          command=combined,)
    signup_button1.place(x=330,y=490)
    
    signwin.mainloop()

def signfunc():
    messagebox.showinfo(title="Signup Success", 
                        message="You successfully Signed Up.Now you can login")
    signwin.withdraw() 

def combined():
    signfunc()
    get_details()

def login1():
    global username_entry
    global password_entry
    global logwin
    logwin=Tk()
    logwin.geometry('720x720')
    logwin.title("Login")
    logwin.config(background="#FAF3E0")
    logwin.resizable(False,False)
    
    login_label = Label(logwin, 
                        text="Login", 
                        bg='#FAF3E0', 
                        fg="#193452", 
                        font=("Provicali", 50))  
    login_label.place(x=270,y=50)

    username_label =Label(logwin, 
                          text="Username", 
                          bg='#FAF3E0', 
                          fg="#193452", 
                          font=("Provicali", 28))
    username_label.place(x=20,y=190)

    username_entry = Entry(logwin, 
                           font=("Arial", 28))
    username_entry.place(x=220,y=190)

    password_label = Label(logwin, 
                           text="Password", 
                           bg='#FAF3E0', 
                           fg="#193452", 
                           font=("Provicali", 28))
    password_label.place(x=20,y=290)

    password_entry = Entry(logwin,
                           show="*", 
                           font=("Arial", 28))
    password_entry.place(x=220,y=290)
    login_button = Button(logwin, 
                          text="LOGIN", 
                          font=("lemondays",19),
                          width=10,
                          height=1,
                          bg='#193452',
                          fg="white",
                          activeforeground="white",
                          activebackground="#193452",
                          cursor="hand2",
                          command=loginFunc)
    login_button.place(x=330,y=390)
    logwin.grab_set()
    logwin.mainloop()

def loginFunc():
    global username
    global password
    entered_username=username_entry.get()
    entered_password=password_entry.get()
    if entered_username == username[0] and entered_password == password[0]:
        messagebox.showinfo(title="Login Success", 
                            message="You successfully logged in.")
        logwin.withdraw()
    else:
        messagebox.showerror(title="Error", 
                             message="Invalid login.") 

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

def searchonweb():
    query = search.get()
    query=query.replace(" ","+")
    url=f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def booknow():
    messagebox.showinfo(title="Succesfully Booked", 
                        message="An Email has been sent to you!")
    bookwin.withdraw() 


def booking1():
    global bookwin
    bookwin = Toplevel()
    bookwin.geometry('800x720')
    bookwin.config(bg="#FAF3E0")
    bookwin.title("Booking")
    bookwin.resizable(False,False)
    TOPHeader = Label(bookwin, text="ENTER YOUR BOOKING DETAILS HERE",
                   font=("provicali", 30,),
                   fg="#193452",
                   bg="#FAF3E0",
                   bd=10,
                   compound="top",
                   underline=17)
    TOPHeader.place(x=50,y=50)

    first_name=Label(bookwin,
                     text="First Name",
                     font=("arcane nine",28),
                     bg='#FAF3E0', 
                     fg="#193452",)
    first_name.place(x=20,y=190)

    first_name_entry = Entry(bookwin, 
                           font=("Arial", 28))
    first_name_entry.place(x=220,y=190)

    last_name=Label(bookwin,
                     text="Last Name",
                     font=("arcane nine",28),
                     bg='#FAF3E0', 
                     fg="#193452",)
    last_name.place(x=20,y=260)

    last_name_entry = Entry(bookwin, 
                           font=("Arial", 28))
    last_name_entry.place(x=220,y=260)

    email_label=Label(bookwin,
                     text="Email",
                     font=("arcane nine",28),
                     bg='#FAF3E0', 
                     fg="#193452",)
    email_label.place(x=20,y=330)

    email_label_entry = Entry(bookwin, 
                           font=("Arial", 28))
    email_label_entry.place(x=220,y=330)

    address_label=Label(bookwin,
                        text="Address",
                        font=("arcane nine",28),
                        bg='#FAF3E0', 
                        fg="#193452",)
    address_label.place(x=20,y=400)

    address_label_entry=Entry(bookwin,
                         font=("Arial", 28))
    address_label_entry.place(x=220,y=400)

    destination_label= Label(bookwin,
                             text="Destination",
                            font=("arcane nine",28),
                            bg='#FAF3E0', 
                            fg="#193452",)
    destination_label.place(x=19,y=470)

    choices=["Kashmir","Murre","Naran","Swat","Jammu","Lahore","Karachi"]
    destination_label_entry=ttk.Combobox(bookwin, 
                           font=("Arial", 28),values=choices) 
    destination_label_entry.place(x=220,y=470,)

    submit_button_booking=Button(bookwin,text="Submit", 
                          font=("lemondays",19),
                          width=10,
                          height=1,
                          bg='#193452',
                          fg="white",
                          activeforeground="white",
                          activebackground="#193452",
                          cursor="hand2",
                          command=booknow)
    submit_button_booking.place(x=320,y=550) 

    bookwin.mainloop()

def places1():
    global placewin
    placewin=Toplevel()
    placewin.geometry('800x720')
    placewin.config(bg="#FAF3E0") 
    placewin.title("Places")
    placewin.resizable(False,False)
    
    canvas=Canvas(placewin, width=750, height=150, bg="#193452")
    canvas.place(x=25,y=60)
    canvas1=Canvas(placewin, width=750, height=150, bg="#193452")
    canvas1.place(x=25,y=220)
    canvas2=Canvas(placewin, width=750, height=150, bg="#193452")
    canvas2.place(x=25,y=380)
    canvas3=Canvas(placewin, width=750, height=150, bg="#193452")
    canvas3.place(x=25,y=540)

    destination=Label(placewin,
                      text="DESTINATIONS",
                      font=("provicali",35),
                      bg='#FAF3E0', 
                      fg="#193452")
    destination.pack()

    kashmir=Label(placewin,
                  bg='#193452',
                  fg="#FAF3E0",
                  text='Kashmir :',
                  font=("provicali",30),
                  )
    kashmir.place(x=40,y=70)

    kashmir_info=Label(placewin,
                text="\"Kashmir, known for its stunning natural beauty and",
                font=("Arial",17),
                bg='#193452',
                fg="#FAF3E0",)
    kashmir_info.place(x=40,y=120)
    kashmir_info1=Label(placewin,
                text="rich cultural heritage, captivates with its majestic",
                font=("Arial",17),
                bg='#193452',
                fg="#FAF3E0",)
    kashmir_info1.place(x=48,y=147)
    kashmir_info2=Label(placewin,
                text="mountains, serene lakes, and vibrant traditions\"",
                font=("Arial",17),
                bg='#193452',
                fg="#FAF3E0",)
    kashmir_info2.place(x=48,y=175)

    kashmir_book=Button(placewin,
                        text="BOOK NOW",
                        fg='#193452',
                        bg="#fcf8ef",
                        font=("Provicali",20,),
                        height=2,
                        activebackground="#fcf8ef",
                        activeforeground="#193452",
                        cursor="hand2",
                        command=booking1,
                        )
    kashmir_book.place(x=575,y=100)

    murre=Label(placewin,
                  bg='#193452',
                  fg="#FAF3E0",
                  text='Murre :',
                  font=("provicali",30),
                  )
    murre.place(x=40,y=230)

    murre_info=Label(placewin,
                text="\"Murre, a Pakistani hill town, offers serene",
                font=("Arial",17),
                bg='#193452',
                fg="#FAF3E0",)
    murre_info.place(x=40,y=280)
    murre_info1=Label(placewin,
                text="mountain vistas and refreshing retreats amidst",
                font=("Arial",17),
                bg='#193452',
                fg="#FAF3E0",)
    murre_info1.place(x=48,y=307)
    murre_info2=Label(placewin,
                text=" captivating landscapes.\"",
                font=("Arial",17),
                bg='#193452',
                fg="#FAF3E0",)
    murre_info2.place(x=40,y=335)

    murre_book=Button(placewin,
                        text="BOOK NOW",
                        fg='#193452',
                        bg="#fcf8ef",
                        font=("Provicali",20,),
                        height=2,
                        activebackground="#fcf8ef",
                        activeforeground="#193452",
                        cursor="hand2",
                        command=booking1,
                        )
    murre_book.place(x=575,y=260)

    naran=Label(placewin,
                  bg='#193452',
                  fg="#FAF3E0",
                  text='Naran :',
                  font=("provicali",30),
                  )
    naran.place(x=40,y=390)

    naran_info=Label(placewin,
                text="\"Naran, a Pakistani gem, mesmerizes with its",
                font=("Arial",17),
                bg='#193452',
                fg="#FAF3E0",)
    naran_info.place(x=40,y=440)
    naran_info1=Label(placewin,
                text="panoramas and serene natural escapes.",
                font=("Arial",17),
                bg='#193452',
                fg="#FAF3E0",)
    naran_info1.place(x=48,y=467)
    naran_info2=Label(placewin,
                text=" It's a captivating haven amidst nature's splendor.\"",
                font=("Arial",17),
                bg='#193452',
                fg="#FAF3E0",)
    naran_info2.place(x=40,y=495)

    naran_book=Button(placewin,
                        text="BOOK NOW",
                        fg='#193452',
                        bg="#fcf8ef",
                        font=("Provicali",20,),
                        height=2,
                        activebackground="#fcf8ef",
                        activeforeground="#193452",
                        cursor="hand2",
                        command=booking1
                        )
    naran_book.place(x=575,y=420)

    sawat=Label(placewin,
                  bg='#193452',
                  fg="#FAF3E0",
                  text='Swat :',
                  font=("provicali",30),
                  )
    sawat.place(x=40,y=550)

    sawat_info=Label(placewin,
                text="\"Swat, a Pakistani paradise,enchants with its scenic",
                font=("Arial",17),
                bg='#193452',
                fg="#FAF3E0",)
    sawat_info.place(x=40,y=600)
    sawat_info1=Label(placewin,
                text="grandeur and captivating natural beauty.",
                font=("Arial",17),
                bg='#193452',
                fg="#FAF3E0",)
    sawat_info1.place(x=48,y=627)
    sawat_info2=Label(placewin,
                text=" It's a haven amidst majestic mountains.\"",
                font=("Arial",17),
                bg='#193452',
                fg="#FAF3E0",)
    sawat_info2.place(x=40,y=655)

    sawat_book=Button(placewin,
                        text="BOOK NOW",
                        fg='#193452',
                        bg="#fcf8ef",
                        font=("Provicali",20,),
                        height=2,
                        activebackground="#fcf8ef",
                        activeforeground="#193452",
                        cursor="hand2",
                        command=booking1
                        )
    sawat_book.place(x=575,y=580)


    placewin.mainloop() 

def about_us():
    about_win=Toplevel()
    about_win.title("About Us")
    about_win.geometry('800x720')
    about_win.resizable(False,False)
    about_win.config(bg="#FAF3E0")


    about_label = Label(about_win,
                       text="ABOUT US",
                       font=("provicali", 40,),
                        fg="#193452",
                        bg="#FAF3E0",
                        bd=10,
                        underline=4)
    about_label.place(x=260,y=16)

    canvas=Canvas(about_win, width=700, height=600, bg="#193452")
    canvas.place(x=45,y=90)
    description = Label(about_win,
                       text="Welcome to Explore Ease, your gateway to extraordinary\n"
                            "journeys and unforgettable adventures. At Explore Ease,\n"
                            "nwe're dedicated to curating travel transcend expectations\n"
                            "offering a passport to the world's captivating destinations.\n\n"
                            "With a commitment to personalized service and meticulous\n"
                            "planning, we craft tailored itineraries that reflect your\n"
                            "travel aspirations. From uncovering hidden treasures to \n"
                            "embracing iconic landmarks, we're passionate creating \n"
                            "moments that linger as cherished memories\n\n"
                            "Join us on a voyage where each itinerary is a narrative\n"
                            "waiting to unfold. Our team of seasoned travel experts \n"
                            "is here to transform your dreams into seamless realities.\n",
                        anchor="center",
                        font=("Times New Roman", 20),
                        bg='#193452',
                        fg="#FAF3E0")
    description.place(x=50,y=100,)
    description.pack(expand=True)
    developer_info = Label(about_win,
                        text="Developed by: Mutashim ,Izhar, Anas, Ali\nContact: muhtashimmohsin@gmail.com",
                        font=("Times New Roman", 20),
                        bg='#193452',
                        fg="#FAF3E0",
                        )
    
    developer_info.place(x=170,y=600)              

    about_win.mainloop() 

def career_section():
    career_win=Toplevel()
    career_win.title("Career")
    career_win.geometry('800x720')
    career_win.resizable(False,False)
    career_win.config(bg="#FAF3E0")

    career_label = Label(career_win,
                        text="CAREER",
                        font=("provicali", 40,),
                        fg="#193452",
                        bg="#FAF3E0",
                        bd=10,
                        underline=4)
    
    career_label.place(x=291,y=16)

    careers_text = (
        "\n\t\t\t    Join Our Team at Explore Ease\n\n"
        "At Explore Ease, we foster a culture of innovation, collaboration, and growth. We're passionate about creating meaningful experiences, and we're always seeking exceptional talent to join our journey.\n\n"
        "Why Work With Us?\n"
        "- Innovative Environment: Be part of a dynamic and creative workspace that encourages fresh ideas and innovation.\n"
        "- Collaborative Culture: Join a team that values collaboration, diversity, and mutual respect, fostering a supportive work environment.\n"
        "- Professional Development: Access ongoing learning opportunities and career advancement programs designed to help you excel.\n"
        "- Impactful Work: Contribute to exciting projects that make a difference and leave impact.\n"
        "- Work-Life Balance: Enjoy flexible schedules and initiatives that promote a healthy work-life balance.\n\n"
        "Current Openings\n"
        "Explore our current job openings below. If you believe you're a great fit for our team and there's no current vacancy matching your expertise, feel free to reach out to us at \"muhtashimmohsin@gmail.com\" with your resume and a cover letter detailing how you can contribute to our mission.\n\n"
        "- Travel Experience Curator - Islamabad, Pakistan\n"
        "- Marketing Specialist - Karachi, Pakistan\n"
        "- Customer Service Representative - Lahore, Pakistan\n"
        "- Digital Content Creator - Remote, Pakistan\n\n")

    Text_label = tk.Label(career_win, 
                     text=careers_text, 
                     justify="left", 
                     anchor="center", 
                     wraplength=780,
                     font=("Times New Roman", 15),
                     bg='#FAF3E0',
                     fg="#193452",
                     )
    Text_label.place(x=20,y=80)



    career_win.mainloop()

def reviews_tab():
    reviews_win=Toplevel()
    reviews_win.title("Customer Reviews")
    reviews_win.geometry('800x720')
    reviews_win.resizable(False, False)
    reviews_win.config(bg="#FAF3E0")

    reviews_label=Label(reviews_win,
                          text="CUSTOMER REVIEWS",
                          font=("provicali", 40,),
                          fg="#193452",
                          bg="#FAF3E0",
                          bd=10,
                          underline=4)
    reviews_label.place(x=130,y=16)

    canvas=Canvas(reviews_win, width=700, height=600, bg="#193452")
    canvas.place(x=45,y=90)


    review_1_text_label =Label(reviews_win,
                                text="The trip was phenomenal! Amazing service and breathtaking views. 5 stars!",
                                font=("Times New Roman",20),
                                bg='#193452',
                                fg="#FAF3E0",
                                wraplength=680,
                                justify="left")
    review_1_text_label.place(x=60,y=100)

    review_1_name_label=Label(reviews_win,
                                text="- Reviewer: Sana",
                                font=("Times New Roman",18),
                                bg='#193452',
                                fg="#FAF3E0")
    review_1_name_label.place(x=60,y=180)

    review_1_rating_label=Label(reviews_win,
                                  text="- Rating: ⭐⭐⭐⭐⭐",
                                  font=("Times New Roman", 18),
                                  bg='#193452',
                                  fg="#FAF3E0")
    review_1_rating_label.place(x=60,y=210)

    line_label=Label(reviews_win,
                     text="------------------------------------------------------------------------------------",
                     font=("Times New Roman",18),
                     bg='#193452',
                     fg="#FAF3E0")

    line_label.place(x=60,y=250)

    review_2_text_label=Label(reviews_win,
                                text="Absolutely loved the experience, especially the hospitality. 4 stars!",
                                font=("Times New Roman",20),
                                bg='#193452',
                                fg="#FAF3E0",
                                wraplength=680,
                                justify="left")
    review_2_text_label.place(x=60,y=300)

    review_2_name_label=Label(reviews_win,
                                text="- Reviewer: Ahmed",
                                font=("Times New Roman",18),
                                bg='#193452',
                                fg="#FAF3E0")
    review_2_name_label.place(x=60,y=380)

    review_2_rating_label=Label(reviews_win,
                                  text="- Rating: ⭐⭐⭐⭐",
                                  font=("Times New Roman",18),
                                  bg='#193452',
                                  fg="#FAF3E0")
    review_2_rating_label.place(x=60,y=410)


    line_label_1=Label(reviews_win,
                     text="------------------------------------------------------------------------------------",
                     font=("Times New Roman",18),
                     bg='#193452',
                     fg="#FAF3E0")

    line_label_1.place(x=60,y=450)

    review_3_text_label = Label(reviews_win,
                            text="Had an amazing time exploring new places. 5 stars!",
                            font=("Times New Roman", 20),
                            bg='#193452',
                            fg="#FAF3E0",
                            wraplength=680,
                            justify="left")
    review_3_text_label.place(x=60, y=520)

    review_3_name_label = Label(reviews_win,
                            text="- Reviewer: Sarah",
                            font=("Times New Roman", 18),
                            bg='#193452',
                            fg="#FAF3E0")
    review_3_name_label.place(x=60, y=580)

    review_3_rating_label = Label(reviews_win,
                              text="- Rating: ⭐⭐⭐⭐⭐",
                              font=("Times New Roman", 18),
                              bg='#193452',
                              fg="#FAF3E0")
    review_3_rating_label.place(x=60, y=610)


    reviews_win.mainloop()

window=Tk()
window.geometry('1280x720')
window.title("ExploreEase Travel & Tours")
icon=PhotoImage(file='Untitled-1.png')
window.iconphoto(False,icon)
window.config(background="#FAF3E0")
window.resizable(False,False)

menu=PhotoImage(file="menu.png")
menu1=Label(window,
            image=menu,bg='#FAF3E0')
menu1.pack()
 
menus=PhotoImage(file="menus.png")
menus1=Label(window,
             image=menus,
             bg="#fcf8ef") 
menus1.place(x=58,y=375)

label=Label(window,text="Explore Eaze",
            font=("Stencil",20),
            fg="#193452",
            bg="#FAF3E0",
            bd=10,
            image=icon,
            compound="top")
label.place(x=40,y=-10)

search=Entry(window,
             justify="center",
             width=36,
             font=("poppins",25,"bold"))
search.place(x=260,y=40)

image1=PhotoImage(file="seach.png")
sbutton=Button(window,
               image=image1,
               fg="#193452",
               bg="#193452",
               activeforeground="#193452",
               activebackground="#193452",
               border=0,
               cursor="hand2",
               command=searchonweb)
sbutton.place(x=910,y=40)

login=Button(window,
             text="LOGIN",
             font=("lemondays",15),
             width=10,
             height=1,
             bg='#193452',
             fg='white',
             activeforeground="white",
             activebackground="#193452",
             cursor="hand2",
             command=login1)
login.place(x=1130,y=44)

signup=Button(window,
             text="SIGNUP",
             font=("lemondays",15),
             width=10,
             height=1,
             bg='#193452',
             fg='white',
             activeforeground="white",
             activebackground="#193452",
             cursor="hand2",
             command=signup1)
signup.place(x=990,y=44)                

navpic=PhotoImage(file="nav-bar.png")
nav=Label(image=navpic,
          bg='#FAF3E0',
          border=0)
nav.place(x=260,y=110) 

tab1=Button(window,
            text="Booking",
            font=("provicali",19,),
            bd=0,
            relief=RAISED,
            bg='#193452',
            padx=0,
            pady=0,
            fg='white',
            activeforeground="white",
            activebackground="#193452",
            cursor="hand2",
            command=booking1)

tab1.place(x=307,y=122)

tab2=Button(window,
            text="Places",
            font=("provicali",19,),
            bd=0,
            relief=tk.FLAT,
            bg='#193452',
            padx=0,
            pady=0,
            fg='white',
            activeforeground="white",
            activebackground="#193452",
            cursor="hand2",
            command=places1)

tab2.place(x=507,y=122)

tab3=Button(window,
            text="About Us",
            font=("provicali",19,),
            bd=0,
            relief=tk.FLAT,
            bg='#193452',
            padx=0,
            pady=0,
            fg='white',
            activeforeground="white",
            activebackground="#193452",
            cursor="hand2",
            command=about_us)

tab3.place(x=690,y=122)

tab4=Button(window,
            text="Carrers",
            font=("provicali",19,),
            bd=0,
            relief=tk.FLAT,
            bg='#193452',
            padx=0,
            pady=0,
            fg='white',
            activeforeground="white",
            activebackground="#193452",
            cursor="hand2",
            command=career_section)

tab4.place(x=900,y=122)

tab5=Button(window,
            text="Reviews",
            font=("provicali",19,),
            bd=0, relief=tk.FLAT,
            bg='#193452',
            padx=0,
            pady=0,
            fg='white',
            activeforeground="white",
            activebackground="#193452",
            cursor="hand2",
            command=reviews_tab)

tab5.place(x=1100,y=122)

sale=PhotoImage(file="sale-sale.png")
sale2=Label(window,
            image=sale)
saletext=PhotoImage(file="sale-text.png")
strip=Label(window,
            image=saletext,
            fg="#193452",
            bg="#193452",)
sale2.place(x=-2,y=210)
strip.place(x=-2,y=210)

selling=Label(window,
              text="\"Our Most Selling Packages\"",
              font=("Arcane Nine",30),
              bg='#193452',
              fg='white')
selling.place(x=390,y=280)

menutab1=Button(window,
                text="BOOK NOW",
                fg='#193452',
                bg="#fcf8ef",
                font=("Provicali",20,),
                border=0,
                activebackground="#fcf8ef",
                activeforeground="#193452",
                cursor="hand2",
                padx=40,
                command=booking1)

menutab2=Button(window,
                text="BOOK NOW",
                fg='#193452',
                bg="#fcf8ef",
                font=("Provicali",20,),
                border=0,
                activebackground="#fcf8ef",
                activeforeground="#193452",
                cursor="hand2",
                padx=40,
                command=booking1)

menutab3=Button(window,
                text="BOOK NOW",
                fg='#193452',
                bg="#fcf8ef",
                font=("Provicali",20,),
                border=0,
                activebackground="#fcf8ef",
                activeforeground="#193452",
                cursor="hand2",
                padx=40,
                command=booking1)

menutab1.place(x=130,y=612)
menutab2.place(x=522,y=612) 
menutab3.place(x=895,y=612)


window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop() 