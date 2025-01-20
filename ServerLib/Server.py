import os, requests, json, subprocess, time, ngrok
import pyautogui as pag

def Folder(Path):
    if os.path.exists(Path) != True:
        os.mkdir(Path)

class Server:
    def GetPaperVersions():
        Reqest = requests.get("https://api.papermc.io/v2/projects/paper")
        VersionList = json.loads(Reqest.text)["versions"]
        print(VersionList)
        return VersionList 

    def Download(Version, Destination):
        BuildRequest = requests.get(f"https://api.papermc.io/v2/projects/paper/versions/{Version}")
        BuildsList = json.loads(BuildRequest.text)["builds"]

        BuildNumber = BuildsList[len(BuildsList) - 1]

        JarName = f"paper-{Version}-{BuildNumber}.jar"
        DownloadRequest = requests.get(f"https://api.papermc.io/v2/projects/paper/versions/{Version}/builds/{BuildNumber}/downloads/{JarName}")

        open("Server.jar", 'wb').write(DownloadRequest.content)
        os.rename("./Server.jar", f"{Destination}/Server.jar")

        print(f"=== Download Complete! ===\n Version: {Version}\n Build: {BuildNumber}\n Jar: {JarName}\n Path: {Destination}/Server.jar\n ==========================")
        return JarName

    def New(Version, Name, Memory):
        ServerRoot = f"./Servers/{Name}"
        JavaVersion = "17"
        Config = {
            "Memory": Memory,
            "Version": Version,
            "JavaVersion": JavaVersion
        }

        Folder(ServerRoot)
        Folder(f"{ServerRoot}/Server")
        with open(f"{ServerRoot}/Config.json", "x") as ConfigFile:
            ConfigJson = json.dumps(Config)
            ConfigFile.write(ConfigJson)

        JarFile = Server.Download(Version, f"{ServerRoot}/Server")

        with open(f"{ServerRoot}/Run.bat", "x") as RunFile:
            JavaExe = os.path.abspath(f"./Java/Java{JavaVersion}/bin/java.exe")
            LaunchCMD = f'"{JavaExe}" -Xmx{Memory} -Xms{Memory} -jar "./Server.jar" --nogui'
            RunFile.writelines(["start ngrok.bat\n", f"cd ./Servers/{Name}/Server/\n", LaunchCMD])

        with open(f"{ServerRoot}/Server/eula.txt", "x") as HahaFakUMojank:
            HahaFakUMojank.write("eula=true")

    def GetList():
        ServerFolders = os.listdir("./Servers")
        Servers = []

        for ServerFolder in ServerFolders:
            with open(f"./Servers/{ServerFolder}/Config.json", "r") as Config:
                ServerInfo = json.loads(Config.read())

            SplitName = ServerFolder.split("/")
            ServerInfo["Name"] = SplitName[len(SplitName) - 1]
            print(ServerInfo)
            Servers.append(ServerInfo)

        return Servers
    
    def Get(Name):
        ServerList = Server.GetList()

        for ServerInfo in ServerList:
            if ServerInfo["Name"] == Name:
                ServerInfo["Jar"] = f"./Servers/{Name}/Server/Server.jar"

                return ServerInfo
            
    def Start(Name):
        ##ServerData = Server.Get(Name)
        
        os.system(f"start Servers\{Name}\Run.bat")
        ##Listener = ngrok.forward(addr="localhost:25565", authtoken="2K25ORb6kn2ewp5mjlrap7vai7f_6V28qdNsDmk5yJQ35FbQU", proto="tcp")

        #listener = ngrok.forward(25565, "tcp", authtoken= )

        ##print(Listener)
        try:
            os.remove("./tunnels.json")
        except:
            pass
        
        time.sleep(2)

        os.system("curl  http://localhost:4040/api/tunnels > tunnels.json")

        with open('tunnels.json') as data_file:    
            datajson = json.load(data_file)
            ip = datajson["tunnels"][0]["public_url"]

        return ip