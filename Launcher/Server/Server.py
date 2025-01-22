from .. import Config

import os
import subprocess
import json

class Server:
    def __init__(self, Name: str):
        self.Directory: str = f"{Config.Data["Instances"]}/{Name}"
        self.Server = f"{self.Directory}/Server"

        self.Config: str = f"{self.Directory}/Config.json"
        
        self.LoadConfig()

        self.Process = None

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

    def Run(self):
        LaunchCMD = f'{self.Java} -Xmx{self.Memory} -Xms{self.Memory} -jar "./Server.jar"'

        if self.NoGui:
            LaunchCMD = LaunchCMD  #+ " --nogui"

        def Boot():
            os.chdir(self.Server)
            self.Process = subprocess.run(LaunchCMD, capture_output = True) #, capture_output = True)
        
        print(f"Launch Command: {LaunchCMD}")

        Boot()
        
        #self.Process: subprocess.Popen

        #while True:
        #    Input = input("Say something > ")

        #    Out, Err = self.Process.communicate(Input)

        #    print(Out, Err)

        #Thread = threading.Thread(target=Boot)

        #Thread.start()
        #Thread.

        #self.Process = subprocess.Popen(Cmds). #, capture_output = True)