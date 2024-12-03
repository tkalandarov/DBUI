from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

# Database connection
def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="", # replace with your database name
        user="", # replace with your username
        password="" # replace with your password
    )

@app.route('/')
def home():
    return render_template('base.html')

# Insert Screen
@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        table = request.form['table']
        columns = request.form['columns']
        values = request.form['values']
        conn = get_db_connection()
        cur = conn.cursor()
        query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/query')
    return render_template('insert.html')

# Update Screen
@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        table = request.form['table']
        set_clause = request.form['set_clause']
        where_clause = request.form['where_clause']
        conn = get_db_connection()
        cur = conn.cursor()
        query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/query')
    return render_template('update.html')

# Delete Screen
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        table = request.form['table']
        where_clause = request.form['where_clause']
        conn = get_db_connection()
        cur = conn.cursor()
        query = f"DELETE FROM {table} WHERE {where_clause}"
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/query')
    return render_template('delete.html')

# Query Screen
@app.route('/query', methods=['GET'])
def query():
    conn = get_db_connection()
    cur = conn.cursor()

    # List of all tables
    tables = [
        "customer", "vendor", "product", "delivery_company",
        "Order", "order_items", "shopping_cart", "review",
        "address", "payment", "administrator"
    ]

    selected_table = request.args.get('table')  # Get the selected table from the query parameters
    data = None

    if selected_table:
        try:
            cur.execute(f'SELECT * FROM "{selected_table}"')
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            data = {"columns": columns, "rows": rows}
        except Exception as e:
            print(f"Error fetching data for table {selected_table}: {e}")

    cur.close()
    conn.close()

    return render_template('query.html', tables=tables, selected_table=selected_table, data=data)

@app.route('/report', methods=['GET'])
def report():
    conn = get_db_connection()
    cur = conn.cursor()

    # List of available views
    views = {
        "total_sales_by_customer": "Total Sales by Customer",
        "top_selling_products": "Top Selling Products",
        "customers_no_orders": "Customers with No Orders",
        "customer_contact_info": "Customer Contact Info"
    }

    selected_view = request.args.get('view')  # Get the selected view from the query parameters
    view_data = None
    view_name = views.get(selected_view)

    if selected_view:
        try:
            cur.execute(f'SELECT * FROM {selected_view}')
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            view_data = {"columns": columns, "rows": rows}
        except Exception as e:
            print(f"Error fetching data for view {selected_view}: {e}")

    cur.close()
    conn.close()

    return render_template('report.html', views=views, selected_view=selected_view, view_name=view_name, view_data=view_data)


if __name__ == '__main__':
    app.run(debug=True)
