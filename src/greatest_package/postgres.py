import psycopg2
from typing import Tuple


def query_example(sql_user: str, pw: str, eth_username: str = "daniehei") -> Tuple[int, str]:
    """
    Queries the table corresponding to an eth_username and returns the name and age

    :param sql_user: Your sql username
    :type sql_user: str

    :param pw: The password corresponding to sql_user
    :type pw: str
    
    :param eth_username: The ETH username (should correspond to a table name; default: "Daniel")
    :type eth_username: str

    :returns tuple(str, int) with name and age
    """
    # Connect to an existing database
    with psycopg2.connect(
        host="id-hdb-psgr-cp76.ethz.ch",
        port="5432",
        user=sql_user,
        password=pw,
        database="ivtdata"
        ) as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            # Query the database and obtain data as Python objects.
            cur.execute("SELECT * FROM {}".format(eth_username))
            person = cur.fetchall()
            return person[0]
