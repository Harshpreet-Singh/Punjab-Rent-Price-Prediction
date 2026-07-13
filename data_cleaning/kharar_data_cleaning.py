import pandas as pd 
df = pd.read_csv('./data/kharar_combine.csv')

df.rename(columns={
    "_1DNjI href": "url",
    "_3vnjf src": "image_url",
    "_2Ks63": "price",
    "YBbhy": "property_details",
    "_2poNJ": "title",
    "_2VQu4": "location",
    "_2jcGx": "posted",
}, inplace=True)
# print(df.head())    # to check if columns are renamed

df.drop(columns=["url", "image_url", "posted"], inplace=True)

df[['bhk', 'bathroom', 'area']] = df['property_details'].str.split(' - ', expand=True)
df.drop(columns=['property_details'], inplace=True)

df["price"] = (
    df["price"]
      .str.replace("₹", "", regex=False)
      .str.replace(",", "", regex=False)
      .str.strip()
)
df['price'] = df['price'].astype("Int64")

df["bhk"] = df["bhk"].str.replace("4+ BHK", "4 BHK", regex=False)
df["bhk"] = df["bhk"].str.replace(" BHK", "", regex=False)
df["bhk"] = df["bhk"].astype("Int64")

df["bathroom"] = df["bathroom"].str.replace("4+ Bathroom", "4 Bathroom", regex=False)
df["bathroom"] = df["bathroom"].str.replace(" Bathroom", "", regex=False)
df["bathroom"] = df["bathroom"].astype("Int64")

df['area'] = df['area'].str.replace(" sqft", "", regex=False)
df["area"] = df['area'].astype("Int64")

df.dropna(subset=['bhk'], inplace=True)
df.drop_duplicates(inplace=True)

df = df[(df["area"] > 0) & (df["area"] <= 10000)]
sale_keywords = "sale|sell|ready to move|cr|crore|lakh"
df = df[~df["title"].str.contains(sale_keywords, case=False, na=False)]
df = df[df["price"] < 100000]   # Remove prices >= ₹1 lakh

print(df.head())

df.to_csv('data/kharar_cleaned_data.csv',  index=False)
