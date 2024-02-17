from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokemon', methods=['POST'])
def pokemon():
    if 'pokemon_name' in request.form:
        pokemon_name = request.form['pokemon_name']
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    elif 'pokemon_number' in request.form:
        pokemon_number = request.form['pokemon_number']
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}"
    else:
        return render_template('index.html')
    
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_info = response.json()
        return render_template('pokemon.html', pokemon_info=pokemon_info)
    else:
        return render_template('pokemon.html', error=True)

if __name__ == '__main__':
    app.run(debug=True)