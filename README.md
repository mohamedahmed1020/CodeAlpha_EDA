# CodeAlpha - Exploratory Data Analysis (EDA)

## 📌 Project Overview
This project is the second task of the **CodeAlpha Data Analytics Internship**. Building upon the dataset scraped in Task 1 (`books_dataset.csv`), this analysis explores data structure, checks data quality, uncovers pricing and rating patterns, and statistically tests the relationship between book prices and customer ratings.

## ❓ Key Questions Explored
1. **Data Quality:** Are there missing values, duplicate records, or structural anomalies?
2. **Price Distribution:** What is the average, median, and spread (IQR) of book prices?
3. **Rating Patterns:** How are customer star ratings (1 to 5) distributed across the catalog?
4. **Hypothesis Testing:** Does a higher book price correlate with a higher star rating?
5. **Extremes & Inventory:** Which books represent the highest and lowest price points, and what is the stock availability status?

## 🛠️ Tools & Libraries Used
- **Python 3**
- **Pandas & NumPy:** For data manipulation, grouping, and descriptive statistics.
- **SciPy (`scipy.stats`):** For Pearson correlation and hypothesis testing.

## 🔍 Key Findings
- **Zero Missing Data:** The scraped dataset is 100% complete with no null values or duplicate entries.
- **No Price-Rating Correlation:** Statistical testing (`Pearson r` close to 0, `p-value > 0.05`) confirms that expensive books do not necessarily receive higher customer ratings.
- **Stock Availability:** 100% of the analyzed catalog items are currently listed as "In stock".

## 🚀 How to Run
1. Ensure `books_dataset.csv` is in the project directory.
2. Install required libraries: `pip install pandas numpy scipy`
3. Run the script: `python eda_analysis.py`
