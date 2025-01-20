import os
import sys

def Folder(Path: os.PathLike, Name: str):
    Location = f"{Path}/{Name}"

    if os.path.isdir(Location):
        return True
    else:
        os.mkdir(Location)
        return False