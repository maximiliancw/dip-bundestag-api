"""
    Deutscher Bundestag - DIP

    API des Dokumentations- und Informationssystems für Parlamentsmaterialien  # noqa: E501

    The version of the OpenAPI document: 1.2
    Contact: parlamentsdokumentation@bundestag.de
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland.dip_bundestag.api.drucksachen_api import DrucksachenApi  # noqa: E501

from deutschland import dip_bundestag


class TestDrucksachenApi(unittest.TestCase):
    """DrucksachenApi unit test stubs"""

    def setUp(self):
        self.api = DrucksachenApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_drucksache(self):
        """Test case for get_drucksache

        Liefert Metadaten zu einer Drucksache  # noqa: E501
        """
        pass

    def test_get_drucksache_list(self):
        """Test case for get_drucksache_list

        Liefert eine Liste von Metadaten zu Drucksachen  # noqa: E501
        """
        pass

    def test_get_drucksache_text(self):
        """Test case for get_drucksache_text

        Liefert Volltext und Metadaten zu einer Drucksache  # noqa: E501
        """
        pass

    def test_get_drucksache_text_list(self):
        """Test case for get_drucksache_text_list

        Liefert eine Liste von Volltexten und Metadaten zu Drucksachen  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
