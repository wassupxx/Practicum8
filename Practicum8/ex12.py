import keyword

name = input()
def valid_python_name(name):
    if not name or not (name[0].isalpha() or name[0] == '_'):
        return False

    if not all(c.isalnum() or c == '_' for c in name):
        return False

    if keyword.iskeyword(name):
        return False

    return True
result = valid_python_name(name)
print("Строка может быть именем." if result else "Строка не может быть именем!")