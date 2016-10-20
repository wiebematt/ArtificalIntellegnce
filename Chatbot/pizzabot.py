import ujson as json

class PizzaBot:
    """Ticary chatbot"""
    initialized = False

    @staticmethod
    def initialize():
        PizzaBot.initialized = True

    @staticmethod
    def process_user_input(inp, session=None):
        """
        Process the input, return answer in the form of a JSON-encoded string
        input: JSON-encoded string, containing at minimum, the user's text
        session: session object, containing user state
        return: JSON-encoded string, containing the response
        """

        in_json = json.loads(inp)
        text = in_json["text"]

        ####################


        ## ENTER YOUR CODE HERE


        ####################

        response = {"answer": text, "type": "followup"}
        respstr = json.dumps(response)
        return respstr
