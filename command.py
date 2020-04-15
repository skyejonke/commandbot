import subprocess

class Command:
    def __init__(self, cmd, description):
        self.cmd = cmd
        self.description = description
    def run(self):
        process = subprocess.Popen(self.cmd.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        return output, error

