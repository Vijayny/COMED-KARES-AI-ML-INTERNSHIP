# Netflix Data Analysis using Python

## 📚 Project Overview
This project analyzes the Netflix Movies and TV Shows dataset using Python. It demonstrates data cleaning, visualization, grouping, and sentiment analysis.

---

# Libraries Used

```python
import numpy as np
import pandas as pd
import plotly.express as px
from textblob import TextBlob
import kagglehub
```

### 1. NumPy
- Used for numerical operations.
- Imported as:
  ```python
  import numpy as np
  ```

### 2. Pandas
- Used for loading and manipulating datasets.
- Functions used:
  - `read_csv()`
  - `head()`
  - `tail()`
  - `shape`
  - `columns`
  - `groupby()`
  - `fillna()`
  - `rename()`
  - `sort_values()`

### 3. Plotly Express
Used for interactive graphs.

Graphs created:
- Pie Chart
- Bar Chart
- Line Chart

Example:
```python
px.pie()
px.bar()
px.line()
```

### 4. TextBlob
Used for Sentiment Analysis.

```python
TextBlob(text).sentiment.polarity
```

Sentiments:
- Positive
- Neutral
- Negative

### 5. KaggleHub
Used to download the Netflix dataset.

```python
kagglehub.dataset_download()
```

---

# Dataset

Dataset:
**Netflix Shows Dataset**

Contains information such as:
- Title
- Type
- Director
- Cast
- Country
- Rating
- Release Year
- Description

---

# Data Exploration

Useful commands:

```python
df.shape
df.head()
df.tail()
df.columns
```

---

# Data Cleaning

Missing values handled using:

```python
fillna()
```

Examples:
- Missing directors
- Missing cast

---

# Analysis Performed

## 1. Content Rating Distribution
Grouped by:

```python
rating
```

Visualization:
- Pie Chart

---

## 2. Netflix Content by Country

Grouped by:

```python
country
```

Visualization:
- Pie Chart

---

## 3. Top Directors

Steps:
- Split multiple directors
- Convert to DataFrame
- Group by director
- Count total shows
- Sort descending
- Display Top Directors

Visualization:
- Horizontal Bar Chart

---

## 4. Top Actors

Steps:
- Split cast names
- Group by actor
- Count appearances
- Display Top Actors

Visualization:
- Horizontal Bar Chart

---

## 5. Content Trend by Year

Grouped using:
- Release Year
- Type

Visualization:
- Line Chart

Shows:
- Movies released each year
- TV Shows released each year

---

## 6. Sentiment Analysis

Description column analyzed using:

```python
TextBlob
```

Categories:
- Positive
- Neutral
- Negative

Visualization:
- Bar Chart

---

# Plotly Charts Used

## Pie Chart

```python
px.pie()
```

Used for:
- Rating Distribution
- Country Distribution

---

## Bar Chart

```python
px.bar()
```

Used for:
- Top Directors
- Top Actors
- Sentiment Analysis

---

## Line Chart

```python
px.line()
```

Used for:
- Content Production Trend

---

# Pandas Functions Used

- read_csv()
- head()
- tail()
- shape
- columns
- groupby()
- reset_index()
- rename()
- fillna()
- sort_values()
- stack()

---

# Project Workflow

1. Import Libraries
2. Download Dataset
3. Load Dataset
4. Explore Dataset
5. Clean Missing Values
6. Analyze Ratings
7. Analyze Countries
8. Find Top Directors
9. Find Top Actors
10. Analyze Release Trends
11. Perform Sentiment Analysis
12. Visualize Results

---

# Skills Learned

- Data Loading with Pandas
- Data Cleaning
- Data Manipulation
- Grouping and Aggregation
- Interactive Visualization with Plotly
- Sentiment Analysis using TextBlob
- Working with Real-world Datasets
- Basic Exploratory Data Analysis (EDA)

---

# Conclusion

This project demonstrates the complete workflow of Exploratory Data Analysis (EDA) on the Netflix dataset. It includes data preprocessing, visualization, trend analysis, and sentiment analysis to gain meaningful insights from the data.
