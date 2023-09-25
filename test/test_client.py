import json
import pathlib
import unittest
from facebook_ad_library import FacebookAdsLibrary
from facebook_ad_library.exceptions import OAuthException, exceptions
from facebook_ad_library import fields

ROOT = pathlib.Path(__file__).parent.parent
MOCK_FOLDER = ROOT / 'mock'
EMPTY_SEARCH = MOCK_FOLDER / 'empty-search.json'
BASIC_SEARCH = MOCK_FOLDER / 'basic-search.json'
FIELDS_SEARCH = MOCK_FOLDER / 'fields-search.json'


class TestClient(unittest.TestCase):

    def setUp(self) -> None:
        self.instance = FacebookAdsLibrary()

    def test_check_files(self):
        self.assertTrue(EMPTY_SEARCH.exists())
        self.assertTrue(BASIC_SEARCH.exists())
        self.assertTrue(FIELDS_SEARCH.exists())

    def test_oauth_exception(self):
        with self.assertRaises(OAuthException):
            with open(EMPTY_SEARCH) as handler:
                response = json.load(handler)
                raise exceptions[response['type']](response)

    def test_basic_search(self):
        with open(BASIC_SEARCH) as handler:
            response = json.load(handler)
            self.assertIsInstance(response, dict)
            data = response.get('data', [])
            self.assertEqual(len(data), 20)

            for item in data:
                self.assertIsInstance(item, dict)
                keys = item.keys()
                self.assertEqual(['id'], list(keys))

    def test_fields_search(self):
        with open(FIELDS_SEARCH) as handler:
            items = fields.__all__

            fields_list = [
                getattr(fields, item) for item in items if isinstance(getattr(fields, item), fields.ADField)
            ]

            response = json.load(handler)

            self.assertIsInstance(response, dict)
            data = response.get('data', [])
            self.assertEqual(len(data), 20)

            for item in data:
                for field in fields_list:
                    self.assertIsInstance(field, fields.ADField)
                    self.assertIn(field.field_name, item)
