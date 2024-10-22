
import sqlite3
import pandas as pd

def generate_report():
    conn = sqlite3.connect('data/energy_data.db')
    query = "SELECT * FROM energy_usage"
    df = pd.read_sql(query, conn)
    
    report_file = 'data/report.csv'
    df.to_csv(report_file, index=False)
    print(f"Report generated: {report_file}")

if __name__ == "__main__":
    generate_report()
