# Personal Portfolio

Django portfolio with an admin-only sign-in, a dashboard of projects and tech stacks, and create forms for both. Projects added in the dashboard appear on the public portfolio.

Live site: (add after deployment)

## Setup
1. Clone: `git clone https://github.com/01RF/django-project.git` then `cd django-project`
2. Create a virtual environment: `python -m venv .venv`
3. Activate it: `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install -r requirements.txt`
5. Create your environment file: `copy .env.example .env` (Windows) or `cp .env.example .env` (Mac/Linux), then fill in:
   - `SECRET_KEY`: generate one with `python -c "from django.core.management.utils import get_random_secret_key as g; print(g())"`
   - `DEBUG`: `True` locally, `False` in production
   - `ALLOWED_HOSTS`: comma-separated, e.g. `localhost,127.0.0.1`
6. Run migrations (no makemigrations needed): `python manage.py migrate`
7. Create an admin account: `python manage.py createsuperuser`
8. Start the server: `python manage.py runserver`
9. Open `/` for the portfolio and `/signin/` for admin login. After signing in you are redirected to `/dashboard/`.