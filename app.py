from chalice import Chalice, Response
from urllib.parse import urlparse, parse_qs
import os, logging, random
import jinja2

app = Chalice(app_name='rps-chalice')
app.log.setLevel(logging.DEBUG)

computer_choice_options = ['🪨', '📜', '✂️']

def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or "./")).get_template(filename).render(context)

@app.route('/', methods = ['GET'], content_types=['application/json'])
@app.route('/index', methods = ['GET'], content_types=['application/json'])
def index():
    context = {
        "title": "Devs in the Shed",
        "subtitle": "Rock 🪨, Paper 📜, Scissors ✂️ mini game"
    }
    template = render("chalicelib/templates/index.html", context)
    return Response(template, status_code=200,
                    headers={'Content-Type': 'text/html; charset=utf-8'})

@app.route('/result', methods = ['POST'], content_types=['application/x-www-form-urlencoded'])
def result():
    
    request = app.current_request
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
    return Response(template, status_code=200,
                    headers={'Content-Type': 'text/html; charset=utf-8'})

