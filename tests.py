"""
tests.py - Unit tests for the FarmHelper library.

Run with:
    python -m unittest tests.py
"""

import unittest
from datetime import date, timedelta

from farmhelper import (
    acres_to_hectares,
    hectares_to_acres,
    plots_to_hectares,
    estimate_yield,
    fertilizer_needed,
    days_to_harvest,
)


class TestLandConversions(unittest.TestCase):

    def test_acres_to_hectares(self):
        self.assertAlmostEqual(acres_to_hectares(2), 0.809, places=3)

    def test_hectares_to_acres(self):
        self.assertAlmostEqual(hectares_to_acres(1), 2.471, places=3)

    def test_plots_to_hectares(self):
        self.assertEqual(plots_to_hectares(5), 0.1)

    def test_acres_to_hectares_negative_raises_error(self):
        with self.assertRaises(ValueError):
            acres_to_hectares(-1)

    def test_hectares_to_acres_negative_raises_error(self):
        with self.assertRaises(ValueError):
            hectares_to_acres(-1)

    def test_plots_to_hectares_negative_raises_error(self):
        with self.assertRaises(ValueError):
            plots_to_hectares(-1)


class TestYieldEstimation(unittest.TestCase):

    def test_estimate_yield(self):
        self.assertEqual(estimate_yield(3, 15), 45)

    def test_estimate_yield_zero_area(self):
        self.assertEqual(estimate_yield(0, 15), 0)

    def test_estimate_yield_negative_area_raises_error(self):
        with self.assertRaises(ValueError):
            estimate_yield(-1, 15)

    def test_estimate_yield_negative_rate_raises_error(self):
        with self.assertRaises(ValueError):
            estimate_yield(3, -15)


class TestFertilizerCalculation(unittest.TestCase):

    def test_fertilizer_needed(self):
        self.assertEqual(fertilizer_needed(2, 50), 100)

    def test_fertilizer_needed_zero_area(self):
        self.assertEqual(fertilizer_needed(0, 50), 0)

    def test_fertilizer_needed_negative_area_raises_error(self):
        with self.assertRaises(ValueError):
            fertilizer_needed(-1, 50)

    def test_fertilizer_needed_negative_rate_raises_error(self):
        with self.assertRaises(ValueError):
            fertilizer_needed(2, -50)


class TestHarvestCountdown(unittest.TestCase):

    def test_days_to_harvest_future(self):
        planted = date.today() - timedelta(days=30)
        self.assertEqual(days_to_harvest(planted, 90), 60)

    def test_days_to_harvest_today(self):
        planted = date.today() - timedelta(days=90)
        self.assertEqual(days_to_harvest(planted, 90), 0)

    def test_days_to_harvest_past(self):
        planted = date.today() - timedelta(days=100)
        self.assertEqual(days_to_harvest(planted, 90), -10)

    def test_days_to_harvest_negative_growth_period_raises_error(self):
        with self.assertRaises(ValueError):
            days_to_harvest(date.today(), -5)


if __name__ == "__main__":
    unittest.main()
