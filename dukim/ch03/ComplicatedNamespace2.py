class ComplicatedNamespace2:
    ACCEPTED_VALUES = ("id_", "user", "location")

    def __init__(self, **data):
        accepted_data = {
            k: v for k, v in data.items() if k in self.ACCEPTED_VALUES
        }
        self.__dict__.update(accepted_data)


cn = ComplicatedNamespace2(id_=42, user="root", location="127.0.0.1", extra="excluded")

print(cn.id_, cn.user, cn.location)

print(hasattr(cn, "extra"))
