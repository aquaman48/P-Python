from breezypythongui import EasyFrame

class ButtonDemo(EasyFrame):
	"""Illustrates command buttons and user events."""

	def __init__(self):
		"""Sets up the window, label, and buttons."""
		EasyFrame.__init__(self)

		#a single label in the first row
		self.label = self.addLabel(text = "Hello there!!!!", 
								   row = 0, column = 0, 
								   columnspan = 2,
								   sticky = "NSEW")

		#Two command buttons in the second row
		#handler methods supplied
		
		self.clearBtn = self.addButton(text = "Erase Greeting",
									   row = 1, column = 0,
									   command = self.clear)
		self.restoreBtn = self.addButton(text = "Restore Greeting", 
										 row = 1, column = 1,
										 state = "disabled", 
										 command = self.restore)
	#methods to handle user events
	def clear(self):
		"""Resets the label to empty string and updates the button states"""
		self.label["text"] = ''
		self.clearBtn["state"] = "disabled"
		self.restoreBtn["state"] = "normal"

	def restore(self):
		"""Resets label to original text and updates button"""
		self.label["text"] = "ABRA CADABRA, Hello there!!!!!"
		self.clearBtn["state"] = "normal"
		self.restoreBtn["state"] = "disabled"

def main():
    """Instantiates and pops up the window."""
    ButtonDemo().mainloop()
    
if __name__ == "__main__":
    main()
    