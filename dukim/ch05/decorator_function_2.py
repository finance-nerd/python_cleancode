import logging


class ControlledException(Exception):
    """도메인에서 발생하는 일반적인 예외"""


RETRIES_LIMIT = 3


def with_retry(retries_limit=RETRIES_LIMIT, allowed_exceptions=None):
    allowed_exceptions = allowed_exceptions or (ControlledException,)

    def retry(operation):
        def wrapped(*args, **kwargs):
            last_raised = None
            for _ in range(retries_limit):
                try:
                    return operation(*args, **kwargs)
                except allowed_exceptions as e:
                    print(f"retrying {operation.__qualname__}")
                    last_raised = e
            return last_raised

        return wrapped

    return retry


@with_retry()
def run_operation(task):
    return task.run()


@with_retry(4)
def run_with_custom_retries_limit(task):
    return task.run()


@with_retry(allowed_exceptions=(AttributeError, ))
def run_with_custom_exceptions(task):
    return task.run()


@with_retry(retries_limit=4, allowed_exceptions=(ZeroDivisionError, ZeroDivisionError ))
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
