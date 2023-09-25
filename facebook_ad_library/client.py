from typing import List
import requests
from facebook_ad_library import fields, types
from facebook_ad_library.exceptions import exceptions
from facebook_ad_library.config import FACEBOOK_TOKEN


class FacebookAdsLibrary:
    """
        A class for interacting with the Facebook Ads API.

        :param access_token: The access token for authentication with the API.
        :type access_token: str
        :param api_version: The API version to be used (optional, default is "v14.0").
        :type api_version: str
    """
    default_api_version = "v14.0"
    default_url_pattern = ("https://graph.facebook.com/"
                           "{api_version}/"
                           "ads_archive?access_token={access_token}")
    api_url = None
    session = requests.Session()

    def __init__(self, access_token: str = FACEBOOK_TOKEN,
                 api_version: str = "v14.0",
                 ):
        assert access_token != "" and access_token is not None
        """
            Initializes an instance of the FacebookAdsLibrary class.

            :param access_token: The access token for authentication with the API.
            :type access_token: str
            :param api_version: The API version to be used (optional, default is "v14.0").
            :type api_version: str
        """
        self.default_api_version = api_version
        self.api_url = self.default_url_pattern.format(
            api_version=self.default_api_version,
            access_token=access_token
        )

    def search(self,
               query: List[types.AdLibraryType] = None,
               fields: List[fields.ADField] = None,
               limit: int = 20, ):
        """
        Performs a search in the Facebook Ads API.

        :param query: A list of search criteria (optional).
        :type query: List[types.AdLibraryType]
        :param fields: A list of fields to retrieve (optional).
        :type fields: List[fields.ADField]
        :param limit: The maximum number of results to return (optional, default is 20).
        :type limit: int
        :return: The search results.
        :rtype: dict
        """
        if fields is not None:

            new_fields = []

            for field in fields:
                if isinstance(field, str):
                    new_fields.append(field)
                elif isinstance(field, fields.ADField) or (callable(field) and isinstance(field(), fields.ADField)):
                    new_fields.append(field.field_name)
                else:
                    raise Exception(f"Invalid field {field}")
            fields = new_fields

        if query is None:
            query = [types.AdReachedCountries(
                    values=(types.AdReachedCountry.ALL,)
                )]
        query = '&'.join(map(lambda q: repr(q), query))
        with self.session.get(
                self.api_url + f'&limit={limit}&fields={fields}&{query}'
        ) as response:
            return self.__process_response(response)

    def __process_response(self, response: requests.Response):
        """
        Processes the API response.

        :param response: The API response.
        :type response: requests.Response
        :return: The response data or raises an exception in case of an error.
        :rtype: dict
        """
        data = response.json()
        error = data.get('error', None)
        if error:
            raise exceptions[error['type']](error)
        return data
