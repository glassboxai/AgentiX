import unittest
from tiered_energy_bill_code import tiered_energy_bill

class TestTieredEnergyBill(unittest.TestCase):
    def test_valid_inputs(self):
        # Normal cases
        self.assertEqual(tiered_energy_bill(0), 0)
        self.assertEqual(tiered_energy_bill(50), 600)
        self.assertEqual(tiered_energy_bill(100), 1200)
        self.assertEqual(tiered_energy_bill(150), 2100)
        self.assertEqual(tiered_energy_bill(200), 3000)
        self.assertEqual(tiered_energy_bill(250), 4250)
        
        # Edge cases
        self.assertEqual(tiered_energy_bill(1), 12)
        self.assertEqual(tiered_energy_bill(99), 1188)
        self.assertEqual(tiered_energy_bill(101), 1218)
        self.assertEqual(tiered_energy_bill(199), 2982)
        self.assertEqual(tiered_energy_bill(201), 3025)

    def test_invalid_inputs(self):
        # Type checks
        with self.assertRaises(ValueError):
            tiered_energy_bill("100")
        with self.assertRaises(ValueError):
            tiered_energy_bill(100.5)
        with self.assertRaises(ValueError):
            tiered_energy_bill(None)
        
        # Value checks
        with self.assertRaises(ValueError):
            tiered_energy_bill(-50)

if __name__ == "__main__":
    unittest.main()