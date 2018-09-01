from Tkinter import *
import Tkinter as tk
import nelt_backbone_funcs as BBF
import nelt_sql_functions as sql
import nelt_gui as Ap
import __main__ as M
import os.path

class Customer_Function():
    
    def __init__(var):
        var.new_customer_lb = Ap.new_customer_lb
        var.truck_lb = Ap.truck_lb
        var.curitem_truck = var.truck_lb.selection()
        var.contents_truck = (var.truck_lb.item(var.curitem_truck))
        var.selected_truck = var.contents_truck['values'] ### selected[0] = ID
        var.curitem = var.new_customer_lb.selection()
        var.contents = (var.new_customer_lb.item(var.curitem))
        var.selected = var.contents['values'] ### selected[0] = ID
        var.txt = Ap.txt
        var.make_var = Ap.make_var
        var.model_var = Ap.model_var
        var.serial_var = Ap.serial_var
        var.number_var = Ap.number_var
        var.name_var = Ap.name_var
        var.address_var = Ap.address_var
        var.city_var = Ap.city_var
        var.state_var = Ap.state_var
        var.phone_var = Ap.phone_var
        var.edit_name_var =Ap.edit_name_var
        var.edit_address_var = Ap.edit_address_var
        var.edit_city_var = Ap.edit_city_var
        var.edit_state_var = Ap.edit_state_var
        var.edit_phone_var = Ap.edit_phone_var
        var.edit_txt = Ap.edit_txt
        var.edit_make_var = Ap.edit_make_var
        var.edit_model_var = Ap.edit_model_var
        var.edit_serial_var = Ap.edit_serial_var
        var.edit_number_var = Ap.edit_number_var
        var.edit_company_button = Ap.edit_company_button
        var.add_truck_button = Ap.add_truck_button
        var.view_information_button = Ap.view_information_button
        var.delete_truck_button = Ap.delete_truck_button
        var.company_entry_var = Ap.company_entry_var
        var.truck_entry_var = Ap.truck_entry_var
        var.company_var = Ap.company_var.get()
        var.truck_var = Ap.truck_var.get()
        var.truck_entry = Ap.truck_entry
        
    def load_lb(var,event,self):
        var.new_customer_lb.delete(*var.new_customer_lb.get_children())
        sql.Company_SQL().load_company_lb(var,self)
        var.truck_lb.delete(*var.truck_lb.get_children())
        var.edit_company_button.config(state='disabled')
        var.add_truck_button.config(state='disabled')
        var.view_information_button.config(state='disabled')
        var.delete_truck_button.config(state='disabled')
        var.truck_entry.config(state='disabled')

    def make_db(var):
        if os.path.isfile("NELT.db"):
            print 'found'
        else:
            try:
                sql.Login_SQL().create_db(var)
            except:
                print 'error'


    def customer_lb_click(var,event,self):
        var.truck_lb.delete(*var.truck_lb.get_children())
        sql.Company_SQL().load_equipment_lb(var,self)
        var.edit_company_button.config(state='normal')
        var.add_truck_button.config(state='normal')
        var.truck_entry.config(state='normal')

    def sort_status(var,self,column):
        var.new_customer_lb.delete(*var.new_customer_lb.get_children())
        var.edit_company_button.config(state='disabled')
        var.add_truck_button.config(state='disabled')
        var.truck_entry.config(state='disabled')
        sql.Company_SQL().sort_company_lb(var,self,column)


    def truck_lb_click(var,event,self):
        var.view_information_button.config(state='normal')
        var.delete_truck_button.config(state='normal')

    def sort_truck(var,self,column):
        var.truck_lb.delete(*var.truck_lb.get_children())
        var.view_information_button.config(state='disabled')
        var.delete_truck_button.config(state='disabled')
        sql.Company_SQL().sort_truck_lb(var,self,column)
        
    def add_company(var,self):
        M.app.show_frame(Ap.Add_Company)

    def edit_company(var,self):
        sql.Company_SQL().load_company_field(var,self)
        M.app.show_frame(Ap.Edit_Company)

    def add_equipment(var,self):
        M.app.show_frame(Ap.Information)

    def view_equipment(var,self):
        sql.Company_SQL().load_equipment_field(var,self)
        M.app.show_frame(Ap.Edit_Information)

    def remove_equipment(var,self):
        sql.Company_SQL().remove_equipment(var,self)
        var.truck_lb.delete(*var.truck_lb.get_children())
        sql.Company_SQL().load_equipment_lb(var,self)
        var.view_information_button.config(state='disabled')
        var.delete_truck_button.config(state='disabled')

    def company_entry_search(var,self,*args):
        var.new_customer_lb.delete(*var.new_customer_lb.get_children())
        sql.Company_SQL().search_company_entry(var,self)
        var.edit_company_button.config(state='disabled')
        var.add_truck_button.config(state='disabled')
        var.truck_entry.config(state='disabled')
        
    def truck_entry_search(var,self,*args):
        var.truck_lb.delete(*var.truck_lb.get_children())
        sql.Company_SQL().search_truck_entry(var,self)
        var.view_information_button.config(state='disabled')
        var.delete_truck_button.config(state='disabled')

        
