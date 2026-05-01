# Cost of Living & Salary Analysis (Global Countries)

This project is a data analysis study of global cost of living vs income levels across countries.
It explores how salaries relate to living expenses and estimates a simple **quality of life index** based on economic indicators.

---

## Project Goals

- Analyze global cost of living differences between countries
- Compare average salaries with living expenses
- Identify countries with the best and worst affordability
- Visualize economic disparities across the world
- Build a simple quality of life indicator

---

## Dataset

The dataset includes worldwide cost-of-living indicators such as:

- Food prices (restaurants and groceries)
- Housing costs (rent and property prices)
- Transport costs
- Utilities and services
- Average monthly net salary (after tax)

Each row represents a country with multiple economic variables.

---

## Data Processing

- Missing values were handled using mean imputation
- Column names were renamed for better readability
- Features were grouped into categories:
  - Housing
  - Food
  - Transport
- A composite **cost of living index** was created

---

## Analysis Performed

### 1. Salary comparison across countries
Countries ranked by average monthly net salary.

### 2. Cost of living comparison
Countries ranked by estimated living expenses.

### 3. Salary vs cost of living relationship
- Scatter plot analysis
- Linear regression model
- R² score to measure correlation

### 4. Quality of life index
Defined as:

> quality_of_life = salary - cost_of_living

Used to rank countries by affordability.

### 5. Global visualization
- Interactive choropleth map showing quality of life by country
- Hover tooltips for country-level insights

---

## Visualizations

The project includes:

- Bar charts (country comparisons)
- Scatter plot (salary vs cost of living)
- Regression line with R² score
- Interactive world map (Plotly choropleth)

---

## Key Insights

- High salary does not always guarantee better quality of life
- Some countries with moderate salaries have better affordability
- Cost of living varies significantly worldwide


---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Plotly
- Scikit-learn

---

## Summary

This project demonstrates an end-to-end data analysis workflow:
data cleaning → feature engineering → visualization → insight generation.
