import logging


class ControlledException(Exception):
    """도메인에서 발생하는 일반적인 예외"""


def retry(operation):
    def wrapped(*args, **kwargs):
        last_raised = None
        RETRIES_LIMIT = 3
        for _ in range(RETRIES_LIMIT):
            try:
                return operation(*args, **kwargs)
            except ControlledException as e:
                print(f"retrying {operation.__qualname__}")
                last_raised = e
        return last_raised

    return wrapped


@retry
def run_operation(task):
    return task.run()


class Task:
    def run(self):
        print("task run")


class ExceptionTask:
    def run(self, *args, **kwargs):
        raise ControlledException()


run_operation(Task())
run_operation(ExceptionTask())
