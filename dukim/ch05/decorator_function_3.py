import logging


class ControlledException(Exception):
    """도메인에서 발생하는 일반적인 예외"""


RETRIES_LIMIT = 3


class WithRetry:
    def __init__(self, retries_limit=RETRIES_LIMIT, allowed_exceptions=None):
        self.retries_limit = retries_limit
        self.allowed_exceptions = allowed_exceptions or (ControlledException,)

    def __call__(self, operation):
        def wrapped(*args, **kwargs):
            last_raised = None
            for _ in range(self.retries_limit):
                try:
                    return operation(*args, **kwargs)
                except self.allowed_exceptions as e:
                    print(f"retrying {operation.__qualname__}")
                    last_raised = e
            return last_raised

        return wrapped


@WithRetry()
def run_operation(task):
    return task.run()


@WithRetry(4)
def run_with_custom_retries_limit(task):
    return task.run()


@WithRetry(allowed_exceptions=(AttributeError, ))
def run_with_custom_exceptions(task):
    return task.run()


@WithRetry(retries_limit=4, allowed_exceptions=(ZeroDivisionError, ZeroDivisionError ))
def run_with_custom_parameters(task):
    return task.run()


class Task:
    def run(self):
        print("task run")


class ControlledExceptionTask:
    def run(self, *args, **kwargs):
        raise ControlledException()


class ZeroDivisionErrorTask:
    def run(self, *args, **kwargs):
        raise ZeroDivisionError()


class AttributeErrorTask:
    def run(self, *args, **kwargs):
        raise AttributeError()


run_operation(Task())
run_with_custom_retries_limit(ControlledExceptionTask())
run_with_custom_exceptions(AttributeErrorTask())
run_with_custom_parameters(ZeroDivisionErrorTask())
# run_with_custom_exceptions(ZeroDivisionErrorTak())
