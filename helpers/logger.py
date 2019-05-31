import logging


class Logger:

    def __init__(self):
        self.logger = logging.getLogger("api-test")
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(funcName)s(%(lineno)d)] :: %(message)s')
        formatter.default_time_format = '%H:%M:%S'
        self.handler = logging.StreamHandler()
        self.handler.setLevel(logging.DEBUG)
        self.handler.setFormatter(formatter)
        self.logger.addHandler(self.handler)
        self.file_handler = logging.FileHandler("script.log")
        self.file_handler.setLevel(logging.DEBUG)
        self.file_handler.setFormatter(formatter)
        self.logger.addHandler(self.file_handler)

    def get_logger(self):
        return self.logger

    def quit_logger(self):
        try:
            self.logger.info("Closing Logger.")
            self.logger.removeHandler(self.handler)
            self.logger.removeHandler(self.file_handler)
        except Exception as e:
            print("*** Error Removing Logger Handler. Error: {} ***\n\n\n".format(e))
        self.logger = None
