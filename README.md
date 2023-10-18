# parcare

Parking Management System
This is a Django project designed to manage parking staff, and clients. As a superuser, you can add staff, clients, and manage their accounts, invoices, and contracts. As a staff member, you can add clients if they pay directly at the office point and check clients' statuses and invoices lists, but not the contracts. Clients can manage all of their parking management needs themselves by registering an account with the system. Once registered, clients can complete a form with their details, select a contract, and pay for it. After that, clients can see all details related to their contracts and invoices. Clients can also add up to three cars to their accounts.

Installation and Setup
To set up this project on your local machine, you will need Python 3 installed, as well as pip and virtualenv. Once you have those installed, follow these steps:

Clone the repository from GitHub.

Create a virtual environment for the project: virtualenv venv.

Activate the virtual environment: source venv/bin/activate (Linux/Mac) or .\venv\Scripts\activate (Windows).

Install the required dependencies: pip install -r requirements.txt.

Set up the database by running migrations: python manage.py migrate.

Create a superuser account: python manage.py createsuperuser.

Start the development server: python manage.py runserver.

Navigate to http://localhost:8000 in your web browser to view the application.

You need to register to www.stripe.com for test payments and add API KEY in parkproject/settings.py 

    STRIPE_PUBLISHABLE_KEY = ''
    STRIPE_SECRET_KEY = ''

Also you need to add your own email settings to send emails to activate new accounts or contracts and invoices:

    EMAIL_BACKEND = ''
    EMAIL_HOST = ''
    EMAIL_FROM = ''
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_PORT = ''
    EMAIL_USE_TLS = True
