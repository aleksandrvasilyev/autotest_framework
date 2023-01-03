import json


class User:
    def __init__(self, **kwargs):
        self.id = 1 if "id" not in kwargs.keys() else kwargs["id"]
        self.email = "george.bluth@reqres.in" if "email" not in kwargs.keys() else kwargs["email"]
        self.first_name = "George" if "first_name" not in kwargs.keys() else kwargs["first_name"]
        self.last_name = "Bluth" if "last_name" not in kwargs.keys() else kwargs["last_name"]
        self.avatar = "https://reqres.in/img/faces/1-image.jpg" if "avatar" not in kwargs.keys() else kwargs["avatar"]

    @classmethod
    def from_json(cls, **kwargs):
        return cls(**kwargs)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_dict(self):
        return self.__dict__

    def update_dict(self, **kwargs):
        self.__dict__.update(**kwargs)

    def get_json(self):
        return json.dumps(self.__dict__)
