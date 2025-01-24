from .. import Config
#from .Console import Console

import os
import subprocess
import json
import threading

class Server:
    def __init__(self, Name: str):
        self.Directory: str = f"{Config.Data["Instances"]}/{Name}"
        self.Server = f"{self.Directory}/Server"
        #self.Console = Console(self)
        self.Config: str = f"{self.Directory}/Config.json"
        self.Running = False

        self.LoadConfig()

        self.Process: subprocess.Popen = None

    def LoadConfig(self):
        self.Data: dict = json.load(open(self.Config, "r"))
        
        self.Version = self.Data["Version"]
        self.Modded = self.Data["Modded"]
        self.Type = self.Data["Type"]

        self.Memory = self.Data["Memory"]
        self.Jar = self.Data["Jar"]
        self.Java = self.Data["Java"]

        self.NoGui = self.Data["NoGui"]

    def EditConfig(self):
        OldConfig = json.load(open(self.Config, "r"))

        Memory = input(f"Memory [Old: {OldConfig["Memory"]}] > ")
        Java = input(f"Java [Old: {OldConfig["Java"]}] > ")
        #Gui = input(f"NoGui [Old: {OldConfig["NoGui"]}] > ")

        Data = {
            "Version": OldConfig["Version"],
            "Type": self.Type,
            "Modded": self.Type == "Fabric",
            "Jar": "Server.jar",
            "Java": Java,
            "Memory": Memory,
            "NoGui": OldConfig["NoGui"]
        }

        with open(self.Config, "w") as File:
            json.dump(Data, File)

    def Stop(self):
        self.Running = False
        self.Process.kill()
        #self.Console.Send("stop")
        #self.Console.Close()

    def Run(self):
        LaunchCMD = f'{self.Java} -Xmx{self.Memory} -Xms{self.Memory} -jar "./Server.jar"'

        if self.NoGui:
            LaunchCMD = LaunchCMD + " --nogui"

        def Boot():
            os.chdir(self.Server)
            self.Process = subprocess.Popen(LaunchCMD, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, text=True)
            self.Running = True
            os.chdir("../../")

        Boot()

        

        print(f"Launch Command: {LaunchCMD}")            