
def average_sales_by_city(df):
    return df.groupby("city")["sales"].mean()

    return df.groupby("city")["sales"].sum().sort_values(ascending=False)

 main
