from tkinter import *
import navigation as nav

class Statusbar(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		status = Label(root, text="Idle", bd=1, relief=SUNKEN, anchor=W)
		status.pack(side=BOTTOM, fill=X)


class Mainbody(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		
		# Main screen title
		title = Label(self, text="pyTime")
		title.config(font=("Courier", 36))
		title.grid(row=0,column=0, columnspan=5)
		
		MOTD = Label(self, text="Thanks for taking part in the testing of pyTime!\n\n", justify=LEFT)
		MOTD.config(font=("Courier", 10))
		MOTD.grid(row=1,sticky=W, columnspan=5)
		
		LoginButton = Button(self, text="Log in", command=nav.login)
		LoginButton.grid(row=2, column=2)
		RegisterButton = Button(self, text="Register", command=nav.register)
		RegisterButton.grid(row=3, column=2)
		
		# Image implementation for future reference.
		#splash = PhotoImage(file="splash.png")
		#splashImage = Label(self, image=splash)
		#splashImage.image = splash
		#splashImage.grid(row=0,column=0)
		
		
class Navbar(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		
		# ***** Navigation bar layout *****
		menu = Menu(root)
		root.config(menu=menu)
		
		# Account menu option
		accountMenu = Menu(menu, tearoff=0)
		accountMenu.add_command(label="Login", command=nav.login)
		accountMenu.add_command(label="Register", command=nav.register)
		
		# Help menu option
		helpMenu = Menu(menu, tearoff=0)
		helpMenu.add_command(label="Documentation", command=nav.documentation)
		helpMenu.add_command(label="Support", command=nav.support)
		helpMenu.add_command(label="FAQ", command=nav.faq)
		
		# Adding menu options to navigation menus
		menu.add_cascade(label="Account", menu=accountMenu)
		menu.add_cascade(label="Help", menu=helpMenu)


class GUI(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.statusbar = Statusbar(self)
		self.navbar = Navbar(self)
		self.statusbar.pack()
		self.mainbody = Mainbody(self)
		self.mainbody.pack()


if __name__ == "__main__":
	root = Tk()
	root.title(" pyTime")
	root.iconbitmap("C:\clock.ico")
	root.geometry("400x300")
	root.resizable(0, 0)
	GUI(root).pack()
	root.mainloop()