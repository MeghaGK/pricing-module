# build instructions

git clone https://github.com/MeghaGK/pricing-module.git
cd pricing-module
python -m venv venv
venv\Scripts\activate 
# on linux, use `source venv/bin/activate`
pip install -r requirements.txt
cd modules
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# Usage

Access the Django Admin UI - http://localhost:8000/admin/ to add, modify and delete pricing configuration.
Use API endpoint http://localhost:8000/pricing/calculate-pricing/'distance'/'time'/'waiting_time'/ for pricing calculation

# Example API request

http://localhost:8000/pricing/calculate-pricing/10.5/1.5/5.0/
Replace 10.5, 1.5, and 5.0 with desired distance, time and waiting time values.
