# Georgia Tech Campus Map

A Django web application that displays an interactive map of the Georgia Tech campus using Leaflet.js, allowing users to explore campus landmarks visually.

## Features

- Interactive map of Georgia Tech campus
- Multiple landmarks with markers and descriptions
- Click on markers to see detailed information
- Responsive design that works on desktop and mobile devices
- Clean, modern UI with Georgia Tech branding colors

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd "Exam 3 Optional"
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

## Running the Application

1. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

2. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:8000/
   ```

## Project Structure

```
campus_map_project/
├── campus_map_project/      # Main project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── campus_map/               # Main app
│   ├── templates/           # HTML templates
│   │   └── campus_map/
│   │       └── map.html     # Main map page
│   ├── views.py             # View logic
│   └── urls.py              # App URL configuration
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Technologies Used

- **Django**: Web framework
- **Leaflet.js**: Interactive map library
- **OpenStreetMap**: Map tiles provider

## Campus Landmarks Included

The map includes the following Georgia Tech landmarks:

- Tech Tower (main administrative building)
- Bobby Dodd Stadium (football stadium)
- Klaus Advanced Computing Building
- Student Center
- Library (Price Gilbert)
- Campus Recreation Center (CRC)
- Clough Undergraduate Learning Commons (CULC)
- Tech Green (central green space)

## Customization

To add more landmarks, edit `campus_map/views.py` and add entries to the `landmarks` list in the `campus_map_view` function. Each landmark should have:
- `name`: The name of the landmark
- `latitude`: Latitude coordinate
- `longitude`: Longitude coordinate
- `description`: Description text shown in the popup

## License

This project is for educational purposes.

