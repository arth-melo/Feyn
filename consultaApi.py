
from dotenv import load_dotenv
from google import genai
from google.genai import types
load_dotenv()
cliente = genai.Client(http_options=types.HttpOptions(timeout=60000))
def consulta(mensagem):
    prompt = "Quando eu enviar uma frase ou expressão, explique-a" 
    esquema_dict = {
        "type": "OBJECT",
        "properties": {
        'nome':       {"type": "STRING"},
        'classe gramatical' : {"type": "STRING"},
        'definição' : {"type": "STRING"},
        'analogia' :  {"type": "STRING"},
        'exemplo1' :  {"type": "STRING"},
        'exemplo2' :  {"type": "STRING"},
        'exemplo3' :  {"type": "STRING"},
        'sinonimos_list': {
                "type": "ARRAY",
                "items": {"type": "STRING"},
        },
        'etimologia' : {"type": "STRING"}
    }
    }
    print("Enviando mensagem para o Gemini...", flush=True)
    resposta = cliente.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt + mensagem,
        config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=esquema_dict,
        )
    )
    uso = resposta.usage_metadata
    print(
        "Tokens: "
        f"entrada={uso.prompt_token_count}, "
        f"saida={uso.candidates_token_count}, "
        f"total={uso.total_token_count}",
        flush=True,
    )
    return resposta.parsed

if __name__ == "__main__":
    palavra = input("palavra para testar: ")
    print(consulta(palavra))