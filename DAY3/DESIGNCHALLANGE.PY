# NumPy + Pandas Final Capstone

## 🎯 Objective
Create a DataFrame of **5 students** with the following columns:

- Name
- Python Marks
- AI Marks
- ML Marks

Using **NumPy** and **Pandas**, perform the following tasks.

---

# 📚 Requirements

## 1. Import Required Libraries

```python
import numpy as np
import pandas as pd
```

---

## 2. Create Student Names

```python
names = ["Vijay", "Rahul", "Sneha", "Priya", "Arjun"]
```

---

## 3. Generate Random Marks

Generate random marks between **60 and 100** for three subjects.

```python
np.random.seed(1)

marks = np.random.randint(
    60, 101, (5, 3)
)
```

### Explanation

- `np.random.seed(1)` ensures the same random numbers every time.
- `np.random.randint(60,101,(5,3))`
  - Minimum = 60
  - Maximum = 100
  - 5 Students
  - 3 Subjects

---

## 4. Create a DataFrame

```python
df = pd.DataFrame(
    marks,
    columns=["Python", "AI", "ML"]
)

df.insert(0, "Name", names)
```

### Output

| Name | Python | AI | ML |
|------|---------|----|----|
| Vijay | 97 | 72 | 68 |
| Rahul | 69 | 71 | 65 |
| Sneha | 75 | 60 | 76 |
| Priya | 61 | 72 | 67 |
| Arjun | 66 | 85 | 100 |

---

## 5. Calculate Average Marks

```python
df["Average"] = df[
    ["Python", "AI", "ML"]
].mean(axis=1)
```

### Explanation

`axis=1` means calculate the average across each row (student).

---

## 6. Add Result Column

If Average is **75 or more**, Result = **Pass**

Otherwise Result = **Fail**

```python
df["Result"] = np.where(
    df["Average"] >= 75,
    "Pass",
    "Fail"
)
```

---

## 7. Display Final DataFrame

```python
print(df)
```

Example Output

| Name | Python | AI | ML | Average | Result |
|------|---------|----|----|---------|--------|
| Vijay | 97 | 72 | 68 | 79.00 | Pass |
| Rahul | 69 | 71 | 65 | 68.33 | Fail |
| Sneha | 75 | 60 | 76 | 70.33 | Fail |
| Priya | 61 | 72 | 67 | 66.67 | Fail |
| Arjun | 66 | 85 | 100 | 83.67 | Pass |

---

## 8. Find the Topper

```python
topper = df.loc[
    df["Average"].idxmax()
]

print("Topper :", topper["Name"])
```

### Explanation

- `idxmax()` returns the index of the highest average.
- `loc[]` retrieves the entire row.

---

# 💻 Complete Program

```python
import numpy as np
import pandas as pd

# Student Names
names = ["Vijay", "Rahul", "Sneha", "Priya", "Arjun"]

# Generate Random Marks
np.random.seed(1)
marks = np.random.randint(60, 101, (5, 3))

# Create DataFrame
df = pd.DataFrame(
    marks,
    columns=["Python", "AI", "ML"]
)

df.insert(0, "Name", names)

# Average Marks
df["Average"] = df[
    ["Python", "AI", "ML"]
].mean(axis=1)

# Result Column
df["Result"] = np.where(
    df["Average"] >= 75,
    "Pass",
    "Fail"
)

# Display DataFrame
print("Final DataFrame")
print(df)

# Find Topper
topper = df.loc[df["Average"].idxmax()]

print("\nTopper Details")
print("Name :", topper["Name"])
print("Average :", round(topper["Average"], 2))
```

---

# 📖 Functions Used

| Function | Description |
|----------|-------------|
| `np.random.seed()` | Generates the same random values every run |
| `np.random.randint()` | Generates random integers |
| `pd.DataFrame()` | Creates a DataFrame |
| `insert()` | Inserts a column at a specified position |
| `mean(axis=1)` | Calculates row-wise average |
| `np.where()` | Applies conditional logic |
| `idxmax()` | Finds the index of the maximum value |
| `loc[]` | Retrieves a row using its index |

---

# 🎯 Learning Outcomes

After completing this project, you will be able to:

- Import and use NumPy and Pandas.
- Generate random data using NumPy.
- Create DataFrames in Pandas.
- Add and manipulate DataFrame columns.
- Calculate averages.
- Apply conditional logic with `np.where()`.
- Find the topper using `idxmax()`.
- Display and analyze tabular data.

---

# ✅ Capstone Tasks Checklist

- ✔ Import NumPy and Pandas
- ✔ Generate random marks
- ✔ Create a DataFrame
- ✔ Calculate average marks
- ✔ Add Result column
- ✔ Display the DataFrame
- ✔ Find and print the topper
