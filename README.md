# Restaurant Website

A modern, responsive restaurant website built with Django, featuring a beautiful UI and complete backend functionality.

## Features

- Responsive design with modern UI
- User authentication (signup/login)
- Menu management
- Table reservation system
- Customer reviews
- Contact form
- Admin panel for managing content
- Animated sections using AOS library
- Bootstrap 5 for styling
- Font Awesome icons

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd restaurant
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
python manage.py makemigrations
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

7. Visit http://127.0.0.1:8000/ in your browser

## Project Structure

```
restaurant/
├── main/                    # Main application
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── urls.py             # URL patterns
│   └── admin.py            # Admin configuration
├── templates/              # HTML templates
│   ├── base.html          # Base template
│   └── main/              # App-specific templates
├── static/                # Static files
│   ├── css/              # CSS files
│   ├── js/               # JavaScript files
│   └── images/           # Image files
├── media/                # User-uploaded files
├── restaurant/           # Project settings
└── manage.py            # Django management script
```

## Admin Panel

Access the admin panel at http://127.0.0.1:8000/admin/ to:
- Manage menu items
- Handle table reservations
- Moderate customer reviews
- Update restaurant information

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, email support@restaurant.com or create an issue in the repository. 