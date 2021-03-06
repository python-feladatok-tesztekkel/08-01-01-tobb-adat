from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestOtosokSzama(TestCase):
    def test_diakok_van_otos(self):
        adat = "Kis János,5;Nagy Éva,4;Szabó Éva,5;Péter Imre,3;Kis Gergő,5;Magony Nóra,5;Szántó Regő,4"
        aktualis = feladatok.otosok_szama(adat)
        elvart = 4
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg hányan kaptak ötöst!")
    def test_diakok_nincs_otos(self):
        adat = "Kis János,3;Nagy Éva,4;Szabó Éva,2;Péter Imre,3;Kis Gergő,4;Magony Nóra,4;Szántó Regő,4"
        aktualis = feladatok.otosok_szama(adat)
        elvart = 0
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg hányan kaptak ötöst!")
    def test_nincsdiak(self):
        adat = ""
        aktualis = feladatok.otosok_szama(adat)
        elvart = 0
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg hányan kaptak ötöst!")