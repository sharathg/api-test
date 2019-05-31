import unittest
import jsonschema

from helpers.logger import Logger
from helpers.api import API
from helpers.file import File


class BaseTest(unittest.TestCase, File):

    _logger = None
    base_url = None

    @classmethod
    def setUpClass(cls):
        cls._logger = Logger()
        cls.logger = cls._logger.get_logger()
        cls.api = API(cls.base_url)

    def setUp(self):
        self.logger.info("Starting Test: {}".format(self._testMethodName))
        self.pet_schema = self.get_schema("pet_schema.json")

    def tearDown(self):
        self.logger.info("Test Method Run Complete.\n\n\n\n")

    @classmethod
    def tearDownClass(cls):
        cls._logger.quit_logger()

    def getLogger(self):
        return self._logger.get_logger()

    def assertJsonSchema(self, obj, schema, msg=None):
        try:
            jsonschema.validate(obj, schema)
            self.logger.info("Assert [{}] :: {} : JSON Scheme : {} ? Result :: True".format(msg, obj, schema))
        except Exception as e:
            self.logger.error("Assertion ERROR !!\n[{}]\nActual: {}\nExpected: {}".format(msg, obj, schema))
            raise e

    def assertEqual(self, first, second, msg=None):
        try:
            super().assertEqual(first, second, msg)
            self.logger.info("Assert [{}] :: {} == {} ? Result :: True".format(msg, first, second))
        except AssertionError as ae:
            self.logger.error("Assertion ERROR !!\n[{}]\nActual: {}\nExpected: {}".format(msg, first, second))
            raise ae

    def assertNotEqual(self, first, second, msg=None):
        try:
            super().assertNotEqual(first, second, msg)
            self.logger.info("Assert [{}] :: {} != {} ? Result :: True".format(msg, first, second))
        except AssertionError as ae:
            self.logger.error("Assertion ERROR !!\n[{}]\nActual: {}\nNOT Expected: {}".format(msg, first, second))
            raise ae

    def assertIn(self, member, container, msg=None):
        try:
            super().assertIn(member, container, msg)
            self.logger.info("Assert [{}] :: {} IN {} ? Result :: True".format(msg, member, container))
        except AssertionError as ae:
            self.logger.error("Assertion ERROR !!\n[{}]\nMember: {}\nContainer: {}".format(member, container, member))
            raise ae
