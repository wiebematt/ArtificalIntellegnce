import sys

from pyke import knowledge_engine, ask_tty, krb_traceback

#  Convert
engine = knowledge_engine.engine(__file__)
engine.ask_module = ask_tty


def run():
    engine.reset()
    try:
        engine.activate('relation')
        result = engine.prove_1_goal('relation.build_pizza()')
        print result
    except StandardError:
        krb_traceback.print_exc()
        sys.exit(1)


#
run()
