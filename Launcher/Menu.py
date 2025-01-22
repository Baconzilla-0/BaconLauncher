from . import Instance

class Menu:
    def __init__(self):
        self.List = Instance.List()
        self.List.Load()

    def Main(self):
        self.List.Show()
          
        print(f"Select [S] | New... [N]")

        Selection = input(" > ").lower()
        if Selection == "s":
            self.Select()
        elif Selection == "n":
            Instance.Create()
            self.List.Load()
            self.Main()
        else:
            print("Invalid option!")

    def Select(self):
        self.List.Show()
        Selection = input("Select an Instance > ")

        try:
            Selected: Instance = self.List.List[int(Selection)]
            self.Options(Selected)
        except:
            print("Invalid instance!")
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
            elif Selection == "e":
                Instance.Edit()
                self.Options(Instance)
            elif Selection == "d":
                print("ill add this later")
            elif Selection == "b":
                self.Select()
            else:
                print("Invalid option!")
                Input()
        
        Input()

        


