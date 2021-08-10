from chalice import Chalice, Response
from urllib.parse import parse_qs
import os, logging, random, base64
import jinja2

app = Chalice(app_name='rps-chalice')
app.log.setLevel(logging.DEBUG)
app.api.binary_types =['*/*']

computer_choice_options = ['🪨', '📜', '✂️']
placeholder_spock_variant_emojis = ['🦎', '🖖']

def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or "./")).get_template(filename).render(context)

@app.route('/', methods = ['GET'], content_types=['application/json'])
@app.route('/index', methods = ['GET'], content_types=['application/json'])
def index():
    context = {
        "title": "Devs in the Shed",
        "subtitle": "Rock , Paper 📜, Scissors ✂️ mini game"
    }
    template = render("chalicelib/templates/index.html", context)
    my_str_as_bytes = str.encode(template)
    return Response(my_str_as_bytes, status_code=200,
                    headers={'Content-Type': 'text/html; charset=utf-8'})

@app.route('/error', methods = ['GET'], content_types=['application/json'])
def error_page():
    context = {
        "title": "Devs in the Shed"
    }
    template = render("chalicelib/templates/error.html", context)
    my_str_as_bytes = str.encode(template)
    return Response(my_str_as_bytes, status_code=404,
                    headers={'Content-Type': 'text/html; charset=utf-8'})

@app.route('/result', methods = ['POST'], content_types=['application/x-www-form-urlencoded'])
def result():
    
    parsed = parse_qs(app.current_request.raw_body.decode())
    get_choice = parsed.get('choice')
    choice = ''.join(get_choice)
    computer_choice = random.choice(computer_choice_options)
    if choice == computer_choice:
        outcome = "You tied with the computer"
    elif choice == "🪨" and computer_choice == "📜" or choice == "📜" and computer_choice == "✂️" or choice == "✂️" and computer_choice == "🪨":
        outcome = "You lost to the computer"
    else: outcome = "You won over the computer"
    context = {
        "title": "Devs in the Shed",
        "subtitle": "Rock 🪨, Paper 📜, Scissors ✂️ mini game",
        "choice": choice, 
        "computer_choice": computer_choice, 
        "outcome": outcome
    }
    template = render("chalicelib/templates/result.html", context)
    return Response(str.encode(template), status_code=200,
                    headers={'Content-Type': 'text/html; charset=utf-8'})

@app.route('/css/{css_file}')
def css(css_file):
    with open('chalicelib/static/css/' + css_file, 'r') as file:
        data = file.read().replace('\n', '')

    return Response(str.encode(data), status_code=200,
                    headers={'Content-Type': 'text/css; charset=utf-8'})

@app.route('/images/{image_file}')
def image(image_file):
    f = open("chalicelib/static/images/" + image_file, "rb")
    ima = f.read()
    f.close()
    return Response(ima, status_code=200, headers={'Content-Type': 'image/png'})

