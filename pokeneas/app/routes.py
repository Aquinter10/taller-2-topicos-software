from flask import Blueprint, jsonify, render_template
import random, socket
from .models import pokeneas

routes = Blueprint('routes', __name__)

@routes.route('/api/pokenea')
def pokenea_json():
    pokenea = random.choice(pokeneas)
    contenedor_id = socket.gethostname()
    return jsonify({
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "contenedor_id": contenedor_id
    })

@routes.route('/pokenea')
def pokenea_html():
    pokenea = random.choice(pokeneas)
    contenedor_id = socket.gethostname()
    return render_template('pokenea.html', pokenea=pokenea, contenedor_id=contenedor_id)
