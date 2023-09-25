import json
from facebook_ad_library import FacebookAdsLibrary, queries, fields
from facebook_ad_library.exceptions import OAuthException

if __name__ == "__main__":
    instance = FacebookAdsLibrary()
    try:
        instance.search()
    except OAuthException as exc:
        json.dump(exc.raw, open(
            './mock/empty-search.json','w+', encoding='utf-8'
        ))

    response = instance.search(
        query=(
            queries.SearchTerms("python"),
            queries.AdReachedCountries(
                values=[queries.AdReachedCountry.BR, queries.AdReachedCountry.US]
            )
        )
    )
    json.dump(response, open(
        './mock/basic-search.json', 'w+', encoding="utf-8"
    ))

    items = fields.__all__

    fields_list = [
        getattr(fields, item) for item in items if isinstance(getattr(fields, item), fields.ADField)
    ]
    response = instance.search(
        query=(
            queries.SearchTerms("python"),
            queries.AdReachedCountries(
                values=[queries.AdReachedCountry.BR, queries.AdReachedCountry.US]
            )
        ),
        fields=fields_list
    )
    json.dump(response, open(
        './mock/fields-search.json', 'w+', encoding="utf-8"
    ))
