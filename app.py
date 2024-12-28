from flask import Flask, request, render_template
import pyodbc

# Retrieve the form data and insert it into the database
# def add_product(cursor, conn, product_id, product_name, quantity, price):
#     query =\
#         f'''INSERT INTO Products (product_id, name, quantity, price) 
#             VALUES ({product_id}, '{product_name}', {quantity}, {price})'''
#     cursor.execute(query)
#     conn.commit()

# # Retrieve the search name and perform a search in the database
# def search_product(cursor, keyword):
#     query =\
#         f'''SELECT * 
#             FROM Products 
#             WHERE name LIKE '%{keyword}%\''''
#     cursor.execute(query)
#     results = cursor.fetchall()
#     return results


app = Flask(__name__)

# Establish a connection to the SQL Server
DRIVER_NAME = 'SQL Server'
SERVER_NAME = 'OMAR-WAGIH'
conn = pyodbc.connect('Driver={SQL Server};'
                    'Server=OMAR-WAGIH;'
                    'Database=store;'
                    'Trusted_Connection=yes;')

# Create a cursor object to execute SQL queries
# cursor = conn.cursor()

@app.route('/')
def index():
    return render_template('index-home.html')

# @app.route('/submit_newProduct', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         product_id = request.form['productID']
#         product_name = request.form['productName']
#         quantity = request.form['quantity']
#         price = request.form['price']

#         add_product(cursor, conn, product_id, product_name, quantity, price)
#         return render_template('index-home.html')
    
# @app.route('/submit_search', methods=['GET'])
# def search():
#     if request.method == 'GET':
#         keyword = request.args.get('searchName')
#         results = search_product(cursor, keyword)
#         return render_template('results.html', search_results=results)

app.run(debug=True)

# Close the cursor and connection
cursor.close()
conn.close()