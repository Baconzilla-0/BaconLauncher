from .. import Files
from .. import Config

from .Instance import Instance

import os

class InstanceList:
    def __init__(self):
        self.List = []

    def Load(self):
        self.List = []
        Instances = Config.Data["Instances"]

        for Name in os.listdir(Instances):
            Directory = os.path.join(Instances, Name)
            if os.path.isdir(Directory):
                Item = Instance(Name)
                self.List.append(Item)
    
    def Show(self):
        if len(self.List) < 1:
            print("No instances found, use new to create one.")

        for Index, Item in enumerate(self.List):
            Item: Instance

            print(f"[{Index}] {Item.Name}")

