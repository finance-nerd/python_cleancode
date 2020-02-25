import os
import tempfile

PURCHASES_FILE = os.path.join(tempfile.gettempdir(), "purchases.csv")


def create_purchases_file(filename, entries=1_000_000):
    if os.path.exists(filename):
        return

    with open(filename, "w+") as f:
        for i in range(entries):
            line = f"2018-01-01,{i}\n"
            f.write(line)


if __name__ == "__main__":
    create_purchases_file(PURCHASES_FILE)