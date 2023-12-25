#Import Module
from tkinter import *
import wikipedia as w
from threading import Thread
import speech_recognition as sr
import webbrowser
from tkinter import messagebox
from tkinter.filedialog import *


#Variable
#methods for listen

def set_text(text):
    search_box.delete(0,END)
    search_box.insert(0,text)
    return

def speech():
    try:
        sr_obj = sr.Recognizer()
        with sr.Microphone() as m:
            audio = sr_obj.listen(m)
            data = sr_obj.recognize_google(audio, language='eng-in')
            set_text(data)
            weki(data)
    except:
        messagebox.showinfo('Connection Error','Your Search Did Not Match Any Document \n Make Sure Words Are Types Correctly \n Make Sure You Have Internet Connection')
def weki(dfs):
    try :
        t.config(state='normal')
        result=str(w.summary(dfs))
        t.delete(1.0,END)
        t.insert(INSERT,result)
    except :
        messagebox.showinfo('Connection Error','Your Search Did Not Match Any Document \n Make Sure Words Are Types Correctly \n Make Sure You Have Internet Connection')

def s_b():
    dfs=search_box.get()
    set_text(dfs)
    weki(dfs)


def cls():
    search_box.delete(0,END)
    t.delete(1.0,END)

def openweb():
    try:
        site='https://www.google.com/search?q='
        siteadd = search_box.get()
        c=''
        if siteadd !='':
            webbrowser.open(site+siteadd)
        else :
            messagebox.showinfo('Search Tool','Search Field is Empty \n Please Type Valid Text For Search ')
    except:
        messagebox.showinfo('Browser Error', 'There is a Problem with your Browser \n Install a web browsers')
def save():
    if t.compare("end-1c", "==", "1.0")!=True:
        path=askdirectory()
        c=path
        d=c.strip()
        e=''
        if d is e :
            return
        else:
            try:
                sb = search_box.get()
                filename = '/' + sb + '.txt'
                notcorrect = path + filename
                p = notcorrect.replace('/', '//')
                f = open(p, 'w')
                val = t.get(1.0, END)
                f.write(val)
                f.close()
                messagebox.showinfo('File Saved', 'File Saved Successfully')
            except:
                messagebox.showinfo('Contact Developer', 'Contact Your Developer with Error Code "UnicodeEncodeError"')
    else:
        messagebox.showinfo('Result is Empty','Nothing To Save \n Make Some Search First')

#GUI Building


root=Tk()

root.title("Search Tool")
root.geometry('550x600')
root.iconbitmap('icon.ico')
root.minsize(550,600)
root.maxsize(550,600)

var_name = StringVar()
#Top Image
file=PhotoImage(file='top_image.png')
top_lebel=Label(root,image=file)
top_lebel.pack(side=TOP)
#Search box
search_box=Entry(root,font="Arial 15 bold" )
search_box.pack(side=TOP,fill=X,padx=90)
search_box.focus()

#Thread for Multi Process
def start_thread():
    thread2 = Thread(target=speech)
    thread2.start()

#Menu Defination
def close():
    quit()
    exit()
def reset_fields():
    cls()
def contact_me():
    try:
        site_fb = 'https://www.facebook.com/heyarav'
        webbrowser.open(site_fb)
    except:
        messagebox.showinfo('Browser Error','There is a Problem with your Browser \n Install a web browsers')
def about_st():
    try:
        site_ast='https://docs.google.com/document/d/1PMkM9GQ0Yw56V4tcjiJQri3QKeKBL-SBg3sYejFUZJg/edit'
        webbrowser.open(site_ast)
    except:
        messagebox.showinfo('Browser Error','There is a Problem with your Browser \n Install a web browsers')
def save_into_pc():
    save()
#   Menu
mm=Menu(root)

m_file=Menu(mm,tearoff=0)
m_file.add_command(label='Save',command=save_into_pc)
m_file.add_command(label='Quit',command=close)
mm.add_cascade(label='File',menu=m_file)
root.config(menu=mm)

m_edit=Menu(mm,tearoff=0)
m_edit.add_command(label='Reset Fields',command=reset_fields)
mm.add_cascade(label='Edit',menu=m_edit)
root.config(menu=mm)

m_help=Menu(mm,tearoff=0)
m_help.add_command(label='Contact Me',command=contact_me)
m_help.add_command(label='About Search Tool',command=about_st)
mm.add_cascade(label='Help',menu=m_help)
root.config(menu=mm)

#frame for mic and search
f=Frame(root)
f.pack(side=TOP)

#frame for other control
f2=Frame(root)
f2.pack(side=BOTTOM,pady=50)

#Search Button
file_s=PhotoImage(file='sb.png')
search_button=Button(f,image=file_s,command=s_b)
search_button.grid(row=0, column=0,padx=2,pady=3)

#Frame 2
#Open in browser button
file_wb=PhotoImage(file='open.png')
o_i_b=Button(f2,image=file_wb,command=openweb)
o_i_b.grid(row=1,column=0,padx=6,pady=3)

#save to pc
file_c=PhotoImage(file='save.png')
b_c=Button(f2,image=file_c,command=save)
b_c.grid(row=1,column=1,padx=6,pady=3)

#reset
file_p=PhotoImage(file='reset.png')
b_pc=Button(f2,image=file_p,command=cls)
b_pc.grid(row=1,column=2,padx=6,pady=3)

#frame for text and scroll box
tf=Frame(root)
tf.pack(fill=X,padx=15)
#For Text box Storing Data
scrollbar=Scrollbar(tf)
scrollbar.pack(side=RIGHT,fill=Y)
t=Text(tf,height=12,width=50,wrap=WORD, yscrollcommand=scrollbar.set)
t.pack(side=TOP,fill=BOTH,padx=1,pady=0)
t.config(state='disabled')
scrollbar.config(command=t.yview)


#Mic Lebel

#Mic Button
file_m=PhotoImage(file='mic3.png')
search_button=Button(f,image=file_m,command=start_thread)
search_button.grid(row=0, column=1,padx=2,pady=3)
root.mainloop()
