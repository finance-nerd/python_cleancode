import contextlib

def stop_database():
    print("systemctl stop postgresql.server")


def start_database():
    print("systemctl start postgresql.server")


class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        stop_database()

    def __exit__(self, exc_type, ex_value, ex_traceback):
        start_database()

@dbhandler_decorator()
def offline_backup():
    print("pg_dump database")


if __name__ == '__main__':
    offline_backup()