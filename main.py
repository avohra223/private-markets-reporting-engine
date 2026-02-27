import pandas as pd


def load_data(path):
    df = pd.read_excel(path)
    return df


def main():
    print("Private Markets Reporting Engine")
    print("Ingesting financial dataset...")

    file_path = "sample_data.xlsx"   # we will create this next
    df = load_data(file_path)

    print("Dataset loaded successfully.")
    print("Preview:")
    print(df.head())


if __name__ == "__main__":
    main()
