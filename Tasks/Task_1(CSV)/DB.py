import pandas as pd
import psycopg2

username = 'postgres'
password = '1234'
hostname = 'localhost'
port = '5432'
database_name = 'db'

conn = psycopg2.connect(
    dbname=database_name,
    user=username,
    password=password,
    host=hostname,
    port=port
)

cur = conn.cursor()

csv_file_path = 'DB.csv'

df = pd.read_csv(csv_file_path)

df.columns = df.columns.str.strip()

table_name = 'information_csv'

for index, row in df.iterrows():
    # Extract values from DataFrame row
    name = row['name']
    age = row['age']
    gender = row['gender']
    city = row['city']
    sql = f"INSERT INTO {table_name} (name, age, gender, city) VALUES (%s, %s, %s, %s);"
    cur.execute(sql, (name, age, gender, city))

conn.commit()

cur.close()
conn.close()
print(f'Data has been successfully imported into table "{table_name}" in the database.')
