class ComplicatedNamespace:
    ACCEPTED_VALUES = ("id_", "user", "location")

    @classmethod
    def init_with_data(cls, **data):
        instance = cls()
        for key, value in data.items():
            if key in cls.ACCEPTED_VALUES:
                setattr(instance, key, value)
        return instance

cn = ComplicatedNamespace.init_with_data(id_=42, user="root", location="127.0.0.1", extra="excluded")

print(cn.id_, cn.user, cn.location)

print(hasattr(cn, "extra"))
