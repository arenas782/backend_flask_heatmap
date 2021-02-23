from flask import Flask
from flask import jsonify
from flask_restx import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

@api.route('/heatmap')
class HelloWorld(Resource):
    def get(self):
        data = {}
        new =[
       

                {"y":"Facturación","x":"P. Chile","value":8},
                {"y":"C.O.","x":"P. Chile","value":65},
                {"y":"Avance","x":"P. Chile","value":25},
                {"y":"MW","x":"P. Chile","value":0},
                {"y":"Facturación","x":"P. EEUU","value":37},
                {"y":"C.O.","x":"P. EEUU","value":40},
                {"y":"Avance","x":"P. EEUU","value":100},
                {"y":"MW","x":"P. EEUU","value":80},
                {"y":"Facturación","x":"P. Vzla","value":1},
                {"y":"C.O.","x":"P. Vzla","value":30},
                {"y":"Avance","x":"P. Vzla","value":74},
                {"y":"MW","x":"P. Vzla","value":22},
                {"y":"Facturación","x":"P. Brasil","value":83},
                {"y":"C.O.","x":"P. Brasil","value":15},
                {"y":"Avance","x":"P. Brasil","value":33},
                {"y":"MW","x":"P. Brasil","value":4},
        ]


        return jsonify(new)

if __name__ == '__main__':
    app.run(debug=True,port=8090,host='0.0.0.0')