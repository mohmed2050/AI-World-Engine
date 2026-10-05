agent = {
    "name": "سالم",
    "money": 10,
    "food": 5,
    "goal": "جمع المال"
}


def buy_food(agent, price):
    if agent["money"] >= price:
        agent["money"] -= price
        agent["food"] += 1
        print(agent["name"], "اشترى الطعام.")
    else:
        print(agent["name"], "لا يملك مالًا كافيًا.")


print("قبل الشراء:")
print(agent)

buy_food(agent, 3)

print("بعد الشراء:")
print(agent)