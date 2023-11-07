import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="hello")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    
    firstname = req.params.get('firstname', 'World')
    lastname = req.params.get('lastname', '')

    number = req.params.get('number', 0)
    number_real = int(number)
    number_analyzed = number_real * number_real

    number_2 = req.params.get('number2', 0)
    number_real_2 = int(number_2)
    number_analyzed_2 = number_real_2 + number_real_2

    response_data = {
        'Greeting': f'Hello {firstname} {lastname}',
        'Number': f'{number_analyzed}',
        'Number2': f'{number_analyzed_2}'
    }
    
    return func.HttpResponse(
        json.dumps(response_data),
        status_code=200
        )

# string for query = /api/hello?firstname=John&lastname=Doe&number=5&number2=5
# string for swagger documentation = /apidocs/