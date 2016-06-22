class Electronic():
    def __init__(self, name, switch, error):
        self.name = name
        self.switch = switch
        self.error = error

    def tool_switcher(self):
        if self.error is False:
            if self.switch is True:
                return False
            else:
                return True
        else:
            raise ElectronicError
