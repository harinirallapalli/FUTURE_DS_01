import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_style('whitegrid')


def save_chart(fig, filename):

    os.makedirs('output/charts', exist_ok=True)

    fig.savefig(f'output/charts/{filename}',
                bbox_inches='tight')

    print(f'Chart Saved: {filename}')


def plot_sales_by_region(data):

    fig = plt.figure(figsize=(10, 6))

    data.plot(kind='bar', color='skyblue')

    plt.title('Sales by Region')
    plt.xlabel('Region')
    plt.ylabel('Sales')

    save_chart(fig, 'sales_by_region.png')


def plot_profit_by_region(data):

    fig = plt.figure(figsize=(10, 6))

    data.plot(kind='bar', color='orange')

    plt.title('Profit by Region')
    plt.xlabel('Region')
    plt.ylabel('Profit')

    save_chart(fig, 'profit_by_region.png')


def plot_sales_by_category(data):

    fig = plt.figure(figsize=(8, 5))

    data.plot(kind='pie', autopct='%1.1f%%')

    plt.title('Sales by Category')
    plt.ylabel('')

    save_chart(fig, 'sales_by_category.png')


def plot_monthly_sales(data):

    fig = plt.figure(figsize=(12, 6))

    data.plot(marker='o')

    plt.title('Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Sales')

    plt.xticks(rotation=45)

    save_chart(fig, 'monthly_sales_trend.png')


def plot_top_products(data):

    fig = plt.figure(figsize=(12, 6))

    data.plot(kind='barh', color='green')

    plt.title('Top 10 Products by Sales')
    plt.xlabel('Sales')
    plt.ylabel('Products')

    save_chart(fig, 'top_products.png')