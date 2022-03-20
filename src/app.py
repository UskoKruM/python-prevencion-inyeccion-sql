from db import get_connection

try:
    connection = get_connection()
    with connection.cursor() as cursor:
        id = 3
        # query = "SELECT id, lastname FROM creator WHERE id = 3"
        # query = "SELECT id, lastname FROM creator WHERE id = {}".format(id)
        # query = f"SELECT id, lastname FROM creator WHERE id = {id}".format(id)

        # cursor.execute("SELECT id, lastname FROM creator WHERE id = %s", (int(id),))

        cursor.execute("call sp_readCreator(%s)", (int(id),))

        row = cursor.fetchone()
        print(row)
    connection.close()
except Exception as ex:
    print(ex)
