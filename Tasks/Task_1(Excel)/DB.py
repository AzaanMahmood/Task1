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

excel_file_path = 'DB.xlsx'

df = pd.read_excel(excel_file_path)

table_name = 'information'

for index, row in df.iterrows():
    values = tuple(row)
    # Construct the SQL query
    sql = f"INSERT INTO {table_name} VALUES {values};"
    cur.execute(sql)

conn.commit()

cur.close()
conn.close()

# Confirm the data has been imported successfully
# print(f'Data has been successfully imported into table "{table_name}" in the PostgreSQL database.')
