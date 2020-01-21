def stop_database():
    print("systemctl stop postgresql.server")


def start_database():
    print("systemctl start postgresql.server")


class DBHandler:
    def __enter__(self):
        stop_database()
        return self

    def __exit__(self, exc_type, ex_value, ex_traceback):
        start_database()


def db_backup():
    print("pg_dump database")


if __name__ == '__main__':
    with DBHandler():
        db_backup()