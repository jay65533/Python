from flask import Flask, render_template, request, redirect
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
import copy
app = Flask(__name__)
    
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'

# now, we may invoke the query_db method
#friends = mysql.query_db("SELECT * FROM friends;")
#print("all the users", mysql.query_db("SELECT * FROM friends;"))

@app.route('/') 
def index():
    
    mysql = connectToMySQL('lead_gen_business')
    leads = mysql.query_db("SELECT clients.first_name, clients.last_name, COUNT(leads.leads_id) FROM clients INNER JOIN sites ON clients.client_id = sites.client_id INNER JOIN leads ON leads.site_id = sites.site_id GROUP BY clients.client_id;")
    
    total = 0

    for i in leads:
        total += int(i['COUNT(leads.leads_id)'])
    leads2 = copy.deepcopy(leads)
    #for i in leads2:
    #    i['COUNT(leads.leads_id)'] = str(int(i['COUNT(leads.leads_id)'])/ total * 100)
    
    print(leads)
    print('***************************************************************************')
    print(leads2)
    print(total)
    return render_template("index.html", leads = leads, leads2 = leads2)

if __name__ == "__main__":
    app.run(debug=True)