
def catch_errors(func):
    def wrapper(data, *args, **kwargs):
        try:
            return func(data, *args, **kwargs)
        except KeyError as e:
            print(f"Found 1 error during execution of your function: KeyError no such key as {e.args[0]}")
    return wrapper