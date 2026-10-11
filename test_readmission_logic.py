import unittest
from readmission_logic import predict_readmission


class TestReadmissionLogic(unittest.TestCase):
    def test_high_risk_condition(self):
        self.assertEqual(predict_readmission("Heart Attack", 7), "READMIT")

    def test_low_risk_condition(self):
        self.assertEqual(predict_readmission("Hypertension", 3), "NO READMIT")

    def test_unknown_condition(self):
        self.assertEqual(predict_readmission("Fractured Arm", 1), "NO READMIT")


if __name__ == "__main__":
    unittest.main()
