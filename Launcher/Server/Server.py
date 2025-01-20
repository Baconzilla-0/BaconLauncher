import os
import json

Instances = json.load("./Config.json")["Instances"]

class Server:
    def __init__(self, Name: str):
        self.Directory: str = f"{Instances}/{Name}"
        self.Config: str = f"{self.Directory}/Server.json"
        self.Data: dict = json.load(self.Config)
        
        self.Version = self.Data["Version"]
        self.Modded = self.Modded["Modded"]
        self.Type = self.Data["Type"]

        self.Memory = self.Data["Memory"]
        self.Jar = self.Data["Jar"]
        self.Java = self.Data["Java"]