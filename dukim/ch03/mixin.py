class BaseTokenizer:
    def __init__(self, str_token):
        self.str_token = str_token

    def __iter__(self):
        yield from self.str_token.split("-")


tk = BaseTokenizer("222-333-444-555-abc")
print(list(tk))


class UpperIterableMixin:
    def __iter__(self):
        return map(str.upper, super().__iter__())


class Tokenizer(UpperIterableMixin, BaseTokenizer):
    pass


tk2 = Tokenizer("222-333-444-555-abc")
print(list(tk2))
