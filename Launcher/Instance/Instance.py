import os


from ..Server import Server
from .. import Config

class Instance:
    def __init__(self, Name):
        self.Name = Name
        self.Directory: str = f"{Config.Data["Instances"]}/{Name}"

        self.Server = Server(Name)

    def Delete(self):
        os.rmdir(self.Directory)

    def Edit(self):
        print(f"Editing: {self.Name}")

        self.Server.EditConfig()
        self.Server.LoadConfig()

    def Start(self):
        print(f"Starting: {self.Name}")

        self.Server.Run()