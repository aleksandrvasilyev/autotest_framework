import json
from argparse import ArgumentParser
from dicttoxml import dicttoxml

parser = ArgumentParser(description="Choose file format")
parser.add_argument('--format', help="provide format")
parser.add_argument('--name', help="provide name")
parser.add_argument('--age', help="provide age")
parser.add_argument('--gender', help="provide gender")
parser.add_argument('--birth_year', help="provide birth_year")

arg = parser.parse_args()


class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def get_dict(self):
        return self.__dict__

    def convert_to_json(self):
        return json.dumps(self.get_dict())

    def convert_to_xml(self):
        xml = dicttoxml(self.get_dict(), custom_root='Persons', attr_type=False)
        return xml


person = Human(arg.name, arg.age, arg.gender, arg.birth_year)

if arg.format == 'json':
    print(person.convert_to_json())
elif arg.format == 'xml':
    print(person.convert_to_xml())
else:
    print('error')
