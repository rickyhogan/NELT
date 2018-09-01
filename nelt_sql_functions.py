from Tkinter import *
import tkMessageBox
import nelt_backbone_funcs as BBF
from sqlalchemy.sql import exists
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date, datetime


base = declarative_base()

class Company(base):
    __tablename__='Company'
    Id = Column(Integer, primary_key=True)
    name = Column(String(64))
    address = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))
    phone = Column(String(64))

class Equipment(base):
    __tablename__='Equipment'
    Id = Column(Integer, primary_key=True)
    make = Column(String(64))
    model = Column(String(64))
    serial = Column(String(64))
    number = Column(String(64))
    information = Column(Text)
    company_id = Column(Integer, ForeignKey('Company.Id'))
    company_equipment = relationship(Company)

class DB_connection(object):
    def __enter__(variable):
        variable.engine = create_engine("sqlite:///NELT.db")
        base.metadata.bind = variable.engine
        variable.DBSession = sessionmaker(bind=variable.engine)
        variable.Session = variable.DBSession
        variable.session = variable.Session()
        return variable
    def __exit__(variable, exc_type, exc_val, exc_tb):
        variable.session.commit()
        variable.session.close()

class Login_SQL():
    
    def __init__(variable):
        pass
    
    def create_db(variable,var):
        print"start create db function"
        engine = create_engine('sqlite:///NELT.db')
        base.metadata.create_all(engine)
        print"Success create db function"

