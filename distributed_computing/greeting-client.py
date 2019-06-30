# first time to use Pyro for distributed computing
docs_from = "https://pythonhosted.org/Pyro4/intro.html"

""""""
#saved as a greeting-client.py
import Pyro4


uri = """
	PYRO:obj_228ffca9a1a44d8da03a488933b158af@localhost:49881
""".strip()

name = "david".strip()

"""what is strip()?"""
greeting_maker = Pyro4.Proxy(uri)       #get a Pyro to the greeting object
print(greeting_maker.get_fortune(name))