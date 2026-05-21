import json
import os
import tempfile
import unittest
import sys

sys.path.insert(0, '/workspace/projects/LocalFinanceDashboard')

from finance_dashboard import add_transaction, generate_report, save_report, _ledger

class TestFinanceDashboard(unittest.TestCase):
    def setUp(self):
        _ledger.clear()

    def test_criterion_1_module_exists(self):
        import finance_dashboard
        self.assertIsNotNone(finance_dashboard)

    def test_criterion_2_add_transaction_updates_ledger(self):
        add_transaction(100, 'food', 'expense')
        self.assertEqual(len(_ledger), 1)
        self.assertEqual(_ledger[0]['amount'], 100)

    def test_criterion_3_generate_report_returns_summary(self):
        add_transaction(1000, 'salary', 'income')
        add_transaction(200, 'rent', 'expense')
        report = generate_report()
        self.assertIn('income', report)
        self.assertIn('expenses', report)
        self.assertEqual(report['income'], 1000)
        self.assertEqual(report['expenses'], 200)

    def test_criterion_4_save_report_writes_file(self):
        add_transaction(500, 'income', 'income')
        with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as f:
            filepath = f.name
        save_report(filepath)
        with open(filepath, 'r') as f:
            data = json.load(f)
        self.assertIn('income', data)
        os.unlink(filepath)

if __name__ == '__main__':
    unittest.main()
