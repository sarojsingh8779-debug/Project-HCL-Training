"""
Water Usage and Conservation Analysis
Case study: Green Valley Residential Society

The dataset contains illustrative daily water-use estimates.
Replace the CSV values with verified readings when available.
"""

from pathlib import Path
import numpy as np
import pandas as pd


def load_data(file_path):
    """Load and validate the water-usage CSV file."""
    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}\n"
            "Keep water_usage_data.csv in the same folder as this Python file."
        )

    df = pd.read_csv(file_path)

    required_columns = {"Category", "Daily_Usage_Litres"}
    if not required_columns.issubset(df.columns):
        raise ValueError(
            "CSV must contain the columns: Category, Daily_Usage_Litres"
        )

    df["Daily_Usage_Litres"] = pd.to_numeric(
        df["Daily_Usage_Litres"], errors="coerce"
    )

    if df["Daily_Usage_Litres"].isna().any():
        raise ValueError("Water usage values must all be valid numbers.")
    if (df["Daily_Usage_Litres"] < 0).any():
        raise ValueError("Water usage cannot be negative.")

    return df


def analyse_water_usage(df, residents=450, saving_rate=0.10):
    """Calculate totals, averages, category shares and saving estimates."""
    usage = df["Daily_Usage_Litres"].to_numpy(dtype=float)

    total_usage = np.sum(usage)
    average_usage = np.mean(usage)
    highest_index = int(np.argmax(usage))
    lowest_index = int(np.argmin(usage))
    per_resident = total_usage / residents if residents > 0 else 0
    potential_saving = total_usage * saving_rate
    usage_after_saving = total_usage - potential_saving

    results = df.copy()
    results["Usage_Percentage"] = (
        results["Daily_Usage_Litres"] / total_usage * 100
        if total_usage > 0 else 0
    )

    print("\n========== WATER USAGE DATA ==========")
    print(df.to_string(index=False))

    print("\n========== ANALYSIS RESULTS ==========")
    print(f"Total daily water usage: {total_usage:,.0f} litres")
    print(f"Average usage per category: {average_usage:,.2f} litres")
    print(
        "Highest-use category: "
        f"{df.loc[highest_index, 'Category']} "
        f"({usage[highest_index]:,.0f} litres)"
    )
    print(
        "Lowest-use category: "
        f"{df.loc[lowest_index, 'Category']} "
        f"({usage[lowest_index]:,.0f} litres)"
    )
    print(f"Water usage per resident per day: {per_resident:,.2f} litres")

    print("\n========== CATEGORY-WISE PERCENTAGE ==========")
    print(results[["Category", "Usage_Percentage"]].to_string(index=False,
          formatters={"Usage_Percentage": "{:.2f}%".format}))

    print("\n========== CONSERVATION ESTIMATE ==========")
    print(f"Possible saving at {saving_rate:.0%}: {potential_saving:,.0f} litres/day")
    print(f"Usage after saving: {usage_after_saving:,.0f} litres/day")
    print(f"Estimated saving in 30 days: {potential_saving * 30:,.0f} litres")

    return results


def main():
    # Society assumptions used in this project
    residents = 450
    saving_rate = 0.10

    dataset_file = Path(__file__).resolve().parent / "water_usage_data.csv"

    try:
        water_df = load_data(dataset_file)
        analyse_water_usage(
            water_df,
            residents=residents,
            saving_rate=saving_rate
        )
    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
