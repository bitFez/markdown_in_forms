# markdown_in_forms

Easy markdown implementation in to a Django Project

## 🔧 Setup 🔧

Before trying to run the server

### Django

- add a file named `.env` in the root folder
- create a variable like `SECRET_KEY='replace_this_part_with_secret_key'` in the `.env` file
- generate a secret key from here https://miniwebtool.com/django-secret-key-generator/
- run `python manage.py makemigrations`
- run `python manage.py migrate`
- run `python manage.py createsuperuser` and create an admin user for yourself
- run `python manage.py collectstatic`

