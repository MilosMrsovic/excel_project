import pandas as pd

def extract_files(file_name):
    return pd.read_excel(file_name)

def filter_user(data):
    mask = (pd.Timestamp.today() - data["rental_date"])> pd.Timedelta(days=31)
    return data[mask]
    
def sort_data(data):
    return data.sort_values(by="rental_date", ascending=True)

def add_new_column(data):
    data['overdue_days'] = (pd.Timestamp.today() - data['rental_date']).dt.days - 31
    return data

def remove(data):
    data = data.drop(['address', 'gender', 'city', 'active'], axis=1)
    return data

def extract_books(file_name):
    return pd.read_csv(file_name)

def merge_books(user_data):
    books_data = extract_books("books.csv")
    
    user_data["rental_book_name"] = None
    user_data["rental_book_author"] = None
    
    for i, row in user_data.iterrows():
        book_row = books_data[books_data["id"] == row["rental_book_id"]]
        if not book_row.empty:
            user_data.loc[i, "rental_book_name"] = book_row["title"].iloc[0]
            user_data.loc[i, "rental_book_author"] = book_row["author"].iloc[0]
            
    user_data.drop("rental_book_id",axis=1, inplace=True )      
    return user_data 
    

def load_data(data):
    data.to_excel("overdue_users.xlsx", index=False)
    
df = extract_files('baba.xlsx').pipe(filter_user). pipe(sort_data).pipe(add_new_column).pipe(remove).pipe(merge_books)
load_data(df)