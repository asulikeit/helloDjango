
def copy_by_keys(json, obj, *keys):
    for key in keys:
        json[key] = getattr(obj, key)
        