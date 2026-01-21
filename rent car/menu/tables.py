"""
All tables queries
"""
users="""
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            full_name VARCHAR(100),
            phone VARCHAR(20) UNIQUE NOT NULL,
            email VARCHAR(100) UNIQUE,
            password TEXT NOT NULL,
            role VARCHAR(20) DEFAULT 'client', -- admin, client
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )\

"""
cars="""
    CREATE TABLE cars (
        id SERIAL PRIMARY KEY,
        brand VARCHAR(50),
        model VARCHAR(50),
        year INT,
        color VARCHAR(30),
        price_per_day NUMERIC(10,2) NOT NULL,
        status VARCHAR(20) DEFAULT 'available', -- available, rented, service
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )\

"""
car_images="""
        CREATE TABLE car_images (
    id SERIAL PRIMARY KEY,
    car_id INT REFERENCES cars(id) ON DELETE CASCADE,
    image_url TEXT NOT NULL
)\

"""
rentals="""
    CREATE TABLE rentals (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    car_id INT REFERENCES cars(id),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    total_price NUMERIC(10,2),
    status VARCHAR(20) DEFAULT 'active', -- active, finished, cancelled
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)\

"""
payments="""
CREATE TABLE payments (
    id SERIAL PRIMARY KEY,
    rental_id INT REFERENCES rentals(id),
    amount NUMERIC(10,2),
    payment_method VARCHAR(30), -- cash, card, click, payme
    status VARCHAR(20) DEFAULT 'paid',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)\


"""
reviews="""
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    car_id INT REFERENCES cars(id),
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)\

"""
car_services="""
CREATE TABLE car_services (
    id SERIAL PRIMARY KEY,
    car_id INT REFERENCES cars(id),
    description TEXT,
    service_date DATE,
    cost NUMERIC(10,2)
)\

"""