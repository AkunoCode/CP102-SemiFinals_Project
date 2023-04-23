code = '001'
new_code = input("\nEnter new game code (leave blank to keep current value): ")
if new_code == "/":
    
    print("Cancelled operation.\n")
    
name = input("Enter new game name (leave blank to keep current value): ")
if name == "/":
    
    print("Cancelled operation.\n")
    
publisher = input("Enter new game publisher (leave blank to keep current value): ")
if publisher == "/":
    
    print("Cancelled operation.\n")
    
genre = input("Enter new game genre (leave blank to keep current value): ")
if genre == "/":
    
    print("Cancelled operation.\n")
    
price = input("Enter new game price (ex. 800.00 or 799.90) (leave blank to keep current value): ")
if price == "/":
    
    print("Cancelled operation.\n")
    
year = input("Enter new game year of release (leave blank to keep current value): ")
if year == "/":
    
    print("Cancelled operation.\n")
    
update_query = "UPDATE Details SET "
query_list = []
params = []
if new_code:
    query_list.append("GameCode = %s")
    params.append(new_code)
if name:
    query_list.append("GameName = %s")
    params.append(name)
if publisher:
    query_list.append("GamePublisher = %s")
    params.append(publisher)
if genre:
    query_list.append("GameGenre = %s")
    params.append(genre)
if price:
    query_list.append("GamePrice = %s")
    params.append(price)
if year:
    query_list.append("GameYear = %s")
    params.append(year)
update_query += ", ".join(query_list)
update_query += " WHERE GameCode = %s"
params.append(code)
params = tuple(params)
cursor.execute(update_query, params)

# Print the query and params
