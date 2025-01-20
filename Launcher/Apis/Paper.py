from Base import Downloader
from Base import Step

class PaperApi(Downloader):

    def __init__(self):
        Main = "https://api.papermc.io/v2/projects/paper"

        Steps = [
            Step(Main, "versions", "", "Select Paper Version.", "Enter a number"),
            Step(Main, "builds", "", "Select Paper Build.", "Enter a number"),
        ]

        super().__init__(Main, Steps, "downloads/application/name")
