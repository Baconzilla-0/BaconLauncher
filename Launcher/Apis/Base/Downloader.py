import requests
import os
import json

from . import Utils

class Downloader:
    def __init__(self, Path: str, Steps: list, Final: str = None, FinalStep: int = None):
        self.Path = Path
        self.Steps = Steps

        self.Final = Final
        self.FinalStep = FinalStep

        self.Goal = ""

    def RunSteps(self):
        Last = self.Steps[0].Path

        for Index, Step in enumerate(self.Steps):
            if type(Step) is str:
                Last = f"{Last}/{Step}"
            else:
                Step.Path = Last
                Step.Output = Last

                Step.Run()
                Step.Select()
                Last = Step.Output

            if Index == len(self.Steps) - 1:
                self.Goal = Last

            print(Last)

        print(self.Goal)


    def Download(self, Destination):
        if self.Final != None:
            FinalRequest = requests.get(self.Steps[self.FinalStep].Output)
            print(FinalRequest.text)
            FinalRequest = json.loads(FinalRequest.text)
            self.Goal = f"{self.Goal}/{Utils.Get(FinalRequest, self.Final)}"

        DownloadRequest = requests.get(self.Goal)

        open("Server.jar", 'wb').write(DownloadRequest.content)
        os.rename("./Server.jar", f"{Destination}/Server.jar")
        

        print(f"=== Download Complete! ===\n Url: {self.Goal}\n Path: {Destination}/Server.jar\n ==========================")
        return f"{Destination}/Server.jar"
