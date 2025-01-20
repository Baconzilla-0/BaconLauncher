import os
import json

class Config:
    Instances = json.load(open("./Config.json", "r"))["Instances"]

class Server:
    def __init__(self, Name: str):
        self.Directory: str = f"{Config.Instances}/{Name}"
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
        with open(f"{self.Directory}/Run.bat", "x") as RunFile:
            JavaExe = os.path.abspath(f"./Java/Java{self.Java}/bin/java.exe")
            LaunchCMD = f'"{JavaExe}" -Xmx{self.Memory} -Xms{self.Memory} -jar "./Server.jar" --nogui'
            RunFile.write(LaunchCMD)

        with open(f"{self.Server}/eula.txt", "x") as HahaFakUMojank:
            HahaFakUMojank.write("eula=true")