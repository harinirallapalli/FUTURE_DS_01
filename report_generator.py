import pandas as pd
import os


def generate_excel_report(df):

    os.makedirs('output/reports', exist_ok=True)

    output_file = (
        'output/reports/business_sales_report.xlsx'
    )

    with pd.ExcelWriter(output_file,
                        engine='xlsxwriter') as writer:

        df.to_excel(writer,
                    sheet_name='Cleaned Data',
                    index=False)

    print('Excel Report Generated Successfully')