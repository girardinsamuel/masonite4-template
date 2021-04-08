from masonite.foundation import Kernel

class AppKernel(Kernel):

    def set_framework_options(self):
        self.application.bind(
            "config.application", "config.application"
        )
        self.application.bind("config.mail", "config.mail")
        self.application.bind("config.session", "config.session")
        self.application.bind("config.queue", "config.queue")
        self.application.bind("config.database", "config.database")
        self.application.bind("config.location", "tests/integrations/config")
        self.application.bind("config.cache", "config.cache")
        self.application.bind("config.broadcast", "config.broadcast")
        self.application.bind("config.auth", "config.auth")
        self.application.bind(
            "config.filesystem", "config.filesystem"
        )

    def register_controllers(self):
        self.application.bind("controller.location", "app.controllers")

    def register_templates(self):
        self.application.bind("views.location", "templates")

    def register_framework(self):
        super().register_framework()
        self.application.bind("routes.web", "web.Route")
        self.application.bind("jobs.location", "app/jobs")
        self.application.bind("mailables.location", "app/mailables")
