from tkinter import *

gam = Tk()
gam.title("Jary")

drag = True

buttons = StringVar()

# =========================Row 1====================================================================
player1_1 = Button(gam, text="O", bg='red', font=("Times", 26, "bold"), height=2, width=6, )
player1_1.grid(row=1, column=0, sticky=S + N + E + W)
player1 = Button(gam, text="O", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
player1.grid(row=1, column=2, sticky=S + N + E + W)
player1 = Button(gam, text="O", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
player1.grid(row=1, column=3, sticky=S + N + E + W)
player1 = Button(gam, text="O", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
player1.grid(row=1, column=4, sticky=S + N + E + W)
player1 = Button(gam, text="O", bg='red', font=("Times", 26, "bold"), height=2, width=6)
player1.grid(row=1, column=5, sticky=S + N + E + W)
# =========================Row 2====================================================================
player1 = Button(gam, text="O", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6, )
player1.grid(row=2, column=0, sticky=S + N + E + W)
player1 = Button(gam, text="O", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
player1.grid(row=2, column=2, sticky=S + N + E + W)
player1 = Button(gam, text="O", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
player1.grid(row=2, column=3, sticky=S + N + E + W)
player1 = Button(gam, text="O", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
player1.grid(row=2, column=4, sticky=S + N + E + W)
player1 = Button(gam, text="O", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
player1.grid(row=2, column=5, sticky=S + N + E + W)
# =========================Row 3====================================================================
player1 = Button(gam, text="O", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6, )
player1.grid(row=3, column=0, sticky=S + N + E + W)
player1 = Button(gam, text="O", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
player1.grid(row=3, column=2, sticky=S + N + E + W)
Free_position = Button(gam, text=" ", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
Free_position.grid(row=3, column=3, sticky=S + N + E + W)
Free_position = Button(gam, text=" ", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
Free_position.grid(row=3, column=4, sticky=S + N + E + W)
Free_position = Button(gam, text=" ", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
Free_position.grid(row=3, column=5, sticky=S + N + E + W)
# =========================Row 4====================================================================
Free_position = Button(gam, text=" ", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
Free_position.grid(row=4, column=0, sticky=S + N + E + W)
Free_position = Button(gam, text=" ", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
Free_position.grid(row=4, column=2, sticky=S + N + E + W)
Free_position = Button(gam, text=" ", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
Free_position.grid(row=4, column=3, sticky=S + N + E + W)
Free_position = Button(gam, text="X", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
Free_position.grid(row=4, column=4, sticky=S + N + E + W)
Free_position = Button(gam, text="X", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
Free_position.grid(row=4, column=5, sticky=S + N + E + W)
# =========================Row 5====================================================================
player2 = Button(gam, text="X", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
player2.grid(row=5, column=0, sticky=S + N + E + W)
player2 = Button(gam, text="X", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
player2.grid(row=5, column=2, sticky=S + N + E + W)
player2 = Button(gam, text="X", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
player2.grid(row=5, column=3, sticky=S + N + E + W)
player2 = Button(gam, text="X", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
player2.grid(row=5, column=4, sticky=S + N + E + W)
player2 = Button(gam, text="X", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
player2.grid(row=5, column=5, sticky=S + N + E + W)
# =========================Row 6====================================================================
player2 = Button(gam, text="X", bg='red', font=("Times", 26, "bold"), height=2, width=6)
player2.grid(row=6, column=0, sticky=S + N + E + W)
player2 = Button(gam, text="X", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
player2.grid(row=6, column=2, sticky=S + N + E + W)
player2 = Button(gam, text="X", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
player2.grid(row=6, column=3, sticky=S + N + E + W)
player2 = Button(gam, text="X", bg='powder blue', font=("Times", 26, "bold"), height=2, width=6)
player2.grid(row=6, column=4, sticky=S + N + E + W)
player2 = Button(gam, text="X", bg='red', font=("Times", 26, "bold"), height=2, width=6)
player2.grid(row=6, column=5, sticky=S + N + E + W)

gam.mainloop()
