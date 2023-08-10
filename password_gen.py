import string
import random
import tkinter as tk

class create_pass:
    window=tk.Tk()
    username=tk.StringVar()
    passlength=tk.StringVar()
    updated=tk.StringVar()
    user=username.get()
    len=passlength.get()
    def __init__(self):
        self.window.geometry("500x500")
        self.window.title("Password_Generator")
        self.heading_f=self.create_heading_frame()
        self.other_f=self.create_other_frame()
        self.create_heading_label()
        self.create_username_label()
        self.create_username_entry()
        self.create_length_label()
        self.create_length_entry()
        self.createpassword_button()
        self.create_updated_label()
        self.updatedentry=self.create_updated_entry()
        self.create_regenerate()
    def create_heading_frame(self):
        f=tk.Frame(self.window,bg="#191919")
        f.pack(fill="x")
        return f
    def create_other_frame(self):
        f=tk.Frame(self.window,bg="#191919")
        f.pack(fill="both",expand=True)
        return f

    def create_heading_label(self):
        h=tk.Label(self.heading_f,text="PASSWORD GENERATOR",font="Arial 14 bold",fg="white",bg="#191919")
        h.pack(fill="both",expand=True,pady=20,anchor="w")

    def create_username_label(self):
        l=tk.Label(self.other_f,text="Username: ",font="Arial 14 bold",bg="#191919",fg="white")
        l.grid(row=1,column=1)
    def create_username_entry(self):
        usernameentry=tk.Entry(self.other_f,textvariable=self.username,font="Arial 12",bg="#191919",fg="white",insertbackground="#EF8555")
        usernameentry.grid(row=1,column=2)
    def create_length_label(self):
        l=tk.Label(self.other_f,text="Password length: ",font="Arial 14 bold",bg="#191919",fg="white")
        l.grid(row=2,column=1)
    def create_length_entry(self):
        passlengthentry=tk.Entry(self.other_f,textvariable=self.passlength,font="Arial 12",bg="#191919",fg="white",insertbackground="#EF8555")
        passlengthentry.grid(row=2,column=2)
    def createpassword_button(self):
        self.btn=tk.Button(self.other_f,text="CREATE PASSWORD",font="Arial 12 bold",bg="#EF8555",fg="black",command=self.create_pass)
        self.btn.grid(row=3,column=2,columnspan=2,pady=20)
    def create_updated_label(self):
        l=tk.Label(self.other_f,text="Generated password: ",font="Arial 14 bold",bg="#191919",fg="white")
        l.grid(row=4,column=1)
    def create_updated_entry(self):
        e=tk.Entry(self.other_f,textvariable=self.updated,font="Arial 12",bg="#191919",fg="white",insertbackground="#EF8555")
        e.grid(row=4,column=2)
        return e
    def create_regenerate(self):
        btn=tk.Button(self.other_f,text="REGENERATE",font="Arial 12 bold",bg="#EF8555",fg="black",command=self.rege)
        btn.grid(row=5,column=2,pady=20)
    def run(self):
        self.window.mainloop()

    def create_pass(self):
      try:
        s1=string.ascii_lowercase
        s2=string.ascii_uppercase
        s3=string.digits
        s4=string.punctuation
        length=int(self.passlength.get())
        s=[]
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        # in place of next two line
        # temp="".join(random.sample(s,length))
        random.shuffle(s)
        temp="".join(s[0:length])
        self.updated.set(temp)
        self.btn.config(state='disabled')
      except:
          self.updated.set("ERROR")
    def rege(self):
      try:
        s1=string.ascii_lowercase
        s2=string.ascii_uppercase
        s3=string.digits
        s4=string.punctuation
        length=int(self.passlength.get())
        s=[]
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        random.shuffle(s)
        temp="".join(s[0:length])
        self.updated.set(temp)
      except:
          self.updated.set("ERROR")

if __name__=='__main__':
    root=create_pass()
    root.run()