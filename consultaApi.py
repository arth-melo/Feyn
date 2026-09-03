
from dotenv import load_dotenv
from google import genai
from google.genai import types

def consulta(mensagem):
    load_dotenv()
    prompt = "Quando eu enviar uma frase ou expressão, explique-a seguindo este formato:\n\n**\"[Frase ou expressão]\"**\n\n**Classificação:** [expressão idiomática, frase poética, frase descritiva, metáfora, gíria, ditado popular, expressão coloquial, etc.]\n\n**Explique como para uma criança:** [Explique o significado real da frase de forma simples, clara e didática, como se estivesse explicando para uma criança sem nenhum contexto. Não apenas substitua as palavras por sinônimos. Se a frase for figurativa, metafórica ou idiomática, explique o significado pretendido, e não apenas o sentido literal.]\n\n**Analogia:** [Faça uma comparação com algo concreto do dia a dia que ajude a visualizar e compreender a ideia da frase.]\n\n**Palavras-chave da frase:** [Liste apenas os termos centrais que precisam de explicação e explique o significado de cada um dentro daquele contexto específico.]\n\n**Origem (complementar):** [Inclua somente se houver uma origem histórica, cultural ou linguística confiável e documentada. Seja breve. Nunca invente uma origem ou apresente uma etimologia popular como fato. Se não houver origem confiável ou se a frase não possuir uma origem documentada, omita esta seção.]\n\n**Expressões equivalentes:** [Apresente outras frases ou formas naturais de transmitir a mesma ideia, sem alterar significativamente o sentido ou a intensidade.]\n\nRegras:\n1. Priorize sempre o significado real e o uso da frase no contexto fornecido.\n2. Se houver contexto fornecido, use-o para interpretar a frase.\n3. Se não houver contexto e houver mais de uma interpretação possível, use a mais provável e mencione outras apenas quando forem relevantes.\n4. Explique de forma simples, mas mantenha a precisão.\n5. Evite jargões e explicações excessivamente acadêmicas.\n6. Não invente informações.\n7. Não invente origens ou relações etimológicas por semelhança superficial entre palavras.\n8. A origem deve ser sempre complementar e nunca o foco principal.\n9. Não repita a mesma informação em diferentes seções.\n10. Cada seção deve acrescentar algo útil para a compreensão.\n11. Responda sempre em português brasileiro.\n12. Não adicione conclusões, observações ou seções que não foram solicitadas e comece diretamente assim que eu enviar a palavra para você."

    cliente = genai.Client(http_options=types.HttpOptions(timeout=60000))
    print("Enviando mensagem para o Gemini...", flush=True)
    resposta = cliente.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt + mensagem,
    )
    uso = resposta.usage_metadata
    print(
        "Tokens: "
        f"entrada={uso.prompt_token_count}, "
        f"saida={uso.candidates_token_count}, "
        f"total={uso.total_token_count}",
        flush=True,
    )
    return resposta.text
