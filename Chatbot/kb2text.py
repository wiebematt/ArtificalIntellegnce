from __future__ import with_statement
from pyke import knowledge_engine, ask_tty

#  Convert
engine = knowledge_engine.engine(__file__)
engine.ask_module = ask_tty
