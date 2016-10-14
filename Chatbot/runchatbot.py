import json

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


def main():
    # The chatbot object's lifecycle is independent of the input itself.
    PizzaBot.initialize()
    while True:
        chat_in_progress = True
        print("// Starting chat")
        while chat_in_progress:
            text = raw_input(': ')
            request = json.dumps({"text": text})
            response = PizzaBot.process_user_input(request)

            # response is a json string, so we need to parse this for the response object
            response_obj = json.loads(response)
            chat_in_progress = handle_response(response_obj)
        print("// Chat should now be considered complete")


if __name__ == '__main__':
    main()
