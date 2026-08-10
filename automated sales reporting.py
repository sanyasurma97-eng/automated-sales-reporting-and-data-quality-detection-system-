import sqlite3
import pandas as pd
from datetime import datetime

def load_data():
    data = {
        "order_id": [1,2,3,4,5,6],
        "date": ["2026-08-07","2026-08-07","2026-08-08","2026-08-08","2026-08-08","2026-08-08"],
        "city": ["Delhi","Mumbai","Delhi","Pune","Mumbai","Delhi"],
        "product": ["Laptop","Phone","Tablet","Laptop","Phone","Tablet"],
        "amount": [50000,20000,15000,50000,"ERROR",15000],  # <-- Intentional error
        "status": ["Success","Success","Failed","Success","Success","Failed"]
    }

    df = pd.DataFrame(data)

    conn = sqlite3.connect("sales.db")
    df.to_sql("orders", conn, if_exists="replace", index=False)

    return conn


def run_queries(conn):
    print("\n--- Running Business Queries ---")

    try:
        q1 = "SELECT SUM(amount) as total_sales FROM orders"
        result1 = pd.read_sql_query(q1, conn)
        print("\nTotal Sales:\n", result1)

        
        q2 = "SELECT city, SUM(amount) as total FROM orders GROUP BY city"
        result2 = pd.read_sql_query(q2, conn)
        print("\nSales by City:\n", result2)

        
        q3 = """
        SELECT product, SUM(amount) as total
        FROM orders
        GROUP BY product
        ORDER BY total DESC
        LIMIT 1
        """
        result3 = pd.read_sql_query(q3, conn)
        print("\nTop Product:\n", result3)

        return True

    except Exception as e:
        print("\n Query Failed:", e)
        return str(e)

def check_nulls(conn):
    q = "SELECT * FROM orders WHERE amount IS NULL"
    df = pd.read_sql_query(q, conn)

    if len(df) > 0:
        return " Null values found in 'amount' column"
    return None


def check_invalid_data(conn):
    
    q = "SELECT amount FROM orders"
    df = pd.read_sql_query(q, conn)

    for val in df['amount']:
        try:
            float(val)
        except:
            return f" Invalid value detected in amount column: {val}"

    return None


def check_columns(conn):
    q = "PRAGMA table_info(orders)"
    df = pd.read_sql_query(q, conn)

    columns = df['name'].tolist()

    if 'amount' not in columns:
        return "️ Column 'amount' is missing"

    return None
def diagnose_error(error):
    if "no such column" in error:
        return "Column missing → schema changed"
    elif "datatype" in error:
        return "Data type mismatch in column"
    else:
        return "Unknown error → check raw data"


def save_log(message):
    with open("log.txt", "a") as f:
        f.write(f"{datetime.now()} - {message}\n")


def main():
    print(" Starting Daily Sales Report System...")

    conn = load_data()

    result = run_queries(conn)

    print("\n--- Running Data Checks ---")

    null_check = check_nulls(conn)
    invalid_check = check_invalid_data(conn)
    column_check = check_columns(conn)

    if null_check:
        print(null_check)
        save_log(null_check)

    if invalid_check:
        print(invalid_check)
        save_log(invalid_check)

    if column_check:
        print(column_check)
        save_log(column_check)

    if result != True:
        diagnosis = diagnose_error(result)
        print("\n Diagnosis:", diagnosis)
        save_log(diagnosis)

    print("\n Process Completed")


if __name__ == "__main__":
    main()
