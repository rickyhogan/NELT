from Tkinter import *
import ScrolledText as tkst
import Tkinter as tk
import nelt_functions as Func
import ttk

class Main(tk.Frame):
    
    def __init__(self, parent, controller, *args, **kwargs):
        self.controller = controller
        Frame.__init__(self, parent, *args, **kwargs)
        self.frame1 = Frame(self, borderwidth=2, highlightbackground='grey', highlightthickness=2)
        self.frame1.pack(fill=BOTH, side=TOP,pady=5,padx=5,expand=True)
        self.frame2 = Frame(self, borderwidth=2, highlightbackground='grey', highlightthickness=2)
        self.frame2.pack(fill=BOTH, side=BOTTOM,pady=5,padx=5,expand=True)
        self.labels()
        self.entrys()
        self.option_menu()
        self.customer_listbox()
        self.truck_listbox()
        self.buttons()
        self.bind("<<showframe>>", lambda event: Func.Customer_Function().load_lb(event,self))


    def labels(self):
        title_label = Label(self.frame1,
                            text='Company Information',font='bold')
        search_label = Label(self.frame1,
                           text='Search By :')
        search2_label = Label(self.frame2,
                           text='Search By :')
        title2_label = Label(self.frame2,
                            text='Equipment Information',font='bold')

        title_label.grid(row=0, column=0, columnspan=2, pady=5, padx=5,sticky=N+S+E+W)
        title2_label.grid(row=0, column=0, columnspan=2, pady=5, padx=5,sticky=N+S+E+W)
        search_label.grid(row=1, column=0, pady=5,padx=5, sticky=W)
        search2_label.grid(row=1, column=0, pady=5,padx=5, sticky=W)
        
    def entrys(self):
        global company_entry_var,truck_entry_var,truck_entry
        
        company_entry_var = StringVar()
        truck_entry_var = StringVar()

        x = lambda *args :Func.Customer_Function().company_entry_search(self,*args)
        y = lambda *args :Func.Customer_Function().truck_entry_search(self,*args)
        company_entry_var.trace('w',x)
        truck_entry_var.trace('w',y)
        company_entry = Entry(self.frame1, textvariable=company_entry_var)
        truck_entry = Entry(self.frame2, textvariable=truck_entry_var, state='disabled')
        company_entry.grid(row=1, column=1, padx=5, pady=5, stick=E+W)
        truck_entry.grid(row=1, column=1, padx=5, pady=5, stick=E+W)

    def customer_listbox(self):
        global new_customer_lb
        
        scrollbar = Scrollbar(self.frame1, orient="vertical")
        new_customer_lb = ttk.Treeview(self.frame1, columns=('ID','Company','City','Contact Number','Street Address'))
        new_customer_lb['show']='headings'
        new_customer_lb.heading('#1', text= 'ID')
        new_customer_lb.column('#1', width=50, stretch=NO)
        new_customer_lb.heading('#2', text= 'Company', command=lambda:Func.Customer_Function().sort_status(self, 'first'))
        new_customer_lb.column('#2', width=225, stretch=NO)
        new_customer_lb.heading('#3', text= 'City', command=lambda:Func.Customer_Function().sort_status(self, 'city'))
        new_customer_lb.column('#3', width=100, stretch=NO)
        new_customer_lb.heading('#4', text= 'Contact Number', command=lambda:Func.Customer_Function().sort_status(self, 'contact'))
        new_customer_lb.column('#4', width=125, stretch=NO)
        new_customer_lb.heading('#5', text= 'Street Address', command=lambda:Func.Customer_Function().sort_status(self, 'address'))
        new_customer_lb.column('#5', width=300, stretch=YES)
        new_customer_lb.configure(yscroll = scrollbar.set, selectmode="browse")
        new_customer_lb.tag_configure('oddrow', background='blue')
        scrollbar.config(command=new_customer_lb.yview)
        self.tag_background = ["odd","even"]
        new_customer_lb.tag_configure("odd",background='light grey',foreground='black')
        new_customer_lb.tag_configure("even",background='gray',foreground='black')
        new_customer_lb.grid(row=2, column=0, columnspan=2, sticky=N+S+W+E, padx=5)
        new_customer_lb.bind("<<TreeviewSelect>>", lambda event: Func.Customer_Function().customer_lb_click(event,self))

    def truck_listbox(self):
        global truck_lb
        
        scrollbar = Scrollbar(self.frame2, orient="vertical")
        truck_lb = ttk.Treeview(self.frame2, columns=('ID','Make','T/N','Model','Serial Number'))
        truck_lb['show']='headings'
        truck_lb.heading('#1', text= 'ID')
        truck_lb.column('#1', width=50, stretch=NO)
        truck_lb.heading('#2', text= 'Make', command=lambda:Func.Customer_Function().sort_truck(self, 'make'))
        truck_lb.column('#2', width=200, stretch=NO)
        truck_lb.heading('#3', text= 'T/N', command=lambda:Func.Customer_Function().sort_truck(self, 't/n'))
        truck_lb.column('#3', width=50, stretch=NO)
        truck_lb.heading('#4', text= 'Model', command=lambda:Func.Customer_Function().sort_truck(self, 'model'))
        truck_lb.column('#4', width=200, stretch=NO)
        truck_lb.heading('#5', text= 'Serial Number', command=lambda:Func.Customer_Function().sort_truck(self, 'serial'))
        truck_lb.column('#5', width=300, stretch=YES)
        truck_lb.configure(yscroll = scrollbar.set, selectmode="browse")
        truck_lb.tag_configure('oddrow', background='blue')
        scrollbar.config(command=truck_lb.yview)
        self.tag_background = ["odd","even"]
        truck_lb.tag_configure("odd",background='light grey',foreground='black')
        truck_lb.tag_configure("even",background='gray',foreground='black')
        truck_lb.grid(row=2, column=0, columnspan=2, sticky=N+S+W+E, padx=5)
        truck_lb.bind("<<TreeviewSelect>>", lambda event: Func.Customer_Function().truck_lb_click(event,self))

    def option_menu(self):
        global company_var,truck_var
        
        company = ['Company Name','City','Contact Number']
        truck = ['Truck Model','Truck Number','Truck Serial Number']

        company_var = StringVar()
        truck_var = StringVar()
        company_var.set(company[0])
        truck_var.set(truck[2])
        company_dropbox = OptionMenu(self.frame1, company_var, *company)
        truck_dropbox = OptionMenu(self.frame2, truck_var, *truck)
        company_dropbox.grid(row=1, column=0, padx=5)
        truck_dropbox.grid(row=1, column=0, padx=5)


    def buttons(self):
        global new_company_button,edit_company_button,add_truck_button,view_information_button,delete_truck_button
        
        new_company_button = Button(self.frame1,
                             text='Add Company', command=lambda:Func.Customer_Function().add_company(self))
        edit_company_button = Button(self.frame1, state='disabled',
                             text='Edit Company', command=lambda:Func.Customer_Function().edit_company(self))
        add_truck_button = Button(self.frame1, state='disabled',
                             text='Add Equipment', command=lambda:Func.Customer_Function().add_equipment(self))
        view_information_button = Button(self.frame2, state='disabled',
                             text='Add/View Information', command=lambda:Func.Customer_Function().view_equipment(self))
        delete_truck_button = Button(self.frame2, state='disabled',
                             text='Remove Equipment', command=lambda:Func.Customer_Function().remove_equipment(self))

        new_company_button.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        edit_company_button.grid(row=3, column=0, padx=5, pady=5)
        add_truck_button.grid(row=3, column=1, sticky=E, padx=5, pady=5)
        view_information_button.grid(row=3, column=0, sticky=E, padx=5, pady=5)
        delete_truck_button.grid(row=3, column=0, sticky=W, padx=5, pady=5)

