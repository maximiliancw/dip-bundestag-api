"""
    Deutscher Bundestag - DIP

    API des Dokumentations- und Informationssystems für Parlamentsmaterialien  # noqa: E501

    The version of the OpenAPI document: 1.2
    Contact: parlamentsdokumentation@bundestag.de
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.dip_bundestag.model.aktivitaet_anzeige import AktivitaetAnzeige
from deutschland.dip_bundestag.model.beschlussfassung import Beschlussfassung
from deutschland.dip_bundestag.model.fundstelle import Fundstelle
from deutschland.dip_bundestag.model.ressort import Ressort
from deutschland.dip_bundestag.model.ueberweisung import Ueberweisung
from deutschland.dip_bundestag.model.urheber import Urheber
from deutschland.dip_bundestag.model.vorgangspositionbezug import Vorgangspositionbezug
from deutschland.dip_bundestag.model.zuordnung import Zuordnung

from deutschland import dip_bundestag

globals()["AktivitaetAnzeige"] = AktivitaetAnzeige
globals()["Beschlussfassung"] = Beschlussfassung
globals()["Fundstelle"] = Fundstelle
globals()["Ressort"] = Ressort
globals()["Ueberweisung"] = Ueberweisung
globals()["Urheber"] = Urheber
globals()["Vorgangspositionbezug"] = Vorgangspositionbezug
globals()["Zuordnung"] = Zuordnung
from deutschland.dip_bundestag.model.vorgangsposition import Vorgangsposition


class TestVorgangsposition(unittest.TestCase):
    """Vorgangsposition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVorgangsposition(self):
        """Test Vorgangsposition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Vorgangsposition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
