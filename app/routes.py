from flask import Blueprint, render_template
import requests
import time


cached_reviews = None
last_updated = 0

def fetch_google_reviews():
    global cached_reviews, last_updated
    if time.time() - last_updated > 60:  # Atualiza a cada 24 horas
        api_key = 'AIzaSyBOFMxpjGme0_rNF70lMLmbNBtxtkOngvE'
        place_id = '0xd19e57fc71ff81f:0xb647930f79b4e4f9'
        url = 'https://maps.googleapis.com/maps/api/place/details/json?place_id={}&fields=reviews&key={}'.format(place_id, api_key)
        response = requests.get(url)
        cached_reviews = response.json().get('result', {}).get('reviews', [])
        last_updated = time.time()
    return cached_reviews

main = Blueprint('main', __name__)

@main.route('/')
def index():
        reviews = fetch_google_reviews()  # Buscar os comentários do Google Maps
        return render_template('index.html', reviews=reviews)   # Passar os comentários para o template

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/booking')
def booking():
    return render_template('booking.html')

@main.route('/menu')
def menu():
    return render_template('menu.html')

@main.route('/service')
def service():
    return render_template('service.html')

@main.route('/menu_pt')
def menu_pt():
    return render_template('menu_pt.html')

@main.route('/menu_en')
def menu_en():
    return render_template('menu_en.html')

