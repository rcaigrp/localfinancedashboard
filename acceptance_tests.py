import unittest
import tempfile
import os

class TestFinanceDashboard(unittest.TestCase):
    def test_criterion_1_import(self):
        try:
            import finance_dashboard
            self.assertTrue(True)
        except ImportError:
            self.fail("finance_dashboard module not found")

    def test_criterion_2_add_transaction(self):
        import finance_dashboard
        dashboard = finance_dashboard.FinanceDashboard()
        dashboard.add_transaction('income', 100)
        self.assertEqual(dashboard.ledger[-1]['amount'], 100)

    def test_criterion_3_generate_report(self):
        import finance_dashboard
        dashboard = finance_dashboard.FinanceDashboard()
        dashboard.add_transaction('income', 100)
        dashboard.add_transaction('expense', 50)
        report = dashboard.generate_report()
        self.assertIn('income', report)
        self.assertIn('expense', report)

    def test_criterion_4_save_report(self):
        import finance_dashboard
        import tempfile
        dashboard = finance_dashboard.FinanceDashboard()
        dashboard.add_transaction('income', 100)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as f:
            path = f.name
        dashboard.save_report(path)
        self.assertTrue(os.path.exists(path))
        os.unlink(path)

if __name__ == '__main__':
    unittest.main()
