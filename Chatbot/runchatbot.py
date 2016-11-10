import kb2text
from pizzabot import PizzaBot


def handle_response(response_obj):
    chat_in_progress = True
    # If the order is not complete, ask a followup question
    if response_obj['type'] == "followup":
        print(response_obj['answer'])

    # When all the constraints are satisfied, you can end the chat
    elif response_obj['type'] == "order":
        print(response_obj['answer'])
        chat_in_progress = False
    return chat_in_progress


def pizza_price(order):
    pizza = order["pizza"]
    order_print = " That will be "
    price = len(pizza["size"]) * 1.1 + len(filter_no_fields(pizza['vegetarian_toppings'])) * .5
    if "meat_toppings" in pizza:
        price += len(filter_no_fields(pizza['meat_toppings'])) * 1.25 if pizza['meat_toppings'] else 0
    return order_print + "$" + str(price) + "."


def filter_no_fields(topping_tuple):
    return filter(lambda x: not ("no" in x), topping_tuple)


def validate_order(order):
    order_print = "You ordered: "
    if "soup" in order:
        order_print += order["soup"].replace("_", " ") + " Soup. That's $5.00."
    elif "pizza" in order:
        pizza = order["pizza"]
        # print pizza
        order_print += "A " + pizza["size"] + " pizza with " + pizza["crust"].replace("_", " ") + " crust, "
        order_print += pizza["sauce"].replace("_", " ") + ", "
        order_print += pizza["cheese"].replace("_", " ") + ", "
        toppings = pizza['vegetarian_toppings'] + pizza['meat_toppings'] if 'meat_toppings' in pizza else pizza[
            'vegetarian_toppings']
        toppings = filter_no_fields((x.replace("_", " ") for x in toppings))
        if len(toppings):
            order_print += ", ".join(toppings) + "."
        else:
            order_print += " and no toppings."
        order_print += pizza_price(order)
    print order_print
    return False


def main():
    # The chatbot object's lifecycle is independent of the input itself.
    PizzaBot.initialize()
    while True:
        chat_in_progress = True
        print("// Starting chat")
        while chat_in_progress:
            chat_in_progress = validate_order(kb2text.main())
        print("// Chat should now be considered complete")

if __name__ == '__main__':
    main()
