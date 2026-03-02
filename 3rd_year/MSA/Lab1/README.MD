# FAMCS MSA Lab1

## English Version

**Topic:** Exploratory Data Analysis (EDA)  
**Dataset:** [StudentsPerformance.csv](https://www.kaggle.com/datasets/sadiajavedd/students-academic-performance-dataset/data)

### Objectives

1. Missing value analysis  
2. Outlier detection  
3. Normality testing  
4. Correlation analysis  

---

### 1. Missing Values

```python
df.isnull().sum()
```

Result: No missing values found.

---

### 2. Outliers (IQR Method)

Formula:

```
IQR = Q3 − Q1
Lower = Q1 − 1.5 × IQR
Upper = Q3 + 1.5 × IQR
```

Lower outliers were detected, but they represent valid low student scores.
No removal was performed.

---

### 3. Normality Testing

Data was standardized:

`z = (x − μ) / σ`

Tests used:
- Shapiro–Wilk
- Kolmogorov–Smirnov

Result:
Distributions are visually close to normal, but statistical tests reject normality (p < 0.05).

---

### 4. Correlation Analysis

Pearson correlation coefficient was computed.

Result:
- Strong positive correlations between numeric features
- Highest correlation between reading score and writing score

---

## Русская версия

**Тема**: Предварительный анализ данных (EDA)
**Датасет**: [StudentsPerformance.csv](https://www.kaggle.com/datasets/sadiajavedd/students-academic-performance-dataset/data)

### Задачи
- Анализ пропусков
- Анализ выбросов
- Проверка на нормальность
- Корреляционный анализ

### 1. Пропуски

```python
df.isnull().sum()
```

Пропущенные значения отсутствуют.

### 2. Выбросы

Формула:

```
IQR = Q3 − Q1
Lower = Q1 − 1.5 × IQR
Upper = Q3 + 1.5 × IQR
```

Метод IQR выявил нижние выбросы, однако они допустимы (низкие оценки).
Удаление не производилось.

---

### 3. Нормальность

Проведена стандартизация и применены критерии Шапиро–Уилка и Колмогорова–Смирнова.

`z = (x − μ) / σ`

Статистически нормальность не подтверждена.

---

### 4. Корреляция

- Все числовые признаки положительно коррелируют.
- Максимальная связь между reading score и writing score.