class Company_SQL():

    def __init__(variable):
        variable.truck_col = Equipment.Id
        variable.company_col = Company.Id

    def load_company_lb(variable,var,self):
        print'load'
        with DB_connection() as DB:
            for a,b,c,d,e,f in DB.session.query(Company.Id,Company.name,Company.address,Company.city,Company.
                                            state,Company.phone).order_by(Company.Id):
                if a % 2 == 0:
                    var.new_customer_lb.insert('','end', values=(a,b,c,d,e,f), tags=self.tag_background[0])
                if a % 2 != 0:
                    var.new_customer_lb.insert('','end', values=(a,b,c,d,e,f), tags=self.tag_background[1])

    def load_equipment_lb(variable,var,self):
        with DB_connection() as DB:
            for a,b,c,d,e in DB.session.query(Equipment.Id,Equipment.make,Equipment.number,Equipment.model,Equipment.
                                            serial).filter(Equipment.company_id == var.selected[0]).order_by(Equipment.Id):
                if a % 2 == 0:
                    var.truck_lb.insert('','end', values=(a,b,c,d,e), tags=self.tag_background[0])
                if a % 2 != 0:
                    var.truck_lb.insert('','end', values=(a,b,c,d,e), tags=self.tag_background[1])

    def load_equipment_field(variable,var,self):
         with DB_connection() as DB:
            user = DB.session.query(Equipment)
            user = user.filter(Equipment.Id == var.selected_truck[0])
            for a in user:
                var.edit_make_var.set(a.make)
                var.edit_model_var.set(a.model)
                var.edit_serial_var.set(a.serial)
                var.edit_number_var.set(a.number)
                var.edit_txt.insert(END, a.information)

    def load_company_field(variable,var,self):
        with DB_connection() as DB:
            user = DB.session.query(Company)
            user = user.filter(Company.Id == var.selected[0])
            for a in user:
                var.edit_name_var.set(a.name)
                var.edit_address_var.set(a.address)
                var.edit_city_var.set(a.city)
                var.edit_state_var.set(a.state)
                var.edit_phone_var.set(a.phone)
        
    def save_new_customer(variable,var,self):
        full_company = Company(name=var.name_var.get().upper(),address=var.address_var.get().upper(),
                               city=var.city_var.get().upper(),state=var.state_var.get().upper(),
                               phone=var.phone_var.get().upper())
        with DB_connection() as DB:
            DB.session.add_all([full_company])

    def save_equipment(variable,var,self):
        full_equipment = Equipment(company_id=var.selected[0],
                                   make=var.make_var.get().upper(),model=var.model_var.get().upper(),
                                   serial=var.serial_var.get().upper(),number=var.number_var.get().upper(),
                                   information=var.txt.get("1.0",'end-1c').upper())
        with DB_connection() as DB:
            DB.session.add_all([full_equipment])

    def save_edit_equipment(variable,var,self):
        E=Equipment
        with DB_connection() as DB:
            user = DB.session.query(Equipment)
            user = user.filter(Equipment.Id == var.selected_truck[0])
            user.update({E.make:var.edit_make_var.get().upper(),E.model:var.edit_model_var.get().upper(),
                        E.serial:var.edit_serial_var.get().upper(),E.number:var.edit_number_var.get().upper(),
                        E.information:var.edit_txt.get("1.0",'end-1c').upper()})

    def save_edit_customer(variable,var,self):
        C=Company
        with DB_connection() as DB:
            user = DB.session.query(Company)
            user = user.filter(Company.Id == var.selected[0])
            user.update({C.name:var.edit_name_var.get().upper(),C.address:var.edit_address_var.get().upper(),
                        C.city:var.edit_city_var.get().upper(),C.state:var.edit_state_var.get().upper(),
                        C.phone:var.edit_phone_var.get().upper()})
            
    def remove_equipment(variable,var,self):
        with DB_connection() as DB:
            user = DB.session.query(Equipment).filter(Equipment.Id == var.selected_truck[0]).delete()

    def sort_company_lb(variable,var,self,column):
        if column == 'first':
            variable.company_col = Company.name
        if column == 'city':
            variable.company_col = Company.city
        if column == 'contact':
            variable.company_col = Company.phone
        if column == 'address':
            variable.company_col = Company.address
        with DB_connection() as DB:
            if var.company_entry_var.get() == '':
                for a,b,c,d,e,f in DB.session.query(Company.Id,Company.name,Company.address,Company.city,Company.
                                                state,Company.phone).order_by(variable.company_col):
                    if a % 2 == 0:
                        var.new_customer_lb.insert('','end', values=(a,b,c,d,e,f), tags=self.tag_background[0])
                    if a % 2 != 0:
                        var.new_customer_lb.insert('','end', values=(a,b,c,d,e,f), tags=self.tag_background[1])
            if var.company_entry_var.get() != '':
                variable.search_company_entry(var,self)

    def sort_truck_lb(variable,var,self,column):
        if column == 'make':
            variable.truck_col = Equipment.make
        if column == 't/n':
            variable.truck_col = Equipment.number
        if column == 'model':
            variable.truck_col = Equipment.model
        if column == 'serial':
            variable.truck_col = Equipment.serial
        with DB_connection() as DB:
            if var.truck_entry_var.get() == '':
                for a,b,c,d,e in DB.session.query(Equipment.Id,Equipment.make,Equipment.number,Equipment.model,Equipment.
                                            serial).filter(Equipment.company_id == var.selected[0]).order_by(variable.truck_col):
                    if a % 2 == 0:
                        var.truck_lb.insert('','end', values=(a,b,c,d,e), tags=self.tag_background[0])
                    if a % 2 != 0:
                        var.truck_lb.insert('','end', values=(a,b,c,d,e), tags=self.tag_background[1])
            if var.truck_entry_var.get() != '':
                variable.search_truck_entry(var,self)


    def search_company_entry(variable,var,self):
        if var.company_var == 'Company Name':
            variable.company_entry = Company.name.contains(var.company_entry_var.get().upper())
        if var.company_var == 'City':
            variable.company_entry = Company.city.contains(var.company_entry_var.get().upper())
        if var.company_var == 'Contact Number':
            variable.company_entry = Company.phone.contains(var.company_entry_var.get().upper())
        with DB_connection() as DB:
            for a,b,c,d,e,f in DB.session.query(Company.Id,Company.name,Company.address,Company.city,Company.
                                                state,Company.phone).filter(variable.company_entry).order_by(variable.company_col):
                    if a % 2 == 0:
                        var.new_customer_lb.insert('','end', values=(a,b,c,d,e,f), tags=self.tag_background[0])
                    if a % 2 != 0:
                        var.new_customer_lb.insert('','end', values=(a,b,c,d,e,f), tags=self.tag_background[1])

    def search_truck_entry(variable,var,self):
        if var.truck_var == 'Truck Model':
            variable.truck_entry = Equipment.model.contains(var.truck_entry_var.get().upper())
        if var.truck_var == 'Truck Number':
            variable.truck_entry = Equipment.number.contains(var.truck_entry_var.get().upper())
        if var.truck_var == 'Truck Serial Number':
            variable.truck_entry = Equipment.serial.contains(var.truck_entry_var.get().upper())
        with DB_connection() as DB:
            for a,b,c,d,e in DB.session.query(Equipment.Id,Equipment.make,Equipment.number,Equipment.model,Equipment.
                                            serial).filter(Equipment.company_id == var.selected[0]).filter(variable.truck_entry).order_by(variable.truck_col):
                    if a % 2 == 0:
                        var.truck_lb.insert('','end', values=(a,b,c,d,e), tags=self.tag_background[0])
                    if a % 2 != 0:
                        var.truck_lb.insert('','end', values=(a,b,c,d,e), tags=self.tag_background[1])
