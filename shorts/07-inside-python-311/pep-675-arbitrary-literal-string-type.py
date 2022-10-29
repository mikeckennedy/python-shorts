# PEP 675 – Arbitrary Literal String Type
from sqlite3 import Connection


class User: ...


conn = Connection()


def query_user(connection: Connection, user_id: str) -> User:
    query = f"SELECT * FROM data WHERE user_id = {user_id}"
    connection.execute(query)
    return User()  # With details from query


query_user(conn, "user123")  # OK.
query_user(conn, "user123; DROP TABLE data;")  # Delete the table.
query_user(conn, "user123 OR 1 = 1")  # Fetch all users (since 1 = 1 is always true).


def query_user(connection: Connection, user_id: str) -> User:
    query = "SELECT * FROM data WHERE user_id = ?"  # <-- Safe, literal string.
    conn.execute(query, (user_id,))  # <-- Safe, database parameter.
    return User()  # With details from query




















# def safer_func(text: str):
#     print(text)
# x = 7
#
# literal_text: LiteralString = "ABC"
# literal_text2 = f"ABC{x}"
# safer_func(literal_text)
# safer_func(literal_text2)
