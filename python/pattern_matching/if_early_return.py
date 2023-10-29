import typing as t


def if_early_return(data: t.Any):
    if data is None:
        return f"{data} is None"
    if isinstance(data, int):
        return f"{data} is int"
    if isinstance(data, bytes):
        return f"{data} is bytes"
    if isinstance(data, list):
        return f"{data} is list"
    if isinstance(data, dict):
        return f"{data} is dict"
    if isinstance(data, tuple):
        return f"{data} is tuple"
    if isinstance(data, set):
        return f"{data} is set"
    if isinstance(data, bytearray):
        return f"{data} is bytearray"
    if isinstance(data, float):
        return f"{data} is float"
    if isinstance(data, bool):
        return f"{data} is bool"
    if isinstance(data, complex):
        return f"{data} is complex"
    if isinstance(data, frozenset):
        return f"{data} is frozenset"
    if isinstance(data, range):
        return f"{data} is range"
    if isinstance(data, slice):
        return f"{data} is slice"
    if isinstance(data, memoryview):
        return f"{data} is memoryview"
    if isinstance(data, str):
        return f"{data} is str"
    return f"{data} is unknown"
