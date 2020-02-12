def trace_decorator(function):
    def wrapped(*args, **kwargs):
        print(f"{function.__qualname__} 실행")
        return function(*args, **kwargs)
    return wrapped

@trace_decorator
def process_account(account_id):
    """ id별 계정 처리 """
    print(f"{account_id} 계정 처리")

help(process_account)

print(process_account.__qualname__)

