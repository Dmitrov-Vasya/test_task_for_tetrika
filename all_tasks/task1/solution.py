def strict(func):
    annotations = func.__annotations__
    parameter_names = [param for param in annotations if param != 'return']

    def wrapper(*args, **kwargs):
        if parameter_names:
            for i, arg in enumerate(args):
                param_name = parameter_names[i]
                expected_type = annotations[param_name]
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Parameter '{param_name}' expected type {expected_type.__name__}, got {type(arg).__name__}")
            for param_name, value in kwargs.items():
                if param_name in parameter_names:
                    expected_type = annotations[param_name]
                    if not isinstance(value, expected_type):
                        raise TypeError(f"Parameter '{param_name}' expected type {expected_type.__name__}, got {type(value).__name__}")
        return func(*args, **kwargs)
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

print(sum_two(1, 2)) #3
try:
    print(sum_two(1, 2.5))
except TypeError as e:
    print(e)

@strict
def string_and_boolean(text: str, is_active: bool):
    print(f"Text: {text}, Is Active: {is_active}")

string_and_boolean("Example", True)
try:
    string_and_boolean(123, True)
except TypeError as e:
    print(e)

@strict
def string_and_int(text: str, num: int):
    print(f"Text: {text}, Is Active: {num}")

string_and_int("Example", 5)
try:
    string_and_int(123, 5)
except TypeError as e:
    print(e)