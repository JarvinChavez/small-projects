import psycopg2
import random
from faker import Faker
            
conn = psycopg2.connect("dbname=business_data user=db password=db")
cur = conn.cursor()

# Insert 1000 employees
fake = Faker()
for _ in range(1000):
    name = fake.name()
    email = fake.email()
    phone_number = fake.phone_number()
    status = random.choice(['active', 'inactive'])
    department = random.choice(['HR', 'Engineering', 'Sales', 'Marketing'])
    salary = round(random.uniform(40000, 120000), 2)
    employment_time = fake.date_between(start_date='-10y', end_date='today')  
    
    cur.execute("""
        INSERT INTO large_employees_db (name, email, phone_number, status, department, salary, employment_time)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (name, email, phone_number, status, department, salary, employment_time))

conn.commit()
cur.close()
conn.close()
