import requests
import json

from . import Utils

class Step:
    def __init__(self, Path, ListPath, OptionPath, OutPath, Title, Prompt, Selection = None, Filter = [], Reverse = False):
        self.Path = Path

        self.OptionPath = OptionPath
        self.ListPath = ListPath
        self.OutPath = OutPath
        
        self.Filter = Filter
        self.List = None
        self.Request = None
        self.Reverse = Reverse

        self.Title = Title
        self.Prompt = Prompt
        self.Selection = Selection

        self.Output = self.Path

    def Run(self):
        self.Request = requests.get(f"{self.Path}")
        self.List = json.loads(self.Request.text)
        self.List: list = Utils.Get(self.List, self.ListPath)

        if self.Reverse:
            self.List.reverse()

    def Select(self):
        print(self.Title)

        Index = 0
        AllowedList = []
        for Option in self.List:
            Output = Utils.Get(Option, self.OptionPath)
            
            Allowed = True
            for Blacklisted in self.Filter:
                if Blacklisted in Output:
                    Allowed = False

            if Allowed:
                print(f"[{Index}] {Output}")
                AllowedList.append(Option)
                Index += 1

        self.List = AllowedList

        if self.Selection == None:
            def Select():
                self.Selection = input(f"{self.Prompt} > ")

                try:
                    Selected = self.List[int(self.Selection)]

                    if self.OutPath != None:
                        self.Output = f"{self.Output}/{self.OutPath}/{Utils.Get(Selected, self.OptionPath)}"
                    else:
                        self.Output = f"{self.Output}/{Utils.Get(Selected, self.OptionPath)}"
                except:
                    print("Invalid selection!")
                    Select()

            Select()
        else:
            if self.OutPath != None:
                self.Output = f"{self.Output}/{self.OutPath}/{Utils.Get(self.List[int(self.Selection)], self.OptionPath)}"
            else:
                self.Output = f"{self.Output}/{Utils.Get(self.List[int(self.Selection)], self.OptionPath)}"
        
        return self.Output

