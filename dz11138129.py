def gadget_power(base_power, bonus=10):
    total_power = base_power + bonus
    return total_power

result_default = gadget_power(50)
print(f"Сила гаджета (базова 50, бонус за замовчуванням): {result_default}")

result_custom = gadget_power(50, 25)
print(f"Сила гаджета (базова 50, власний бонус 25): {result_custom}")

result_test2 = gadget_power(80, 15)
print(f"Сила гаджета (базова 80, власний бонус 15): {result_test2}")