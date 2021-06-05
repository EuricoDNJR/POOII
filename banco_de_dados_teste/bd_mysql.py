import mysql.connector as mysql

conexao = mysql.connect(host = "localhost", db="pooii", user="root", passwd="sh40l1nm4t4d0rdeporco")
cursor = conexao.cursor()

sql = """CREATE TABLE IF NOT EXISTS usuarios(id integer AUTO_INCREMENT PRIMARY KEY,
         nome text NOT NULL,email text NOT NULL);"""

nome = "flavinho"
email = "flavinhodopineu@gmail.com"

cursor.execute(sql)
for i in range(5):
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (%s,%s)", (nome, email))

cursor.execute("SELECT * from usuarios")

for c in cursor:
    print(c)

conexao.commit()
conexao.close()

