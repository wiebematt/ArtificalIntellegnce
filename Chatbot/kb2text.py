from pyke import knowledge_engine, ask_tty

engine = knowledge_engine.engine(__file__)
engine.ask_module = ask_tty
order = {}


def option_display(param):
    return tuple(map((lambda x: (x, unicode(x).capitalize().replace("_", " "))), param))


def get_all_fact(goalstr, value):
    with engine.prove_goal(goalstr) as gen:
        return map(lambda x: x[value], [var for var, plan in gen])


def ask_question(function, field):
    return function("What " + field + " would you like? (Please enter all options separated by a comma)",
                    option_display(get_all_fact("fact." + field + "($" + field + ")", field)))


def make_pizza():
    order["pizza"] = {}
    veggie = ask_tty.ask_yn("Would you like a vegetarian pizza?")
    order["pizza"]["size"] = ask_question(ask_tty.ask_select_1, "size")
    order["pizza"]["crust"] = ask_question(ask_tty.ask_select_1, "crust")
    order["pizza"]["sauce"] = ask_question(ask_tty.ask_select_1, "sauce")
    order["pizza"]["cheese"] = ask_question(ask_tty.ask_select_1, "cheese")
    order["pizza"]["vegetarian_toppings"] = ask_question(ask_tty.ask_select_n, "vegetarian_toppings")
    if not veggie:
        order["pizza"]["meat_toppings"] = ask_question(ask_tty.ask_select_n, "meat_toppings")


def make_soup():
    soup = ask_question(ask_tty.ask_select_1, "soup")
    order["soup"] = soup
    engine.add_case_specific_fact("fact", "order_complete", ())


def activate_pizzabot():
    food = ask_question(ask_tty.ask_select_1, "food")
    if food == "pizza":
        engine.add_case_specific_fact("fact", "order_pizza", ())
        make_pizza()
    elif food == "soup":
        engine.add_case_specific_fact("fact", "order_soup", ())
        # make_soup()


def main():
    engine.reset()
    engine.activate("relation")
    engine.assert_("fact", "order_start", ())
    # activate_pizzabot()
    # return order


print main()
