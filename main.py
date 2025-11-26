import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")
df.info()
print(df.describe())
#определение количества пропусков
print(df.isnull().sum())

#исследуем на выбросы
numeric_cols = df.select_dtypes(include='number').columns  # выбираем только числовые колонки
for col in numeric_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    print(f"Выбросы в колонке {col}:")
    print(outliers)

    plt.figure(figsize=(6, 3))
    plt.boxplot(df[col], vert=False)
    plt.title(f"Boxplot для признака: {col}")
    plt.xlabel(col)
    plt.show()

