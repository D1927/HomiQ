# HomiQ Backend

Backend API for **HomiQ**, an AI-powered real-estate platform designed to help users discover properties, connect with owners, and access home-related services.

The backend is being developed in parts. **The current phase (Part 1) focuses on user management and authentication.** Property management, AI/ML features, bookings, communication, payments, virtual tours, and reviews are planned for later phases.

## Tech Stack

- **Language:** Python
- **Backend Framework:** Django
- **API Framework:** Django REST Framework
- **Database:** PostgreSQL
- **API Testing:** Postman
- **Frontend:** Next.js (developed separately)

## Project Structure

```text
homiq-backend/
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── permissions.py
│   └── migrations/
│
├── properties/          # Planned
├── intelligence/        # Planned
├── bookings/             # Planned
├── services/             # Planned
├── reviews/              # Planned
├── payments/             # Planned
├── communication/        # Planned
├── virtual_tours/        # Planned
│
├── .env                  # Local environment variables
├── .gitignore
├── requirements.txt
└── README.md