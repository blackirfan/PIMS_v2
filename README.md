# web_gis103



this is geoDjango based website in this sector
Installation using pip:

pip install django-adminlte3
Add to installed apps:

INSTALLED_APPS = [
     # General use templates & template tags (should appear first)
    'adminlte3',
     # Optional: Django admin theme (must be before django.contrib.admin)
    'adminlte3_theme',

    ...
]

Don't forget to collect static

python manage.py collectstatic 


https://medium.com/analytics-vidhya/how-to-use-adminlte-in-django-225359ce8c72
# From my end
need connect to postgres database.
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver



…or create a new repository on the command line
echo "# PIMS_v2" >> README.md
git init
git add README.md

git status


git add -A stages all changes

git add . stages new files and modifications, without deletions

git add -u stages modifications and deletions, without new files

git status

git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/blackirfan/PIMS_v2.git
git push -u origin main