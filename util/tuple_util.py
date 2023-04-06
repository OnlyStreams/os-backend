def tuple_list_find(tuple_list, key, default=None):
    for tuple_key, tuple_value in tuple_list:
        if tuple_key == key:
            return tuple_value
    return default
