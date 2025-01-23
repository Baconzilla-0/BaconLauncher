import importlib
SysInstalled = True
try:
    import sys
except:
    SysInstalled = False

Name = "BaconLauncher"
Requirements = ["requests", "sys", "os", "subprocess", "json"]

print(f"Welcome to the {Name} Setup")

print(f"\nThe requirements of this program are: ")

MissingRequirement = False
for Require in Requirements:
    try:
        importlib.import_module(Require)
        print(f"{Require} [INSTALLED]")
    except ImportError:
        print(f"{Require} [MISSING]")
        MissingRequirement = True
print(" ")

if MissingRequirement:
    if SysInstalled:
        Install = f"{sys.executable} -m pip install [Name of requirement]"
    else:
        Install = f"python -m pip install [Name of requirement]"

    print("It appears you are missing one or more of the modules required to run this program,")
    print(f"You can install modules by typing '{Install}'")
else:
    print('It looks like you have everything you need!')
    print(f"run Main.py to start using {Name}.")