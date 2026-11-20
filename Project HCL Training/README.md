# Water Usage and Conservation Analysis

## 1. Project overview
This Python project analyses daily water use in a fictional residential society named **Green Valley Residential Society**. It uses Python, NumPy and Pandas to calculate water consumption and estimate possible conservation savings.

## 2. Society assumptions
- Number of flats: 100
- Number of residents: 450
- Daily water supply / usage represented in the sample dataset: 50,000 litres

The figures are illustrative assumptions for a college project. They are not actual meter readings from a real society.

## 3. Files in this folder
- `water_usage_analysis.py` — main Python program.
- `water_usage_data.csv` — sample dataset used by the program.
- `requirements.txt` — Python libraries required to run the program.
- `README.md` — project setup and usage instructions.

## 4. Software requirements
- Python 3.9 or later
- Visual Studio Code, IDLE, or another Python editor
- NumPy
- Pandas

## 5. Installation
Open this project folder in VS Code. Open the terminal using **Terminal > New Terminal** and run:

```bash
python -m pip install -r requirements.txt
```

If the `python` command does not work on Windows, try:

```bash
py -m pip install -r requirements.txt
```

## 6. How to run
Make sure `water_usage_analysis.py` and `water_usage_data.csv` are in the same folder.

In the VS Code terminal, run:

```bash
python water_usage_analysis.py
```

Or, on Windows if needed:

```bash
py water_usage_analysis.py
```

The program prints:
1. The input dataset.
2. Total daily water usage.
3. Average water use per category.
4. Highest- and lowest-use categories.
5. Estimated daily usage per resident.
6. Percentage share of each category.
7. Estimated savings if usage is reduced by 10%.

## 7. Dataset description
The CSV has two columns:
- `Category` — water-use category.
- `Daily_Usage_Litres` — estimated daily usage in litres.

| Category | Daily usage |
|---|---:|
| Drinking and Cooking | 5,000 L |
| Bathrooms and Toilets | 20,000 L |
| Laundry | 8,000 L |
| Kitchen Cleaning | 4,000 L |
| Gardening | 7,000 L |
| Common-area Cleaning | 6,000 L |
| **Total** | **50,000 L** |

## 8. Changing the dataset
You can edit the values in `water_usage_data.csv` using Excel or a text editor. Keep the column names unchanged and enter non-negative numeric values. The Python program reads the CSV automatically when it runs.

If the resident count or conservation target changes, edit the `residents` or `saving_rate` values near the bottom of `water_usage_analysis.py`. For example, `saving_rate = 0.10` means a 10% reduction target.

## 9. Libraries used
- **Pandas:** reads the CSV file and manages the tabular dataset.
- **NumPy:** performs numerical calculations such as total, mean, maximum and minimum.
- **Python:** controls the program flow, validates input and displays results.

## 10. Limitations and future improvements
- The sample dataset is hypothetical and should be replaced with verified readings for real-world decisions.
- The program analyses daily totals; it does not connect to live water meters.
- Future versions could store readings over time, compare months, or accept household-level records.
