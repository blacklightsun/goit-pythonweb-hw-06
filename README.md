# goit-pythonweb-hw-06
goit-pythonweb-hw-06 GoIT Neoversity module "FullStack Web Development with Python" Homework 6


**Опис файлів:**
1. models.py - моделі даних для міграції
2. connect.py - налаштування з'єднання з базою та створення сесій
3. seed.py - заповнення бази випадковими значеннями
4. my_select.py - виконання запитів до бази (10+2 штук)
5. functions.py - службовий модуль з CRUD-функціями для CLI-додатку
6. main.py - запуск CLI-додатку
7. my_select.sql - sql-запити до бази для перевірки python-запитів



**Порядок використання:**
1. Запустити контейнер бази Postgresql командою:
```bash
docker-compose up -d
```

2. Створити моджелі даних в базі командами:
```bash
alambic init migrations
alembic revision --autogenerate -m "Init"
alembic upgrade head
```

3. Заповнити базу даними командою:
```bash
python seed.py
```

4. Перевірити select-запити до бази:
```bash
python my_select.py
```

5. Ознайомитися з синтавксисом команд CLI-додатку:
```bash
python main.py --help
```

6. Зупинити контейнер бази Postgresql командою:
```bash
docker-compose down
```