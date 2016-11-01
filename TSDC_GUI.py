from tkinter import *
import TSDC

window = Tk()
var = IntVar()
tvar_is = StringVar()
tvar_is.set('0')
tvar_Na = StringVar()

window.geometry('+500+300')
window.title('Th(IV) Species Distribution in Aqueous System')

def radiobutton1_check():
    if var.get() == 0:
        label1_2['state'] = DISABLED
        entry1_1['state'] = DISABLED
        tvar_is.set('0')
        entry2_1['state'] = NORMAL
        entry2_1['textvariable'] = tvar_Na
    else:
        label1_2['state'] = ACTIVE
        entry1_1['state'] = NORMAL
        entry2_1['state'] = DISABLED
        entry2_1['textvariable'] = tvar_is

# frame1
frame1 = Frame(window)
frame1.grid(row=0, column=0)
label1_1 = Label(frame1, text='Ionic Strength Correction Option', padx=23, pady=5, font=(None, 15, 'bold'))
label1_1.grid(row=0, column=0, columnspan=2, sticky=N)
radiobutton1_1 = Radiobutton(frame1, text='On', variable=var, value=1, pady=5, command=radiobutton1_check)
radiobutton1_1.grid(row=1, column=0)
radiobutton1_2 = Radiobutton(frame1, text='Off', variable=var, value=0, pady=5, command=radiobutton1_check)
radiobutton1_2.grid(row=1, column=1)
label1_2 = Label(frame1, text='Ionic Strength [NaClO4] (M) :', state=DISABLED)
label1_2.grid(row=2, column=0, sticky=E)
entry1_1 = Entry(frame1, state=DISABLED, textvariable=tvar_is)
entry1_1.grid(row=2, column=1, sticky=W)

# frame2
frame2 = Frame(window)
frame2.grid(row=1, column=0)
label2_1 = Label(frame2, text='Input Parameter Setting', pady=10, font=(None, 15, 'bold'))
label2_1.grid(row=0, column=0, columnspan=2)
label2_2 = Label(frame2, text='[Na+] (M) :')
label2_2.grid(row=1, column=0, sticky=E)
entry2_1 = Entry(frame2, textvariable=tvar_Na)
entry2_1.grid(row=1, column=1, sticky=W)
label2_3 = Label(frame2, text='[F-] (M) :')
label2_3.grid(row=2, column=0, sticky=E)
entry2_2 = Entry(frame2)
entry2_2.grid(row=2, column=1, sticky=W)
label2_4 = Label(frame2, text='[Cl-] (M) :')
label2_4.grid(row=3, column=0, sticky=E)
entry2_3 = Entry(frame2)
entry2_3.grid(row=3, column=1, sticky=W)
label2_5 = Label(frame2, text='[SO42-] (M) :')
label2_5.grid(row=4, column=0, sticky=E)
entry2_4 = Entry(frame2)
entry2_4.grid(row=4, column=1, sticky=W)
label2_6 = Label(frame2, text='pCO2 (atm) :')
label2_6.grid(row=5, column=0, sticky=E)
entry2_5 = Entry(frame2)
entry2_5.grid(row=5, column=1, sticky=W)
label2_7 = Label(frame2, text='Total amount of Th(IV) in system (M) :')
label2_7.grid(row=6, column=0, sticky=E)
entry2_6 = Entry(frame2)
entry2_6.grid(row=6, column=1, sticky=W)

# frame3
frame3 = Frame(window)
frame3.grid(row=0, column=1)
label3_1 = Label(frame3, text='Calculation Parameter Setting', padx=10, pady=10, font=(None, 15, 'bold'))
label3_1.grid(row=0, column=0, columnspan=2, sticky=N)
label3_2 = Label(frame3, text='pH start point :')
label3_2.grid(row=1, column=0, sticky=E)
entry3_1 = Entry(frame3)
entry3_1.grid(row=1, column=1, sticky=W)
label3_3 = Label(frame3, text='pH end point :')
label3_3.grid(row=2, column=0, sticky=E)
entry3_2 = Entry(frame3)
entry3_2.grid(row=2, column=1, sticky=W)
label3_4 = Label(frame3, text='pH gap :')
label3_4.grid(row=3, column=0, sticky=E)
entry3_3 = Entry(frame3)
entry3_3.grid(row=3, column=1, sticky=W)

#frame4
frame4 = Frame(window)
frame4.grid(row=1, column=1)
button4_1 = Button(frame4, text='Calculate', font=(None, 15, 'bold'))
button4_1.grid(row=0, column=0, sticky=N+E+S+W)

window.mainloop()
