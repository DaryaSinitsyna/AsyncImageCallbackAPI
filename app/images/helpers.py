import httpx
import spacy


async def get_words_from_text(image_data):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(image_data)
    result = [token.lemma_ for token in doc]
    return result


async def send_request(url, data):
    headers = {"Content-Type": "application/json"}
    async with httpx.AsyncClient() as client:
        await client.post(url, headers=headers, json=data)
