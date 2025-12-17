# Modern E-Commerce Platform

A scalable, full-stack E-Commerce application built with **Django 5**, utilizing a modern tech stack including **Docker**, **PostgreSQL**, and **Gunicorn**. This project simulates a real-world online store with product management, shopping cart functionality, and user authentication.

## 🚀 Tech Stack

- **Backend:** Python 3.11, Django 5.0
- **Database:** PostgreSQL 15 (Production), SQLite (Dev)
- **Containerization:** Docker & Docker Compose
- **Server:** Gunicorn (WSGI)
- **Frontend:** Bootstrap 5, Custom CSS/JS

## 🛠 Installation & Setup

### Option 1: Using Docker (Recommended)

1. Clone the repository:

   ```bash
   git clone https://github.com/AmirArsalanTaqavi/django-ecommerce.git
   cd django-ecommerce
   ```

2. Build and run with Docker Compose:

   ```bash
   docker-compose up --build
   ```

3. Access the app at `http://localhost:8000`.

### Option 2: Local Development

1. Clone the repository:

   ```bash
   git clone https://github.com/AmirArsalanTaqavi/django-ecommerce.git
   cd django-ecommerce
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the app at `http://localhost:8000`.

## 📋 Features

- User registration and authentication
- Product catalog with categories
- Shopping cart (session-based with DB persistence for logged users)
- Order management
- Search functionality
- Responsive design with Bootstrap

## 🧪 Testing

Run tests with:

```bash
python manage.py test
```

## 🚀 Deployment

For production, use Gunicorn and PostgreSQL. Update environment variables accordingly.
