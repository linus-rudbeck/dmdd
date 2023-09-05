import pandas as pd
import requests
from sqlalchemy import create_engine

## Get one DF from API
def get_df_from_api(endpoint):
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    response = requests.get(f"{BASE_URL}{endpoint}")
    data = response.json()
    return pd.DataFrame(data)

## Format address from API
def format_address(row):
    address = row["address"]
    street = address["street"]
    suite = address["suite"]
    zipcode = address["zipcode"]
    city = address["city"]
    
    return f"{street} {suite}\n{zipcode} {city}"

## Save DF to MySQL
def save_df_to_mysql(df, table_name):
    connection_string = "mysql+mysqlconnector://root@localhost/dmdd_mdm_db"
    engine = create_engine(connection_string)
    connection = engine.connect()
    df.to_sql(table_name, connection, if_exists="replace", index=False, chunksize=50, method='multi')


## Get all DFs from API
df_users = get_df_from_api("/users")
df_posts = get_df_from_api("/posts")
df_comments = get_df_from_api("/comments")
print("Loaded from API")

## Clean users DF
df_users["formatted_address"] = df_users.apply(format_address, axis=1)
df_users.drop("company", axis=1, inplace=True)
df_users.drop("address", axis=1, inplace=True)


## Get from CSV
df_products = pd.read_csv("olist_products_dataset.csv")
print("Loaded from CSV")

## Get from MySQL
connection_string = "mysql+mysqlconnector://root@localhost/northwind"
engine = create_engine(connection_string)
connection = engine.connect()
query = "SELECT * FROM customers"
df_customers = pd.read_sql(query, connection)
print("Loaded from MySQL")


## Save to CSV
df_users.to_csv("df_users.csv")
df_posts.to_csv("df_posts.csv")
df_comments.to_csv("df_comments.csv")
df_products.to_csv("df_products.csv")
df_customers.to_csv("df_customers.csv")
print("Saved to CSV")



## Save to MySQL
save_df_to_mysql(df_users, "df_users")
save_df_to_mysql(df_posts, "df_posts")
save_df_to_mysql(df_comments, "df_comments")
save_df_to_mysql(df_products, "df_products")
save_df_to_mysql(df_customers, "df_customers")
print("Saved to MySQL")