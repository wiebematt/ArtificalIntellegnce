from pyke import knowledge_engine, ask_tty, goal

engine = knowledge_engine.engine(__file__)
engine.ask_module = ask_tty


# def run():
#     engine.reset()
#     try:
#         engine.activate('relation')
#         result = engine.prove_1_goal('relation.ask_for_pizza()')
#         print result
#     except StandardError:
#         krb_traceback.print_exc()
#         sys.exit(1)
#
# run()

def option_display(param):
    return tuple(map((lambda x: (x, unicode(x).capitalize())), param))


def get_all_fact(goalstr, value, veggie=False):
    with engine.prove_goal(goalstr) as gen:
        result = filter(lambda x: x["veggie"] == "veg", [var for var, plan in gen]) if veggie else \
            [var for var, plan in gen]
        return map(lambda x: x[value], result)


def ask_question(function, field, veggie):
    return function("What " + field + " would you like?",
                    option_display(get_all_fact("fact." + field + "($" + field + ", $veggie)", field, veggie)))


def make_pizza():
    veggie = ask_tty.ask_yn("Would you like a vegetarian pizza?")
    size = ask_question(ask_tty.ask_select_1, "size", False)
    crust = ask_question(ask_tty.ask_select_1, "crust", veggie)
    sauce = ask_question(ask_tty.ask_select_1, "sauce", veggie)
    cheese = ask_question(ask_tty.ask_select_1, "cheese", veggie)
    toppings = ask_question(ask_tty.ask_select_n, "toppings", veggie)
    engine.prove_goal(
        "fact.pizza(custom, $" + size + ", $" + crust + ", $" + sauce + ", $" + cheese + ", $" + toppings + ", $" + veggie)


def make_soup():
    print "Really? Not Pizza?!?"


def activate_pizzabot():
    engine.reset()
    food = ask_question(ask_tty.ask_select_1, "food")
    if food == "Pizza":
        make_pizza()
    elif food == "Soup":
        make_soup()
