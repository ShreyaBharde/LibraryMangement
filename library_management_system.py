# Bookstore Management System

import tkinter as tk
from tkinter import ttk,messagebox
import pymysql,datetime


class LibraryManagementSystem:
    
    def __init__(self,root) -> None:
        self.root = root
        self.root.title('Library Management System')
        self.root.geometry('1540x1080+0+0')


        self.member_var = tk.StringVar()
        self.prn_var = tk.StringVar()
        self.id_var = tk.StringVar()
        self.firstname_var = tk.StringVar()
        self.lastname_var = tk.StringVar()
        self.address1_var = tk.StringVar()
        self.address2_var = tk.StringVar()
        self.postcode_var = tk.StringVar()
        self.mobile_var = tk.StringVar()
        self.bookid_var = tk.StringVar()
        self.booktitle_var = tk.StringVar()
        self.author_var = tk.StringVar()
        self.dateborrowed_var = tk.StringVar()
        self.datedue_var = tk.StringVar()
        self.daysonbook_var = tk.StringVar()
        self.latereturnfine_var = tk.StringVar()
        self.daysoverdue_var = tk.StringVar()
        self.finalprice_var = tk.StringVar()

        #===========================Create Database====================================
        con = pymysql.connect(host="localhost", user="root", password="root")
        cursor = con.cursor()
        cursor.execute('create database if not exists library_management_system')
        con.commit()
        con.close()



        #===========================Create Table========================================
        con = pymysql.connect(host="localhost", user="root", password="root", db='library_management_system')
        cursor = con.cursor()
        cursor.execute('create table if not exists library(Member VARCHAR(40),PRN_NO VARCHAR(45),ID VARCHAR(45),FirstName VARCHAR(45),LastName VARCHAR(45),Address1 VARCHAR(45),Address2 VARCHAR(45),PostID VARCHAR(45),Mobile VARCHAR(45),BookID VARCHAR(45),BookTitle VARCHAR(45),Author VARCHAR(45),DateBorrowed VARCHAR(45),DateDue VARCHAR(45),DaysonBook VARCHAR(45),LateReturnFine VARCHAR(45),DateOverdue VARCHAR(45),Finalprice VARCHAR(45))')
        con.commit()
        con.close()


        lbl_header = tk.Label(self.root, text = 'Library Management System',bg = 'powder blue',
                             fg = 'green',bd = 20,relief = 'ridge',font = ('helvetica',50,'bold'),
                             padx = 2,pady = 6)
        lbl_header.pack(side='top',fill='x')

        frame = tk.Frame(self.root, bd = 12 , relief = 'ridge', padx = 20, bg = 'powder blue')
        frame.place(x = 0, y = 130, width = 1530, height = 400)




        #=================================Data Frame Left===================================
        frm_data_left = tk.LabelFrame(frame, text = 'Library Membership Info',bg = 'powder blue',
                                fg = 'green',bd = 12,relief = 'ridge',font = ('helvetica',12,'bold'))
        frm_data_left.place(x = 0, y = 5, width = 900, height = 350)

        entry_width = 31

        

        lbl_member = tk.Label(frm_data_left,text = 'Member Type:',font = ('helvetica',12,'bold'),
                              padx = 2, pady = 6, bg = 'powder blue')
        lbl_member.grid(row = 0,column = 0,sticky = 'w')

        cbx_member = ttk.Combobox(frm_data_left, font = ('helvetica',12,'bold'), width = entry_width - 2,
                                   state = 'readonly',textvariable = self.member_var)
        cbx_member['value'] = ('Admin Staff','Student','Lecturer')
        cbx_member.grid(row = 0, column = 1,)


        lbl_prn_no = tk.Label(frm_data_left,text = 'PRN No.:',font = ('helvetica',12,'bold'),
                              padx = 2, pady = 6, bg = 'powder blue')
        lbl_prn_no.grid(row = 1,column = 0,sticky = 'w')

        ent_prn_no = tk.Entry(frm_data_left,font = ('helvetica',12,'bold'), width = entry_width,
                              textvariable = self.prn_var)
        ent_prn_no.grid(row = 1,column = 1)


        lbl_id_no = tk.Label(frm_data_left,text = 'ID No.:',font = ('helvetica',12,'bold'),
                              padx = 2, pady = 6, bg = 'powder blue')
        lbl_id_no.grid(row = 2,column = 0,sticky = 'w')

        ent_id_no = tk.Entry(frm_data_left,font = ('helvetica',12,'bold'), width = entry_width,
                             textvariable = self.id_var)
        ent_id_no.grid(row = 2,column = 1)

        
        lbl_first_name = tk.Label(frm_data_left,text = 'First Name:',font = ('helvetica',12,'bold'),
                              padx = 2, pady = 6, bg = 'powder blue')
        lbl_first_name.grid(row = 3,column = 0,sticky = 'w')

        ent_first_name = tk.Entry(frm_data_left,font = ('helvetica',12,'bold'), width = entry_width,
                                  textvariable = self.firstname_var)
        ent_first_name.grid(row = 3,column = 1)


        lbl_last_name = tk.Label(frm_data_left,text = 'Last Name:',font = ('helvetica',12,'bold'),
                              padx = 2, pady = 6, bg = 'powder blue')
        lbl_last_name.grid(row = 4,column = 0,sticky = 'w')

        ent_last_name = tk.Entry(frm_data_left,font = ('helvetica',12,'bold'), width = entry_width,
                                 textvariable = self.lastname_var)
        ent_last_name.grid(row = 4,column = 1)

        
        lbl_address1 = tk.Label(frm_data_left,text = 'Address 1:',font = ('helvetica',12,'bold'),
                              padx = 2, pady = 6, bg = 'powder blue')
        lbl_address1.grid(row = 5,column = 0,sticky = 'w')

        ent_address1 = tk.Entry(frm_data_left,font = ('helvetica',12,'bold'), width = entry_width,
                                textvariable = self.address1_var)
        ent_address1.grid(row = 5,column = 1)


        lbl_address2 = tk.Label(frm_data_left,text = 'Address 2:',font = ('helvetica',12,'bold'),
                              padx = 2, pady = 6, bg = 'powder blue')
        lbl_address2.grid(row = 6,column = 0,sticky = 'w')

        ent_address2 = tk.Entry(frm_data_left,font = ('helvetica',12,'bold'), width = entry_width,
                                textvariable = self.address2_var)
        ent_address2.grid(row = 6,column = 1)


        lbl_postal_code = tk.Label(frm_data_left,text = 'Postal Code:',font = ('helvetica',12,'bold'),
                              padx = 2, pady = 6, bg = 'powder blue')
        lbl_postal_code.grid(row = 7,column = 0,sticky = 'w')

        ent_postal_code = tk.Entry(frm_data_left,font = ('helvetica',12,'bold'), width = entry_width,
                                   textvariable = self.postcode_var)
        ent_postal_code.grid(row = 7,column = 1)


        lbl_mobile_no = tk.Label(frm_data_left,text = 'Mobile No.:',font = ('helvetica',12,'bold'),
                              padx = 2, pady = 6, bg = 'powder blue')
        lbl_mobile_no.grid(row = 8,column = 0,sticky = 'w')

        ent_mobile_no = tk.Entry(frm_data_left,font = ('helvetica',12,'bold'), width = entry_width,
                                 textvariable = self.mobile_var)
        ent_mobile_no.grid(row = 8,column = 1)


        # Book details


        lbl_book_id = tk.Label(frm_data_left,text = 'Book ID:',font = ('helvetica',12,'bold'),
                              padx = 2, pady = 6, bg = 'powder blue')
        lbl_book_id.grid(row = 0,column = 2,sticky = 'w')

        ent_book_id = tk.Entry(frm_data_left,font = ('helvetica',12,'bold'), width = entry_width,
                               textvariable = self.bookid_var)
        ent_book_id.grid(row = 0,column = 3)


        lbl_book_title = tk.Label(frm_data_left, text = 'Book Title:', font = ('helvetica',12,'bold'),
                              padx = 2, pady = 6, bg = 'powder blue')
        lbl_book_title.grid(row = 1, column = 2, sticky = 'w')

        ent_book_title = tk.Entry(frm_data_left, font = ('helvetica',12,'bold'), width = entry_width,
                                  textvariable = self.booktitle_var)
        ent_book_title.grid(row = 1, column = 3)


        lbl_author = tk.Label(frm_data_left, text = 'Author:', font = ('helvetica',12,'bold'),
                              padx = 2, pady = 6, bg = 'powder blue')
        lbl_author.grid(row = 2, column = 2, sticky = 'w')

        ent_author = tk.Entry(frm_data_left, font = ('helvetica',12,'bold'), width = entry_width,
                              textvariable = self.author_var)
        ent_author.grid(row = 2, column = 3)


        lbl_date_borrowed = tk.Label(frm_data_left, text = 'Date Borrowed:', font = ('helvetica',12,'bold'),
                              padx = 2, pady = 6, bg = 'powder blue')
        lbl_date_borrowed.grid(row = 3, column = 2, sticky = 'w')

        ent_date_borrowed = tk.Entry(frm_data_left, font = ('helvetica',12,'bold'), width = entry_width,
                                     textvariable = self.dateborrowed_var)
        ent_date_borrowed.grid(row = 3, column = 3)


        lbl_date_due = tk.Label(frm_data_left, text = 'Date due:',font = ('helvetica',12,'bold'),
                              padx = 2, pady = 6, bg = 'powder blue')
        lbl_date_due.grid(row = 4, column = 2, sticky = 'w')

        ent_date_due = tk.Entry(frm_data_left, font = ('helvetica',12,'bold'), width = entry_width,
                                textvariable = self.datedue_var)
        ent_date_due.grid(row = 4, column = 3)


        lbl_days_on_book = tk.Label(frm_data_left, text = 'Days on Book:',font = ('helvetica',12,'bold'),
                              padx = 2, pady = 6, bg = 'powder blue')
        lbl_days_on_book.grid(row = 5, column = 2, sticky = 'w')

        ent_days_on_book = tk.Entry(frm_data_left, font = ('helvetica',12,'bold'), width = entry_width,
                                    textvariable = self.daysonbook_var)
        ent_days_on_book.grid(row = 5, column = 3)


        lbl_late_return_fine = tk.Label(frm_data_left, text = 'Late Return Fee:',font = ('helvetica',12,'bold'),
                              padx = 2, pady = 6, bg = 'powder blue')
        lbl_late_return_fine.grid(row = 6, column = 2, sticky = 'w')

        ent_late_return_fine = tk.Entry(frm_data_left, font = ('helvetica',12,'bold'), width = entry_width,
                                        textvariable = self.latereturnfine_var)
        ent_late_return_fine.grid(row = 6, column = 3)


        lbl_date_overdue = tk.Label(frm_data_left, text = 'Date Overdue:',font = ('helvetica',12,'bold'),
                              padx = 2, pady = 6, bg = 'powder blue')
        lbl_date_overdue.grid(row = 7, column = 2, sticky = 'w')

        ent_date_overdue = tk.Entry(frm_data_left, font = ('helvetica',12,'bold'), width = entry_width,
                                    textvariable = self.daysoverdue_var)
        ent_date_overdue.grid(row = 7, column = 3)


        lbl_final_price = tk.Label(frm_data_left, text = 'Final Price:',font = ('helvetica',12,'bold'),
                              padx = 2, pady = 6, bg = 'powder blue')
        lbl_final_price.grid(row = 8, column = 2, sticky = 'w')

        ent_final_price = tk.Entry(frm_data_left, font = ('helvetica',12,'bold'), width = entry_width,
                                    textvariable = self.finalprice_var)
        ent_final_price.grid(row = 8, column = 3)





        #=================================Data Frame Right===================================
        frm_data_right = tk.LabelFrame(frame, text = 'Book Details',bg = 'powder blue',
                                fg = 'green',bd = 12,relief = 'ridge',font = ('helvetica',12,'bold'))
        frm_data_right.place(x = 910, y = 5, width = 560, height = 350)

        self.textbox = tk.Text(frm_data_right, font = ('helvetica',12,'bold'), width = 32,
                               height = 16, padx = 2, pady = 6)
        self.textbox.grid(row = 0, column = 2)

        list_books = ['Head First book','Learn Python the Hard Way','Python Programming','Python Cookbook',
                      'Intro to machine learning','Machine Techno','My Python','Josh Elif guru',
                      'Elite Jungle Python','Jungli Python','Machine Python','Advance Python',
                      'Intro Python','RedChilli Python','Ishq Python']
        
        def SelectBook(event):
            x = str(list_box.get(list_box.curselection()))

            if (x in ['Head First book','Ishq Python','Elite Jungle Python']):
                self.bookid_var.set('BKID5454')
                self.booktitle_var.set('Python Manual')
                self.author_var.set('Paul Berry')

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set('Rs.50')
                self.daysoverdue_var.set('No')
                self.finalprice_var.set('Rs.788')

            elif (x in ['Learn Python the Hard Way','RedChilli Python','Josh Elif guru']):
                self.bookid_var.set('BKID6789')
                self.booktitle_var.set('Basic of Python')
                self.author_var.set('Zed A. Shaw')

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set('15')
                self.latereturnfine_var.set('Rs.25')
                self.daysoverdue_var.set('No')
                self.finalprice_var.set('Rs.725')


            elif (x in ['Intro Python','My Python']):
                self.bookid_var.set('BKID2354')
                self.booktitle_var.set('Intro to Python Computer Science')
                self.author_var.set('John Zhelle')

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set('15')
                self.latereturnfine_var.set('Rs.25')
                self.daysoverdue_var.set('No')
                self.finalprice_var.set('Rs.500')


            elif (x in ['Python Cookbook','Advance Python','Machine Python'] ):
                self.bookid_var.set('BKID2344')
                self.booktitle_var.set('Python Cookbook')
                self.author_var.set('Dylan Ader')

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set('15')
                self.latereturnfine_var.set('Rs.35')
                self.daysoverdue_var.set('No')
                self.finalprice_var.set('Rs.600')


            elif (x in ['Intro to machine learning','RedChilli Python']):
                self.bookid_var.set('BKID7854')
                self.booktitle_var.set('Intro to machine learning')
                self.author_var.set('Alan Border')

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set('15')
                self.latereturnfine_var.set('Rs.27')
                self.daysoverdue_var.set('No')
                self.finalprice_var.set('Rs.550')


            elif (x in ['Machine Techno', 'Python Programming','Jungli Python'] ):
                self.bookid_var.set('BKID2323')
                self.booktitle_var.set('Machine Techno')
                self.author_var.set('John Doe')

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set('05')
                self.latereturnfine_var.set('Rs.15')
                self.daysoverdue_var.set('No')
                self.finalprice_var.set('Rs.400')





        list_box = tk.Listbox(frm_data_right,font = ('helvetica',12,'bold'), width = 20,
                               height = 16)
        list_box.bind('<<ListboxSelect>>',SelectBook)
        list_box.grid(row = 0, column = 0, padx = 4)

        scrollbar_list = tk.Scrollbar(frm_data_right)
        scrollbar_list.grid(row = 0, column = 1,sticky = 'ns')
        scrollbar_list.config(command = list_box.yview)

        for item in list_books:
            list_box.insert('end',item)






        #===============================Buttons======================================
        frm_button = tk.Frame(self.root, bd = 12, relief = 'ridge', bg = 'powder blue', padx = 20)
        frm_button.place(x = 0, y = 530, width = 1530, height = 70)


        btn_add_data = tk.Button(frm_button,font = ('helvetica',12,'bold'), width = 23, bg = 'blue',
                                 fg = 'white',text = 'Add Data',command = self.add_data)
        btn_add_data.grid(row = 0,column = 0)

        btn_show_data = tk.Button(frm_button,font = ('helvetica',12,'bold'), width = 23, bg = 'blue',
                                 fg = 'white',text = 'Show Data',command = self.show_data)
        btn_show_data.grid(row = 0,column = 1)

        btn_update = tk.Button(frm_button,font = ('helvetica',12,'bold'), width = 23, bg = 'blue',
                                 fg = 'white',text = 'Update',command = self.update_data)
        btn_update.grid(row = 0,column = 2)

        btn_delete = tk.Button(frm_button,font = ('helvetica',12,'bold'), width = 23, bg = 'blue',
                                 fg = 'white',text = 'Delete',command = self.delete_data)
        btn_delete.grid(row = 0,column = 3)

        btn_reset = tk.Button(frm_button,font = ('helvetica',12,'bold'), width = 23, bg = 'blue',
                                 fg = 'white',text = 'Reset',command = self.reset)
        btn_reset.grid(row = 0,column = 4)

        btn_exit = tk.Button(frm_button,font = ('helvetica',12,'bold'), width = 23, bg = 'blue',
                                 fg = 'white',text = 'Exit',command = self.exit)
        btn_exit.grid(row = 0,column = 5)






        #================================Info Frame====================================
        frm_info = tk.Frame(self.root, bd = 12, relief = 'ridge', bg = 'powder blue', padx = 20)
        frm_info.place(x = 0, y = 600, width = 1530, height = 200)

        frm_table =tk.Frame(frm_info, bd = 6, relief = 'ridge', bg = 'powder blue')
        frm_table.place(x = 0, y = 2, width = 1460, height = 180)

        xscroll = ttk.Scrollbar(frm_table,orient = 'horizontal')
        yscroll = ttk.Scrollbar(frm_table,orient = 'vertical')

        heading_list = ['Member Type','PRN No.','ID No.','First Name','Last Name','Address 1','Address 2',
                        'Postal Code','Mobile No.','Book ID','Book Title','Author','Date Borrowed',
                        'Date Due','Days on Book','Late Return Fine','Date Overdue','Final Price']
        
        hd_list = ['membertype','prnno','title','firstname','lastname','address1','address2',
                    'postid','mobile','bookid','booktitle','author','dateborrowed','datedue','daysonbook',
                    'latereturnfine','dateoverdue','finalprice']

        self.library_table = ttk.Treeview(frm_table,columns = hd_list, xscrollcommand = xscroll,
                                        yscrollcommand = yscroll)
        xscroll.pack(side = 'bottom', fill = 'x')
        yscroll.pack(side = 'right',fill = 'y')

        xscroll.config(command = self.library_table.xview)
        yscroll.config(command = self.library_table.yview)

        for i in range(len(heading_list)):
            self.library_table.heading(hd_list[i],text = heading_list[i])
            self.library_table.column(hd_list[i],width = 100)
        

        self.library_table['show'] = 'headings'
        self.library_table.pack(fill = 'both',expand = 1)
        self.fetch_data()
        self.library_table.bind('<ButtonRelease-1>',self.get_cursor)



    def add_data(self):
        connect = pymysql.connect(host = 'localhost', user = 'root', passwd = 'root',
                                  database = 'library_management_system')
        cursor = connect.cursor()

        comm = 'insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

        cursor.execute(comm,(
                       self.member_var.get(),
                       self.prn_var.get(),
                       self.id_var.get(),
                       self.firstname_var.get(),
                       self.lastname_var.get(),
                       self.address1_var.get(),
                       self.address2_var.get(),
                       self.postcode_var.get(),
                       self.mobile_var.get(),
                       self.bookid_var.get(),
                       self.booktitle_var.get(),
                       self.author_var.get(),
                       self.dateborrowed_var.get(),
                       self.datedue_var.get(),
                       self.daysonbook_var.get(),
                       self.latereturnfine_var.get(),
                       self.daysoverdue_var.get(),
                       self.finalprice_var.get()
                       ))
        connect.commit()
        self.fetch_data()
        connect.close()
        messagebox.showinfo('Success','Member has been inserted successfully.')


    def update_data(self):
        connect = pymysql.connect(host = 'localhost', user = 'root', passwd = 'root',
                                  database = 'library_management_system')
        cursor = connect.cursor()
        query = 'update library set Member=%s,PRN_NO=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostID=%s,Mobile=%s,BookID=%s,BookTitle=%s,Author=%s,DateBorrowed=%s,DateDue=%s,DaysonBook=%s,LateReturnFine=%s,DateOverdue=%s,Finalprice=%s where PRN_NO=%s'

        cursor.execute(query,(
                       self.member_var.get(),
                       self.prn_var.get(),
                       self.id_var.get(),
                       self.firstname_var.get(),
                       self.lastname_var.get(),
                       self.address1_var.get(),
                       self.address2_var.get(),
                       self.postcode_var.get(),
                       self.mobile_var.get(),
                       self.bookid_var.get(),
                       self.booktitle_var.get(),
                       self.author_var.get(),
                       self.dateborrowed_var.get(),
                       self.datedue_var.get(),
                       self.daysonbook_var.get(),
                       self.latereturnfine_var.get(),
                       self.daysoverdue_var.get(),
                       self.finalprice_var.get(),
                       self.prn_var.get()
                       ))
        connect.commit()
        self.fetch_data()
        self.reset()
        connect.close()

        messagebox.showinfo('Updated','Info updated successfully')


    def fetch_data(self):
        connect = pymysql.connect(host = 'localhost', user = 'root', passwd = 'root',
                                  database = 'library_management_system')
        cursor = connect.cursor()
        cursor.execute('select * from library')
        rows = cursor.fetchall()

        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert('','end',values = i)
                connect.commit()

        connect.close()


    def get_cursor(self,event = ''):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']

        self.member_var.set(row[0])
        self.prn_var.set(row[1])
        self.id_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.postcode_var.set(row[7])
        self.mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])
        self.author_var.set(row[11])
        self.dateborrowed_var.set(row[12])
        self.datedue_var.set(row[13])
        self.daysonbook_var.set(row[14])
        self.latereturnfine_var.set(row[15])
        self.daysoverdue_var.set(row[16])
        self.finalprice_var.set(row[17])


    def show_data(self):
        self.textbox.delete('1.0','end')
        self.textbox.insert('end','Member Type:\t\t'+self.member_var.get()+'\n')
        self.textbox.insert('end','PRN No.:\t\t'+self.prn_var.get()+'\n')
        self.textbox.insert('end','ID No.:\t\t'+self.id_var.get()+'\n')
        self.textbox.insert('end','First Name:\t\t'+self.firstname_var.get()+'\n')
        self.textbox.insert('end','Last Name:\t\t'+self.lastname_var.get()+'\n')
        self.textbox.insert('end','Address1:\t\t'+self.address1_var.get()+'\n')
        self.textbox.insert('end','Address2:\t\t'+self.address2_var.get()+'\n')
        self.textbox.insert('end','Postal Code:\t\t'+self.postcode_var.get()+'\n')
        self.textbox.insert('end','Mobile No.:\t\t'+self.mobile_var.get()+'\n')
        self.textbox.insert('end','Book ID.:\t\t'+self.bookid_var.get()+'\n')
        self.textbox.insert('end','Book Title:\t\t'+self.booktitle_var.get()+'\n')
        self.textbox.insert('end','Author:\t\t'+self.author_var.get()+'\n')
        self.textbox.insert('end','Date Borrowed:\t\t'+self.dateborrowed_var.get()+'\n')
        self.textbox.insert('end','Date Due:\t\t'+self.datedue_var.get()+'\n')
        self.textbox.insert('end','Days on Book:\t\t'+self.daysonbook_var.get()+'\n')
        self.textbox.insert('end','Late Return Fine:\t\t'+self.latereturnfine_var.get()+'\n')
        self.textbox.insert('end','Date Overdue:\t\t'+self.daysoverdue_var.get()+'\n')
        self.textbox.insert('end','Final Price:\t\t'+self.finalprice_var.get()+'\n')
        

    def reset(self):
        self.member_var.set('')
        self.prn_var.set('')
        self.id_var.set('')
        self.firstname_var.set('')
        self.lastname_var.set('')
        self.address1_var.set('')
        self.address2_var.set('')
        self.postcode_var.set('')
        self.mobile_var.set('')
        self.bookid_var.set('')
        self.booktitle_var.set('')
        self.author_var.set('')
        self.dateborrowed_var.set('')
        self.datedue_var.set('')
        self.daysonbook_var.set('')
        self.latereturnfine_var.set('')
        self.daysoverdue_var.set('')
        self.finalprice_var.set('')
        self.textbox.delete('1.0','end')


    def exit(self):
        exit_prompt = messagebox.askyesno('Exit Confirmation','Do you want to exit?')
        if exit_prompt:
            self.root.destroy()


    def delete_data(self):
        if self.prn_var.get() == '' or self.id_var.get() == '':
            messagebox.showerror('Invalid','First Give the PRN No. or id to delete')

        else:
            connect = pymysql.connect(host = 'localhost', user = 'root', passwd = 'root',
                                  database = 'library_management_system')
            cursor = connect.cursor()
            query ='delete from library where PRN_NO=%s'
            cursor.execute(query,(self.prn_var.get(),))

            connect.commit()
            self.fetch_data()
            self.reset()
            connect.close()
            messagebox.showinfo('Success','Data has been deleted')
        
        





if __name__ == '__main__':
    root = tk.Tk()
    lib = LibraryManagementSystem(root)
    root.mainloop()