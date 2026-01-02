import pandas as pd

# Read sales data
file_path = "data/sales_data.csv"
df = pd.read_csv(file_path)

# Data validation
df = df[(df['Quantity'] > 0) & (df['Price'] > 0)]

# Add Total column
df['Total'] = df['Quantity'] * df['Price']

# Generate summary report
summary = df.groupby('Product').agg({
'Quantity': 'sum',
'Total': 'sum'
}).reset_index()

# Save to Excel
output_path = "reports/sales_report.xlsx"
summary.to_excel(output_path, index=False)

print("Report generated successfully!")