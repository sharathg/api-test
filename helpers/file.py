import json
from os.path import join, dirname


class File:

    def get_schema(self, filename):
        relative_path = join('../schemas', filename)
        absolute_path = join(dirname(__file__), relative_path)
        with open(absolute_path) as schema_file:
            return json.loads(schema_file.read())

    def get_testdata(self, filename):
        relative_path = join('../testdata', filename)
        absolute_path = join(dirname(__file__), relative_path)
        with open(absolute_path) as schema_file:
            return json.loads(schema_file.read())

    def get_imagefile(self, filename):
        relative_path = join('../testdata', filename)
        absolute_path = join(dirname(__file__), relative_path)
        image = open(absolute_path, 'rb')
        return image