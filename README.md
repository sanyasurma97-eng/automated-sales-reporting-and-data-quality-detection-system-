# automated-sales-reporting-and-data-quality-detection-system-

##  Project Overview
This project is a simple real-world simulation of a data analytics workflow where daily business reports are generated automatically using SQL, and data quality issues are detected using Python.

The main goal of this project is to not only run queries but also identify and diagnose problems in the data, such as invalid values, null entries, and schema changes.

---

## Objectives
- Automate daily sales reporting
- Execute SQL queries using Python
- Detect data quality issues
- Provide simple error diagnosis
- Simulate real-world data pipeline behavior

---

##  Tools & Technologies Used
- Python
- SQL (SQLite)
- Pandas
- File Handling (for logs)

---

##  Features
-  Runs business queries:
  - Total Sales
  - Sales by City
  - Top Selling Product

-  Data Quality Checks:
  - Detects null values
  - Detects invalid data types (e.g., text in numeric column)
  - Detects missing columns

-  Error Diagnosis:
  - Identifies cause of query failure
  - Provides readable error messages

-  Logging System:
  - Stores detected issues in `log.txt`

---

##  Workflow
1. Load dataset into SQLite database
2. Run SQL queries using Python
3. Perform data validation checks
4. Detect and report errors
5. Save logs for debugging

## Example Output
Total Sales: 150000
Sales by City: Delhi, Mumbai, Pune
Top Product: Laptop

Invalid value detected in amount column: ERROR
## Key Highlight

The system can detect incorrect data (like text in numeric columns) even when SQL queries do not fail.

This simulates real-world scenarios where bad data can silently affect reports.

## Learning Outcomes
SQL query writing
Python automation
Data validation techniques
Error handling and debugging
Real-world data pipeline thinking
## Future Improvements
Add email alerts for failures
Connect with Power BI dashboard
Use AI/ML for advanced anomaly detection
Automate using scheduler (cron/Task Scheduler)
## Author

Sanya Surma



### 1. Install Required Library
```bash
pip install pandas
