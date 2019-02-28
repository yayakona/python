# coding: UTF-8

def splits_string(org_str: str, keys: List[str]) -> List[str]:
    edit_str = org_str
    for key, next_key in zip(keys[:-1], keys[1:]):
        edit_str = edit_str.replace(key, next_key)
    return edit_str.split(keys[-1])