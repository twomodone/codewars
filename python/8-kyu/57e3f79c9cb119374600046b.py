def hello(name = ""):
    if not name:
        return "Hello, World!"
    return f"Hello, {name[:1].upper() + name[1:].lower()}!"
