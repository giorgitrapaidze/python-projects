from flask import Flask, render_template, request
import MySQLdb as mydb
import math


app = Flask(__name__)


def get_time(input_time):
	hours =  input_time / 60
	minutes = input_time % 60
	if minutes <= 9:
	 minutes = f"0{minutes}"

	return f"{math.floor(hours)}:{minutes}"


def log_request(inp, res, ip):
	dbconfig = {'host': 'gio1009.mysql.pythonanywhere-services.com',
				'user': 'gio1009',
				'password': 'smart2021',
				'database': 'gio1009$exam',}

	conn = mydb.connect(**dbconfig)
	cursor = conn.cursor()
	_SQL = """INSERT INTO log
			(number, results, ip)
			VALUES
			(%s, %s, %s)"""
	cursor.execute(_SQL, (inp,
						  res,
						  ip, ))

	conn.commit()
	cursor.close()
	conn.close()

@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html')


@app.route('/time', methods = ['POST'])
def do_time():
	number = request.form['input_time']


	results = get_time(int(number))
	ip = request.remote_addr
	log_request(str(number), str(results), str(ip))
	return render_template('time.html',
							the_results = results)

@app.route('/viewlog')
def view_the_log():
	dbconfig = {'host': 'gio1009.mysql.pythonanywhere-services.com',
				'user': 'gio1009',
				'password': 'smart2021',
				'database': 'gio1009$exam',}

	conn = mydb.connect(**dbconfig)
	cursor = conn.cursor()

	_SQL = """select number, results, ip from log"""
	cursor.execute(_SQL)
	contents = cursor.fetchall()
	titles = ('Input', 'Result', 'IP')

	cursor.close()
	conn.close()

	return render_template('viewlog.html', the_title='View Log', the_row_titles=titles, the_data=contents,)



if __name__ == '__main__':
	app.run(debug = True)