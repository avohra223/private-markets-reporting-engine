from pathlib import Path
import pandas as pd


SHEETS = ["Funds", "Investors", "Commitments", "Transactions", "NAV_Quarterly"]


def load_workbook():
    base_path = Path(__file__).resolve().parent.parent
    file_path = base_path / "data" / "Private Markets Data and Reporting.xlsx"

    print(f"Loading workbook from: {file_path}")

    data = {}
    for sheet in SHEETS:
        data[sheet] = pd.read_excel(file_path, sheet_name=sheet)

    return data


def control_summary(data):
    print("\n--- CONTROL SUMMARY ---")

    funds = data["Funds"]
    investors = data["Investors"]
    commitments = data["Commitments"]
    transactions = data["Transactions"]

    print(f"Funds loaded: {len(funds)}")
    print(f"Investors loaded: {len(investors)}")
    print(f"Commitments loaded: {len(commitments)}")
    print(f"Transactions loaded: {len(transactions)}")

    total_txn_local = transactions["Amount_Local"].sum()
    print(f"Total transaction volume (local currency): {total_txn_local:,.2f}")


def main():
    print("Private Markets Reporting Engine\n")

    data = load_workbook()
    control_summary(data)


if __name__ == "__main__":
    main()
