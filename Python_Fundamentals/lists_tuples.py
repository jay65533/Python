capitals = {"svk":"Bratislava","deu":"Berlin", "dnk":"Copenhagen"}
# creating a new key/value pair
capitals["abc"] = "New Country" 
# updating
capitals["abc"] = "ABC Country"
#to print all keys
for data in capitals:
     print(data)
#another way to print all keys
for key in capitals.keys():
     print(key)
#to print the values
for val in capitals.values():
     print(val)
#to print all keys and values
for key, val in capitals.items():
     print(key, " = ", val)
