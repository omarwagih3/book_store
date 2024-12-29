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
DRIVER_NAME = ''
SERVER_NAME = ''
conn = pyodbc.connect('Driver={SQL Server};'
                    'Server=serve_name;'
                    'Database=data_base_name;'
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
    authors = get_data("Authors")
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
    rows = get_data('Order_Books')
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
        authors = get_data("Authors")
        return render_template('index-author.html',authors=authors)

@app.route('/add_order', methods=['POST'])
def submit_ordered():
    if request.method == 'POST':  # method of send data
        order_custmer_email= request.form['order_custmer_email']
        order_book_id = request.form['order_book_id']
        order_quantity = request.form['order_quantity']
        add_product_ordered(cursor, conn, order_custmer_email, order_book_id, order_quantity)
        rows = get_data('orders')
        return render_template('index-orders.html', orders=rows)


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


@app.route('/add_book', methods=['POST'])
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

def search_product(cursor, keyword,table_name,attr):
    query =\
        f'''SELECT * 
            FROM {table_name} 
            WHERE {attr} LIKE '%{keyword}%\''''
    cursor.execute(query)
    results = cursor.fetchall()
    return results

def del_product(cursor, conn, id, table_name,attrb):
    query = \
        f'''DELETE FROM {table_name}
            WHERE {attrb} ={id}'''
    cursor.execute(query)
    conn.commit()

@app.route('/delete_customer', methods=['POST'])
def delete_customers():
    if request.method == 'POST':  # method of send data
        customer_id = request.form['customer_id']
        del_product(cursor, conn, customer_id,'Customers','Customer_ID')
        rows = get_data('customers')
        return render_template('index-customers.html', customers=rows)


@app.route('/delete_author', methods=['POST'])
def delete_author():
    if request.method == 'POST':  # method of send data
        author_id = request.form['author_id']
        del_product(cursor, conn,author_id,'Authors ','Author_ID')
        authors = get_data("Authors")
        return render_template('index-author.html', authors=authors)


@app.route('/delete_publisher', methods=['POST'])
def delete_publishers():
    if request.method == 'POST':  # method of send data
        publishers_id = request.form['publishers_id']
        del_product(cursor, conn,publishers_id ,'publishers','Publisher_ID')
        rows = get_data('publishers')
        return render_template('index-publishers.html', publishers=rows)



@app.route('/delete_book', methods=['POST'])
def delete_books():
    if request.method == 'POST':  # method of send data
        book_id = request.form['book_id']
        del_product(cursor, conn, book_id ,'Books','Book_ID'  )
        rows = get_data("books")
        return render_template('index-books.html', books=rows)

@app.route('/search_book', methods=['GET'])
def search_book():
    if request.method == 'GET':
        keyword = request.args.get('searchBookName')
        results = search_product(cursor, keyword, 'Books', 'title')

        return render_template('index-books.html', books=results)

@app.route('/search_author', methods=['GET'])
def search_author():
    if request.method == 'GET':
        keyword = request.args.get('searchAutherName')
        results = search_product(cursor, keyword, 'Authors', 'name')
        return render_template('index-author.html', authors=results)

@app.route('/search_publisher', methods=['GET'])
def search_publisher():
    if request.method == 'GET':
        keyword = request.args.get('searchPublisherName')
        results = search_product(cursor, keyword, 'Publishers', 'name')
        return render_template('index-publishers.html', publishers=results)

@app.route('/search_order', methods=['GET'])
def search_order():
    if request.method == 'GET':
        keyword = request.args.get('searchOrderName')
        results = search_product(cursor, keyword, 'Orders', 'order_id')
        return render_template('index-orders.html', orders=results)

@app.route('/search_customer', methods=['GET'])
def search_customer():
    if request.method == 'GET':
        keyword = request.args.get('searchCustomerName')
        results = search_product(cursor, keyword, 'Customers', 'name')
        return render_template('index-customers.html', customers=results)


app.run(debug=True)

# Close the cursor and connection
cursor.close()
conn.close()