import pandas as pd
from pandas import DataFrame

books = [
    [101, "To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"],
    [102, "1984", "George Orwell", 1949, "Dystopian"],
    [103, "Moby Dick", "Herman Melville", 1851, "Adventure"],
    [104, "War and Peace", "Leo Tolstoy", 1869, "Historical"],
    [105, "The Catcher in the Rye", "J.D. Salinger", 1951, "Coming-of-Age"]
]

df = DataFrame(data=books, columns=["id", "title", "author", "published", "genre"])

df.to_excel("my_excel.xlsx")