class Add_Company(tk.Frame):
    
    def __init__(self, parent, controller, *args, **kwargs):
        self.controller = controller
        Frame.__init__(self, parent, *args, **kwargs)
        self.labels()
        self.entrys()
        self.buttons()

    def labels(self):
        title_label = Label(self,
                            text='Please fill all fields')

        name_label = Label(self,
                           text='Company Name :')

        address_label = Label(self,
                              text='Company Address :')

        city_label = Label(self,
                           text='City :')

        state_label = Label(self,
                           text='State :')

        phone_label = Label(self,
                           text='Phone Number :')
        
        title_label.grid(row=0, column=0, columnspan=2, pady=5, padx=5)
        name_label.grid(row=1, column=0, pady=5, padx=5, sticky=W)
        address_label.grid(row=2, column=0, pady=5, padx=5, sticky=W)
        city_label.grid(row=3, column=0, pady=5, padx=5, sticky=W)
        state_label.grid(row=4, column=0, pady=5, padx=5, sticky=W)
        phone_label.grid(row=5, column=0, pady=5, padx=5, sticky=W)
        
    def entrys(self):
        global name_var,address_var,city_var,state_var,phone_var
        
        name_var = StringVar()
        address_var = StringVar()
        city_var = StringVar()
        state_var = StringVar()
        phone_var = StringVar()

        self.name_entry = Entry(self, textvariable=name_var)
        self.address_entry = Entry(self, textvariable=address_var)
        self.city_entry = Entry(self, textvariable=city_var)
        self.state_entry = Entry(self, textvariable=state_var)
        self.phone_entry = Entry(self, textvariable=phone_var)

        self.name_entry.grid(row=1, column=1, padx=5, pady=5)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5)
        self.city_entry.grid(row=3, column=1, padx=5, pady=5)
        self.state_entry.grid(row=4, column=1, padx=5, pady=5)
        self.phone_entry.grid(row=5, column=1, padx=5, pady=5)


    def buttons(self):
        save_button = Button(self,
                             text='Save Company', command=lambda:Func.Add_company().save_company(self))
        cancel_button = Button(self,
                             text='Cancel', command=lambda:Func.Add_company().cancel_add(self))

        save_button.grid(row=6, column=1,padx=5, pady=5)
        cancel_button.grid(row=6, column=0,padx=5, pady=5)

