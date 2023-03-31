from flask import Flask, render_template, request, url_for, redirect, send_file
import datetime
import sqlite3
import pathlib

def db_connection(input: int):
    path = pathlib.Path(__file__).parent
    path = pathlib.Path.joinpath(path, 'production_db.db')
    con = sqlite3.connect(path)

    if input == 0:
        try:
            con.cursor().executescript('''
            CREATE TABLE GROCERY_LIST ( "USERNAME" text UNIQUE, "LIST" text, PRIMARY KEY("USERNAME") )
            ''')
            
            con.cursor().executescript(
            '''
            CREATE TABLE LOGIN ("USERNAME" text UNIQUE, "PASSWORD" text, PRIMARY KEY("USERNAME"))
            '''
            )
            con.commit()
        except:
            print("error generating table(s)")
            pass
    else:
        pass

    return con

def convert_to_binary(filename):
    with open(filename, 'rb') as filehandler:
        blobData = filehandler.read()
        return blobData

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    con = db_connection(1)
    cur = con.cursor()

    if request.method == 'POST':
        text_file = request.files['file_input']
        result = text_file.stream.read() # Bytes of data representing file contents
        # text_file.save(f"{text_file.name}.txt", 16834) # Saves a copy
        print(text_file.name)
        
        current_stamp = str(datetime.date.today())

        sql_list = [current_stamp, result]

        try:
            cur.execute("INSERT INTO GROCERY_LIST (USERNAME, LIST) VALUES (?, ?)", sql_list)
            con.commit()
            print('success')
        except:
            print('error, sql')

        con.close()
        return render_template('index.html', secret_var='Information gathered')
    else:
        return render_template('index.html')

@app.route("/next", methods=['POST', 'GET'])
def next_page():

    if request.method == 'POST':
        try:
            result = request.form['username_text']
            password_var = request.form['password_text']
        except:
            result = request.get_json()['username_text']
            print('exception: result.get_json')
        return render_template('next.html',name_var=result, password_var=password_var)
    else:
        return redirect(url_for('index'))
    
@app.route("/register", methods=['POST', 'GET'])
def register():
    con = db_connection(1)
    cur = con.cursor()
    if request.method == 'POST':
        try:
            username_var = request.form['username_text']
            print(username_var)
            password_var = request.form['password_text']
            try:
                cur.execute("INSERT INTO LOGIN (USERNAME, PASSWORD) VALUES (?, ?)", [username_var, password_var])
                con.commit()
                print('success')
            except:
                print('error, login may exist')
                return render_template('register.html', error_var = 'error, login may exist')
            con.close()
            return render_template('index.html', name_var=username_var)
        
        except:
            print('exception: cannot gather register form')
    
    else:
        return render_template('register.html')

@app.route("/FAQ")
def faq():
    return render_template('faq.html')

@app.route("/download")
def download():
    #win_path = pathlib.WindowsPath(__file__).parent
    #win_path = pathlib.WindowsPath.joinpath(path, 'template.txt')
    path = pathlib.Path(__file__).parent
    path = pathlib.Path.joinpath(path, 'template.txt')

    try:
        return send_file(path, as_attachment=True, download_name='List_template.txt')
    except:
        return "Str"

if __name__ == "__main__":
    db_connection(0)
    app.run()