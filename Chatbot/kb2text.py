from pyke import knowledge_engine, ask_tty

engine = knowledge_engine.engine(__file__)
engine.ask_module = ask_tty
order = {}
Meatza = {'cheese': 'mozzarella', 'meat_toppings': ('pepperoni', 'italian_sausage', 'Steak', 'Bacon', 'Chorizo'),
          'vegetarian_toppings': (), 'crust': 'normal', 'sauce': 'tomato', 'size': 'medium'}
Pepperoni = {'cheese': 'mozzarella', 'meat_toppings': ('pepperoni'), 'vegetarian_toppings': (), 'crust': 'normal',
             'sauce': 'tomato', 'size': 'medium'}
Supreme = {'cheese': 'mozzarella', 'meat_toppings': ('pepperoni', 'italian_sausage'),
           'vegetarian_toppings': ('tomato', 'spinach', 'onion', 'red_onion', 'red_pepper', 'green_pepper'),
           'crust': 'normal', 'sauce': 'tomato', 'size': 'medium'}


def option_display(param):
    return tuple(map((lambda x: (x, unicode(x).capitalize().replace("_", " "))), param))


def get_all_fact(goalstr, value):
    with engine.prove_goal(goalstr) as gen:
        return map(lambda x: x[value], [var for var, plan in gen])


def ask_question(function, field):
    return function(
        "What " + field.replace("_", " ") + " would you like? ",
        option_display(get_all_fact("fact." + field + "($" + field + ")", field)))


def premade_pizza():
    ppizza = ask_question(ask_tty.ask_select_1, "premade_pizza")
    order["pizza"] = eval(ppizza)


def make_pizza():
    order["pizza"] = {}
    pizza_type = ask_question(ask_tty.ask_select_1, "type_of_pizza")
    if pizza_type == "custom":
        engine_add_cntrlog("ordered_" + pizza_type)
        if not bool(ask_tty.ask_yn("Would you like a vegetarian pizza?")):
            engine_add_cntrlog("ordered_non_veggie")
    else:
        premade_pizza()


def ask_for_toppings(tag):
    ask_for(tag, ask_tty.ask_select_n)


def ask_for(tag, question_type=ask_tty.ask_select_1):
    order["pizza"][str(tag)] = ask_question(question_type, str(tag))
    # print var
    engine_add_cntrlog("ordered_" + str(tag))


def engine_add_cntrlog(fact, fact_base="fact", *args):
    engine.add_case_specific_fact(fact_base, fact, args)


def make_soup():
    soup = ask_question(ask_tty.ask_select_1, "soup")
    order["soup"] = soup
    engine_add_cntrlog("order_complete")


def activate_pizzabot():
    food = ask_question(ask_tty.ask_select_1, "food")
    if food == "pizza":
        engine_add_cntrlog("order_pizza")
    elif food == "soup":
        engine_add_cntrlog("order_soup")
        make_soup()


def main():
    engine.reset()
    engine.activate("relation")
    activate_pizzabot()
    return order
