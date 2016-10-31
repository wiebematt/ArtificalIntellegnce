from pyke import knowledge_engine, ask_tty

engine = knowledge_engine.engine(__file__)
engine.ask_module = ask_tty


def option_display(param):
    return tuple(map((lambda x: (x, unicode(x).capitalize().replace("_", " "))), param))


def get_all_fact(goalstr, value):
    with engine.prove_goal(goalstr) as gen:
        result = [var for var, plan in gen]
        return map(lambda x: x[value], result)


def ask_question(field, function=ask_tty.ask_select_1):
    return function("What " + field + " would you like?",
                    option_display(get_all_fact("fact." + field + "($" + field + ")", field)))


def make_pizza():
    engine.prove_goal("relation.ask_for_custom_pizza")


def ask_veggie():
    veggie = ask_tty.ask_yn("Would you like a vegetarian pizza?")
    if veggie:
        engine.prove_goal("ask_veggie_topping")
    else:
        engine.prove_goal("ask_all_toppings")


def make_soup():
    engine.prove_goal("relation.ask_for_soup")


def activate_pizzabot():
    engine.reset()
    engine.activate("relation")
    food = ask_question("food")
    if food == "Pizza":
        make_pizza()
    elif food == "Soup":
        make_soup()


activate_pizzabot()
