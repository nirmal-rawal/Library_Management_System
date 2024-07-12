                                    #Library Management Systme 

from tkinter import*
from tkinter import ttk
from tkinter import Frame, RIDGE
import tkinter.messagebox
import psycopg2
from tkinter import messagebox
import datetime
import tkinter


class LibraryManagementSystem:
    def __init__(self,root) -> None:
        self.root = root
        self.root.title( "Library Mangemnt System")
        self.root.geometry("1550x800+0+0")
    
        #=================================Varibales=======================
        self.member_type_var =StringVar()
        self.date_borrowed_var =StringVar()
        self.id_number_var =StringVar()
        self.fullname_var =StringVar()
        self.address_var =StringVar()
        self.contact_number_var =StringVar()
        self.book_id_var =StringVar()
        self.book_name_var =StringVar()
        self.author_name_var =StringVar()
        self.late_return_fine_var =StringVar()
        self.days_on_book_var =StringVar()
        self.due_date_var =StringVar()
        


        
    

        lbtitle =Label(self.root, text='Library Managemnt system',bg="violet",fg="blue",border=20,relief=RIDGE,font=("times new roman",65,"bold"),padx=2,pady=6)
        lbtitle.pack(side=TOP,fill=X)

        frme = Frame(self.root,bd=12,relief=RIDGE, padx=20, bg="powder blue")
        frme.place(x=0,y=130,width=1530,height=400)

        #========================DataframeLeft==================================
        DataframeLeft =LabelFrame(frme,text='Library member informantion',bg="powder blue",fg="blue",border=12,relief=RIDGE,font=("times new roman",17,"bold"))
        DataframeLeft.place(x=0,y=5,width=900,height =350)

        #========================Dataframeleft Member==================================


       
        dflmember = Label(DataframeLeft,text="Member Type",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
        dflmember.grid(row=0,column=0,sticky=W)
        comMembe =ttk.Combobox(DataframeLeft,font=("times new roman",15,"bold"),textvariable=self.member_type_var,width =27,state="readonly")
        comMembe['values']=('Admin staf',"student","lecturer")
        comMembe.grid(row=0,column =1)

        dfldateb = Label(DataframeLeft,text="Date Borrowed",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
        dfldateb.grid(row=1,column=0,sticky=W)
        dfldateb =Entry(DataframeLeft,font=("times new roman",15,"bold"),textvariable=self.date_borrowed_var,width=29)
        dfldateb.grid(row=1,column=1)

        dflid_num = Label(DataframeLeft,text="ID Number",bg="powder Blue",font=("times new roman",15,"bold"),padx=2,pady=6)
        dflid_num.grid(row=2,column=0,sticky=W)
        dflid_num = Entry(DataframeLeft,font=("times new roman",15,"bold"),textvariable=self.id_number_var,width=29)
        dflid_num.grid(row=2,column=1)


      
        
        dflid_full_name =Label(DataframeLeft,text="fullname",bg="powder Blue",font=("times new roman",15,"bold"),padx=2,pady=6)
        dflid_full_name.grid(row=3,column=0,sticky=W)
        dflid_full_name = Entry(DataframeLeft,font=("times new roman",15,"bold"),textvariable=self.fullname_var,width=29)
        dflid_full_name.grid(row=3,column=1)


        dfladdress = Label(DataframeLeft,text="Address",bg="powder Blue",font=("times new roman",15,"bold"),padx=2,pady=6)
        dfladdress.grid(row=4,column=0,sticky=W)
        dfladdress = Entry(DataframeLeft ,font=("times new roman",15,"bold"),textvariable=self.address_var,width=29)
        dfladdress.grid(row=4,column=1)


        dflmobileNUmber = Label(DataframeLeft,text="Contact number",bg="powder Blue",font=("times new roman",15,"bold"),padx=2,pady=6)
        dflmobileNUmber.grid(row=5,column=0,sticky=W)
        dflmobileNUmber = Entry(DataframeLeft ,font=("times new roman",15,"bold"),textvariable=self.contact_number_var,width=29)
        dflmobileNUmber.grid(row=5,column=1)

        dflbookid = Label(DataframeLeft,text="Book ID",bg="powder Blue",font=("arial",12,"bold"),padx=2)
        dflbookid.grid(row=0,column=2,sticky=W)
        dflbookid = Entry(DataframeLeft ,font=("times new roman",15,"bold"),textvariable=self.book_id_var,width=29)
        dflbookid.grid(row=0,column=3)

        dflbookname = Label(DataframeLeft,text="Book Name",bg="powder Blue",font=("arial",12,"bold"),padx=2)
        dflbookname.grid(row=1,column=2,sticky=W)
        dflbookname= Entry(DataframeLeft ,font=("times new roman",15,"bold"),textvariable=self.book_name_var,width=29)
        dflbookname.grid(row=1,column=3)

        dflbookauthor =Label(DataframeLeft,text="Author Name ",bg="powder Blue",font=("arial",12,"bold"),padx=2)
        dflbookauthor.grid(row=2,column=2,sticky=W)
        dflbookauthor = Entry(DataframeLeft ,font=("times new roman",15,"bold"),textvariable=self.author_name_var,width=29)
        dflbookauthor.grid(row=2,column=3)

        dfllrf =Label(DataframeLeft,text="Late return fine ",bg="powder Blue",font=("arial",12,"bold"),padx=2)
        dfllrf.grid(row=3,column=2,sticky=W)
        dfllrf = Entry(DataframeLeft ,font=("times new roman",15,"bold"),textvariable=self.late_return_fine_var,width=29)
        dfllrf.grid(row=3,column=3)

        dfldob =Label(DataframeLeft,text="Days on Book ",bg="powder Blue",font=("arial",12,"bold"),padx=2)
        dfldob.grid(row=4,column=2,sticky=W)
        dfldob = Entry(DataframeLeft ,font=("times new roman",15,"bold"),textvariable=self.days_on_book_var,width=29)
        dfldob.grid(row=4,column=3)

        dflduedate_label = Label(DataframeLeft, text="Date due", bg="powder blue", font=("arial", 12, "bold"), padx=2)
        dflduedate_label.grid(row=5, column=2, sticky=W)
        dflduedate_entry = Entry(DataframeLeft, font=("times new roman", 15, "bold"),textvariable=self.due_date_var, width=29)
        dflduedate_entry.grid(row=5, column=3)


       



        
        #========================Dataframeright==================================
        Dataframeright =LabelFrame(frme,text='Book Details ',bg="powder blue",fg="blue",border=20,relief=RIDGE,font=("times new roman",12,"bold"))
        Dataframeright.place(x=910,y=5,width=540,height =350)


        self.textbox = Text(Dataframeright, font=("times new roman", 15, "bold"), width=50, height=16, padx=2, pady=6)
        self.textbox.grid(row=0, column=2)

       

        ListScrollbar=Scrollbar(Dataframeright)
        ListScrollbar.grid(row =0,column = 1,sticky  =NS)

        Listbooks =[
    "To Kill a Mockingbird",
    "1984",
    "The Great Gatsby",
    "The Catcher in the Rye",
    "Moby-Dick",
    "Pride and Prejudice",
    "War and Peace",
    "The Lord of the Rings",
    "Ulysses",
    "The Brothers Karamazov",
    "Jane Eyre",
    "Crime and Punishment",
    "Wuthering Heights",
    "Brave New World",
    "The Odyssey",
    "Great Expectations",
    "One Hundred Years of Solitude",
    "The Divine Comedy",
    "The Iliad",
    "Don Quixote",
    "Les Misérables",
    "The Hobbit",
    "Anna Karenina",
    "Fahrenheit 451",
    "Madame Bovary",
    "The Picture of Dorian Gray",
    "The Kite Runner",
    "Dracula",
    "The Catch-22",
    "Beloved",
    "The Alchemist",
    "Harry Potter and the Sorcerer's Stone",
    "The Grapes of Wrath",
    "The Sound and the Fury",
    "To the Lighthouse",
    "The Chronicles of Narnia",
    "Slaughterhouse-Five",
    "The Handmaid's Tale",
    "A Tale of Two Cities",
    "Frankenstein",
    "Moby-Dick",
    "Lolita",
    "The Old Man and the Sea",
    "Gone with the Wind",
    "The Stranger",
    "Catch-22",
    "Heart of Darkness",
    "The Metamorphosis",
    "Middlemarch",
    "The Count of Monte Cristo",
    "The Road",
    "The Secret Garden",
    "The Bell Jar",
    "A Clockwork Orange"
]
        def selectbook(event,):
            selected_book = listBox.get(listBox.curselection()[0])
            # Update the text variables based on the selected book
            if selected_book == "To Kill a Mockingbird":
                self.book_id_var.set("BK001")
                self.book_name_var.set("To Kill a Mockingbird")
                self.author_name_var.set("Harper Lee")
                self.late_return_fine_var.set("$2")
                self.days_on_book_var.set("14")
                self.due_date_var.set(str(datetime.date.today() + datetime.timedelta(days=14)))

            elif selected_book == "1984":
                self.book_id_var.set("BK002")
                self.book_name_var.set("1984")
                self.author_name_var.set("George Orwell")
                self.late_return_fine_var.set("$2")
                self.days_on_book_var.set("14")
                self.due_date_var.set(str(datetime.date.today() + datetime.timedelta(days=14)))

            elif selected_book == "The Great Gatsby":
                self.book_id_var.set("BK003")
                self.book_name_var.set("The Great Gatsby")
                self.author_name_var.set("F. Scott Fitzgerald")
                self.late_return_fine_var.set("$2")
                self.days_on_book_var.set("14")
                self.due_date_var.set(str(datetime.date.today() + datetime.timedelta(days=14)))

            # Add more cases for other books...

        listBox = Listbox(Dataframeright, font=("times new roman", 15, "bold"), width=20, height=16)
        listBox.bind("<<ListboxSelect>>", selectbook)
        listBox.grid(row=0, column=0, padx=8)
        ListScrollbar.config(command=listBox.yview)
        for items in Listbooks:
            listBox.insert(END,items)

                        #Buttons frame 
        buttonsframe = Frame(self.root,bd=12,relief=RIDGE, padx=20, bg="powder blue")
        buttonsframe.place(x=0,y=530,width=1530,height=70)
        
        btnAddData =Button(buttonsframe,text="Add Data",command=self.add_data,font=("times new roman",12,"bold"),width=23,bg ="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnShowData =Button(buttonsframe,command=self.show_data,text="Show Data",font=("times new roman",12,"bold"),width=23,bg ="blue",fg="white")
        btnShowData.grid(row=0,column=1)
        
        btnupdate =Button(buttonsframe,command=self.update,text="Update Data",font=("times new roman",12,"bold"),width=23,bg ="blue",fg="white")
        btnupdate.grid(row=0,column=2)

        btndelete =Button(buttonsframe,command=self.delete,text="Delete Data",font=("times new roman",12,"bold"),width=23,bg ="blue",fg="white")
        btndelete.grid(row=0,column=3)

        btnreset =Button(buttonsframe,command=self.reset,text="Reset Data",font=("times new roman",12,"bold"),width=23,bg ="blue",fg="white")
        btnreset.grid(row=0,column=4)

        btnexit =Button(buttonsframe,command=self.exit,text="Exit",font=("times new roman",12,"bold"),width=23,bg ="blue",fg="white")
        btnexit.grid(row=0,column=5)


                         #Data Information frame 
        framredetails = Frame(self.root,bd=12,relief=RIDGE, padx=20, bg="powder blue")
        framredetails.place(x=0,y=600,width=1530,height=195)

        table_frame = Frame(framredetails, bd=6, relief=RIDGE, padx=20, bg="powder blue")
        table_frame.place(x=0, y=2, width=1460, height=190)

        xsscroll =ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        ysscroll =ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(table_frame,columns=("Memeber type","Book Borrowed","ID Number","Full Name","Address","Contact Number","Book ID","Book Title","Author Name","Late return fine","Days on books", "Due Date"),xscrollcommand=xsscroll.set,yscrollcommand=ysscroll.set)

        xsscroll.pack(side=BOTTOM,fill=X)
        ysscroll.pack(side=RIGHT,fill=Y)
        xsscroll.config(command=self.library_table.xview)
        ysscroll.config(command=self.library_table.yview)

        self.library_table.heading("Memeber type",text="Member type")
        self.library_table.heading("Book Borrowed",text=" Date of Book Borrowed")
        self.library_table.heading("ID Number",text="ID Number")
        self.library_table.heading("Full Name",text="Enter the full name")
        self.library_table.heading("Address",text="Address")
        self.library_table.heading("Contact Number",text="Contact Number")
        self.library_table.heading("Book ID",text="book Id number")
        self.library_table.heading("Book Title",text="Book Title")
        self.library_table.heading("Author Name",text="Author Name")
        self.library_table.heading("Late return fine",text="Late return fine")
        self.library_table.heading("Days on books",text="book keeping days")
        self.library_table.heading("Due Date",text="Deu date")

        # self.library_table.pack(fill=BOTH, expand=1)
        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)
        # self.fetch_data()


        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)


    
        self.fetch_data()
    def add_data(self):
        if any(not var.get() for var in [self.member_type_var,             
        self.date_borrowed_var,
        self.id_number_var, 
        self.fullname_var ,
        self.address_var ,
        self.contact_number_var, 
        self.book_id_var ,
        self.book_name_var, 
        self.author_name_var, 
        self.late_return_fine_var ,
        self.days_on_book_var ,
        self.due_date_var ]):
            messagebox.showerror("Error", "First fill out all the form")
        else:
            conn = psycopg2.connect(
                host="localhost",
                database="Demo",
                user="postgres",
                password="postgres",
                port="5432"
            )
            cursor = conn.cursor()

            try:
                cursor.execute(
                    "INSERT INTO lab (\"mt\", \"db\", \"in\", \"fn\", add, \"cn\", \"bi\", \"bn\", \"an\", \"lrf\", \"dob\", \"dd\") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.member_type_var.get(),
                        self.date_borrowed_var.get(),
                        self.id_number_var.get(),
                        self.fullname_var.get(),
                        self.address_var.get(),
                        self.contact_number_var.get(),
                        self.book_id_var.get(),
                        self.book_name_var.get(),
                        self.author_name_var.get(),
                        self.late_return_fine_var.get(),
                        self.days_on_book_var.get(),
                        self.due_date_var.get()
                    )
                )
                conn.commit()
                self.fetch_data()
                messagebox.showinfo("Success", "Record added successfully")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
            finally:
                cursor.close()
                conn.close()

            messagebox.showinfo("Sucess", "member has bee inserted sucessfully")


    def update(self):
        if self.id_number_var.get()==""or self.fullname_var.get()=="":
            messagebox.showerror("Error", "first select the data")
        else:
            try:
                conn = psycopg2.connect(
                    host="localhost",
                    database="Demo",
                    user="postgres",
                    password="postgres",
                    port="5432"
                )
                cursor = conn.cursor()
                # Check if the record exists
                cursor.execute('''SELECT * FROM lab WHERE "in"=%s''', (self.id_number_var.get(),))
                record = cursor.fetchone()
                if record is None:
                    messagebox.showerror("Error", "Data does not exist")
                else:
                    cursor.execute(
                        '''UPDATE lab SET mt=%s, db=%s, fn=%s, add=%s, cn=%s, bi=%s, bn=%s, an=%s, lrf=%s, dob=%s, dd=%s WHERE "in"=%s''',
                        (
                            self.member_type_var.get(),
                            self.date_borrowed_var.get(),
                            self.fullname_var.get(),
                            self.address_var.get(),
                            self.contact_number_var.get(),
                            self.book_id_var.get(),
                            self.book_name_var.get(),
                            self.author_name_var.get(),
                            self.late_return_fine_var.get(),
                            self.days_on_book_var.get(),
                            self.due_date_var.get(),
                            self.id_number_var.get()
                        )
                    )

                    conn.commit()
                    self.fetch_data()
                    self.reset()
                    
                    messagebox.showinfo("Success", "Record updated successfully")
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}")



    def fetch_data(self):
        conn = psycopg2.connect(
            host="localhost",
            database="Demo",
            user="postgres",
            password="postgres",
            port="5432"
        )
        cursor = conn.cursor()
        
        try:
            cursor.execute("select * from lab")
            rows = cursor.fetchall()

            if len(rows) != 0:
                self.library_table.delete(*self.library_table.get_children())
                for i in rows:
                    self.library_table.insert("", END, values=i)
            
            conn.commit()
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {e}")
        finally:
            cursor.close()
            conn.close()
        
    def get_cursor(self,event =""):
        cursor_row= self.library_table.focus()
        content =self.library_table.item(cursor_row)
        row= content['values']
        
        self.member_type_var.set(row[0]),
        self.date_borrowed_var.set(row[1]),
        self.id_number_var.set(row[2]),
        self.fullname_var.set(row[3]),
        self.address_var.set(row[4]),
        self.contact_number_var.set(row[5]),
        self.book_id_var.set(row[6]),
        self.book_name_var.set(row[7]),
        self.author_name_var.set(row[8]),
        self.late_return_fine_var.set(row[9]),
        self.days_on_book_var.set(row[10]),
        self.due_date_var.set(row[11])


    def show_data(self):
        if self.id_number_var.get()==" " or self.fullname_var.get()==" ":
            messagebox.showerror("Error","First select the member")
        else:
            try:
                conn = psycopg2.connect(
                host="localhost",
                database="Demo",
                user="postgres",
                password="postgres",
                port="5432")

                cursor = conn.cursor()
            
                #check the record exit or not 
                cursor.execute('''select *from lab where "in" =%s''',(self.id_number_var.get(),))
                record =cursor.fetchone()
                if record is None:
                    messagebox.showerror("Error", "data does not exist")

                else:
                    # Display the record if it exists
                    self.textbox.insert(END, "Member type:\t\t" + self.member_type_var.get() + "\n")
                    self.textbox.insert(END, "Date borrowed:\t\t" + self.date_borrowed_var.get() + "\n")
                    self.textbox.insert(END, "ID number:\t\t" + self.id_number_var.get() + "\n")
                    self.textbox.insert(END, "Full name:\t\t" + self.fullname_var.get() + "\n")
                    self.textbox.insert(END, "Address:\t\t" + self.address_var.get() + "\n")
                    self.textbox.insert(END, "Contact number:\t\t" + self.contact_number_var.get() + "\n")
                    self.textbox.insert(END, "Book ID:\t\t" + self.book_id_var.get() + "\n")
                    self.textbox.insert(END, "Book name:\t\t" + self.book_name_var.get() + "\n")
                    self.textbox.insert(END, "Author name:\t\t" + self.author_name_var.get() + "\n")
                    self.textbox.insert(END, "Late return fine:\t\t" + self.late_return_fine_var.get() + "\n")
                    self.textbox.insert(END, "Days on book:\t\t" + self.days_on_book_var.get() + "\n")
                    self.textbox.insert(END, "Due date:\t\t" + self.due_date_var.get() + "\n")

                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Error due to {str(e)}")
    
            



    def reset(self):
        if self.id_number_var.get()==""or self.fullname_var.get()=="":
            messagebox.showerror("Error", "first select the member") 
        else:       
            self.member_type_var.set(""),
            self.date_borrowed_var.set(""),
            self.id_number_var.set(""),
            self.fullname_var.set(""),
            self.address_var.set(""),
            self.contact_number_var.set(""),
            self.book_id_var.set(""),
            self.book_name_var.set(""),
            self.author_name_var.set(""),
            self.late_return_fine_var.set(""),
            self.days_on_book_var.set(""),
            self.due_date_var.set("")
            self.textbox.delete("1.0",END)



    def exit(self):
        exit =tkinter.messagebox.askyesno("Library Management System", "Do you want to exit")
        if exit>0:
            self.root.destroy()
            return



    def delete(self):
        if self.id_number_var.get() == "" or self.fullname_var.get() == "":
            messagebox.showerror("Error", "First select the member")
        else:
            try:
                conn = psycopg2.connect(
                    host="localhost",
                    database="Demo",
                    user="postgres",
                    password="postgres",
                    port="5432"
                )
                cursor = conn.cursor()

                # Check if the record exists
                cursor.execute('''SELECT * FROM lab WHERE "in"=%s''', (self.id_number_var.get(),))
                record = cursor.fetchone()

                if record is None:
                    messagebox.showerror("Error", "Data does not exist")
                else:
                    # Delete the record if it exists
                    cursor.execute('''DELETE FROM lab WHERE "in"=%s''', (self.id_number_var.get(),))
                    conn.commit()
                    self.fetch_data()
                    self.reset()
                    messagebox.showinfo("Success", "Member has been deleted")

                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}")


        # query ='''delete from lab where "in"=%s'''
        # value =(self.id_number_var.get(),)
        # cursor.execute(query,value)
        # conn.commit()
        # self.fetch_data()
        # self.reset()
        # conn.close()

        # messagebox.showinfo("Member has be Deleted ")

        

     
        
            
           

   

        




if __name__ == "__main__":
    root=Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()