class Edit_Company(tk.Frame):
    
    def __init__(self, parent, controller, *args, **kwargs):
        self.controller = controller
        Frame.__init__(self, parent, *args, **kwargs)
        self.labels()
        self.entrys()
        self.buttons()

    def labels(self):
        title_label = Label(self,
                            text='Please fill all fields')

        name_label = Label(self,
                           text='Company Name :')

        address_label = Label(self,
                              text='Company Address :')

        city_label = Label(self,
                           text='City :')

        state_label = Label(self,
                           text='State :')

        phone_label = Label(self,
                           text='Phone Number :')
        
        title_label.grid(row=0, column=0, columnspan=2, pady=5, padx=5)
        name_label.grid(row=1, column=0, pady=5, padx=5, sticky=W)
        address_label.grid(row=2, column=0, pady=5, padx=5, sticky=W)
        city_label.grid(row=3, column=0, pady=5, padx=5, sticky=W)
        state_label.grid(row=4, column=0, pady=5, padx=5, sticky=W)
        phone_label.grid(row=5, column=0, pady=5, padx=5, sticky=W)
        
    def entrys(self):
        global edit_name_var,edit_address_var,edit_city_var,edit_state_var,edit_phone_var
        
        edit_name_var = StringVar()
        edit_address_var = StringVar()
        edit_city_var = StringVar()
        edit_state_var = StringVar()
        edit_phone_var = StringVar()

        self.name_entry = Entry(self, textvariable=edit_name_var)
        self.address_entry = Entry(self, textvariable=edit_address_var)
        self.city_entry = Entry(self, textvariable=edit_city_var)
        self.state_entry = Entry(self, textvariable=edit_state_var)
        self.phone_entry = Entry(self, textvariable=edit_phone_var)

        self.name_entry.grid(row=1, column=1, padx=5, pady=5)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5)
        self.city_entry.grid(row=3, column=1, padx=5, pady=5)
        self.state_entry.grid(row=4, column=1, padx=5, pady=5)
        self.phone_entry.grid(row=5, column=1, padx=5, pady=5)


    def buttons(self):
        save_button = Button(self,
                             text='Save Company', command=lambda:Func.Edit_company().save_company(self))
        cancel_button = Button(self,
                             text='Cancel', command=lambda:Func.Edit_company().cancel_add(self))

        save_button.grid(row=6, column=1,padx=5, pady=5)
        cancel_button.grid(row=6, column=0,padx=5, pady=5)
        
