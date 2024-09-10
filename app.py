from customtkinter import *

class App(CTk):
    def __init__(self):
        # App Initialization
        super().__init__()
        self.title("Inventory Tracker")

        # App variables
        self.prefix = "%"
        self.suffix = "$"

        # Events binding
        self.bind('<FocusIn>', self.onFocusIn)
        self.bind('<FocusOut>', self.onFocusOut)

        self.bind(self.suffix, self.onSuffixPress)
        self.bind(self.prefix, self.onPrefixPress)

    def onSuffixPress(self, eventArg):
        print("Suffix entered.")

    def onPrefixPress(self, eventArg):
        print("Prefix entered.")
    
    def onFocusIn(self, eventArg):
        print("Got focus.")

    def onFocusOut(self, eventArg):
        print("Focus lost.")

app = App()
app.mainloop()
