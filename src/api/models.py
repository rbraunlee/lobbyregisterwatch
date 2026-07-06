def key_type(dic:dict)->dict:
    overview = {}
    for key, value in dic.items():
        if isinstance(value, dict):
            overview.update({key: key_type(value)})

        elif isinstance(value, list):
            for ele in value:
                if isinstance(ele, dict):
                    overview.update({f"{key}_list": key_type(ele)})

                else:
                    overview.update({"list": str(type(ele))})

        else:
            overview.update({key: str(type(value))})
    return overview
