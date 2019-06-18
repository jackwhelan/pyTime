from tkinter import *

class GUI(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent

if __name__ == "__main__":
	root = Tk()
	root.title(" pyTime")
	root.iconbitmap("C:\clock.ico")
	GUI(root).pack(side="top", fill="both", expand=True)
	root.mainloop()