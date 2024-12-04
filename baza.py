import sqlite3

conn = sqlite3.connect('travel_agency.db')
cursor = conn.cursor()

# Типы виз
cursor.execute('''
    CREATE TABLE IF NOT EXISTS types_of_visas (
        type_id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL
    )
''')

# Страны
cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        country_id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL
    )
''')

# Средства перемещения
cursor.execute('''
    CREATE TABLE IF NOT EXISTS transport_types (
        transport_id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL
    )
''')

# Отели
cursor.execute('''
    CREATE TABLE IF NOT EXISTS hotels (
        hotel_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        country_id INTEGER,
        region TEXT,
        FOREIGN KEY (country_id) REFERENCES countries(country_id)
    )
''')

# Питание
cursor.execute('''
    CREATE TABLE IF NOT EXISTS food_types (
        food_id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL
    )
''')

# Клиенты
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        client_id INTEGER PRIMARY KEY AUTOINCREMENT,
        last_name TEXT NOT NULL,
        first_name TEXT NOT NULL,
        middle_name TEXT,
        phone TEXT UNIQUE NOT NULL,
        passport TEXT NOT NULL,
        registration_date DATE NOT NULL,
        notes TEXT
    )
''')

# Путёвки
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tours (
        tour_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        country_id INTEGER,
        hotel_id INTEGER,
        transport_included BOOLEAN NOT NULL,
        food_id INTEGER,
        departure_date DATE NOT NULL,
        return_date DATE NOT NULL,
        price REAL NOT NULL,
        visa_discount REAL DEFAULT 0,
        passport_discount REAL DEFAULT 0,
        FOREIGN KEY (country_id) REFERENCES countries(country_id),
        FOREIGN KEY (hotel_id) REFERENCES hotels(hotel_id),
        FOREIGN KEY (food_id) REFERENCES food_types(food_id)
    )
''')

# Продажа путёвок
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tour_sales (
        sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER NOT NULL,
        tour_id INTEGER NOT NULL,
        client_level INTEGER NOT NULL,
        sale_date DATE NOT NULL,
        payment_amount REAL NOT NULL,
        FOREIGN KEY (client_id) REFERENCES clients(client_id),
        FOREIGN KEY (tour_id) REFERENCES tours(tour_id)
    )
''')

# Скидки клиентам
cursor.execute('''
    CREATE TABLE IF NOT EXISTS client_discounts (
        level INTEGER PRIMARY KEY,
        tour_discount REAL NOT NULL
    )
''')

# Тарифы на визы
cursor.execute('''
    CREATE TABLE IF NOT EXISTS visa_tariffs (
        tariff_id INTEGER PRIMARY KEY,
        validity_period INTEGER NOT NULL,
        type_id INTEGER NOT NULL,
        country_id INTEGER NOT NULL,
        price REAL NOT NULL,
        FOREIGN KEY (type_id) REFERENCES types_of_visas(type_id),
        FOREIGN KEY (country_id) REFERENCES countries(country_id)
    )
''')

# Тарифы на загранпаспорта
cursor.execute('''
    CREATE TABLE IF NOT EXISTS passport_tariffs (
        tariff_id INTEGER PRIMARY KEY,
        price REAL NOT NULL
    )
''')

# Виза
cursor.execute('''
    CREATE TABLE IF NOT EXISTS visas (
        visa_id INTEGER PRIMARY KEY,
        series TEXT NOT NULL,
        number TEXT NOT NULL,
        issue_date DATE NOT NULL,
        valid_until DATE NOT NULL,
        type_id INTEGER NOT NULL,
        country_id INTEGER NOT NULL,
        num_entries INTEGER NOT NULL,
        duration INTEGER NOT NULL,
        client_id INTEGER NOT NULL,
        FOREIGN KEY (type_id) REFERENCES types_of_visas(type_id),
        FOREIGN KEY (country_id) REFERENCES countries(country_id),
        FOREIGN KEY (client_id) REFERENCES clients(client_id)
    )
''')

# Выдача виз
cursor.execute('''
    CREATE TABLE IF NOT EXISTS visa_issuances (
        issue_date DATE NOT NULL,
        tariff_id INTEGER NOT NULL,
        visa_id INTEGER NOT NULL,
        tour_id INTEGER,
        payment_amount REAL NOT NULL,
        FOREIGN KEY (tariff_id) REFERENCES visa_tariffs(tariff_id),
        FOREIGN KEY (visa_id) REFERENCES visas(visa_id),
        FOREIGN KEY (tour_id) REFERENCES tours(tour_id)
    )
''')

# Загранпаспорт
cursor.execute('''
    CREATE TABLE IF NOT EXISTS passports (
        passport_id INTEGER PRIMARY KEY,
        series TEXT NOT NULL,
        number TEXT NOT NULL,
        issue_date DATE NOT NULL,
        valid_until DATE NOT NULL,
        last_name TEXT NOT NULL,
        first_name TEXT NOT NULL,
        client_id INTEGER NOT NULL,
        FOREIGN KEY (client_id) REFERENCES clients(client_id)
    )
''')

# Выдача загранпаспортов
cursor.execute('''
    CREATE TABLE IF NOT EXISTS passport_issuances (
        issue_date DATE NOT NULL,
        tariff_id INTEGER NOT NULL,
        passport_id INTEGER NOT NULL,
        tour_id INTEGER,
        payment_amount REAL NOT NULL,
        FOREIGN KEY (tariff_id) REFERENCES passport_tariffs(tariff_id),
        FOREIGN KEY (passport_id) REFERENCES passports(passport_id),
        FOREIGN KEY (tour_id) REFERENCES tours(tour_id)
    )
''')

# Маршруты
cursor.execute('''
    CREATE TABLE IF NOT EXISTS routes (
        route_id INTEGER PRIMARY KEY AUTOINCREMENT,
        tour_id INTEGER NOT NULL,
        day INTEGER NOT NULL,
        time TIME NOT NULL,
        transport_id INTEGER NOT NULL,
        country_id INTEGER NOT NULL,
        place TEXT NOT NULL,
        FOREIGN KEY (tour_id) REFERENCES tours(tour_id),
        FOREIGN KEY (transport_id) REFERENCES transport_types(transport_id),
        FOREIGN KEY (country_id) REFERENCES countries(country_id)
    )
''')

# Мероприятия
cursor.execute('''
    CREATE TABLE IF NOT EXISTS events (
        event_id INTEGER PRIMARY KEY AUTOINCREMENT,
        tour_id INTEGER NOT NULL,
        day INTEGER NOT NULL,
        time TIME NOT NULL,
        event TEXT NOT NULL,
        FOREIGN KEY (tour_id) REFERENCES tours(tour_id)
    )
''')


conn.commit()
conn.close()
