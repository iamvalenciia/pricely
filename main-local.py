from lambda_function import lambda_handler
import json

if __name__ == "__main__":
    evento_prueba = {'tweet_text': 'Probando localmente'}
    respuesta = lambda_handler(evento_prueba, None)
    print(json.dumps(respuesta, indent=4))