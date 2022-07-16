import logging

class CommonLog:

    def __init__(self, name) -> None:
        app_name = ''.join(x.capitalize() or '.' for x in name.split('.'))
        self.logger = logging.getLogger(app_name)

    def bebug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)
