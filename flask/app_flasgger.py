from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/hello', methods=['GET'])
def hello_get():
    """
    This endpoint returns a greeting message.
    ---
    parameters:
      - name: firstname
        in: query
        type: string
        required: false
        default: World
      - name: lastname
        in: query
        type: string
        required: false
        default: ''
      - name: number
        in: query
        type: integer
        required: false
        default: 0
      - name: number2
        in: query
        type: integer
        required: false
        default: 0
    responses:
      200:
        description: A greeting message
    """
    
    firstname = request.args.get('firstname', 'World')
    lastname = request.args.get('lastname', '')

    number = request.args.get('number', 0)
    number_real = int(number)
    number_analyzed = number_real * number_real

    number_2 = request.args.get('number2', 0)
    number_real_2 = int(number_2)
    number_analyzed_2 = number_real_2 + number_real_2

    response_data = {
        'Greeting': f'Hello {firstname} {lastname}',
    }

    response_data_2 = {
        'Number': f'{number_analyzed}',
    }

    response_data_3 = {
        'Number2': f'{number_analyzed_2}',
    }
    
    return jsonify(response_data, response_data_2, response_data_3)

# string for query = hello?firstname=John&lastname=Doe&number=5&number2=5
# string for swagger documentation = /apidocs/

if __name__ == '__main__':
    app.run(debug=True)