# Urly-Bird

A URL shortener/bookmarking site

Run:

echo layout python3 >> .envrc
direnv allow
pip install -r requirements.txt
cd urly-bird
python manage.py migrate
python manage.py shell
from bookmarks import load_fake_data.load_bookmarks()[for fake data]
python manage.py runserver

open localhost link
 
 
 

