import os
import json

class Config:
    Data = json.load(open("./Config.json", "r"))

class Server:
    def __init__(self, Name: str):
        self.Directory: str = f"{Config.Data["Instances"]}/{Name}"
        self.Server = f"{self.Directory}/Server"

        self.Config: str = f"{self.Directory}/Config.json"
        self.Data: dict = json.load(open(self.Config, "r"))
        
        self.Version = self.Data["Version"]
        self.Modded = self.Modded["Modded"]
        self.Type = self.Data["Type"]

        self.Memory = self.Data["Memory"]
        self.Jar = self.Data["Jar"]
        self.Java = self.Data["Java"]

    def Start(self):
        LaunchCMD = f'"{Config.Data["Java"]}" -Xmx{self.Memory} -Xms{self.Memory} -jar "./Server.jar" --nogui'