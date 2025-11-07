"""
Sitora API Core
----------------
Это базовый модуль, через который внешние приложения (бот, веб-панель)
могут обращаться к ИИ-ядру Sitora.

Позже сюда добавится подключение к локальной модели или ChatGPT-API.
"""

from datetime import datetime

def ask_sitora(prompt: str, lang: str = "ru") -> dict:
    """
    Получить ответ от Sitora.
    """
    # Пока имитация
    response = f"[{lang.upper()}] Ситора думает над запросом: {prompt}"
    return {
        "timestamp": datetime.now().isoformat(),
        "input": prompt,
        "output": response
    }

if __name__ == "__main__":
    demo = ask_sitora("Привет, кто ты?", "ru")
    print(demo["output"])
