from . import Instance
import time

class Menu:
    def __init__(self):
        self.List = Instance.List()
        self.List.Load()

    def Main(self):
        time.sleep(0.5)
        self.List.Show()
          
        print(f"Select [Index] | New... [N], Exit [E]")

        Selection = input(" > ").lower()
        if Selection == "n":
            Instance.Create()
            self.List.Load()
            self.Main()
        elif Selection == "e":
            exit()
        else:
            self.Select(Selection)
            #print("Invalid option!")

    def Select(self, Index):
        #Selection = input("Back [B] | [Index]  > ")

        try:
            Selected: Instance = self.List.List[int(Index)]
            self.Options(Selected)
        except IndexError:
            print("Invalid index!")
            self.Main()

    def Options(self, Instance: Instance.Instance):
        def Display():
            print(f"Selected: {Instance.Name}")
            print(f"Start [S] | Edit [E] | Delete [D] | Back [B]")
        
        def Input():
            Display()

            Selection = input(" > ").lower()
            if Selection == "s":
                Instance.Start()
                self.Options(Instance)
            elif Selection == "e":
                Instance.Edit()
                self.Options(Instance)
            elif Selection == "d":
                print(f"Are you sure? [Deleting: {Instance.Name}]")
                Sure = input("Y/N > ")

                print(Sure)
                if Sure.lower().__contains__("y"):
                    Instance.Delete()
                    print(f"Deleted: {Instance.Name}")
                
                self.Main()

            elif Selection == "b":
                self.Main()
            else:
                print("Invalid option!")
                Input()
        
        Input()

        


