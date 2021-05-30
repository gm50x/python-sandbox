def get_hello_message(name=None):
    if (name is None):
        name = 'World'

    return f'Hello {name}!'
