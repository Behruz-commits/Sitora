"""
Sitora Bot Interface
---------------------
Интерфейс общения с пользователем.
Позже будет интеграция с Telegram или Web-чатом.
"""

from api.main import ask_sitora

def start_dialogue():
    print("🌟 Добро пожаловать в чат с Ситорой!")
    while True:
        user_input = input("Вы: ")
        if user_input.lower() in ["выход", "exit", "quit"]:
            print("👋 До встречи, друг!")
            break
        reply = ask_sitora(user_input)
        print("Ситора:", reply["output"])

if __name__ == "__main__":
    start_dialogue()
