from tkinter import *
root = Tk()

def update_options_B(*args):
    types = data[variable_a.get()]
    variable_b.set(types[0])
    menu = optionmenu_b['menu']
    menu.delete(0, 'end')
    for type in types:
        menu.add_command(label=type, command=lambda under_type=type: variable_b.set(under_type))
        
    update_res()
def update_res(event):
    b = variable_b.get()
    
    c = variable_inp.get()
    c=int(float(c))

    if b == "Fahrenheit":
        res = round((float(c) - 32) * 5/9,2)
        res2=round(res+273.15,2)
        res_label_1.config(text =f"""Fahrenheit:

{c}""")
        res_label_2.config(text =f"""Celcius:

{res}""" )
        res_label_3.config(text =f"""Kelvin: 

{res2}""")
    
    if b == "Celcius":
        res = round((float(c)*9/5)+32,2)
        res2 = round(float(c)+273.15,2)
        res_label_1.config(text =f"""Fahrenheit:

{res}""")
        res_label_2.config(text =f"""Celcius:

{c}""")
        res_label_3.config(text =f"""Kelvin:

{res2}""")
        
    if b == "Kelvin":
        res = round((float(c))-275.15,2)
        res2 = round((float(res)*9/5)+32,2)
        res_label_1.config(text =f"""Fahrenheit:

{res2}""")
        res_label_2.config(text =f"""Celcius:
                
{res}""" )
        res_label_3.config(text =f"""Kelvin: 
                           
{c}""")
    
    if b == "Kilometer":
        res= round((float(c))/1.609,2)   
        res2=round(float(res)*1760,2) 
        res_label_1.config(text =f"""Kilometer:
                           
{c}""")
        res_label_2.config(text =f"""Miles:
                           
{res}""" )
        res_label_3.config(text =f"""Yards: 

{res2}""")
        
    if b == "Miles":
        res= round((float(c))*1.609,2)   
        res2=round(float(c)*1760,2) 
        res_label_1.config(text =f"""Kilometer:

{res}""")
        res_label_2.config(text =f"""Miles:

{c}""" )
        res_label_3.config(text =f"""Yards: 
                           
{res2}""")
        
    if b == "Yards":
        res= round((float(c))/1094,2)   
        res2=round(float(c)/1760,2) 
        res_label_1.config(text =f"""Kilometer:
                           
{res}""")
        res_label_2.config(text =f"""Miles:
                           
{res2}""" )
        res_label_3.config(text =f"""Yards: 
                           
{c}""")
        
    if b == "Kilogram":
        res= round((float(c))*2.205,2)   
        res2=round(float(res)*16,2) 
        res_label_1.config(text =f"""Kilogram:
                           
{c}""")
        res_label_2.config(text =f"""Pounds:
                           
{res}""" )
        res_label_3.config(text =f"""Ounces: 
                           
{res2}""")
        
    if b == "Pounds":
        res= round((float(c))/2.205,2)   
        res2=round(float(c)*16,2) 
        res_label_1.config(text =f"""Kilogram:
                           
{res}""")
        res_label_2.config(text =f"""Pounds:
                           
{c}""" )
        res_label_3.config(text =f"""Ounces: 
                           
{res2}""")
        
    if b == "Ounces":
        res= round((float(c))/35.274,2)   
        res2=round(float(c)/16,2) 
        res_label_1.config(text =f"""Kilogram:
                           
{res}""")
        res_label_2.config(text =f"""Pounds:
                           
{res2}""" )
        res_label_3.config(text =f"""Ounces: 
                           
{c}""")
        
        
data = {'Temperature': ['Fahrenheit', 'Celcius','Kelvin'],'Distance': ['Kilometer', 'Miles', 'Yards'], 'Weight': ['Kilogram', 'Pounds', 'Ounces']}

variable_a = StringVar()
variable_b = StringVar()
variable_inp =StringVar()
variable_a.trace('w', update_options_B)

variable_b.trace('w',update_res)
optionmenu_a = OptionMenu(root, variable_a, *data.keys(),)
inp = Entry(root, textvariable = variable_inp,width = 20)
inp.bind("<KeyRelease>",  update_res)
optionmenu_b = OptionMenu(root, variable_b, '',)
res_label_1 = Label(text = '',width=15,bg="#a3ffbc")
res_label_2 = Label(text = '',width=15,bg="#a3ffbc")
res_label_3 = Label(text = '',width=15,bg="#a3ffbc")



variable_a.set('Temperature')
optionmenu_a.grid(row=1,column=1)
optionmenu_b.grid(row=1,column=3)
inp.grid(row=1,column=2)
res_label_1.grid(row = 2,column=1)
res_label_2.grid(row = 2,column=2)
res_label_3.grid(row = 2,column=3)

root.geometry("350x400")
root.config(bg="#a3ffbc")
root.mainloop()
