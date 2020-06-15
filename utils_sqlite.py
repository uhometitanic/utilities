import sqlite3


class AutoCloseDB:
    """Automatically close database upon exit.
    Return a cursor object.
    """

    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)

    def __enter__(self):
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, *exc_info):
        result = self.conn.__exit__(*exc_info)
        self.cur.close()
        self.conn.close()
        return result
