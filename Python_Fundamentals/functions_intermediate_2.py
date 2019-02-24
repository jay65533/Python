x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]["last_name"] = "Bryant"
print(students)

sports_directory["soccer"][0] = "Andres"
print(sports_directory)

z[0]['y'] = 30
print(z)

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(list):
    for i in range(len(students)):
        print("first_name" + " - " + students[i]['first_name'] + ", " + "last_name" + " - " + students[i]['last_name'])
iterateDictionary(students)

def iterateDictionary2(list):
    for i in range(len(students)):
        print(students[i]['first_name'])
iterateDictionary2(students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def iterateDojo(list):
    print('LOCATIONS')
    for i in range(len(dojo['locations'])):
        print(dojo['locations'][i])
    print('INSTRUCTORS')
    for i in range(len(dojo['instructors'])):
        print(dojo['instructors'][i])
iterateDojo(dojo)



