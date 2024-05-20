@echo off
pytest -v -s --alluredir=".\Reports" .\testCases\CI\Sanity\test_TC02_VerifyE2EFunctionalityForPODocumentType.py
timeout /T 10
pytest -v -s .\testCases\CI\Sanity\test_Completed.py
timeout /T 10
allure serve .\Reports
pause
