from masonite.foundation import Application, HttpKernel
from config.providers import PROVIDERS
from Kernel import AppKernel
import os


application = Application(os.getcwd())

"""First Bind important providers needed to start the server
"""

application.register_providers(AppKernel, HttpKernel)
application.add_providers(*PROVIDERS)