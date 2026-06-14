# Postgres seed script

Inserts 1000 fake employee rows using Faker. Requires a local Postgres database with table `large_employees_db`.

Update the connection string in `seed_employees.py` before running.

```bash
pip install -r requirements.txt
python seed_employees.py
```
