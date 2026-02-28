import json
from json import JSONEncoder


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Custom Encoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {
                "name": o.name,
                "age": o.age,
                "__User__": True
            }
        return super().default(o)


# Custom Decoder
def decode_user(dct):
    if "__User__" in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct


# Create object
user = User("Max", 27)

# Convert to JSON
user_json = json.dumps(user, cls=UserEncoder)
print("Encoded JSON:")
print(user_json)

# Convert back to Python object
decoded_user = json.loads(user_json, object_hook=decode_user)

print("\nDecoded Object:")
print(type(decoded_user))
print(decoded_user.name)
