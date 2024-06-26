import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
teachers=[]
UGstudents=[]
PGstudents=[]
students=[UGstudents,PGstudents]
persons=[teachers,students]
#this function checks whether the str is a crt gmail id or not
def is_gmail_correct(str):
    if "@gmail.com" in str:
        
        return 1
    else:
        return 0 

#Person class        
class person:
    def __init__(self,email=None,password=None,name=None,age=None,gender=None,chances=None,birthday=None):
        self.password=password
        self.email=email
        self.name=name
        self.age=age
        self.gender=gender
        self.birthday=birthday
        self.isactive=False  
        self.chances=chances 

#Teacher class
class teacher(person):
    
    def __init__(self,email=None,password=None,name=None,age=None,gender=None,subject=None,chances=None,birthday=None):
        super().__init__(email,password,name,age,gender,chances,birthday)
        self.subject=subject 

#Student class
class student(person):
    def __init__(self,password=None,email=None,age=None,name=None,gender=None,year=None,chances=None,birthday=None):
        super().__init__(email,password,name,age,gender,chances,birthday)
        self.year=year

#UGstudent class        
class UGstudent(student):
    
    def __init__(self,password=None,email=None,name=None,age=None,gender=None,year=None,program=None,chances=None,birthday=None):
        super().__init__(email,password,name,age,gender,year,chances,birthday)
        self.program=program

#PGstudent class
class PGstudent(student):
    def __init__(self,password=None,email=None,name=None,age=None,gender=None,year=None,experience_area=None,chances=None,birthday=None):
        super().__init__(email,password,name,age,gender,year,chances,birthday)
        self.experience_area=experience_area

