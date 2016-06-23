class Electronic():

    def __init__(self, name, switch, error):
        self.name = name
        self.switch = switch
        self.error = error

    def tool_switcher(self):
        if self.error is False:
            if self.switch is True:
                self.switch = False
                print("The tool is switched OFF")
            else:
                self.switch = True
                print("The tool is switched ON")
        else:
            print("The tool doesn't working! :(")

    def tool_repair(self):
        if self.error is True:
            self.error = False
            print("The tool is working now! :)")
        else:
            print("The tool already working!")


class Laptop(Electronic):
    def __init__(self, name, switch, error):
        super().__init__(name, switch, error)

    def coding(self):
        # This function need a student object!
        if self.switch is True:
            print("The student knowledge level increasing and the energy level decreasing.")
        else:
            print("The laptop isn't turned on.")
        # This will be returned student object.
        return
