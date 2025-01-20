def Get(Dict: dict, Path: str):
    Result = Dict
    for Level in Path.split("/"):
        Result = Result[Level]

    return Result