#Teacher window
class Teacher_window():
    def __init__(self,root,email,password):
        self.root=root
        self.email=email
        self.password=password
        self.root.title('Teacher Window')
        self.root.config(bg='#90EE90')
        window_width=530
        window_height=420
        self.root.geometry("{}x{}".format(window_width, window_height))

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.root.geometry("+{}+{}".format(x_position, y_position))
  
    #this function opens teacher window for registration
    def teacher_system(self):
        self.entry_frame=tk.Frame(self.root,bg='black')
        self.entry_frame.place(anchor='center',relx=0.5,rely=0.45)
        font=('Arial',13);text_font=('Arial',9)

        self.label=tk.Label(self.entry_frame,text='Registration Form',font=font,bg='black',fg='white')
        self.label.grid(row=0)

        self.attribute1=tk.Label(self.entry_frame,text='Age',font=text_font,bg='black',fg='white')
        self.attribute1.grid(row=1,column=0,padx=5,pady=5)
        self.age=tk.IntVar()
        self.attribute1_value=tk.Entry(self.entry_frame,textvariable=self.age)
        self.attribute1_value.grid(row=1,column=1,padx=5,pady=5)
        

        self.attribute2=tk.Label(self.entry_frame,text='Name',font=text_font,bg='black',fg='white')
        self.attribute2.grid(row=2,column=0,padx=5,pady=5)
        self.name=tk.StringVar()
        self.attribute2_value=tk.Entry(self.entry_frame,textvariable=self.name)
        self.attribute2_value.grid(row=2,column=1,padx=5,pady=5)

        self.attribute3=tk.Label(self.entry_frame,text='Subject',font=text_font,bg='black',fg='white')
        self.attribute3.grid(row=3,column=0,padx=5,pady=5)
        self.subject=tk.StringVar()
        self.attribute3_value=tk.Entry(self.entry_frame,textvariable=self.subject)
        self.attribute3_value.grid(row=3,column=1,padx=5,pady=5)  
        

        self.gendertype=tk.Label(self.entry_frame,text='gender',font=text_font,bg='black',fg='white')
        self.gendertype.grid(row=5,column=0,padx=5,pady=5)
        self.genddertypes=['Male','Female','Others']
        self.gender_type_var=tk.StringVar()
        self.gender_type_combox=ttk.Combobox(self.entry_frame,values=self.genddertypes,font=font,textvariable=self.gender_type_var)
        self.gender_type_combox.grid(row=5,column=1,padx=5,pady=5)   

        self.attribute4=tk.Label(self.entry_frame,text='Birthday',font=text_font,bg='black',fg='white')
        self.attribute4.grid(row=4,column=0,padx=5,pady=5)
        self.birthday=tk.StringVar()
        self.attribute4_value=tk.Entry(self.entry_frame,textvariable=self.birthday)
        self.attribute4_value.grid(row=4,column=1,padx=5,pady=5)

        self.button=tk.Button(self.entry_frame,text='submit',command=lambda:self.append(),bg='#90EE90',fg='white')
        self.button.grid(row=6)

    #this function appends the teacher in the list and closes the registration window
    def append(self):
          T1=teacher(email=self.email,password=self.password,age=self.age.get(),name=self.name.get(),subject=self.subject.get(),gender=self.gender_type_var.get(),birthday=self.attribute4_value.get())
          T1.isactive=True
          T1.chances=0
          teachers.append(T1)
          self.root.destroy()

    #this function displayes the profile window
    def teacher_display(self,T1):
        self.entry_frame=tk.Frame(self.root,bg='black')
        self.entry_frame.place(anchor='center',relx=0.5,rely=0.45)
        font=('Arial',13);text_font=('Arial',9)

        self.label=tk.Label(self.entry_frame,text='Your Atributes:',font=font,bg='black',fg='white')
        self.label.grid(row=0)

        self.attribute1=tk.Label(self.entry_frame,text='Age',font=('Bold',11),bg='black',fg='white')
        self.attribute1.grid(row=1,column=0,padx=5,pady=5)
        self.attribute1_value=tk.Label(self.entry_frame,text=f'{T1.age}',font=('bold',11),bg='black',fg='white')
        self.attribute1_value.grid(row=1,column=1,padx=5,pady=5)
        
        self.attribute2=tk.Label(self.entry_frame,text='Name',font=('bold',11),bg='black',fg='white')
        self.attribute2.grid(row=2,column=0,padx=5,pady=5)
        self.attribute2_value=tk.Label(self.entry_frame,text=f'{T1.name}',font=('bold',11),bg='black',fg='white')
        self.attribute2_value.grid(row=2,column=1,padx=5,pady=5)

        self.attribute3=tk.Label(self.entry_frame,text='Subject',font=('bold',11),bg='black',fg='white')
        self.attribute3.grid(row=3,column=0,padx=5,pady=5)
        self.attribute3_value=tk.Label(self.entry_frame,text=f'{T1.subject}',font=('bold',11),bg='black',fg='white')
        self.attribute3_value.grid(row=3,column=1,padx=5,pady=5)  
        
        self.gendertype=tk.Label(self.entry_frame,text='gender',font=('bold',11),bg='black',fg='white')
        self.gendertype.grid(row=4,column=0,padx=5,pady=5)
        self.gendervalue=tk.Label(self.entry_frame,text=f'{T1.gender}',font=('bold',11),bg='black',fg='white')
        self.gendervalue.grid(row=4,column=1,padx=5,pady=5)

        self.attribute4=tk.Label(self.entry_frame,text='Birthday',font=('bold',11),bg='black',fg='white')
        self.attribute4.grid(row=5,column=0,padx=5,pady=5)
        self.attribute4_value=tk.Label(self.entry_frame,text=f'{T1.birthday}',font=('bold',11),bg='black',fg='white')
        self.attribute4_value.grid(row=5,column=1,padx=5,pady=5)

        self.button=tk.Button(self.entry_frame,text='Edit',command=lambda:self.edit(T1),fg='white',bg='#90EE90')
        self.button.grid(row=6,padx=5,pady=5)

        self.dbutton=tk.Button(self.entry_frame,text='Deregistrate',command=lambda:self.Deactivate(T1),fg='white',bg='#90EE90')
        self.dbutton.grid(row=7,padx=5,pady=5)

    #this opens a edit window to edit attributes
    def edit(self,T1):
        self.root.destroy()
        self.root=tk.Tk()
        Teacher_window(self.root,T1.email,T1.password)
        #from display function
        self.entry_frame=tk.Frame(self.root,bg='black')
        self.entry_frame.place(anchor='center',relx=0.5,rely=0.45)
        font=('Arial',13);text_font=('Arial',11)

        self.label=tk.Label(self.entry_frame,text='Edit Your Atributes',font=font,bg='black',fg='white')
        self.label.grid(row=0)

        self.attribute1=tk.Label(self.entry_frame,text='Age',font=text_font,bg='black',fg='white')
        self.attribute1.grid(row=1,column=0,padx=5,pady=5)
        self.age=tk.IntVar()
        self.attribute1_value=tk.Entry(self.entry_frame,textvariable=self.age)
        self.attribute1_value.grid(row=1,column=1,padx=5,pady=5)
        

        self.attribute2=tk.Label(self.entry_frame,text='Name',font=text_font,bg='black',fg='white')
        self.attribute2.grid(row=2,column=0,padx=5,pady=5)
        self.name=tk.StringVar()
        self.attribute2_value=tk.Entry(self.entry_frame,textvariable=self.name)
        self.attribute2_value.grid(row=2,column=1,padx=5,pady=5)

        self.attribute3=tk.Label(self.entry_frame,text='Subject',font=text_font,bg='black',fg='white')
        self.attribute3.grid(row=3,column=0,padx=5,pady=5)
        self.subject=tk.StringVar()
        self.attribute3_value=tk.Entry(self.entry_frame,textvariable=self.subject)
        self.attribute3_value.grid(row=3,column=1,padx=5,pady=5) 

        self.attribute4=tk.Label(self.entry_frame,text='Birthday',font=text_font,bg='black',fg='white')
        self.attribute4.grid(row=4,column=0,padx=5,pady=5)
        self.birthday=tk.StringVar()
        self.attribute4_value=tk.Entry(self.entry_frame,textvariable=self.birthday)
        self.attribute4_value.grid(row=4,column=1,padx=5,pady=5) 
        

        self.gendertype=tk.Label(self.entry_frame,text='gender',font=text_font,bg='black',fg='white')
        self.gendertype.grid(row=5,column=0,padx=5,pady=5)
        self.genddertypes=['Male','Female','Others']
        self.gender_type_var=tk.StringVar()
        self.gender_type_combox=ttk.Combobox(self.entry_frame,values=self.genddertypes,font=font,textvariable=self.gender_type_var)
        self.gender_type_combox.grid(row=5,column=1,padx=5,pady=5)



        self.attribute1_value.insert(0, T1.age)
        self.attribute2_value.insert(0, T1.name)
        self.attribute3_value.insert(0, T1.subject)
        self.gender_type_combox.set(T1.gender)
        self.attribute4_value.insert(0,T1.birthday)
        

        self.button2=tk.Button(self.entry_frame,text='save',command=lambda:self.show_saved(T1),fg='white',bg='#90EE90')
        self.button2.grid(row=6)
   
    #this function displays the profile window after editing 
    def show_saved(self,T1):
        T1.age=self.attribute1_value.get()
        T1.name=self.attribute2_value.get()
        T1.subject=self.attribute3_value.get()
        T1.gender=self.gender_type_combox.get()
        T1.birthday=self.attribute4_value.get()
        self.root.destroy()
        self.saved_window=tk.Tk()
        (Teacher_window(self.saved_window,T1.email,T1.password)).teacher_display(T1)
   
    #this function deactivates the user
    def Deactivate(self,T1):
        result=messagebox.askquestion('Confirm Deregistration','are you sure you want to deregister')
        if result=='yes':
          messagebox.showinfo('user deregister succesfully')
          T1.isactive=False
          self.root.destroy()

