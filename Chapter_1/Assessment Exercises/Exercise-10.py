# EXERCISE 10 - FILM DICTIONARY
 # Assigned a variable "film_dictionary" with the "key" : "value" pairs with the details of each movie
film_dictionary = { 
    'Movie Title': 'Titanic',
    'Director': 'James Cameron',
    'Budget':'$200 million',
    'Year':'1997',
    'Genre':'Romance/Adventure',
    'Rating': '7.9/10'
        
}
print("\n⛴---⛴---⛴---⛴---⛴---⛴---⛴---⛴---⛴---⛴\n")
# print the film details 
print("\nThe Film Details:\n")
# for loop iterating key-value pair in dictionary film from the assigned variable "film_dictionary" 
# using the method items() to view objects from the tuples in list
for key, value in film_dictionary.items():
    # print the "key" : "value" which are the items inside the dictionary
    print(f"{key}: {value}")
    
print("\n⛴---⛴---⛴---⛴---⛴---⛴---⛴---⛴---⛴---⛴")