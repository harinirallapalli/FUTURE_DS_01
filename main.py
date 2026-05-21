from data_loader import load_data, clean_data
from analysis import *
from visualization import *
from report_generator import generate_excel_report


def print_line():
    print("=" * 60)


def main():

    print_line()
    print("        BUSINESS SALES ANALYSIS REPORT PROJECT")
    print_line()

    # STEP 1 - LOAD DATASET
    print("\nStep 1: Loading Dataset...")

    file_path = 'Sample - Superstore.csv'

    df = load_data(file_path)

    if df is None:
        return

    # STEP 2 - CLEAN DATA
    print("\nStep 2: Cleaning Dataset...")

    before_rows = df.shape[0]

    df = clean_data(df)

    after_rows = df.shape[0]

    print("Duplicates Removed")
    print("Missing Values Removed")
    print("Date Columns Converted Successfully")

    print(f"\nDataset Shape: {df.shape}")

    # SALES SUMMARY
    print_line()
    print("                    SALES SUMMARY")
    print_line()

    total_sales_value = total_sales(df)

    total_profit_value = total_profit(df)

    print(f"\nTotal Sales  : {total_sales_value:,.2f}")
    print(f"Total Profit : {total_profit_value:,.2f}")

    # REGIONAL ANALYSIS
    print_line()
    print("                REGIONAL SALES ANALYSIS")
    print_line()

    sales_region = sales_by_region(df)

    print()

    for region, value in sales_region.items():
        print(f"{region:<10}: {value:,.2f}")

    # CATEGORY ANALYSIS
    print_line()
    print("               CATEGORY SALES ANALYSIS")
    print_line()

    sales_category = sales_by_category(df)

    print()

    for category, value in sales_category.items():
        print(f"{category:<17}: {value:,.2f}")

    # GENERATE CHARTS
    print_line()
    print("               GENERATING CHARTS")
    print_line()

    profit_region = profit_by_region(df)

    monthly_sales_data = monthly_sales(df)

    top_products_data = top_products(df)

    plot_sales_by_region(sales_region)
    print("✔ Sales by Region Chart Saved")

    plot_profit_by_region(profit_region)
    print("✔ Profit by Region Chart Saved")

    plot_sales_by_category(sales_category)
    print("✔ Sales by Category Chart Saved")

    plot_monthly_sales(monthly_sales_data)
    print("✔ Monthly Sales Trend Chart Saved")

    plot_top_products(top_products_data)
    print("✔ Top Products Chart Saved")

    print("\nCharts saved inside:")
    print("output/charts/")

    # GENERATE EXCEL REPORT
    print_line()
    print("               GENERATING EXCEL REPORT")
    print_line()

    generate_excel_report(df)

    print("\n✔ Excel Report Generated Successfully")

    print("\nSaved File:")
    print("output/reports/business_sales_report.xlsx")

    # TOP PRODUCTS
    print_line()
    print("                    TOP 10 PRODUCTS")
    print_line()

    print()

    for product in top_products_data.index:
        print(product)

    # PROJECT COMPLETED
    print_line()
    print("                 PROJECT COMPLETED")
    print_line()

    print("\nThank You for Using")
    print("Business Sales Analysis Report Project")


if __name__ == "__main__":
    main()
