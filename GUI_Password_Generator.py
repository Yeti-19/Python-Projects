#PASSWORD GENERATOR

import tkinter as t
import random



def passw0rd_generator():
    
    digits = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-=<>?/  "
    global password 
    password = ""


    for i in range(21): 
        q = random.randint(0,len(digits)-1)
        password += digits[q]
    
    l.config(text = password)
    a = " YOUR PASSWORD HAS BEEN GENERATED ! "
    l1 = t.Label(root, text = a)
    l1.config(font = ("Monospace",20))
    l1.place(x = 80, y = 230)


    print("Your Password is: ")
    print(password)
    return password





root = t.Tk()


root.title(" Password Generator ")  
root.geometry("750x750") 
root.configure(bg="black") 



''' LABEL '''
l = t.Label(root, text = " Your password will be shown here ")
l.config(font = ("Monospace",20))
l.place(relx = 0.5, rely = 0.5, anchor = "center")




''' BUTTONS'''

b = t.Button(root, text = " Generate Password ! ")
b.config(command = passw0rd_generator) 
b.config(font = ("Ink free",20,"bold")) 
b.config(bg = "blue", fg = "black") 
b.config(activebackground = "red", activeforeground = "black")

'''i = t.PhotoImage(file = "image.png")            #Insert your own image, otherwise remove this part
b.config(image = i) 
b.config(compound = "top") '''


b.pack(side = "top") 


c = t.Button(root, text = " CLOSE ")
c.config(command = root.destroy) 
c.config(font = ("Ink free",10,"bold")) 
c.config(bg = "blue", fg = "black") 
c.config(activebackground = "red", activeforeground = "black") 
c.pack(side = "bottom")


root.mainloop() 
