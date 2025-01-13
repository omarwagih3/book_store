# Library Management System with Flask and SQL Server

This project is a **Library Management System** built using Flask, SQL Server, and PyODBC. It provides a web-based interface for managing books, authors, customers, publishers, and orders in a library system.



## Features

- **Books Management**:
  - Add, view, search, and delete books.
  - Search books by title.

- **Authors Management**:
  - Add, view, search, and delete authors.
  - Search authors by name.

- **Customers Management**:
  - Add, view, search, and delete customers.
  - Search customers by name.

- **Publishers Management**:
  - Add, view, search, and delete publishers.
  - Search publishers by name.

- **Orders Management**:
  - Add, view, search, and delete orders.
  - Search orders by order ID.

- **Dynamic Data Display**:
  - All data from the database is dynamically rendered in HTML templates.

## Tech Stack

- **Backend**:
  - Flask: A lightweight WSGI web application framework for Python.
  - PyODBC: A Python library to connect to SQL Server databases.
  
- **Database**:
  - SQL Server: Used to store and manage data related to books, authors, publishers, customers, and orders.
  
- **Frontend**:
  - HTML, CSS, JavaScript: For building and styling the interface.
  - **Bootstrap**: A CSS framework used for responsive and visually appealing design.

## Installation

### Prerequisites

- Python (3.6+)
- SQL Server
- Virtual environment (optional but recommended)

### Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install flask pyodbc
   ```

3. Configure the database:
   - Update the `DRIVER_NAME`, `SERVER_NAME`, and database connection details in the script.

4. Run the application:
   ```bash
   python app.py
   ```

5. Access the application in your browser at `http://127.0.0.1:5000`.

## Folder Structure

```
.
├── templates/
│   ├── index-home.html
│   ├── index-author.html
│   ├── index-books.html
│   ├── index-customers.html
│   ├── index-orders.html
│   ├── index-ordered-bks.html
│   └── index-publishers.html
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── scripts.js
│   ├── images/
│       └── example.jpg
├── app.py
└── README.md
```

## Key Functions

- **Data Insertion**:
  - `add_product_book()`: Insert a new book into the database.
  - `add_product_author()`: Insert a new author into the database.
  - `add_product_customer()`: Insert a new customer into the database.
  - `add_product_publisher()`: Insert a new publisher into the database.
  - `add_product_ordered()`: Insert a new order into the database.

- **Data Retrieval**:
  - `get_data(table_name)`: Fetch all data from a specified table.

- **Data Deletion**:
  - `del_product(cursor, conn, id, table_name, attrb)`: Delete data by ID from a specified table.

- **Data Search**:
  - `search_product(cursor, keyword, table_name, attr)`: Perform a search in a specified table.

## Usage

1. **Homepage**: Access the main page at `/`.
2. Navigate to different sections:
   - Authors: `/index-author.html`
   - Books: `/index-books.html`
   - Customers: `/index-customers.html`
   - Orders: `/index-orders.html`
   - Ordered Books: `/index-ordered-bks.html`
   - Publishers: `/index-publishers.html`

## Future Enhancements

- Add user authentication for enhanced security.
- Include pagination for large datasets.
- Improve UI/UX design for better usability.

## Screenshot
![book_store](https://github.com/user-attachments/assets/91449fa8-28d4-4618-8e87-5ae2d12cc22a)


