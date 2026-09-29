# 🎙️ Time To Talk — Django Website

A Django-based website built by integrating a pre-designed podcast-themed frontend template with a custom Django backend.

The project was developed as a practical Django project to implement backend functionality such as page routing, contact form handling, email subscription, database models, Django ModelForms, admin management, messages, static files, and template integration.

> **Note:** The frontend design is based on a pre-designed **Pod Talk** HTML template from TemplateMo. The main development work focused on integrating the frontend with Django and implementing the backend functionality.

---

## ✨ Features

### 🏠 Website Pages

The project includes several website pages:

* Home page
* About page
* Contact page
* Listing page
* Detail page
* Shared base template
* Navigation between Django views using named URLs

---

### 📩 Contact Form

The website includes a contact form implemented using Django `ModelForm`.

Users can submit:

* Full name
* Email address
* Company
* Message

Submitted contact information is stored in the database and can be managed through the Django Admin panel.

Example:

```python
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
```

The contact form also uses Django's Messages Framework to display success and error messages after submission.

---

### 📧 Email Subscription

The website includes an email subscription form in the footer.

Users can submit their email address to subscribe.

The submitted email addresses are stored in the database using a dedicated `Email` model.

Example:

```python
class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
```

---

### 🛠️ Django Admin

The Django Admin panel is used to manage submitted contact information and email subscriptions.

The Contact model includes:

* Date hierarchy
* Custom list display
* Filtering
* Search functionality

Example:

```python
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = (
        "full_name",
        "email",
        "created_date",
    )
    list_filter = ("email",)
    search_fields = (
        "name",
        "message",
    )
```

Email subscriptions can also be managed through the Django Admin panel.

---

### 📝 Django Forms & ModelForms

The project uses Django `ModelForm` to handle user-submitted data.

Two forms are implemented:

* `ContactForm`
* `EmailForm`

These forms are connected directly to their corresponding database models.

---

### 💬 Django Messages Framework

The contact form uses Django's Messages Framework to provide feedback after form submission.

Users receive a success message when their contact request is submitted successfully and an error message when the form submission fails.

---

### 🧭 URL Routing

The project uses Django's URL routing system with named URL patterns.

The `website` application provides routes for:

```text
/
about/
contact/
subscribe_email
```

The `pages` application provides:

```text
pages/
pages/listing-page/
pages/detail-page/
```

Named URLs are used throughout the templates for navigation.

---

### 🎨 Static Files

The project uses Django's static files system for frontend assets.

Static resources include:

* CSS
* JavaScript
* Bootstrap
* Bootstrap Icons
* Owl Carousel
* Fonts
* Images

Project static directory:

```text
statics/
```

The frontend JavaScript files include:

* jQuery
* Bootstrap Bundle
* Owl Carousel
* Custom JavaScript

---

### 🧩 Template Inheritance

The project uses Django template inheritance through a shared `base.html`.

The base template contains common website elements such as:

* Navigation
* Footer
* Subscription form
* Static asset loading
* JavaScript files

Individual pages extend the base template using Django's template inheritance system.

Example:

```django
{% extends "base.html" %}
{% load static %}
```

---

## 🧰 Technologies Used

### Backend

* 🐍 Python
* 🌐 Django 5.2
* 🗄️ Django ORM
* 📝 Django Forms & ModelForms
* 🛠️ Django Admin
* 💬 Django Messages Framework
* 🧩 Django Templates
* 🔗 Django URL Routing

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* jQuery
* Owl Carousel
* Bootstrap Icons
* Django Template Language

### Database

* SQLite

### Development Tools

* Git
* GitHub
* VS Code

---

## 📁 Project Structure

```text
time-to-talk-website/
│
├── pages/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── website/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── talksite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   ├── base.html
│   ├── pages/
│   │   ├── detail-page.html
│   │   └── listing-page.html
│   │
│   └── website/
│       ├── index.html
│       ├── about.html
│       └── contact.html
│
├── statics/
│   ├── css/
│   ├── fonts/
│   ├── images/
│   └── js/
│
├── manage.py
├── requirements.txt
├── .gitignore
├── .gitattributes
└── LICENSE
```

---

## 📦 Requirements

Before running the project, make sure you have:

* Python 3.x
* pip
* Git

All required Python packages are listed in `requirements.txt`.

The project currently uses the following Python dependencies:

* `Django`
* `asgiref`
* `sqlparse`
* `tzdata`

The `requirements.txt` file contains the package versions and version constraints used by the project.

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/sepehrabbaspour/time-to-talk-website.git
cd time-to-talk-website
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv env
env\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv env
source env/bin/activate
```

> The virtual environment name `env` is only a local convention. You can use any name you prefer.

---

### 3. Install project dependencies

All required Python packages are listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

---

### 4. Apply database migrations

```bash
python manage.py migrate
```

---

### 5. Create a superuser

To access the Django Admin panel:

```bash
python manage.py createsuperuser
```

Follow the instructions in the terminal to create your administrator account.

---

### 6. Run the development server

```bash
python manage.py runserver
```

The website will be available at:

```text
http://127.0.0.1:8000/
```

The Django Admin panel is available at:

```text
http://127.0.0.1:8000/admin/
```

---

## 🗄️ Database

The project uses **SQLite** as its database during development.

Database configuration:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

The database stores data such as:

* Contact form submissions
* Email subscriptions

SQLite was chosen for simplicity during development and learning.

---

## 📝 Development Notes

This project was developed primarily as a Django learning and portfolio project.

The frontend design was based on a pre-designed **Pod Talk** HTML template, while the main development work focused on integrating the frontend with Django and implementing backend functionality.

The project covers practical Django concepts including:

* Project and application structure
* URL routing
* Views
* Models
* Django ORM
* Forms and ModelForms
* Django Admin
* Template inheritance
* Static files
* Database migrations
* SQLite
* Messages Framework
* Form validation
* Handling POST requests
* Named URL patterns
* Serving static assets

The project is currently intended for development and portfolio purposes and has not been deployed as a production website.

---

## 🚀 Future Improvements

Possible future improvements include:

* 🌐 Production deployment
* 🔐 Environment variable management
* 📧 Email notifications for contact submissions and subscriptions
* 🔎 Functional website search
* 🧪 Adding automated tests
* 🗄️ PostgreSQL database integration
* 📱 Further frontend responsiveness improvements
* 🔒 Improved production security configuration

---

## 👨‍💻 Author

**Sepehr Abbaspour**

Computer Engineering Graduate
Python & Django Backend Developer

🔗 GitHub:
https://github.com/sepehrabbaspour

---

⭐ If you find this project useful, feel free to explore the code and give the repository a star.
