def get_all(data):
    """
    Покажет всех кандидатов
    """
    result = '<pre>'
    for name in data:
        result += f"""\n{name['name']}\n
                        {name['position']}\n
                        {name['skills']}\n
                   """
    result += '</pre>'
    return result


def get_by_pk(pk, data):
    """
    Вернет кандидата по pk
    """
    result = '<pre>'
    for name in data:
        if pk == name['pk']:
            result += f"""<img src='{name["picture"]}'>"""
            result += f"""\n{name['name']}\n
                            {name['position']}\n
                            {name['skills']}\n
                       """
    result += '</pre>'
    return result


def get_by_skill(skill_name, data):
    """
    Вернет кандидатов по навыку
    """
    result = '<pre>'
    for name in data:
        if skill_name.lower() in name['skills']:
            result += f"""\n{name['name']}\n
                            {name['position']}\n
                            {name['skills']}\n
                       """
    result += '</pre>'
    return result
