from .. import Files
from .. import Apis

from . import Info

from .Server import Server as Base
from .Server import Config


import json
import os

class Server(Base):
    def __init__(self, Name, Type: str):
        self.Directory = f"{Config.Data["Instances"]}/{Name}"
        self.Server = f"{self.Directory}/Server"

        self.Downloader = None
        self.Type = Type

        if not Files.Folder(Config.Data["Instances"], Name):
            Files.Folder(self.Directory, "Server")

            if Type == "Fabric":
                self.Downloader = Apis.Fabric()
            elif Type == "Paper":
                self.Downloader = Apis.Paper()

            self.Downloader.RunSteps()
            self.Downloader.Download(self.Server)

            self.MakeConfig()
            self.MakeFiles()

            super().__init__(Name)

    def MakeFiles(self):
        with open(f"{self.Server}/eula.txt", "x") as HahaFakUMojank:
            HahaFakUMojank.write("eula=true")

    def MakeConfig(self):
        Memory = input("How much memory do you need? ")
        Java = input("Which java version do you need? ")

        JarInfo = Info.GetInfo(self)

        Data = {
            "Version": JarInfo["id"],
            "Type": self.Type,
            "Modded": self.Type == "Fabric",
            "Jar": "Server.jar",
            "Java": Java,
            "Memory": Memory,
            "NoGui": True
        }

        with open(f"{self.Directory}/Config.json", "w") as File:
            json.dump(Data, File)