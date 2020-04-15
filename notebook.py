from command import Command

class Notebook:
    userid = [156903320945033216,184051428589830145]


    def __init__(self):
        print("Using default config")
        self.commandDict = {"restart": Command("screen -d -r minecraft-simplex -X stuff \"./startup.sh\n\"", " Restarts the server") }

    # def __init__(self, userid):
    #     self.commandDict = {}
        # self.userid = []

