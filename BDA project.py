from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymongo
try:
    client = pymongo.MongoClient('127.0.0.1',27017)
    print("Server connection made     : ", client)
except pymongo.errors.ConnectionFailure as e:
    print("Could not connect to MongoDB: %s" % e)
    print(client)

# cursor to move around the databse
db = client.bda # bda db
class App(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.widgets()
        
    def cmd(self):
        newwin= Toplevel(root)   
        newwin.geometry("300x300")
        lbl = Label(newwin,text="Enter the password to find the secret").pack()
        nam = StringVar().set(None)
       # print("hi")
        nam = Entry(newwin)
        nam.pack()
       # print(nam)
        def msg():
            messagebox.showinfo("Title", nam.get())
       # print("hello2")
        delete2 = Button(newwin,text="Delete",command=msg).pack()
       # print("hello3")
        newwin.mainloop()
            
        
    def widgets(self):
        l=Label(self,text="University DATABASE",bg="LightSkyBlue3").grid(row=0,column=2,sticky="nesw",padx=100)
##        l['bg']="peachpuff2"
        display=Button(self,text="Display",command=self.display,bg="burlywood1").grid(row=1,column=2,sticky="nesw",pady=10,padx=150)
        
        insert=Button(self,text="Insert", command=self.insert,bg="burlywood1").grid(row=2,column=2,sticky="nesw",pady=10,padx=150)
        update=Button(self,text="Update", command=self.update,bg="burlywood1").grid(row=3,column=2,sticky="nesw",pady=10,padx=150)
        delete=Button(self,text="Delete", command=self.delete,bg="burlywood1").grid(row=4,column=2,sticky="nesw",pady=10,padx=150)
        lang=Button(self,text="Search by Country", command=self.language,bg="burlywood1").grid(row=5,column=2,sticky="nesw",pady=10,padx=150)
        imdb=Button(self,text="Search Universities by Total Score", command=self.tsuni,bg="burlywood1").grid(row=6,column=2,sticky="nesw",pady=10,padx=150)
        noofmovies= Button(self,text="No. of Universities vs Country",command=self.noofmovies,bg="burlywood1").grid(row=8,column=2,sticky="nesw",pady=10,padx=150)
        meanperyer=Button(self,text="Graph of",command=self.graph1,bg="wheat2").grid(row=9,column=2,sticky="nesw",pady=10,padx=150)
        
    def noofmovies(self):
        newwin= Toplevel(root)   
        newwin.geometry("600x400")
        newwin['bg']="LightSkyBlue1"


        tree = ttk.Treeview(newwin)
        tree["columns"]=("mean")
        tree.column("mean", width=200 )
        
        
        tree.heading("mean", text="No. of Universites vs Country")
        
        r=5
        for d in db.univ.aggregate([{"$group":{"_id":"$country","num":{"$sum":1}}},{"$sort":{"_id":1}}]):
            tree.insert("",r, text=d["_id"], values=(d["num"]))
##            print(d)
            r+=2            

        tree.grid(row=4,column=1,columnspan=3,sticky=W, padx=30,pady=50)


    def graph1(self):
        
        newwin= Toplevel(root)   
        newwin.geometry("600x400")
        newwin['bg']="LightSkyBlue1"

    def tsuni(self):
        newwin= Toplevel(root)   
        newwin.geometry("1000x600")
        newwin['bg']="LightSkyBlue1"
        def find():
            print("find btn clicked")
            tree.destroy()
##
            tree2 = ttk.Treeview(newwin)
            tree2["columns"]=("world_rank","university_name","teaching","income","total_score","num_students")
            tree2.column("world_rank", width=100 )
            tree2.column("university_name", width=150)
            tree2.column("teaching", width=100)
            tree2.column("income", width=100)
            tree2.column("total_score", width=100)
            tree2.column("num_students", width=80)
           # tree2.column("country", width=70)
            tree2.heading("world_rank", text="world_rank")
            tree2.heading("university_name", text="university_name")
            tree2.heading("teaching",text="teaching")
            tree2.heading("income",text="income")
            tree2.heading("total_score",text="total_score")
            tree2.heading("num_students",text="num_students")
           # tree2.heading("country", text="country")
            r=5
            num1 = int(lang.get())
            for d in db.univ.find({"total_score":{"$gt":num1}}):

                tree2.insert("",r, text=d["country"], values=(d["world_rank"],d["university_name"],d["teaching"],d["income"],d["total_score"],d["num_students"],d["country"]))
    ##            print(d)
                r+=2            
            tree2.grid(row=4,column=1,columnspan=3,sticky=W, padx=140,pady=50)

        
        lbl = Label(newwin,text="Find Univeristies above total score of  : ",bg="LightSkyBlue3")
        lbl.grid(row=1,column=1,sticky=E,padx=100,pady=20)

        lang=StringVar()
        lang.set(None)
        lang=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        lang.grid(row=1,column=2,sticky=W)

        findbtn=btn=Button(newwin,text="Find",command=find,bg="burlywood1").grid(row=2,column=1,sticky=E)
        tree = ttk.Treeview(newwin)
        tree["columns"]=("world_rank","university_name","teaching","income","total_score","num_students")
        tree.column("world_rank", width=100 )
        tree.column("university_name", width=150)
        tree.column("teaching", width=100)
        tree.column("income", width=100)
        tree.column("total_score", width=100)
        tree.column("num_students", width=80)
       # tree.column("country", width=70)
        tree.heading("world_rank", text="world_rank")
        tree.heading("university_name", text="university_name")
        tree.heading("teaching",text="teaching")
        tree.heading("income",text="income")
        tree.heading("total_score",text="total_score")
        tree.heading("num_students",text="num_students")
       # tree.heading("country", text="country")

        

        r=5
        ##tree.insert("" , 0,    text="Line 1", values=("1A","1b"))
        for d in db.univ.find():
##            tree.insert("",r,d["movie_title"],text=d["movie_title"])
            tree.insert("",r, text=d["country"], values=(d["world_rank"],d["university_name"],d["teaching"],d["income"],d["total_score"],d["num_students"],d["country"]))
##            print(d)
            r+=2            

##        except:
##            print("error")

        tree.grid(row=4,column=1,columnspan=3,rowspan=10,sticky=W, padx=40,pady=50)
        
    def language(self):
        newwin= Toplevel(root)   
        newwin.geometry("1000x600")
        newwin['bg']="LightSkyBlue1"
        def find():
            print("find btn clicked")
            tree.destroy()
##
            tree2 = ttk.Treeview(newwin)
            tree2["columns"]=("world_rank","university_name","teaching","income","total_score","num_students")
            tree2.column("world_rank", width=100 )
            tree2.column("university_name", width=150)
            tree2.column("teaching", width=100)
            tree2.column("income", width=100)
            tree2.column("total_score", width=100)
            tree2.column("num_students", width=80)
           # tree2.column("country", width=70)
            tree2.heading("world_rank", text="world_rank")
            tree2.heading("university_name", text="university_name")
            tree2.heading("teaching",text="teaching")
            tree2.heading("income",text="income")
            tree2.heading("total_score",text="total_score")
            tree2.heading("num_students",text="num_students")
           # tree2.heading("country", text="country")
            r=5
            
            for d in db.univ.find({"country":lang.get()}):

                tree2.insert("",r, text=d["country"], values=(d["world_rank"],d["university_name"],d["teaching"],d["income"],d["total_score"],d["num_students"],d["country"]))
    ##            print(d)
                r+=2            
            tree2.grid(row=4,column=1,columnspan=3,sticky=W, padx=140,pady=50)

        
        lbl = Label(newwin,text="Find University by Country : ",bg="LightSkyBlue1")
        lbl.grid(row=1,column=1,sticky=E,padx=100,pady=20)

        lang=StringVar()
        lang.set(None)
        lang=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        lang.grid(row=1,column=2,sticky=W)

        findbtn=btn=Button(newwin,text="Find",command=find,bg="burlywood1").grid(row=2,column=1,sticky=E)
        tree = ttk.Treeview(newwin)
        tree["columns"]=("world_rank","university_name","teaching","income","total_score","num_students")
        tree.column("world_rank", width=100 )
        tree.column("university_name", width=150)
        tree.column("teaching", width=100)
        tree.column("income", width=100)
        tree.column("total_score", width=100)
        tree.column("num_students", width=80)
       # tree.column("country", width=70)
        tree.heading("world_rank", text="world_rank")
        tree.heading("university_name", text="university_name")
        tree.heading("teaching",text="teaching")
        tree.heading("income",text="income")
        tree.heading("total_score",text="total_score")
        tree.heading("num_students",text="num_students")
       # tree.heading("country", text="country")

        

        r=5
        ##tree.insert("" , 0,    text="Line 1", values=("1A","1b"))
        for d in db.univ.find():
##            tree.insert("",r,d["movie_title"],text=d["movie_title"])
            tree.insert("",r, text=d["country"], values=(d["world_rank"],d["university_name"],d["teaching"],d["income"],d["total_score"],d["num_students"],d["country"]))
##            print(d)
            r+=2            

##        except:
##            print("error")

        tree.grid(row=4,column=1,columnspan=3,rowspan=10,sticky=W, padx=40,pady=50)
        

    def display(self):
        newwin= Toplevel(root)   
        newwin.geometry("1000x1000")
        newwin['bg']="LightSkyBlue1"
        def find():
            print("find btn clicked")
            tree.destroy()
##
            tree2 = ttk.Treeview(newwin)
            tree2["columns"]=("world_rank","university_name","teaching","income","total_score","num_students")
            tree2.column("world_rank", width=100 )
            tree2.column("university_name", width=150)
            tree2.column("teaching", width=100)
            tree2.column("income", width=100)
            tree2.column("total_score", width=100)
            tree2.column("num_students", width=80)
           # tree2.column("country", width=70)
            tree2.heading("world_rank", text="world_rank")
            tree2.heading("university_name", text="university_name")
            tree2.heading("teaching",text="teaching")
            tree2.heading("income",text="income")
            tree2.heading("total_score",text="total_score")
            tree2.heading("num_students",text="num_students")
           # tree2.heading("country", text="country")
            r=5
           
            for d in db.univ.find({"university_name":name.get()}):

                tree2.insert("",r, text=d["university_name"], values=(d["world_rank"],d["university_name"],d["teaching"],d["income"],d["total_score"],d["num_students"],d["country"]))
    ##            print(d)
                r+=2            
            tree2.grid(row=4,column=1,columnspan=3,sticky=W, padx=40,pady=50)

        
        lbl = Label(newwin,text="Find University By Name : ",bg="LightSkyBlue1")
        lbl.grid(row=1,column=1,sticky=E,padx=100,pady=20)

        name=StringVar()
        name.set(None)
        name=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        name.grid(row=1,column=2,sticky=W)

        findbtn=btn=Button(newwin,text="Find",command=find,bg="burlywood1").grid(row=2,column=1,sticky=E)
        tree = ttk.Treeview(newwin)




        #tree2 = ttk.Treeview(newwin)
        tree["columns"]=("world_rank","university_name","teaching","income","total_score","num_students")
        tree.column("world_rank", width=100 )
        tree.column("university_name", width=150)
        tree.column("teaching", width=100)
        tree.column("income", width=100)
        tree.column("total_score", width=100)
        tree.column("num_students", width=80)
       # tree.column("country", width=70)
        tree.heading("world_rank", text="world_rank")
        tree.heading("university_name", text="university_name")
        tree.heading("teaching",text="teaching")
        tree.heading("income",text="income")
        tree.heading("total_score",text="total_score")
        tree.heading("num_students",text="num_students")
       # tree.heading("country", text="country")

        

        r=5
        ##tree.insert("" , 0,    text="Line 1", values=("1A","1b"))
        for d in db.univ.find():
##            tree.insert("",r,d["movie_title"],text=d["movie_title"])
            tree.insert("",r, text=d["country"], values=(d["world_rank"],d["university_name"],d["teaching"],d["income"],d["total_score"],d["num_students"],d["country"]))
##            print(d)
            r+=2            

##        except:
##            print("error")

        tree.grid(row=4,column=1,columnspan=3,rowspan=10,sticky=W, padx=40,pady=50)
        
    
    def delete(self):
        newwin= Toplevel(root)   
        newwin.geometry("600x300")
        newwin['bg']="LightSkyBlue1"
        l1=Label(newwin,text="Enter the name of the University to delete",bg="LightSkyBlue3")
        l1.config(font=("Courier", 24))
        l1.grid(row=0,column=1,columnspan=1,sticky=W,padx=10,pady=10)
        
        lbl1=Label(newwin,text="University Name",bg="darkseagreen3")
        lbl1.grid(row=1,column=1,columnspan=2,sticky=W,padx=250,pady=10)
##        Label(self,text="Password: ").grid(row=1,column=0,sticky=W)
        name=StringVar()
        name.set(None)
##        print("hi")
        name=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        name.grid(row=2,column=1,sticky=W,padx=230,pady=10)

        def check():

            if name.get()=="":
                messagebox.showinfo("error","Fill all the fields")
            else:
                if db.univ.find({"university_name":name.get()}).count()>0:
                    db.univ.delete_one({"university_name":name.get()})
                    messagebox.showinfo("success","University details deleted successfully")
                else:
                    messagebox.showinfo("error","University not found")
                
        btn=Button(newwin,text="Delete",command=check,bg="burlywood1").grid(row=13,column=1,sticky=W,padx=270,pady=10)

    def update(self):
        newwin= Toplevel(root)   
        newwin.geometry("600x600")
        newwin['bg']="LightSkyBlue1"
        l1=Label(newwin,text="Update the University Details",bg="LightSkyBlue3")
        l1.config(font=("Courier", 24))
        l1.grid(row=0,column=1,columnspan=4,sticky=W,padx=10,pady=10)
        
        lbl1=Label(newwin,text="University Name",bg="LightSkyBlue3")
        lbl1.grid(row=1,column=1,columnspan=1,sticky=W,padx=10,pady=10)
##        Label(self,text="Password: ").grid(row=1,column=0,sticky=W)
        name=StringVar()
        name.set(None)
##        print("hi")
        name=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        name.grid(row=1,column=2,sticky=W,padx=10)

        lbl2=Label(newwin,text="Rank",bg="LightSkyBlue3")
        lbl2.grid(row=2,column=1,columnspan=1,sticky=W,padx=10,pady=10)
        rank=StringVar()
        rank.set(None)
        rank=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        rank.grid(row=2,column=2,sticky=W,padx=10)

        lbl3=Label(newwin,text="Country",bg="LightSkyBlue3")
        lbl3.grid(row=3,column=1,columnspan=1,sticky=W,padx=10,pady=10)
        coun=StringVar()
        coun.set(None)
        coun=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        coun.grid(row=3,column=2,sticky=W,padx=10)

        lbl4=Label(newwin,text="Teaching",bg="LightSkyBlue3")
        lbl4.grid(row=4,column=1,columnspan=1,sticky=W,padx=10,pady=10)
        teach=StringVar()
        teach.set(None)
        teach=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        teach.grid(row=4,column=2,sticky=W,padx=10)

        lbl5=Label(newwin,text="International",bg="LightSkyBlue3")
        lbl5.grid(row=5,column=1,columnspan=1,sticky=W,padx=10,pady=10)
        iscor=StringVar()
        iscor.set(None)
        iscor=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        iscor.grid(row=5,column=2,sticky=W,padx=10)

        lbl6=Label(newwin,text="Research",bg="LightSkyBlue3")
        lbl6.grid(row=6,column=1,columnspan=1,sticky=W,padx=10)
        rese=StringVar()
        rese.set(None)
        rese=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        rese.grid(row=6,column=2,sticky=W,padx=10)

        lbl7=Label(newwin,text="Citations",bg="LightSkyBlue3")
        lbl7.grid(row=7,column=1,columnspan=1,sticky=W,padx=10,pady=10)
        cit=StringVar()
        cit.set(None)
        cit=Entry(newwin)
        cit.grid(row=7,column=2,sticky=W,padx=10)

        lbl8=Label(newwin,text="Income",bg="LightSkyBlue3")
        lbl8.grid(row=8,column=1,columnspan=1,sticky=W,padx=10,pady=10)
        income=StringVar()
        income.set(None)
        income=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        income.grid(row=8,column=2,sticky=W,padx=10)

        lbl9=Label(newwin,text="Total Score",bg="LightSkyBlue3")
        lbl9.grid(row=9,column=1,columnspan=1,sticky=W,padx=10,pady=10)
        ts=StringVar()
        ts.set(None)
        ts=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        ts.grid(row=9,column=2,sticky=W,padx=10)

        lb21=Label(newwin,text="Student Staff Ratios",bg="LightSkyBlue3")
        lb21.grid(row=11,column=1,columnspan=1,sticky=W,padx=10,pady=10)
        ss1=StringVar()
        ss1.set(None)
        ss1=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        ss1.grid(row=11,column=2,sticky=W,padx=10)



        lb44=Label(newwin,text="Number of Student",bg="LightSkyBlue3")
        lb44.grid(row=10,column=1,columnspan=1,sticky=W,padx=10,pady=10)
        numst=StringVar()
        numst.set(None)
        numst=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        numst.grid(row=10,column=2,sticky=W,padx=10)

        lb22=Label(newwin,text="International Students",bg="LightSkyBlue3")
        lb22.grid(row=12,column=1,columnspan=1,sticky=W,padx=10,pady=10)
        ih1=StringVar()
        ih1.set(None)
        ih1=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        ih1.grid(row=12,column=2,sticky=W,padx=10)


        lb24=Label(newwin,text="Year",bg="LightSkyBlue3")
        lb24.grid(row=13,column=1,columnspan=1,sticky=W,padx=10,pady=10)
        year=StringVar()
        year.set(None)
        year=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        year.grid(row=13,column=2,sticky=W,padx=10)

        def check():

            if name.get=="" or year.get()=="" or ih1.get()=="" or ss1.get()=="" or income.get()=="" or numst=="" or rese=="" or iscor=="" or teach=="" or coun=="" or cit=="" or rank=="" or ts=="":
                messagebox.showinfo("error","Fill all the fields")
            else:
                if db.univ.find({"university_name":name.get()}).count()>0:
                    db.univ.update({"university_name":name.get()},{"world_rank":rank.get(),"university_name":name.get(),"country":coun.get(),"teaching":teach.get(),"international":iscor.get(),"research":rese.get(),"citations":cit.get(),"income":income.get(),"total_score":ts.get(),"num_students":numst.get(),"student_staff_ratio":ss1.get(),"international_students":ih1.get(),"year":year.get()})
                    messagebox.showinfo("success","University Deatils updated successfully")
                else:
                    messagebox.showinfo("error","University not found")


        
        btn=Button(newwin,text="Update",command=check,bg="burlywood1").grid(row=17,column=2,sticky=W,padx=10,pady=10)

    
    def insert(self):
        newwin= Toplevel(root)   
        newwin.geometry("600x600")
        newwin['bg']="LightSkyBlue1"
        l1=Label(newwin,text="Insert University Details",bg="LightSkyBlue3")
        l1.config(font=("Courier", 24))
        l1.grid(row=0,column=1,columnspan=4,sticky=W,padx=10,pady=10)
        
        lbl1=Label(newwin,text="University Name",bg="LightSkyBlue3")
        lbl1.grid(row=1,column=1,columnspan=1,sticky=W,padx=10,pady=10)
##        Label(self,text="Password: ").grid(row=1,column=0,sticky=W)
        name=StringVar()
        name.set(None)
##        print("hi")
        name=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        name.grid(row=1,column=2,sticky=W,padx=10)

        lbl2=Label(newwin,text="Rank",bg="LightSkyBlue3")
        lbl2.grid(row=2,column=1,columnspan=1,sticky=W,padx=10,pady=10)
        rank=StringVar()
        rank.set(None)
        rank=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        rank.grid(row=2,column=2,sticky=W,padx=10)

        lbl3=Label(newwin,text="Country",bg="LightSkyBlue3")
        lbl3.grid(row=3,column=1,columnspan=1,sticky=W,padx=10,pady=10)
        coun=StringVar()
        coun.set(None)
        coun=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        coun.grid(row=3,column=2,sticky=W,padx=10)

        lbl4=Label(newwin,text="Teaching",bg="LightSkyBlue3")
        lbl4.grid(row=4,column=1,columnspan=1,sticky=W,padx=10,pady=10)
        teach=StringVar()
        teach.set(None)
        teach=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        teach.grid(row=4,column=2,sticky=W,padx=10)

        lbl5=Label(newwin,text="International",bg="LightSkyBlue3")
        lbl5.grid(row=5,column=1,columnspan=1,sticky=W,padx=10,pady=10)
        iscor=StringVar()
        iscor.set(None)
        iscor=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        iscor.grid(row=5,column=2,sticky=W,padx=10)

        lbl6=Label(newwin,text="Research",bg="LightSkyBlue3")
        lbl6.grid(row=6,column=1,columnspan=1,sticky=W,padx=10)
        rese=StringVar()
        rese.set(None)
        rese=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        rese.grid(row=6,column=2,sticky=W,padx=10)

        lbl7=Label(newwin,text="Citations",bg="LightSkyBlue3")
        lbl7.grid(row=7,column=1,columnspan=1,sticky=W,padx=10,pady=10)
        cit=StringVar()
        cit.set(None)
        cit=Entry(newwin)
        cit.grid(row=7,column=2,sticky=W,padx=10)

        lbl8=Label(newwin,text="Income",bg="LightSkyBlue3")
        lbl8.grid(row=8,column=1,columnspan=1,sticky=W,padx=10,pady=10)
        income=StringVar()
        income.set(None)
        income=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        income.grid(row=8,column=2,sticky=W,padx=10)

        lbl9=Label(newwin,text="Total Score",bg="LightSkyBlue3")
        lbl9.grid(row=9,column=1,columnspan=1,sticky=W,padx=10,pady=10)
        ts=StringVar()
        ts.set(None)
        ts=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        ts.grid(row=9,column=2,sticky=W,padx=10)

        lb21=Label(newwin,text="Student Staff Ratios",bg="LightSkyBlue3")
        lb21.grid(row=11,column=1,columnspan=1,sticky=W,padx=10,pady=10)
        ss1=StringVar()
        ss1.set(None)
        ss1=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        ss1.grid(row=11,column=2,sticky=W,padx=10)



        lb44=Label(newwin,text="Number of Student",bg="LightSkyBlue3")
        lb44.grid(row=10,column=1,columnspan=1,sticky=W,padx=10,pady=10)
        numst=StringVar()
        numst.set(None)
        numst=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        numst.grid(row=10,column=2,sticky=W,padx=10)

        lb22=Label(newwin,text="International Students",bg="LightSkyBlue3")
        lb22.grid(row=12,column=1,columnspan=1,sticky=W,padx=10,pady=10)
        ih1=StringVar()
        ih1.set(None)
        ih1=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        ih1.grid(row=12,column=2,sticky=W,padx=10)



        lb24=Label(newwin,text="Year",bg="LightSkyBlue3")
        lb24.grid(row=13,column=1,sticky=W,padx=10,pady=10)
        year=StringVar()
        year.set(None)
        year=Entry(newwin)#.grid(row=1,column=1,sticky=W)
        year.grid(row=13,column=2,sticky=W,padx=10)

        def check():

            if name.get=="" or year.get()=="" or ih1.get()=="" or ss1.get()=="" or income.get()=="" or numst=="" or rese=="" or iscor=="" or teach=="" or coun=="" or cit=="" or rank=="" or ts=="":
                messagebox.showinfo("error","Fill all the fields")
            else:
                db.univ.insert({"world_rank":rank.get(),"university_name":name.get(),"country":coun.get(),"teaching":teach.get(),"international":iscor.get(),"research":rese.get(),"citations":cit.get(),"income":income.get(),"total_score":ts.get(),"num_students":numst.get(),"student_staff_ratio":ss1.get(),"international_students":ih1.get(),"year":year.get()})
                messagebox.showinfo("success","University Deatils updated successfully")
        
        btn=Button(newwin,text="Submit",command=check,bg="burlywood1").grid(row=14,column=2,sticky=W,padx=10,pady=25)

   
    def check(self):
        self.text.delete(0.0,END)
        self.text.insert(0.0,msg)
        print("ji")    
        
root=Tk()
root.geometry("500x500")
root["bg"]="LightSkyBlue1"
##root.configure(background="#00ffff")
app=App(root)
app['bg']="LightSkyBlue1"
root.mainloop()
