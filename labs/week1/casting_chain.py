original = "42"
print("Start:", original, "type =", type(original))

as_int = int(original)
print("To int:", as_int, "type =", type(as_int))

as_float = float(as_int)
print("To float:", as_float, "type =", type(as_float))

as_str = str(as_float)
print("To str:", as_str, "type =", type(as_str))

as_bool = bool(as_str)
print("To bool:", as_bool, "type =", type(as_bool))
# True — because "42.0" is a non-empty string, and any non-empty string is truthy
