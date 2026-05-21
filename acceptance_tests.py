import pytest
import tempfile
import os
from finance_dashboard import FinanceDashboard

def test_criterion_1_module_exists():
    from finance_dashboard import FinanceDashboard
    assert True

def test_criterion_2_add_transaction():
    dashboard = FinanceDashboard()
    dashboard.add_transaction(100, "income")
    dashboard.add_transaction(50, "expense")
    assert len(dashboard.ledger) == 2
    assert dashboard.ledger[0]["amount"] == 100
    assert dashboard.ledger[1]["category"] == "expense"

def test_criterion_3_generate_report():
    dashboard = FinanceDashboard()
    dashboard.add_transaction(1000, "income")
    dashboard.add_transaction(200, "expense")
    report = dashboard.generate_report()
    assert "income" in report
    assert "expenses" in report
    assert report["income"] == 1000
    assert report["expenses"] == 200

def test_criterion_4_save_report():
    dashboard = FinanceDashboard()
    dashboard.add_transaction(100, "income")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp:
        dashboard.save_report(tmp.name)
        tmp_path = tmp.name
    assert os.path.exists(tmp_path)
    with open(tmp_path, "r") as f:
        content = f.read()
        assert "income" in content
    os.remove(tmp_path)
