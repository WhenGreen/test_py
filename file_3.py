from file_1 import load_data
from file_2 import total_sales_by_city

df = load_data()
result = total_sales_by_city(df)
print("Загальні продажі по містах:")
print(result)
