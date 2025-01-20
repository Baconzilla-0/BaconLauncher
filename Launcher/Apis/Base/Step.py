import requests
import json

from . import Utils

class Step:
    def __init__(self, Path, Return, OptionPath, Title, Prompt, Selection = None):
        self.Path = Path
        self.Return = Return
        
        self.List = None
        self.Request = None

        self.OptionPath = OptionPath
        self.Title = Title
        self.Prompt = Prompt
        self.Selection = Selection

        self.Output = self.Path

    def Run(self):
        self.Request = requests.get(f"{self.Path}")
        self.List = json.loads(self.Request.text)
        self.List = Utils.Get(self.List, self.Return)

    def Select(self):
        print(self.Title)


        for Index, Option in enumerate(self.List):
            print(f"[{Index}] {Utils.Get(Option, self.OptionPath)}")

        if self.Selection == None:
            def Select():
                self.Selection = input(f"{self.Prompt} > ")

                try:
                    Selected = self.List[int(self.Selection)]

                    self.Output = f"{self.Output}/{self.Return}/{Utils.Get(Selected, self.OptionPath)}"
                except:
                    print("Invalid selection!")
                    Select()

            Select()
        else:
            self.Output = f"{self.Output}/{self.Return}/{Utils.Get(self.List[int(self.Selection)], self.OptionPath)}"
        
        return self.Output

