import tkinter as tk
import pyperclip

win = tk.Tk()
win.geometry("700x350")

Domain_var = tk.StringVar()
Username_var = tk.StringVar()


def make_password():
    domain = Domain_var.get()
    K = 2
    res = ''.join([domain[idx: idx + K] for idx in range(0, len(domain), K * 2)])
    A = str(res)
    C = '$Mhaa@'
    B = (A[0].upper() + A[1:] + C)
    username = Username_var.get()
    F = '$7440&'
    G = str(len(domain))
    if username == '':
        pyperclip.copy(B + F + G)
        tk.Label(win, text='No username so the password is :- ' + B + F + G,
                 font=('calibre', 10, 'bold')).grid(row=3, column=1)
    else:
        D = 2
        res2 = ''.join([username[idx: idx + D] for idx in range(0, len(username), D * 2)])
        E = str(res2)
        H = (E[0].upper() + E[1:])
        pyperclip.copy(B + H + F + G)
        tk.Label(win, text='password is with username :- ' + B + H + F + G,
                 font=('calibre', 10, 'bold')).grid(row=3, column=1)


Domain = tk.Label(win, text='Enter Domain:- ', font=('calibre', 10, 'bold'))
domain_entry = tk.Entry(win, textvariable=Domain_var, font=('calibre', 10, 'normal'))
Username = tk.Label(win, text='Enter username:- ', font=('calibre', 10, 'bold'))
username_entry = tk.Entry(win, textvariable=Username_var, font=('calibre', 10, 'normal'))
sub_btn = tk.Button(win, text='Submit', command=make_password)

Domain.grid(row=0, column=0)
domain_entry.grid(row=0, column=1)
Username.grid(row=1, column=0)
username_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

win.mainloop()