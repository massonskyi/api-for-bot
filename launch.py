from fastapi import FastAPI

from PasswordGenerator.app.Generator import *
from PasswordGenerator.app import utils
app = FastAPI()


# Определение маршрута FastAPI для отображения веб-страницы
@app.get("/")
def get_index():
    """"
    return gr.Interface(fn=my_function, inputs="text", outputs="text").launch()
    """
    gen = Generator(utils.check_settings())
    s = gen.generate(12, 20)
    return {s[0]}


# Определение функции обработки данных
def my_function(text):
    # Ваш код обработки данных здесь
    return text.upper()


# Запуск FastAPI-приложения
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