#student window class    
class Student_window():
    def __init__(self,root,email,password):
        self.email=email
        self.password=password
        self.root=root
        self.root.title('Student window')
        self.root.config(bg='#90EE90')
        window_width=530
        window_height=420
        self.root.geometry("{}x{}".format(window_width, window_height))

        # Calculate the window position to center it on the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.root.geometry("+{}+{}".format(x_position, y_position))

    #this method displayes student window  
    def student_system(self):
        font=('Arial',13);text_font=('Arial',11)
        self.entry_frame=tk.Frame(self.root,bg='black')
        self.entry_frame.place(anchor='center',relx=0.5,rely=0.25)
        self.label=tk.Label(self.entry_frame,text='Registration From',font=font,fg='white',bg='black')
        self.label.grid(row=0)

        self.attribute1=tk.Label(self.entry_frame,text='Age',font=text_font,fg='white',bg='black')
        self.attribute1.grid(row=1,column=0,padx=5,pady=5)
        self.age=tk.IntVar()
        self.attribute1_value=tk.Entry(self.entry_frame,textvariable=self.age)
        self.attribute1_value.grid(row=1,column=1,padx=5,pady=5)
        

        self.attribute2=tk.Label(self.entry_frame,text='Name',font=text_font,fg='white',bg='black')
        self.attribute2.grid(row=2,column=0,padx=5,pady=5)
        self.name=tk.StringVar()
        self.attribute2_value=tk.Entry(self.entry_frame,textvariable=self.name)
        self.attribute2_value.grid(row=2,column=1,padx=5,pady=5)

        self.attribute3=tk.Label(self.entry_frame,text='year',font=text_font,fg='white',bg='black')
        self.attribute3.grid(row=3,column=0,padx=5,pady=5)
        self.year=tk.IntVar()
        self.attribute3_value=tk.Entry(self.entry_frame,textvariable=self.year)
        self.attribute3_value.grid(row=3,column=1,padx=5,pady=5)  

        self.gendertype=tk.Label(self.entry_frame,text='gender',font=text_font,fg='white',bg='black')
        self.gendertype.grid(row=4,column=0,padx=5,pady=5)
        self.genddertypes=['Male','Female','Others']
        self.gender_type_var=tk.StringVar()
        self.gender_type_combox=ttk.Combobox(self.entry_frame,values=self.genddertypes,font=font,textvariable=self.gender_type_var)
        self.gender_type_combox.grid(row=4,column=1,padx=5,pady=5)

        self.attribute4=tk.Label(self.entry_frame,text='Birthday',font=text_font,fg='white',bg='black')
        self.attribute4.grid(row=5,column=0,padx=5,pady=5)
        self.birthday=tk.StringVar()
        self.attribute4_value=tk.Entry(self.entry_frame,textvariable=self.birthday)
        self.attribute4_value.grid(row=5,column=1,padx=5,pady=5)  
       #new frame
        self.entry_frame0=tk.Frame(self.root,bg='black')
        self.entry_frame0.place(anchor='s',relx=0.5,rely=0.79)
        self.label0=tk.Label(self.entry_frame0,text='select the type',font=text_font,fg='white',bg='black')
        self.label0.grid(row=0)
      
        self.selected_option=tk.IntVar()
        option1=tk.Radiobutton(self.entry_frame0,text='PG student',value=1,variable=self.selected_option,font=text_font,fg='black')
        option1.grid(row=1,column=0,padx=5,pady=5)
        option2=tk.Radiobutton(self.entry_frame0,text='UG student',value=2,variable=self.selected_option,font=text_font,fg='black')
        option2.grid(row=1,column=1,padx=5,pady=5)
        
        self.button=tk.Button(self.entry_frame0,text='Submit',font=text_font,command=lambda:self.student_type_UG_PG(),fg='white',bg='#90EE90')
        self.button.grid(row=2,padx=5,pady=5)

    #this method displayes according to the radio button 
    def student_type_UG_PG(self):
         self.button.destroy()
         font=('Arial',13);text_font=('Arial',9)
         if self.selected_option.get()==2:
           self.attribute4=tk.Label(self.entry_frame0,text='Department',font=text_font,fg='white',bg='black')
           self.attribute4.grid(row=3,column=0,padx=5,pady=5)
           self.program=tk.StringVar()
           self.attribute4_value=tk.Entry(self.entry_frame0,textvariable=self.program)
           self.attribute4_value.grid(row=3,column=1,padx=5,pady=5) 
          
         elif self.selected_option.get()==1:
           self.attribute4=tk.Label(self.entry_frame0,text='experienced area',font=text_font,fg='white',bg='black')
           self.attribute4.grid(row=3,column=0,padx=5,pady=5)
           exp_area=tk.StringVar()
           self.attribute4_value=tk.Entry(self.entry_frame0,textvariable=exp_area)
           self.attribute4_value.grid(row=3,column=1,padx=5,pady=5) 
           
         self.button2=tk.Button(self.entry_frame0, text='submit now', font=text_font, command=lambda: self.append(),fg='white',bg='#90EE90')
         self.button2.grid(row=4,padx=5,pady=5) 

    #this function appends the student in list and closes student window
    def append(self):
        k=self.selected_option.get()
        if k==1:
            P1=PGstudent(email=self.email,password=self.password,age=self.age.get(),name=self.name.get(),year=self.year.get(),gender=self.gender_type_var.get())
            P1.email=self.email;P1.password=self.password
            P1.name=self.name.get();P1.age=self.age.get()
            P1.birthday=self.birthday.get()
            P1.isactive=True; P1.chances=0
            P1.experience_area=self.attribute4_value.get()
            PGstudents.append(P1)
        elif k==2:
           U1=UGstudent(email=self.email,password=self.password,age=self.age.get(),name=self.name.get(),year=self.year.get(),gender=self.gender_type_var.get(),program=self.program.get())
           U1.email=self.email;U1.password=self.password
           U1.name=self.name.get();U1.age=self.age.get()
           U1.birthday=self.birthday.get()
           U1.isactive=True;U1.chances=0
           U1.program=self.attribute4_value.get()
           UGstudents.append(U1)
        self.root.destroy()   

    #this function displayes the student profile window
    def student_display(self,S1):
        self.entry_frame=tk.Frame(self.root,bg='black')
        self.entry_frame.place(anchor='center',relx=0.5,rely=0.45)
        font=('Arial',13);text_font=('Arial',11);capital_font=('bold',15)
      
        self.label=tk.Label(self.entry_frame,text='Your attributes:',font=font,fg='white',bg='black')
        self.label.grid(row=0)

        for obj in PGstudents:
            if obj.email==S1.email and obj.password==S1.password:
                self.label1=tk.Label(self.entry_frame,text='UG Student:',font=capital_font,fg='white',bg='black')
                self.label1.grid(row=1,padx=5,pady=5)
                k=1
        for obj in UGstudents:
            if obj.email==S1.email and obj.password==S1.password:
                self.label1=tk.Label(self.entry_frame,text='PG Student:',font=capital_font,fg='white',bg='black')
                self.label1.grid(row=1,padx=5,pady=5)
                k=2 
        
        self.attribute1=tk.Label(self.entry_frame,text='Age',font=text_font,fg='white',bg='black')
        self.attribute1.grid(row=2,column=0,padx=5,pady=5)
        self.attribute1_value=tk.Label(self.entry_frame,text=f'{S1.age}',font=text_font,fg='white',bg='black')
        self.attribute1_value.grid(row=2,column=1,padx=5,pady=5)
        
        self.attribute2=tk.Label(self.entry_frame,text='Name',font=text_font,fg='white',bg='black')
        self.attribute2.grid(row=3,column=0,padx=5,pady=5)
        self.attribute2_value=tk.Label(self.entry_frame,text=f'{S1.name}',font=text_font,fg='white',bg='black')
        self.attribute2_value.grid(row=3,column=1,padx=5,pady=5)

        self.attribute3=tk.Label(self.entry_frame,text='year',font=text_font,fg='white',bg='black')
        self.attribute3.grid(row=4,column=0,padx=5,pady=5)
        self.attribute3_value=tk.Label(self.entry_frame,text=f'{S1.year}',font=text_font,fg='white',bg='black')
        self.attribute3_value.grid(row=4,column=1,padx=5,pady=5)  
        
        self.gendertype=tk.Label(self.entry_frame,text='gender',font=text_font,fg='white',bg='black')
        self.gendertype.grid(row=5,padx=5,pady=5)
        self.gendervalue=tk.Label(self.entry_frame,text=f'{S1.gender}',font=text_font,fg='white',bg='black')
        self.gendervalue.grid(row=5,column=1,padx=5,pady=5)

        self.attribute4=tk.Label(self.entry_frame,text='Birthday',font=text_font,fg='white',bg='black')
        self.attribute4.grid(row=4,column=0,padx=5,pady=5)
        self.attribute4_value=tk.Label(self.entry_frame,text=f'{S1.birthday}',font=text_font,fg='white',bg='black')
        self.attribute4_value.grid(row=4,column=1,padx=5,pady=5)  

        if k==1 :
            self.exp_areas=tk.Label(self.entry_frame,text='Expereince Area',font=text_font,fg='white',bg='black')
            self.exp_areas.grid(row=6,padx=5,pady=5)
            self.exp_area_value=tk.Label(self.entry_frame,text=f'{S1.experience_area}',font=text_font,fg='white',bg='black')
            self.exp_area_value.grid(row=6,column=1,padx=5,pady=5)
        elif k==2:
            self.programs=tk.Label(self.entry_frame,text='Program',font=text_font,fg='white',bg='black')
            self.programs.grid(row=6,padx=5,pady=5)
            self.program_value=tk.Label(self.entry_frame,text=f'{S1.program}',font=text_font,fg='white',bg='black')
            self.program_value.grid(row=6,column=1,padx=5,pady=5)    
        self.button=tk.Button(self.entry_frame,text='Edit',command=lambda:self.Edit(S1,k),fg='white',bg='#90EE90')
        self.button.grid(row=7,padx=5,pady=5)     
        
        self.dbutton=tk.Button(self.entry_frame,text='Deregistrate',command=lambda:self.Deactivate(S1),fg='white',bg='#90EE90')
        self.dbutton.grid(row=8,padx=5,pady=5)

    #this function is for edit profile
    def Edit(self,S1,k):
        self.root.destroy()
        self.root=tk.Tk()
        Student_window(self.root,S1.email,S1.password)
        self.entry_frame=tk.Frame(self.root,bg='black')
        self.entry_frame.place(anchor='center',relx=0.5,rely=0.45)
        font=('Arial',13);text_font=('Arial',9);capital_font=('bold',15)
      
        self.label=tk.Label(self.entry_frame,text='Edit Your attributes:',font=font,fg='white',bg='black')
        self.label.grid(row=0)

        for obj in PGstudents:
            if obj.email==S1.email and obj.password==S1.password:
                self.label1=tk.Label(self.entry_frame,text='UG Student:',font=capital_font,fg='white',bg='black')
                self.label1.grid(row=1,padx=5,pady=5)
                k=1
        for obj in UGstudents:
            if obj.email==S1.email and obj.password==S1.password:
                self.label1=tk.Label(self.entry_frame,text='PG Student:',font=capital_font,fg='white',bg='black')
                self.label1.grid(row=1,padx=5,pady=5)
                k=2 
        
        self.attribute1=tk.Label(self.entry_frame,text='Age',font=text_font,fg='white',bg='black')
        self.attribute1.grid(row=2,column=0,padx=5,pady=5)
        self.edit_age=tk.IntVar()
        self.attribute1_value=tk.Entry(self.entry_frame,textvariable=self.edit_age)
        self.attribute1_value.grid(row=2,column=1,padx=5,pady=5)
        
        self.attribute2=tk.Label(self.entry_frame,text='Name',font=text_font,fg='white',bg='black')
        self.attribute2.grid(row=3,column=0,padx=5,pady=5)
        self.edit_name=tk.StringVar()
        
        self.attribute2_value=tk.Entry(self.entry_frame,textvariable=self.edit_name)
        self.attribute2_value.grid(row=3,column=1,padx=5,pady=5)

        self.attribute3=tk.Label(self.entry_frame,text='year',font=text_font,fg='white',bg='black')
        self.attribute3.grid(row=4,column=0,padx=5,pady=5)
        self.edit_year=tk.IntVar()
        self.attribute3_value=tk.Entry(self.entry_frame,textvariable=self.edit_year)
        self.attribute3_value.grid(row=4,column=1,padx=5,pady=5)  

        self.attribute4=tk.Label(self.entry_frame,text='Birthday',font=text_font,fg='white',bg='black')
        self.attribute4.grid(row=5,column=0,padx=5,pady=5)
        self.edit_birthday=tk.IntVar()
        self.attribute4_value=tk.Entry(self.entry_frame,textvariable=self.edit_birthday)
        self.attribute4_value.grid(row=5,column=1,padx=5,pady=5)  
        
        self.gendertype=tk.Label(self.entry_frame,text='gender',font=text_font,fg='white',bg='black')
        self.gendertype.grid(row=6,column=0,padx=5,pady=5)
        self.genddertypes=['Male','Female','Others']
        self.edit_gender_type_var=tk.StringVar()
        self.gender_type_combox=ttk.Combobox(self.entry_frame,values=self.genddertypes,font=font,textvariable=self.edit_gender_type_var)
        self.gender_type_combox.grid(row=6,column=1,padx=5,pady=5) 

        if k==1 :
            self.exp_areas=tk.Label(self.entry_frame,text='Expereince Area',font=text_font,fg='white',bg='black')
            self.exp_areas.grid(row=7,padx=5,pady=5)
            self.edit_exparea=tk.StringVar()
            self.exp_area_value=tk.Entry(self.entry_frame,textvariable=self.edit_exparea,font=text_font)
            self.exp_area_value.grid(row=7,column=1,padx=5,pady=5)
            self.exp_area_value.insert(0,str(S1.experience_area))
        elif k==2:
            self.programs=tk.Label(self.entry_frame,text='Program',font=text_font,fg='white',bg='black')
            self.programs.grid(row=7,padx=5,pady=5)
            self.edit_program=tk.StringVar()
            self.program_value=tk.Entry(self.entry_frame,textvariable=self.edit_program,font=text_font)
            self.program_value.grid(row=7,column=1,padx=5,pady=5) 
            self.program_value.insert(0,str(S1.program))
        
        self.attribute1_value.insert(0, str(S1.age))
        self.attribute2_value.insert(0, str(S1.name))
        self.attribute3_value.insert(0, str(S1.year))
        self.gender_type_combox.set(str(S1.gender))
        self.attribute4_value.insert(0,str(S1.birthday))
        
        self.button=tk.Button(self.entry_frame,text='save',command=lambda:self.show_save(S1,k),fg='white',bg='#90EE90')
        self.button.grid(row=8)     
    
    #this function displays the profile after editing
    def show_save(self, S1, k):
        S1.age = self.attribute1_value.get()
        S1.name = self.attribute2_value.get()
        S1.year = self.attribute3_value.get()
        S1.gender = self.gender_type_combox.get()
        S1.birthday=self.attribute4_value.get()
        if k == 1:
            S1.experience_area = self.exp_area_value.get()
        elif k == 2:
            S1.program = self.program_value.get()
        self.root.destroy()
        self.root = tk.Tk()
        (Student_window(self.root, S1.email, S1.password)).student_display(S1)
 
    #this function deactivates user     
    def Deactivate(self,S1):
        result=messagebox.askquestion('Confirm Deregistration','are you sure you want to deregister')
        if result=='yes':
          messagebox.showinfo('user deregister succesfully')
          S1.isactive=False
          self.root.destroy()    

