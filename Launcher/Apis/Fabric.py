from .Base import Downloader
from .Base import Step

import requests
import json

class FabricApi(Downloader):

    def __init__(self):
        Main = "https://meta.fabricmc.net/v2"
        
        Loader = requests.get(f"{Main}/versions/installer")
        Loader = json.loads(Loader.text)
        Loader = Loader[0]["version"]

        Final = f"{Loader}/server/jar"

        Steps = [
            Step(Main, None, None, "Select Fabric Version.", "Enter a number"),
            Step(Main, None, None, "Select Fabric Build.", "Enter a number"),
        ]

        super().__init__(f"{Main}/versions/loader", Steps, Final)
