code_name = "Shadow Lynx"
specialization = "Кіберрозвідка та стелс-операції"
secret_mission = "Операція 'Нічний піксель'"
agent_level = 3

gadgets = [
    "Лазерний годинник-сканер",
    "Дрон розміром з комаху",
    "Шпигунські окуляри ночного бачення",
    "Магнітні рукавички-присоски"
]

def show_profile():
    print("=" * 40)
    print("      СЕКРЕТНЕ ДОСЬЄ АГЕНТА      ")
    print("=" * 40)
    print(f"Кодове ім'я:    {code_name}")
    print(f"Спеціалізація:  {specialization}")
    print(f"Секретна місія: {secret_mission}")
    print(f"Рівень доступу: {agent_level}")
    print("-" * 40)

show_profile()

print("Арсенал гаджетів:")
for index, gadget in enumerate(gadgets, start=1):
    print(f"  {index}. {gadget}")

print("-" * 40)

if agent_level >= 3:
    print("СТАТУС: [ДОСТУП ДОЗВОЛЕНО] — Ласкаво просимо до системи!")
else:
    print("СТАТУС: [ДОСТУП ЗАБОРОНЕНО] — Недостатній рівень допуску!")

print("=" * 40)