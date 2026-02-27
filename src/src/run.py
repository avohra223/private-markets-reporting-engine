from pathlib import Path
import pandas as pd

SHEETS = ["Funds", "Investors", "Commitments", "FX_Rates", "Transactions", "NAV_Quarterly"]

def load_workbook(xlsx_path: Path) -> dict[str, pd.DataFrame]:
    xl = pd.ExcelFile(xlsx_path)
    data = {}
    for s in SHEETS:
        data[s] = pd.read_excel(xl, sheet_name=s)
    return data

def main():
    print("Private Markets Reporting Engine")
    # later: accept path as argument; for now we’ll hardcode after we add /data
    print("Loaded module skeleton ✅")

if __name__ == "__main__":
    main()
