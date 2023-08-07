import logging

import requests
from googletrans import Translator

from api_jokes.sentiment.sentiment_api import get_sentiment

logging.basicConfig(
    level=logging.DEBUG,
    filename=f'app.log',
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def get_memes():
    img_obj = requests.get('https://api.imgflip.com/get_memes')
    with open('pic1.jpg', 'wb') as handle:
        response = requests.get(img_obj.json()['data']['memes'][5]['url'], stream=True)
        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)


if __name__ == '__main__':
    translator = Translator()

    # print(json.dumps(get_cocktail("vodka"), indent=2))
    # show(5)
    # s = yoda_translate_text("Hello young people")
    # print(s)
    # print(get_sentiment("i`m very sad...."))
