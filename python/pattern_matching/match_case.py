import typing as t


def match_case(data: t.Any):
    match data:
        case None:
            return f"{data} is None"
        case int():
            return f"{data} is int"
        case bytes():
            return f"{data} is bytes"
        case list():
            return f"{data} is list"
        case dict():
            return f"{data} is dict"
        case tuple():
            return f"{data} is tuple"
        case set():
            return f"{data} is set"
        case bytearray():
            return f"{data} is bytearray"
        case float():
            return f"{data} is float"
        case bool():
            return f"{data} is bool"
        case complex():
            return f"{data} is complex"
        case frozenset():
            return f"{data} is frozenset"
        case range():
            return f"{data} is range"
        case slice():
            return f"{data} is slice"
        case memoryview():
            return f"{data} is memoryview"
        case str():
            return f"{data} is str"
        case _:
            return f"{data} is unknown"
