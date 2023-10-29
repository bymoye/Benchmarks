from types import NoneType
import typing as t

mapping = {
    None: "%s is None",
    int: "%s is int",
    bytes: "%s is bytes",
    list: "%s is list",
    dict: "%s is dict",
    tuple: "%s is tuple",
    set: "%s is set",
    bytearray: "%s is bytearray",
    float: "%s is float",
    bool: "%s is bool",
    complex: "%s is complex",
    frozenset: "%s is frozenset",
    range: "%s is range",
    slice: "%s is slice",
    memoryview: "%s is memoryview",
    str: "%s is str",
    NoneType: "%s is unknown",
}


def dict_lookup(data: t.Any):
    return mapping.get(type(data), mapping[NoneType]) % data
