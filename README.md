# parcare
Django project parking

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

Usage
As a superuser, you can add staff and clients, manage their accounts, invoices, and contracts. To add a new staff or client, log in as a superuser, navigate to the "Parking" page from navbar, and click the "Add Employee" or "Add Client". When you register a client or a staff, you send them to email an user and password.

As a staff member you have an account with your contract PDF and your details. You can add clients if they pay directly at the office point and check clients' statuses and invoices lists, but not the contracts PDFs. To add a new client, log in as a staff member from the server IP, navigate to the "Parking" page from navbar, and click the "Add Client". When you register a client, you send to email an user and password.

Clients can manage their accounts, contracts, and invoices by registering for an account. To register, click the "Create new User" on the login page, you will receive an email with a link to activate your account. Once registered, clients can log in and select a contract, and pay for it. After payment, clients can view all details related to their contracts and invoices, can make another payments, add or delete cars (up to three cars to their accounts) 

Credits
This project was created by Florin Gafita. If you have any questions or comments, please contact at gafyf19@gmail.com
