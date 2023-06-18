"""
    Deutscher Bundestag - DIP

    API des Dokumentations- und Informationssystems für Parlamentsmaterialien  # noqa: E501

    The version of the OpenAPI document: 1.2
    Contact: parlamentsdokumentation@bundestag.de
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.dip_bundestag.model.drucksache_text import DrucksacheText
from deutschland.dip_bundestag.model.drucksache_text_list_response_all_of import (
    DrucksacheTextListResponseAllOf,
)
from deutschland.dip_bundestag.model.list_response_base import ListResponseBase

from deutschland import dip_bundestag

globals()["DrucksacheText"] = DrucksacheText
globals()["DrucksacheTextListResponseAllOf"] = DrucksacheTextListResponseAllOf
globals()["ListResponseBase"] = ListResponseBase
from deutschland.dip_bundestag.model.drucksache_text_list_response import (
    DrucksacheTextListResponse,
)


class TestDrucksacheTextListResponse(unittest.TestCase):
    """DrucksacheTextListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDrucksacheTextListResponse(self):
        """Test DrucksacheTextListResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DrucksacheTextListResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
