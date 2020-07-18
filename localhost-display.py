"""
auditing webpage
- select a team
- pull data from db and put in laps and diary as 2 tables, combine
- nice GUI
- calculations and abnormalities

- need to display data from pg to localhost website from application
- create gui on localhost or application
- display race data (X, see https://kb.objectrocket.com/postgresql/from-postgres-to-python-to-html-1033#python+web+database+application+source+code)
- edit race data (manage the tables, see https://kb.objectrocket.com/postgresql/manage-postgres-tables-with-python-1103)
"""

from flask import Flask
from flask import render_template #render html form
from flask import request
import psycopg2

app = Flask(__name__)
@app.route("/")


def __init__(self):
    self.team_id
    self.opendb()
    self.team_select()
    self.query_db()

    self.main()

#open db connection
def opendb(self):
    try:
        self.conn = psycopg2.connect(dbname='***', user='***',password='***',host='***',port='***', connect_timeout=1)
        self.cur=self.conn.cursor()
    except:
        print("Unable to connect to the database.")

#select a team
def team_select(self, team):
    team = self.team_id
    s= ""
    s+= "SELECT team_id FROM public.score_diary"
    s+= ""

#pull data from a pg table
def query_db(self):
    s= ""
    s+= "SELECT * FROM public.score_rawclickeydata"
    s+= ""
    self.cur.execute(s)
    try:
        array_data1 = self.cur.fetchall()
    except psycopg2.Error as e:
        error_msg = "Database error: " + e + "/n SQL: " + s
        return render_template("error_report.html", t_error_message = error_msg)

    return render_template("results.html", t_title = t_title, array_data1 = array_data1)
    
if __name__ == '__main__':
   app.run()


# def Main():
    # check querystring for action to take
    ##t_action = request.args.get("t_action", "")
    ##t_name_table = request.args.get("t_name_table", "")

    # if coming from user then delete a table
    ##if t_action != "" AND t_name_table != "":
        #return DeleteTable(t_name_table)

    # Either way: get table list and pull up dynamic HTML page (template)
    ##t_schema = "public"
    ##array_tables = GetTableList(t_schema)
    # Show the dynamic HTML page to user
    #t_url = "[URL to application]" # be sure to fill this in!
    #return render_template("tables_manage.html", array_tables = array_tables, t_url = t_url)

# #create pandas table using db data
# def create_table(sql_query, database=self.conn):
#     table=pd.read_sql_query(sql_query, database)
#     return table

# #create_table()

# self.cur.close()
# self.conn.close()