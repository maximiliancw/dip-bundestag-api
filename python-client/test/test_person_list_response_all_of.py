"""
    Deutscher Bundestag - DIP

    API des Dokumentations- und Informationssystems für Parlamentsmaterialien  # noqa: E501

    The version of the OpenAPI document: 1.2
    Contact: parlamentsdokumentation@bundestag.de
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.dip_bundestag.model.person import Person

from deutschland import dip_bundestag

globals()["Person"] = Person
from deutschland.dip_bundestag.model.person_list_response_all_of import (
    PersonListResponseAllOf,
)


class TestPersonListResponseAllOf(unittest.TestCase):
    """PersonListResponseAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPersonListResponseAllOf(self):
        """Test PersonListResponseAllOf"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PersonListResponseAllOf()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
