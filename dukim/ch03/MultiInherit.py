class BaseModule:
    module_name = "top"

    def __init__(self, module_name):
        self.name = module_name

    def __str__(self):
        return f"{self.module_name}:{self.name}"

class BaseModule1(BaseModule):
    module_name = "module-1"

class BaseModule2(BaseModule):
    module_name = "module-2"

class BaseModule3(BaseModule):
    module_name = "module-3"

class ConcreteModuleA12(BaseModule1, BaseModule2):
    """ 1,2 확장 """

class ConcreteModuleA23(BaseModule2, BaseModule3):
    """ 2,3 확장 """

print(str(ConcreteModuleA12("test")))

print([cls.__name__ for cls in ConcreteModuleA12.mro()])