# def wrong_user_display(user_metadata: dict = {"name": "John", "age": 30}):
#     name = user_metadata.pop("name")
#     age = user_metadata.pop("age")
#     return f"{name} ({age})"

def wrong_user_display(user_metadata: dict=None):
    if user_metadata is None:
        user_metadata = {"name": "John", "age": 30}
    name = user_metadata.pop("name")
    age = user_metadata.pop("age")
    return f"{name} ({age})"

print(wrong_user_display())
print(wrong_user_display({"name": "Jane", "age": 25}))
print(wrong_user_display())