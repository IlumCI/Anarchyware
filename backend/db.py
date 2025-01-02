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

def add_score_column():
    conn = connect()
    cur = conn.cursor()
    cur.execute("ALTER TABLE targets ADD COLUMN score FLOAT DEFAULT 0.0;")
    conn.commit()
    conn.close()

def add_ssl_columns():
    conn = connect()
    cur = conn.cursor()
    cur.execute("ALTER TABLE targets ADD COLUMN domain VARCHAR(255);")
    cur.execute("ALTER TABLE targets ADD COLUMN ssl_valid_days INT;")
    cur.execute("ALTER TABLE targets ADD COLUMN domain_age INT;")
    conn.commit()
    conn.close()

def add_social_columns():
    conn = connect()
    cur = conn.cursor()
    
    # Store employee data
    cur.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            profile_url VARCHAR(255),
            company VARCHAR(255)
        );
    """)
    
    # Store breach data
    cur.execute("""
        CREATE TABLE IF NOT EXISTS email_breaches (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255),
            breach_name VARCHAR(255),
            company VARCHAR(255)
        );
    """)
    conn.commit()
    conn.close()

