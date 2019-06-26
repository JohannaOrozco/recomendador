from flask import Flask
from flask import abort
from flask import jsonify # <- `jsonify` instead of `json`
from flask import request
from flask import url_for
from flask import flash, render_template
import main as m
import findConcepts as f
import recommendAlternativePrograms as r

# Fuente de consulta https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3s

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'recommendPrograms',
        'description': u'Recibe los datos de entrada del formulario inicial y regresa la primer recomendacion de programas', 
        'url' : u'http://localhost:5000/todo/api/v1.0/tasks/recommendPrograms'
        
    },
    {
        'id': 2,
        'title': u'findConcepts',
        'description': u'Encuentra los conceptos asociados con las carreras', 
        'url' : u'http://localhost:5000/todo/api/v1.0/tasks/findConcepts'
        
    },
    {
        'id': 3,
        'title': u'recommendAlternativePrograms',
        'description': u'Recibe los conceptos y a partir de estos realiza la segunda recomendacion de programas.', 
        'url' : u'http://localhost:5000/todo/api/v1.0/tasks/recommendAlternativePrograms'
        
    }
]



@app.route('/')
def index():
    a = '<h1>!La comunicacion por el API REST esta funcionando!</h1>'
    return a


#curl -i http://127.0.0.1:5000/todo/api/v1.0/tasks/2
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

from flask import make_response

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# curl -i -H "Content-Type: application/json" -X POST -d '{"rawdata":"11,NO OFICIAL,URBANA,MIXTO,ACADEMICO,B,A+,SI,CO,2017,1,80,70,80,,,60,17,N,SOLTERO,4,NO,CASADOS,TECNICO,BACHILLERATO,EMPLEADA,INDEPENDIENTE,NO,NO"}' http://localhost:5000/todo/api/v1.0/tasks/recommendPrograms
@app.route('/todo/api/v1.0/tasks/recommendPrograms', methods=['POST'])
def call_recommendPrograms():
    'Llama el servicio que invoca el programa recommendPrograms'
    if not request.json or not 'rawdata' in request.json:
        abort(400)
    task = {

        'rawdata': request.json['rawdata'] #,

    }
    
    rawdata = task['rawdata']
    recommendedPrograms = m.main(rawdata)

    # print ('INFORMACIÓN EN recommendedPrograms: {}'.format(recommendedPrograms))

    return jsonify({'task': recommendedPrograms}), 201


# curl -i -H "Content-Type: application/json" -X POST -d '{"rawdata":"Licenciatura en Matemáticas, Ingeniería Biomédica, Ingeniería Industrial"}' http://localhost:5000/todo/api/v1.0/tasks/findConcepts
@app.route('/todo/api/v1.0/tasks/findConcepts', methods=['POST'])
def call_findConcepts():
    'Llama el servicio que invoca el programa findConcepts'
    if not request.json or not 'rawdata' in request.json:
        abort(400)
    task = {

        'rawdata': request.json['rawdata'] #,

    }
    
    rawdata = task['rawdata']
    findConcepts = f.main(rawdata)

    # print ('INFORMACIÓN EN recommendedPrograms: {}'.format(recommendedPrograms))

    return jsonify({'task': findConcepts}), 201


# curl -i -H "Content-Type: application/json" -X POST -d '{"rawdata":"civil, empresa, ingeniero, ingeniería, proyecto"}' http://localhost:5000/todo/api/v1.0/tasks/recommendAlternativePrograms
@app.route('/todo/api/v1.0/tasks/recommendAlternativePrograms', methods=['POST'])
def call_recommendAlternativePrograms():
    'Llama el servicio que invoca el programa recommendAlternativePrograms'
    if not request.json or not 'rawdata' in request.json:
        abort(400)
    task = {

        'rawdata': request.json['rawdata'] #,

    }
    
    rawdata = task['rawdata']
    alternativePrograms = r.main(rawdata)

    print ('INFORMACIÓN EN recommendedPrograms: {}'.format(alternativePrograms))

    return jsonify({'task': alternativePrograms}), 201

# curl -i http://localhost:5000/todo/api/v1.0/tasks
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():

    return jsonify({'tasks': tasks})



if __name__ == '__main__':
    app.run(debug=False)





