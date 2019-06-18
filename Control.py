from tkinter import *


class Statusbar(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		status = Label(root, text="Idle", bd=1, relief=SUNKEN, anchor=W)
		status.pack(side=BOTTOM, fill=X)


class GUI(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.statusbar = Statusbar(self)
		self.statusbar.pack()


if __name__ == "__main__":
	root = Tk()
	root.title(" pyTime")
	root.iconbitmap("C:\clock.ico")
	GUI(root).pack(side="top", fill="both", expand=True)
	root.mainloop()