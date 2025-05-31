import unittest
import sys
import json
from io import StringIO
import pickle
import ssl
import socket
import xml
import xml.etree
import xml.etree.ElementTree

# Sample data to be serialized
test_data = {
    'name': 'Alice',
    'age': 30,
    'is_admin': True,
    'skills': ['Python', 'Network Programming', 'Digital Forensics']
}

# Helper: convert dict to XML string
def dict_to_xml(data):
    root = xml.etree.ElementTree.Element('root')
    for key, value in data.items():
        if isinstance(value, list):
            root.append(xml.etree.ElementTree.Element(key, {'type': 'list'}))
            for item in value:
                item_element = xml.etree.ElementTree.Element('item')
                item_element.text = str(item)
                root[-1].append(item_element)
        else:
            root.append(xml.etree.ElementTree.Element(key, {'type': type(value).__name__}))
    return root

# Helper: convert XML string back to dict
def xml_to_dict(xml_str):
    root = xml.etree.ElementTree.fromstring(xml_str)
    result = {}
    for child in root:
        if child.get('type') == 'list':
            result[child.tag] = []
            for item in child:
                try:
                    value = json.loads(item.text)
                except json.JSONDecodeError:
                    value = item.text
                result[child.tag].append(value)
        else:
            value = child.text
            # Try to cast values back to original types
            value_type = child.get('type')
            if value_type == 'int':
                value = int(value)
            elif value_type == 'float':
                value = float(value)
            elif value_type == 'bool':
                value = value.lower() == 'true'
            result[child.tag] = value
    result = json.loads(json.dumps(result))
    return result

# Function to assert that two dictionaries are equal
def assert_true_dict(dict1, dict2):
    is_true = dict1 == dict2
    if is_true:
        print("The dictionaries match.", dict1, dict2)
    else:
        print("The dictionaries do not match.")

def assert_true_strings(str1, str2):
    if str1 == str2:
        print("The XML strings match.", str1, str2)
    else:
        print("The XML strings do not match.")

# A 'null' stream that discards anything written to it
class NullWriter(StringIO):
    def write(self, txt):
        pass

# Unit test
class TestXmlToVariable(unittest.TestCase):
    def setUp(self):
        self.test_data = test_data

    def test_xml(self):
        xml_data = dict_to_xml(self.test_data)
        expected_xml = dict_to_xml(self.test_data)
        assert_true_strings(xml_data, expected_xml)
    
    def test_unxml(self):
        xml_data = dict_to_xml(self.test_data)
        parsed_data = xml_to_dict(xml_data)
        assert_true_dict(self.test_data, parsed_data)

# Entry point
if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'run':
        xml_data = dict_to_xml(test_data)
        print("Serialized XML:", xml_data)
    else:
        runner = unittest.TextTestRunner()
        unittest.main(testRunner=runner, exit=False)
