from Tkinter import *
import Tkinter as tk
import nelt_functions as Func
import nelt_backbone_funcs as BBF
import nelt_sql_functions as sql

class start(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        tk.Tk.title(self, "Company Name")

        for F in (Func.Ap.Main,Func.Ap.Add_Company,Func.Ap.Information,
                  Func.Ap.Edit_Information,Func.Ap.Edit_Company):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        Func.Customer_Function().make_db()                
        self.show_frame(Func.Ap.Main)
        
    def show_frame(self, cont):
        
       for frame in self.frames.values():
           frame.grid_remove()
           
       frame = self.frames[cont]
       frame.grid()
       frame.winfo_toplevel().geometry("")
## use this event to populate all listboxs
       frame.event_generate("<<showframe>>")
        
if __name__ == "__main__":
    app = start()
    BBF.center(app)
    app.mainloop()
