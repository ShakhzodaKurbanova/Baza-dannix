import sqlite3

def insert_data(conn):
    cursor = conn.cursor()

    # Типы виз
    cursor.execute('''
        INSERT INTO types_of_visas (type_id, name) VALUES
        (1, 'Туристическая'),
        (2, 'Бизнес'),
        (3, 'Студенческая')
    ''')

    # Страны
    cursor.execute('''
        INSERT INTO countries (country_id, name) VALUES
        (1, 'Россия'),
        (2, 'США'),
        (3, 'Франция')
    ''')

    # Средства перемещения
    cursor.execute('''
        INSERT INTO transport_types (transport_id, name) VALUES
        (1, 'Самолет'),
        (2, 'Поезд'),
        (3, 'Автобус')
    ''')

    # Отели
    cursor.execute('''
        INSERT INTO hotels (hotel_id, name, country_id, region) VALUES
        (1, 'Hilton Moscow Leningradskaya', 1, 'Москва'),
        (2, 'Hyatt Regency Paris Etoile', 3, 'Париж')
    ''')

    # Питание
    cursor.execute('''
        INSERT INTO food_types (food_id, name) VALUES
        (1, 'Завтрак'),
        (2, 'Полупансион'),
        (3, 'Все включено')
    ''')

    # Клиенты
    cursor.execute('''
        INSERT INTO clients (last_name, first_name, middle_name, phone, passport, registration_date, notes) VALUES
        ('Иванов', 'Иван', 'Иванович', '+79161234567', '4567 123456', '2023-10-26', 'Первый клиент'),
        ('Петрова', 'Мария', 'Петровна', '+79267890123', '1234 987654', '2023-10-27', NULL)
    ''')

    # Путёвки
    cursor.execute('''
        INSERT INTO tours (name, country_id, hotel_id, transport_included, food_id, departure_date, return_date, price, visa_discount, passport_discount) VALUES
        ('Тур в Москву', 1, 1, 1, 2, '2024-01-15', '2024-01-22', 50000, 5, 10),
        ('Тур в Париж', 3, 2, 1, 3, '2024-02-20', '2024-02-27', 80000, 0, 0)
    ''')

    # Продажа путёвок
    cursor.execute('''
        INSERT INTO tour_sales (client_id, tour_id, client_level, sale_date, payment_amount) VALUES
        (1, 1, 1, '2023-10-26', 50000),
        (2, 2, 2, '2023-10-27', 70000)
    ''')

    # Скидки клиентам
    cursor.execute('''
        INSERT INTO client_discounts (level, tour_discount) VALUES
        (1, 0.05),
        (2, 0.10)
    ''')

    # Тарифы на визы
    cursor.execute('''
        INSERT INTO visa_tariffs (validity_period, type_id, country_id, price) VALUES
        (90, 1, 2, 100),
        (180, 1, 3, 150)
    ''')

    # Тарифы на загранпаспорта
    cursor.execute('''
        INSERT INTO passport_tariffs (tariff_id, price) VALUES
        (1, 5000)
    ''')

    # Виза
    cursor.execute('''
        INSERT INTO visas (series, number, issue_date, valid_until, type_id, country_id, num_entries, duration, client_id) VALUES
        ('AB', '123456', '2023-10-26', '2024-04-25', 1, 2, 1, 90, 1)
    ''')

    # Выдача виз
    cursor.execute('''
        INSERT INTO visa_issuances (issue_date, tariff_id, visa_id, tour_id, payment_amount) VALUES
        ('2023-10-26', 1, 1, 1, 100)
    ''')

    # Загранпаспорт
    cursor.execute('''
        INSERT INTO passports (series, number, issue_date, valid_until, last_name, first_name, client_id) VALUES
        ('CD', '789012', '2023-10-27', '2028-10-27', 'Петрова', 'Мария', 2)
    ''')

    # Выдача загранпаспортов
    cursor.execute('''
        INSERT INTO passport_issuances (issue_date, tariff_id, passport_id, tour_id, payment_amount) VALUES
        ('2023-10-27', 1, 1, 2, 5000)
    ''')

    # Маршруты
    cursor.execute('''
        INSERT INTO routes (tour_id, day, time, transport_id, country_id, place) VALUES
        (1, 1, '10:00', 1, 1, 'Красная площадь'),
        (2, 1, '14:00', 3, 3, 'Эйфелева башня')
    ''')

    # Мероприятия
    cursor.execute('''
        INSERT INTO events (tour_id, day, time, event) VALUES
        (1, 2, '19:00', 'Экскурсия по Кремлю')
    ''')

    conn.commit()

if __name__ == "__main__":
    conn = sqlite3.connect('travel_agency.db')
    insert_data(conn)
    conn.close()
    print("Data inserted successfully.")

