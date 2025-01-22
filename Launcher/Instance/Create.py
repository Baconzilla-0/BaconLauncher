from ..Server import Create
from .. import Config
from .Instance import Instance as Base

class Instance(Base):
    def __init__(self):
        self.Name = input("Instance Name > ")

        def Select_Software():
            Options = [
                "Paper",
                "Fabric"
            ]

            for Index, Option in enumerate(Options):
                print(f"[{Index}] {Option}")

            Selection = input("Server Software > ")
            try:
                Selected = Options[int(Selection)]

                return Selected
            except:
                print("Invalid software!")
                return Select_Software()


        self.Server = Create(self.Name, Select_Software())

        super().__init__(self.Name)
