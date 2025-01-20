from .Base import Downloader
from .Base import Step

class PaperApi(Downloader):

    def __init__(self):
        Main = "https://api.papermc.io/v2/projects/paper"

        Steps = [
            Step(Main, "versions", None, "Select Paper Version.", "Enter a number", 43),
            Step(Main, "builds", None, "Select Paper Build.", "Enter a number", 112),
            "downloads"
        ]

        super().__init__(Main, Steps, "downloads/application/name", 1)
