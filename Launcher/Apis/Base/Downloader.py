import requests
import os
import Utils

class Downloader:
    def __init__(self, Path: str, Steps: list, Final: str = None):
        self.Path = Path
        self.Steps = Steps
        self.Final = Final
        self.Goal = ""

    def RunSteps(self):
        Path = self.Path

        for Index, Step in enumerate(self.Steps):
            Step.Path = Path

            Step.Run()
            Path = Step.Select()

            if Index == len(self.Steps) - 1:
                self.Goal = Path

            print(Path)

        print(self.Goal)


    def Download(self, Destination):
        if self.Final != None:
            FinalRequest = requests.get(self.Goal)
            self.Goal = self.Goal + Utils.Get(FinalRequest, self.Final)

        DownloadRequest = requests.get(self.Goal)

        open("Server.jar", 'wb').write(DownloadRequest.content)
        os.rename("./Server.jar", f"{Destination}/Server.jar")
        

        print(f"=== Download Complete! ===\n Url: {self.Goal}\n Path: {Destination}/Server.jar\n ==========================")
        return f"{Destination}/Server.jar"
