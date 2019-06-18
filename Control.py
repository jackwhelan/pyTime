from tkinter import *


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
		title.grid(row=0,column=0)
		
		description = Label(self, text="this is an example of what I may have as a description just to check\nhow it formats and if it even works in the first place, i hope this isn't\npicked up as some weird doc reference i just want to display a\nparagraph tbh.", justify=LEFT)
		description.grid(row=1,sticky=W)
		
		# Image implementation for future reference.
		#splash = PhotoImage(file="splash.png")
		#splashImage = Label(self, image=splash)
		#splashImage.image = splash
		#splashImage.grid(row=0,column=0)
		
		
class Navbar(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		
		# ***** Navigation bar functionality *****
		# Account > Login
		def nav_login():
			print("Login button clicked.")
			
		# Account > Register
		def nav_register():
			print("Register button clicked.")
		
		# Help > Documentation
		def nav_documentation():
			print("Documentation button clicked.")
		
		# Help > Support
		def nav_support():
			print("Support button clicked.")
		
		# Help > FAQ
		def nav_faq():
			print("FAQ button clicked.")
		
		# ***** Navigation bar layout *****
		menu = Menu(root)
		root.config(menu=menu)
		
		# Account menu option
		accountMenu = Menu(menu, tearoff=0)
		accountMenu.add_command(label="Login", command=nav_login)
		accountMenu.add_command(label="Register", command=nav_register)
		
		# Help menu option
		helpMenu = Menu(menu, tearoff=0)
		helpMenu.add_command(label="Documentation", command=nav_documentation)
		helpMenu.add_command(label="Support", command=nav_support)
		helpMenu.add_command(label="FAQ", command=nav_faq)
		
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
	GUI(root).pack()
	root.mainloop()