from flask import Flask,render_template,url_for,request,redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="root"
app.config["MYSQL_DB"]="Employee"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)

# Loading Home Page
@app.route("/")
def home():
    con=mysql.connection.cursor()
    sql="SELECT * FROM employeedetails"
    con.execute(sql)
    res=con.fetchall()
    return render_template("home.html",datas=res)

# Add New Employees

@app.route("/add Employees",methods=['GET','POST'])
def addEmployees():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        salary = request.form['salary']
        con = mysql.connection.cursor()
        sql="insert into employeedetails(name,age,city,salary) value (%s,%s,%s,%s)"
        con.execute(sql,[name,age,city,salary])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))
    return render_template("add Employees.html")

# Update Employee Details

@app.route("/edit Employees/<string:id>",methods=['GET','POST'])
def updateEmployees(id):
    con=mysql.connection.cursor()
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        salary = request.form['salary']
        sql="update employeedetails set name=%s,age=%s,city=%s,salary=%s where id=%s"
        con.execute(sql,[name,age,city,salary,id])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))

    sql="select * from employeedetails where id=%s"
    con.execute(sql,[id])
    res=con.fetchone()
    return  render_template("edit Employees.html",datas=res)

# Delete Employee

@app.route("/delete Employees/<string:id>",methods=['GET','POST'])
def deleteEmployees(id):
    con=mysql.connection.cursor()
    sql="delete from employeedetails where id=%s"
    con.execute(sql,id)
    mysql.connection.commit()
    con.close()
    return redirect(url_for("home"))






if(__name__) == ("__main__"):
    app.run(debug=True)