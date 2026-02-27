import pandas as pd

def load_data(path):
    df = pd.read_excel(path)
    return df

def main():
    print("Private Markets Reporting Engine")
    print("Ready to ingest financial dataset...")

if __name__ == "__main__":
    main()
