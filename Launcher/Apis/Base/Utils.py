def Get(Dict: dict, Path: str):
    Result = Dict
    if Path == None:
        return Result
    else:
        for Level in Path.split("/"):
            if Level != "":
                Result = Result[Level]

        return Result