class Information(tk.Frame):
    
    def __init__(self, parent, controller, *args, **kwargs):
        self.controller = controller
        Frame.__init__(self, parent, *args, **kwargs)
        self.labels()
        self.entrys()
        self.textbox()
        self.buttons()

    def labels(self):
        title_label = Label(self,
                            text='Please fill all fields')
        
        make_label = Label(self,
                           text='Equipment Make :')

        model_label = Label(self,
                           text='Model :')

        serial_label = Label(self,
                              text='Serial Number :')

        number_label = Label(self,
                           text='Equipment Number :')
        
        end_label = Label(self,
                            text='Enter Information Below :')
        
        title_label.grid(row=0, column=0, columnspan=2, pady=5, padx=5)
        make_label.grid(row=1, column=0, pady=5, padx=5, sticky=W)
        model_label.grid(row=2, column=0, pady=5, padx=5, sticky=W)
        serial_label.grid(row=3, column=0, pady=5, padx=5, sticky=W)
        number_label.grid(row=4, column=0, pady=5, padx=5, sticky=W)
        end_label.grid(row=5, column=0, columnspan=2, pady=5, padx=5)
        
    def entrys(self):
        global make_var,model_var,serial_var,number_var
        
        make_var = StringVar()
        model_var = StringVar()
        serial_var = StringVar()
        number_var = StringVar()

        self.make_entry = Entry(self, textvariable=make_var)
        self.model_entry = Entry(self, textvariable=model_var)
        self.serial_entry = Entry(self, textvariable=serial_var)
        self.number_entry = Entry(self, textvariable=number_var)

        self.make_entry.grid(row=1, column=1, padx=5, pady=5, sticky=E+W)
        self.model_entry.grid(row=2, column=1, padx=5, pady=5, sticky=E+W)
        self.serial_entry.grid(row=3, column=1, padx=5, pady=5, sticky=E+W)
        self.number_entry.grid(row=4, column=1, padx=5, pady=5, sticky=E+W)

        self.columnconfigure(1, weight=2)

    def textbox(self):
        global txt
        txt = tkst.ScrolledText(self,width=100,height=20)
        txt.grid(row=6, column=0, columnspan=2, pady=5, padx=5)

    def buttons(self):
        save_button = Button(self,
                             text='Save Equipment', command=lambda:Func.Add_equipment().save_equipment(self))
        cancel_button = Button(self,
                             text='Cancel', command=lambda:Func.Add_equipment().cancel_add(self))

        save_button.grid(row=7, column=1,padx=5, pady=5)
        cancel_button.grid(row=7, column=0,padx=5, pady=5)

class Edit_Information(tk.Frame):
    
    def __init__(self, parent, controller, *args, **kwargs):
        self.controller = controller
        Frame.__init__(self, parent, *args, **kwargs)
        self.labels()
        self.entrys()
        self.textbox()
        self.buttons()

    def labels(self):
        title_label = Label(self,
                            text='Please fill all fields')
        
        make_label = Label(self,
                           text='Equipment Make :')

        model_label = Label(self,
                           text='Model :')

        serial_label = Label(self,
                              text='Serial Number :')

        number_label = Label(self,
                           text='Equipment Number :')
        
        end_label = Label(self,
                            text='Enter Information Below :')
        
        title_label.grid(row=0, column=0, columnspan=2, pady=5, padx=5)
        make_label.grid(row=1, column=0, pady=5, padx=5, sticky=W)
        model_label.grid(row=2, column=0, pady=5, padx=5, sticky=W)
        serial_label.grid(row=3, column=0, pady=5, padx=5, sticky=W)
        number_label.grid(row=4, column=0, pady=5, padx=5, sticky=W)
        end_label.grid(row=5, column=0, columnspan=2, pady=5, padx=5)
        
    def entrys(self):
        global edit_make_var,edit_model_var,edit_serial_var,edit_number_var
        
        edit_make_var = StringVar()
        edit_model_var = StringVar()
        edit_serial_var = StringVar()
        edit_number_var = StringVar()

        self.make_entry = Entry(self, textvariable=edit_make_var)
        self.model_entry = Entry(self, textvariable=edit_model_var)
        self.serial_entry = Entry(self, textvariable=edit_serial_var)
        self.number_entry = Entry(self, textvariable=edit_number_var)

        self.make_entry.grid(row=1, column=1, padx=5, pady=5, sticky=E+W)
        self.model_entry.grid(row=2, column=1, padx=5, pady=5, sticky=E+W)
        self.serial_entry.grid(row=3, column=1, padx=5, pady=5, sticky=E+W)
        self.number_entry.grid(row=4, column=1, padx=5, pady=5, sticky=E+W)

        self.columnconfigure(1, weight=2)

    def textbox(self):
        global edit_txt
        edit_txt = tkst.ScrolledText(self,width=100,height=20)
        edit_txt.grid(row=6, column=0, columnspan=2, pady=5, padx=5)

    def buttons(self):
        save_button = Button(self,
                             text='Save Equipment', command=lambda:Func.Edit_equipment().save_equipment(self))
        cancel_button = Button(self,
                             text='Cancel', command=lambda:Func.Edit_equipment().cancel_add(self))

        save_button.grid(row=7, column=1,padx=5, pady=5)
        cancel_button.grid(row=7, column=0,padx=5, pady=5)
