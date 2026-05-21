import pytest
import os
import json
import sys

# Ensure the project directory is in the path
sys.path.insert(0, '/workspace/projects/LocalFinanceDashboard')

def test_criterion_1_module_exists():
    """Criterion 1: finance_dashboard module exists and can be imported."""
    try:
        import finance_dashboard
    except ImportError:
        pytest.fail("finance_dashboard module could not be imported")

def test_criterion_2_add_transaction():
    """Criterion 2: add_transaction function updates the ledger correctly."""
    import finance_dashboard
    ledger = {"transactions": []}
    transaction = {"type": "income", "amount": 100, "date": "2023-01-01"}
    finance_dashboard.add_transaction(ledger, transaction)
    assert ledger['transactions'] == [transaction], "Ledger was not updated correctly"

def test_criterion_3_generate_report():
    """Criterion 3: generate_report function returns a summary dict of income/expenses."""
    import finance_dashboard
    ledger = {
        "transactions": [
            {"type": "income", "amount": 100},
            {"type": "expense", "amount": 50}
        ]
    }
    report = finance_dashboard.generate_report(ledger)
    assert isinstance(report, dict), "Report is not a dict"
    assert 'total_income' in report, "Report missing total_income"
    assert 'total_expenses' in report, "Report missing total_expenses"
    assert report['total_income'] == 100, "Total income incorrect"
    assert report['total_expenses'] == 50, "Total expenses incorrect"

def test_criterion_4_save_report():
    """Criterion 4: save_report function writes a report to a file."""
    import finance_dashboard
    import tempfile
    
    ledger = {"transactions": [{"type": "income", "amount": 200}]}
    
    with tempfile.NamedTemporaryFile(suffix='.json', delete=False, dir='/tmp') as f:
        filename = f.name
        
    try:
        finance_dashboard.save_report(ledger, filename)
        assert os.path.exists(filename), "Report file does not exist"
        with open(filename, 'r') as f:
            content = json.load(f)
        assert 'total_income' in content, "Report file does not contain total_income"
    finally:
        if os.path.exists(filename):
            os.remove(filename)