class Add_company():

    def __init__(var):
        var.new_customer_lb = Ap.new_customer_lb
        var.name_var =Ap.name_var
        var.address_var = Ap.address_var
        var.city_var = Ap.city_var
        var.state_var = Ap.state_var
        var.phone_var = Ap.phone_var

    def cancel_add(var,self):
        M.app.show_frame(Ap.Main)
        self.name_entry.delete(0,END)
        self.address_entry.delete(0,END)
        self.city_entry.delete(0,END)
        self.state_entry.delete(0,END)
        self.phone_entry.delete(0,END)

    def save_company(var,self):
        sql.Company_SQL().save_new_customer(var,self)
        M.app.show_frame(Ap.Main)
        self.name_entry.delete(0,END)
        self.address_entry.delete(0,END)
        self.city_entry.delete(0,END)
        self.state_entry.delete(0,END)
        self.phone_entry.delete(0,END)
        
class Edit_company():

    def __init__(var):
        var.new_customer_lb = Ap.new_customer_lb
        var.curitem = var.new_customer_lb.selection()
        var.contents = (var.new_customer_lb.item(var.curitem))
        var.selected = var.contents['values'] ### selected[0] = ID
        var.new_customer_lb = Ap.new_customer_lb
        var.edit_name_var =Ap.edit_name_var
        var.edit_address_var = Ap.edit_address_var
        var.edit_city_var = Ap.edit_city_var
        var.edit_state_var = Ap.edit_state_var
        var.edit_phone_var = Ap.edit_phone_var

    def cancel_add(var,self):
        M.app.show_frame(Ap.Main)
        self.name_entry.delete(0,END)
        self.address_entry.delete(0,END)
        self.city_entry.delete(0,END)
        self.state_entry.delete(0,END)
        self.phone_entry.delete(0,END)

    def save_company(var,self):
        sql.Company_SQL().save_edit_customer(var,self)
        M.app.show_frame(Ap.Main)
        self.name_entry.delete(0,END)
        self.address_entry.delete(0,END)
        self.city_entry.delete(0,END)
        self.state_entry.delete(0,END)
        self.phone_entry.delete(0,END)
        
class Add_equipment():

    def __init__(var):
        var.new_customer_lb = Ap.new_customer_lb
        var.curitem = var.new_customer_lb.selection()
        var.contents = (var.new_customer_lb.item(var.curitem))
        var.selected = var.contents['values'] ### selected[0] = ID
        var.txt = Ap.txt
        var.make_var = Ap.make_var
        var.model_var = Ap.model_var
        var.serial_var = Ap.serial_var
        var.number_var = Ap.number_var

    def save_equipment(var,self):
        sql.Company_SQL().save_equipment(var,self)
        M.app.show_frame(Ap.Main)
        self.make_entry.delete(0,END)
        self.model_entry.delete(0,END)
        self.serial_entry.delete(0,END)
        self.number_entry.delete(0,END)
        var.txt.delete(1.0,END)
        
    def cancel_add(var,self):
        M.app.show_frame(Ap.Main)
        self.make_entry.delete(0,END)
        self.model_entry.delete(0,END)
        self.serial_entry.delete(0,END)
        self.number_entry.delete(0,END)
        var.txt.delete(1.0,END)

class Edit_equipment():

    def __init__(var):
        var.truck_lb = Ap.truck_lb
        var.curitem_truck = var.truck_lb.selection()
        var.contents_truck = (var.truck_lb.item(var.curitem_truck))
        var.selected_truck = var.contents_truck['values'] ### selected[0] = ID
        var.edit_txt = Ap.edit_txt
        var.edit_make_var = Ap.edit_make_var
        var.edit_model_var = Ap.edit_model_var
        var.edit_serial_var = Ap.edit_serial_var
        var.edit_number_var = Ap.edit_number_var

    def save_equipment(var,self):
        sql.Company_SQL().save_edit_equipment(var,self)
        M.app.show_frame(Ap.Main)
        self.make_entry.delete(0,END)
        self.model_entry.delete(0,END)
        self.serial_entry.delete(0,END)
        self.number_entry.delete(0,END)
        var.edit_txt.delete(1.0,END)
        
    def cancel_add(var,self):
        M.app.show_frame(Ap.Main)
        self.make_entry.delete(0,END)
        self.model_entry.delete(0,END)
        self.serial_entry.delete(0,END)
        self.number_entry.delete(0,END)
        var.edit_txt.delete(1.0,END)