#this is the class contains the main root     
class AcademicSystemGUI:
    def __init__(self,root):
        self.root=root
        self.root.title('Acdemic system')
        self.root.config(bg='#90EE90')

        window_width=530
        window_height=420
        self.root.geometry("{}x{}".format(window_width, window_height))

        # Calculate the window position to center it on the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.root.geometry("+{}+{}".format(x_position, y_position))
        
        self.entry_frame=tk.Frame(root,bg='black')
        self.entry_frame.place(anchor='center',relx=0.5,rely=0.45)
        font=('Arial',12)
        
        self.user_email=tk.StringVar()
        self.user_password=tk.StringVar()
        self.email_label=tk.Label(self.entry_frame,text='Email',font=font,fg='white',bg='black')
        self.email_label.grid(row=0,padx=5,pady=5)
        
        self.userentry=tk.Entry(self.entry_frame,textvariable=self.user_email)
        self.userentry.grid(row=0,column=1,padx=5,pady=5)

        self.pass_label=tk.Label(self.entry_frame,text='Password',font=font,fg='white',bg='black')
        self.pass_label.grid(row=1,padx=5,pady=5)
    
        self.pasentry = tk.Entry(self.entry_frame, textvariable=self.user_password, show='*')
        self.pasentry.grid(row=1,column=1,padx=5,pady=5)

        self.user_type=tk.Label(self.entry_frame,text='select user type',font=font,fg='white',bg='black')
        self.user_type.grid(row=2,padx=5,pady=5)

        self.usertypes=['Teacher','Student']
        self.user_type_var=tk.StringVar()
        self.user_type_combox=ttk.Combobox(self.entry_frame,values=self.usertypes,font=font,textvariable=self.user_type_var)
        self.user_type_combox.grid(row=2,column=1,padx=5,pady=5)
        
        select_font=('Arial',10)
        self.user_login_button=tk.Button(self.entry_frame,text='Sign in',font=select_font,command=self.signin,fg='white',bg='green')
        self.user_login_button.grid(row=3,column=0,padx=5,pady=5)
        self.user_register_button=tk.Button(self.entry_frame,text='Register',font=select_font,command=self.register,fg='white',bg='green')
        self.user_register_button.grid(row=4,column=0,padx=5,pady=5)

        self.message_label = tk.Label(self.entry_frame, text='', font=('Arial', 7), fg='red',bg='black')
        self.message_label.grid(row=5, column=0, columnspan=2, pady=5)
    
    def register(self):
       k=is_gmail_correct(self.user_email.get())
       if k==1:  
        self.deletemessage()
        a=0;b=0;c=0;d=0;e=0;p=0;f=0
        for i in self.user_password.get():
         if i>='0' and i<='9':
           a=1
         if i==' ':
             f=1  
         if i>='a' and i<='z':
          b=1
         if i>='A' and i<='Z':
             c=1
         if i=='#'or i=='@' or i=='&' or i=='!' or i=='$'or i=='%' or i=='*':
             d=1
         e+=1  
        if self.user_type_var.get()!='Teacher' and self.user_type_var.get()!='Student':
            p=1
            message3='Please select a type Teacher or Student'
            self.showmessage(message3)   
        if(a==1 and b==1 and c==1 and d==1 and e<=12 and e>=8 and p==0 and f==0):
            self.user_password=self.user_password
            self.deletemessage()
            if self.user_type_var.get().lower()==self.usertypes[0].lower():
              self.openteacher_window()
              
            elif self.user_type_var.get()==self.usertypes[1]:
                self.openstudent_window() 
            self.user_email.set('')
            self.user_password.set('')
            self.user_type_combox.set('')    
            
        else:
            if p==0:
             message='Password should be 8-12 letters long and must contain a uppercase,lowercase,a number and a special string(@,#,$,%,&,!)'
             self.showmessage(message)
       else:
           message2='Enter correct email id it should be like example@gamail.com'
           self.showmessage(message2)     

    def signin(self):
        k=0;count=0
        for obj in teachers:
            if obj.email==self.user_email.get() and obj.isactive==True:
                k=1
                if obj.password==self.user_password.get():
                  self.user_email.set('')
                  self.user_password.set('')
                  self.user_type_combox.set('')
                  self.deletemessage()
                  self.teacher_display(obj)
                  obj.chances=0
                else:
                    if (obj.chances)<2:
                        self.deletemessage()
                        message5=f'incorrect password you have {2-obj.chances}'
                        obj.chances+=1
                        self.showmessage(message5)   
                    else:
                        obj.isactive=False
                        self.deletemessage()
                        self.showmessage('Your three attempts are over user is deactivated')   
                     
        for obj in PGstudents:
            if obj.email==self.user_email.get() and obj.isactive==True:
                k=1  
                if obj.password==self.user_password.get():
                  self.user_email.set('')
                  self.user_password.set('')
                  self.user_type_combox.set('')
                  self.deletemessage()
                  self.student_display(obj)
                  obj.chances=0
                else:
                    if (obj.chances)<2:
                        self.deletemessage()
                        message5=f'incorrect password you have {2-obj.chances}'
                        obj.chances+=1
                        self.showmessage(message5)   
                    else:
                        obj.isactive=False
                        self.deletemessage()
                        self.showmessage('Your three attempts are over user is deactivated')
        for obj in UGstudents:
            if obj.email==self.user_email.get() and  obj.isactive==True: 
                k=1 
                if obj.password==self.user_password.get():
                  self.user_email.set('')
                  self.user_password.set('')
                  self.user_type_combox.set('')
                  self.deletemessage()
                  self.student_display(obj)
                  obj.chances=0
                else:
                    if (obj.chances)<2:
                        self.deletemessage()
                        message5=f'incorrect password you have {2-obj.chances}'
                        obj.chances+=1
                        self.showmessage(message5)   
                    else:
                        obj.isactive=False
                        self.deletemessage()
                        self.showmessage('Your three attempts are over user is deactivated')
             
        if k==0:
            message4='invalid email id'
            self.showmessage(message4)            
    def showmessage(self,message):
        self.message_label.config(text=message)
    def deletemessage(self):
        self.message_label.config(text='')
    def openteacher_window(self):
        teacher_window = tk.Toplevel(self.root)
        (Teacher_window(teacher_window,self.user_email.get(),self.user_password.get())).teacher_system()     
    def openstudent_window(self):
        student_window = tk.Toplevel(self.root)
        (Student_window(student_window,self.user_email.get(),self.user_password.get())).student_system()
    def teacher_display(self,obj):
        teacher_window = tk.Toplevel(self.root)
        (Teacher_window(teacher_window,obj.email,obj.password)).teacher_display(obj) 
    def student_display(self,obj):
        student_window = tk.Toplevel(self.root) 
        (Student_window(student_window,obj.email,obj.password)).student_display(obj) 

if __name__=="__main__":
     root=tk.Tk()
     window=AcademicSystemGUI(root)
     root.mainloop() 
