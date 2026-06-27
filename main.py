import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

dataset = pd.read_excel("HousePricePrediction.xlsx")

#1

print(dataset.shape)

#2

object_cols = dataset.select_dtypes(include=['object']).columns
print("Categorical variables:", len(object_cols))

int_cols = dataset.select_dtypes(include=['int64']).columns
print("Integer variables:", len(int_cols))

float_cols = dataset.select_dtypes(include=['float64']).columns
print("Floatvariables:", len(float_cols))

#3

numerical_dataset = dataset.select_dtypes(include=['int64', 'float64'])
plt.figure(figsize=(12,6))
sns.heatmap(numerical_dataset.corr(),
            cmap= 'BrBG',
            fmt='.2f',
            linewidths=2,
            annot=True)
plt.title("Correlation Heatmap of Numerical Features")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
print("Heatmap saved as correlation_heatmap.png")

#4

unique_values = []
for col in object_cols:
    unique_values.append(dataset[col].unique().size)
plt.figure(figsize=(10,6))
plt.title('No. Unique values of Categorical Features')
plt.xticks(rotation=90)
sns.barplot(x=object_cols,y=unique_values)

plt.show()