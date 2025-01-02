import psycopg2

def connect():
    return psycopg2.connect(
        database="nato_map",
        user="user",
        password="password",
        host="localhost",
        port="5432"
    )

def get_targets():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT name, industry, ip FROM targets")
    targets = cur.fetchall()
    conn.close()
    return [{"name": t[0], "industry": t[1], "ip": t[2]} for t in targets]
