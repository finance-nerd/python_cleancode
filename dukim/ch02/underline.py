class Connector:
    def __init__(self, source):
        self.source = source
        self._timeout = 60

if __name__ == '__main__':
    conn = Connector("postgresql://localhost")
    print(conn.source)
    print(conn._timeout)
    print(conn.__dict__)