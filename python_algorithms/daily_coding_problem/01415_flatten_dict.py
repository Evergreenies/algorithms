"""
Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur.
"""


def flatten_dict(dct: dict, parent_key: str = "", sep: str = ".") -> dict:
    flattened = dict()
    for key, value in dct.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            flattened.update(flatten_dict(value, new_key))
        else:
            flattened[new_key] = value

    return flattened


nested_dict = {"key": 3, "foo": {"a": 5, "bar": {"baz": 8}}}
print(flatten_dict(nested_dict))
