from .Server import Server
import zipfile
import json
import io

def GetInfo(Server: Server):
    Data = zipfile.ZipFile(f"{Server.Server}/Server.jar", 'r')

    Info = None

    if Server.Type == "Paper":
        with io.TextIOWrapper(Data.open("version.json"), encoding="utf-8") as File:
            Info =  json.loads(File.read())

    if Server.Type == "Fabric": # why dont fabric just use json like normal people D:
        with io.TextIOWrapper(Data.open("install.properties"), encoding="utf-8") as File:
            Text = File.read()
            Split = Text.split("=")
            print(Split)

            Info = { "id": Split[2] }
    
    return Info