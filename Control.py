from tkinter import *


class Statusbar(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		status = Label(root, text="Idle", bd=1, relief=SUNKEN, anchor=W)
		status.pack(side=BOTTOM, fill=X)
		
		
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


if __name__ == "__main__":
	root = Tk()
	root.title(" pyTime")
	root.iconbitmap("C:\clock.ico")
	GUI(root).pack(side="top", fill="both", expand=True)
	root.mainloop()