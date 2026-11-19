import numpy as np
import pandas as pd
from scipy import stats # type: ignore

# 1. Load the dataset generated from Task 1
df = pd.read_csv('books_dataset.csv')

print('=' * 50)
print('1. DATASET STRUCTURE & OVERVIEW')
print('=' * 50)
print(f'Total Rows: {df.shape[0]}, Total Columns: {df.shape[1]}\n')
print('Data Types & Non-Null Counts:')
print(df.info())

print('\n' + '=' * 50)
print('2. DATA QUALITY CHECK (MISSING & DUPLICATES)')
print('=' * 50)
print('Missing Values per Column:\n', df.isnull().sum())
print(f'\nDuplicate Rows: {df.duplicated().sum()}')

print('\n' + '=' * 50)
print('3. DESCRIPTIVE STATISTICS (PRICES & RATINGS)')
print('=' * 50)
print(df[['Price_GBP', 'Rating']].describe().round(2))

# Calculate additional dispersion metrics for Price
price_median = df['Price_GBP'].median()
price_iqr = df['Price_GBP'].quantile(0.75) - df['Price_GBP'].quantile(0.25)
print(f'\nMedian Price: £{price_median:.2f}')
print(f'Price Interquartile Range (IQR): £{price_iqr:.2f}')

print('\n' + '=' * 50)
print('4. ANSWERING KEY ANALYTICAL QUESTIONS')
print('=' * 50)

# Q1: Rating Distribution
print('\n--- Q1: Distribution of Star Ratings ---')
rating_counts = df['Rating'].value_counts().sort_index()
rating_pct = (
    df['Rating'].value_counts(normalize=True).sort_index() * 100
).round(2)
rating_summary = pd.DataFrame({'Count': rating_counts, 'Percentage (%)': rating_pct})
print(rating_summary)

# Q2: Average Price per Rating Tier
print('\n--- Q2: Average Price by Star Rating ---')
avg_price_by_rating = df.groupby('Rating')['Price_GBP'].agg(
    ['count', 'mean', 'median', 'min', 'max']
).round(2)
print(avg_price_by_rating)

# Q3: Hypothesis Testing - Is there a correlation between Price and Rating?
# H0: There is no linear correlation between book price and star rating.
# H1: There is a significant linear correlation between book price and star rating.
corr_coef, p_value = stats.pearsonr(df['Price_GBP'], df['Rating'])
print('\n--- Q3: Hypothesis Test (Price vs. Rating Correlation) ---')
print(f'Pearson Correlation Coefficient (r): {corr_coef:.4f}')
print(f'P-value: {p_value:.4f}')
if p_value < 0.05:
    print(
        'Result: Statistically significant correlation exists (Reject H0).'
    )
else:
    print(
        'Result: No statistically significant correlation (Fail to reject H0).'
    )

# Q4: Top 5 Most Expensive & Cheapest Books
print('\n--- Q4: Top 5 Most Expensive Books ---')
print(
    df.nlargest(5, 'Price_GBP')[['Title', 'Price_GBP', 'Rating']].to_string(
        index=False
    )
)

print('\n--- Top 5 Cheapest Books ---')
print(
    df.nsmallest(5, 'Price_GBP')[['Title', 'Price_GBP', 'Rating']].to_string(
        index=False
    )
)

# Q5: Stock Availability Breakdown
print('\n--- Q5: Stock Availability Breakdown ---')
print(df['Availability'].value_counts())

# Export a summary report to a text file for documentation
with open('eda_summary_report.txt', 'w', encoding='utf-8') as f:
    f.write('EXPLORATORY DATA ANALYSIS (EDA) SUMMARY REPORT\n')
    f.write('=' * 50 + '\n')
    f.write(f'Total Books Analyzed: {len(df)}\n')
    f.write(
        f"Average Price: £{df['Price_GBP'].mean():.2f} (Median: £{price_median:.2f})\n"
    )
    f.write(
        f"Price Range: £{df['Price_GBP'].min():.2f} - £{df['Price_GBP'].max():.2f}\n"
    )
    f.write(f"Average Rating: {df['Rating'].mean():.2f} / 5.0\n")
    f.write(
        f'Price-Rating Correlation (r): {corr_coef:.4f} (p-value: {p_value:.4f})\n'
    )

print('\nAnalysis complete! Summary saved to eda_summary_report.txt')