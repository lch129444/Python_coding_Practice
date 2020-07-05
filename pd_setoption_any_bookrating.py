import pandas as pd
import numpy as np

pd.set_option('precision', 1)
#the precision to be one decimal

books = pd.Series(data=['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine', 'Alice in Wonderland' ])
authors = pd.Series(data=['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll' ])
user_1 = pd.Series(data=[3.2, np.nan ,2.5])
#create some NaN
user_2 = pd.Series(data=[5., 1.3, 4.0, 3.8])
user_3 = pd.Series(data=[2.0, 2.3, np.nan, 4])
user_4 = pd.Series(data=[4, 3.5, 4, 5, 4.2])

dat = {'Book Title' : books,
       'Author' : authors,
       'User 1' : user_1,
       'User 2' : user_2,
       'User 3' : user_3,
       'User 4' : user_4}

book_ratings = pd.DataFrame(dat)
#create dataframe by dictionary of series

book_ratings.fillna(book_ratings.mean(), axis=0, inplace=True)
#fill with previous and after rows' mean

best_rated = book_ratings[(book_ratings == 5).any(axis=1)]['Book Title'].values
#best book is a book with rating 5 given by any user
#data.any if data exists in any column, true;return the related whole rows
#to create a dataframe, then pick title column to create ndarry, then retrieve the values only
print(best_rated)
