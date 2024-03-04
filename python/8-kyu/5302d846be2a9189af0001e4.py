def say_hello(names, city, state):
    hello_message = "Hello, " + " ".join(names) + '!'
    welcome_message = f"Welcome to {city}, {state}!"
    return f"{hello_message} {welcome_message}"
