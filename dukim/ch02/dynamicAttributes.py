class DynamicAttributes:
    def __init__(self, attribute):
        self.attribute = attribute

    def __getattr__(self, attr):
        if attr.startswith("fallback_"):
            name = attr.replace("fallback_", attr)
            return f"[fallback resolved] {name}"
        raise AttributeError(f"{self.__class__.__name__} 에는 {attr} 속성이 없음.")

dyn = DynamicAttributes("value")
print(dyn.attribute)

print(dyn.fallback_test)

dyn.__dict__["fallback_new"] = "new value"
print(dyn.fallback_new)

print(getattr(dyn, "somthing", "default"))