import mysql.connector
from faker import Faker
import random

# Conectar ao banco de dados MySQL
conn = mysql.connector.connect(
    host="localhost",       # Endereço do servidor MySQL
    user="root",            # Seu usuário do MySQL
    password="",   # Sua senha do MySQL
    database="vendas_dashboard"
)

cursor = conn.cursor()

# Gerar dados falsos
fake = Faker('pt_BR')

for i in range(1, 501):
    order_id = i
    date = fake.date_between(start_date='-1y', end_date='today')
    category = random.choice(['Brinquedos', 'Presentes', 'Acessórios'])
    amount = round(random.uniform(20, 500), 2)
    units = random.randint(1, 10)
    
    # Inserir dados na tabela de vendas
    cursor.execute(
        "INSERT INTO vendas (OrderID, Date, Category, Amount, Units) VALUES (%s, %s, %s, %s, %s)",
        (order_id, date, category, amount, units)
    )

# Commit e fechamento da conexão
conn.commit()
cursor.close()
conn.close()

print("Dados inseridos com sucesso!")
