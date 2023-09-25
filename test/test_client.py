import unittest
from facebook_ad_library import FacebookAdsLibrary
from facebook_ad_library.exceptions import OAuthException
from facebook_ad_library import fields, queries


class TestClient(unittest.TestCase):

    def setUp(self) -> None:
        self.instance = FacebookAdsLibrary()

    def test_oauth_exception(self):
        with self.assertRaises(OAuthException):
            self.instance.search()

    def test_basic_search(self):
        response = self.instance.search(
            query=(
                queries.SearchTerms("python"),
                queries.AdReachedCountries(
                    values=[queries.AdReachedCountry.BR, queries.AdReachedCountry.US]
                )
            )
        )
        self.assertIsInstance(response, dict)
        data = response.get('data', [])
        self.assertEqual(len(data), 20)

        for item in data:
            self.assertIsInstance(item, dict)
            keys = item.keys()
            self.assertEqual(['id'], list(keys))

    def test_fields_search(self):
        items = fields.__all__

        fields_list = [
            getattr(fields, item) for item in items if isinstance(getattr(fields, item), fields.ADField)
        ]
        response = self.instance.search(
            query=(
                queries.SearchTerms("python"),
                queries.AdReachedCountries(
                    values=[queries.AdReachedCountry.BR, queries.AdReachedCountry.US]
                )
            ),
            fields=fields_list
        )

        self.assertIsInstance(response, dict)
        data = response.get('data', [])
        self.assertEqual(len(data), 20)

        for item in data:
            for field in fields_list:
                self.assertIsInstance(field, fields.ADField)
                self.assertIn(field.field_name, item)
