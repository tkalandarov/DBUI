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
@app.route('/query')
def query():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Customer")  # Example: Fetch all customers
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('query.html', rows=rows)

# Report Screen
@app.route('/report')
def report():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM total_sales_by_customer")  # Using view
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('report.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
