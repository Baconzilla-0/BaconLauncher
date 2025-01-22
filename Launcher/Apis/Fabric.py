from .Base import Downloader
from .Base import Step
from .Base import AdvStep

import requests
import json

class FabricApi(Downloader):

    def __init__(self):
        Path = "https://meta.fabricmc.net/v2"
        
        Loader = requests.get(f"{Path}/versions/installer")
        Loader = json.loads(Loader.text)
        Loader = Loader[0]["version"]

        Final = f"{Loader}/server/jar"
        Main = f"{Path}/versions"

        Steps = [
            AdvStep(Main, "game", "version", "loader", "Select Minecraft Version.", "Enter the number which corresponds to your required minecraft version", Filter = ["w", "-"], Reverse=True),
            Step(Main, None, "loader/version", "Select Fabric Version.", "Enter the number which corresponds to your required fabric-loader version", Reverse=True),
            Final
        ]

        

        super().__init__(Main, Steps)
