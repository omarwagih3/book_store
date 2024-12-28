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
cursor = conn.cursor()

def add_product_ordered(cursor, conn, order_custmer_email, order_book_id, order_quantity):
    query = \
        f'''exec InsertOrder '{order_custmer_email}', {order_book_id}, '{order_quantity}' '''
    cursor.execute(query)
    conn.commit()

def add_product_customer(cursor, conn, customer_name, customer_email, customer_phone):
    query = \
        f'''exec InsertCustomer '{customer_name}', '{customer_email}', '{customer_phone}' '''
    cursor.execute(query)
    conn.commit()

def add_product_auther(cursor, conn, author_name, author_bio):
    query = \
        f'''exec InsertAuthor '{author_name}','{author_bio}' '''
    cursor.execute(query)
    conn.commit()


def add_product_puplisher(cursor, conn, publishers_name, publishers_email):
    query = \
        f'''exec InsertPublisher '{publishers_name}', '{publishers_email}' '''
    cursor.execute(query)
    conn.commit()


def add_product_book(cursor, conn, book_title, book_genre, book_price, book_quantity, book_publisher, book_author):
    query = \
        f'''exec InsertBook '{book_title}', '{book_genre}', '{book_price}', '{book_quantity}', '{book_publisher}', '{book_author}' '''
    cursor.execute(query)
    conn.commit()

def get_data(table_name):
    cursor.execute(f'''SELECT * FROM {table_name}''')
    rows = cursor.fetchall()
    return rows
@app.route('/')
def index():
    return render_template('index-home.html')

@app.route('/index-author.html')
def index_author():
    authors = get_data("auther")
    return render_template('index-author.html',authors=authors)
    print (authors)

@app.route('/index-books.html')
def index_books():
    rows = get_data("books")
    return render_template('index-books.html',books=rows)

@app.route('/index-customers.html')
def index_customers():
    rows = get_data('customers')
    return render_template('index-customers.html',customers=rows)

@app.route('/index-orders.html')
def index_orders():
    rows = get_data('orders')
    return render_template('index-orders.html',orders=rows)

@app.route('/index-ordered-bks.html')
def index_ordered_bks():
    rows = get_data('ordered_bks')
    return render_template('index-ordered-bks.html',ordered_books=rows)

@app.route('/index-publishers.html')
def index_publishers():
    rows = get_data('publishers')
    return render_template('index-publishers.html',publishers=rows)



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

@app.route('/add_author', methods=['POST'])
def submit_author():
    if request.method == 'POST':  # method of send data
        author_name = request.form['author_name']
        author_bio = request.form['biography']
        add_product_auther(cursor, conn,author_name, author_bio)
        authors = get_data("auther")
        return render_template('index-author.html',authors=authors)

@app.route('/submit_ordered', methods=['POST'])
def submit_ordered():
    if request.method == 'POST':  # method of send data
        order_custmer_email= request.form['order_custmer_email']
        order_book_id = request.form['order_book_id']
        order_quantity = request.form['order_quantity =']
        add_product_ordered(cursor, conn, order_custmer_email, order_book_id, order_quantity)
        index_orders()


@app.route('/add_customer', methods=['POST'])
def submit_customers():
    if request.method == 'POST':  # method of send data
        customer_name = request.form['customer_name']
        customer_email = request.form['customer_email']
        customer_phone = request.form['customer_phone']

        add_product_customer(cursor, conn, customer_name, customer_email, customer_phone)
        rows = get_data('customers')
        return render_template('index-customers.html',customers=rows)


@app.route('/add_publisher', methods=['POST'])
def submit_publishers():
    if request.method == 'POST':  # method of send data
        publishers_name = request.form['publishers_name']
        publishers_email = request.form['publishers_email']
        add_product_puplisher(cursor, conn,publishers_name, publishers_email)
        rows = get_data('publishers')
        return render_template('index-publishers.html',publishers=rows)


@app.route('/add_books', methods=['POST'])
def submit_books():
    if request.method == 'POST':  # method of send data
        book_title = request.form['book_title']
        book_genre = request.form['book_genre']
        book_price = request.form['book_price']
        book_quantity = request.form['book_quantity']
        book_publisher = request.form['book_publisher']
        book_author = request.form['book_author']
        add_product_book(cursor, conn, book_title , book_genre , book_price , book_quantity , book_publisher , book_author )
        rows = get_data("books")
        return render_template('index-books.html',books=rows)

app.run(debug=True)

# Close the cursor and connection
cursor.close()
conn.close()