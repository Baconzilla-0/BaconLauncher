from .Base import Downloader
from .Base import Step

class PaperApi(Downloader):

    def __init__(self):
        Main = "https://api.papermc.io/v2/projects/paper"

        Steps = [
            Step(Main, "versions", None, "Select Minecraft Version.", "Enter the number which corresponds to your required minecraft version"),
            Step(Main, "builds", None, "Select Paper Version.", "Enter the number corresponding to your required papermc version"),
            "downloads"
        ]

        super().__init__(Main, Steps, "downloads/application/name", 1)
