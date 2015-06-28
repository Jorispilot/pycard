import unittest

from pycard.param import params
from pycard.prop import from_string, props


class CategoryPropTestCase(unittest.TestCase):

    def test_1(self):
        Prop = props["CATEGORIES"]
        string = "CATEGORIES:Work,La Phase,Dynamo\r\n"
        obj = Prop(["Work", "La Phase", "Dynamo"])
        self.assertEqual(obj, from_string(string))
        self.assertEqual(obj.format(), string)

    def test_3(self):
        Prop = props["CATEGORIES"]
        string = "CATEGORIES:Work,A\, B\, and C\r\n"
        obj = Prop(["Work", "A, B, and C"])
        self.assertEqual(obj, from_string(string))
        self.assertEqual(obj.format(), string)


class DeliveryAddressPropTestCase(unittest.TestCase):

    def test_1(self):
        Prop = props["ADR"]
        string = "ADR;INTL;WORK:Albert;S S.A.R.L.;213 rue Martz;Mince;Papis;99999;Zut\r\n"
        obj = Prop( ["Albert","S S.A.R.L.","213 rue Martz", "Mince", "Papis", "99999", "Zut"],
                    [params["INTL"], params["WORK"]])
        self.assertEqual(obj, from_string(string))
        self.assertEqual(obj.format(), string)


class NameTestCase(unittest.TestCase):

    def test_1(self):
        Prop = props["N"]
        string = "N:;Albert;;Sir.;Jr.\r\n"
        obj = Prop( ["", "Albert", "", "Sir.", "Jr."])
        self.assertEqual(obj, from_string(string))
        self.assertEqual(obj.format(), string)
