"""
    Deutscher Bundestag - DIP

    API des Dokumentations- und Informationssystems für Parlamentsmaterialien  # noqa: E501

    The version of the OpenAPI document: 1.2
    Contact: parlamentsdokumentation@bundestag.de
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.dip_bundestag.model.deskriptor import Deskriptor
from deutschland.dip_bundestag.model.vorgang_deskriptor_all_of import (
    VorgangDeskriptorAllOf,
)

from deutschland import dip_bundestag

globals()["Deskriptor"] = Deskriptor
globals()["VorgangDeskriptorAllOf"] = VorgangDeskriptorAllOf
from deutschland.dip_bundestag.model.vorgang_deskriptor import VorgangDeskriptor


class TestVorgangDeskriptor(unittest.TestCase):
    """VorgangDeskriptor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVorgangDeskriptor(self):
        """Test VorgangDeskriptor"""
        # FIXME: construct object with mandatory attributes with example values
        # model = VorgangDeskriptor()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
