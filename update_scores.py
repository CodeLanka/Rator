import os
from dotenv import load_dotenv, find_dotenv
import pymysql.cursors
import json

load_dotenv(find_dotenv())


db_host=os.environ.get("DB_HOST")
db_database=os.environ.get("DB_DATABASE")
db_username=os.environ.get("DB_USERNAME")
db_password=os.environ.get("DB_PASSWORD")

connection = pymysql.connect(host=db_host,
                             user=db_username,
                             password=db_password,
                             db=db_database,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


with connection.cursor() as cursor:
 sql = """SELECT
    user_id,
    count(response_id) AS registered,
    SUM(accepted = 'yes') AS accepted_yes,
    SUM(accepted = 'no') AS accepted_no,
    SUM(accepted = 'pending') AS accepted_pending,
    SUM(accepted = 'canceled') AS accepted_canceled,
    SUM(confirmed = 'yes') AS confirmed_yes,
    SUM(confirmed = 'no') AS confirmed_no,
    SUM(confirmed = 'pending') AS confirmed_pending,
    SUM(checked_in > '0000-00-00 00:00:00') AS checked_in,
    SUM(event_rating = 3) AS event_rating_3,
    SUM(event_rating = 4) AS event_rating_4,
    SUM(event_rating = 5) AS event_rating_5
FROM responses
GROUP BY user_id"""

 cursor.execute(sql)
 responses = cursor.fetchall()

 for response in responses:
    registered = response['registered']
    accepted_yes = response['accepted_yes']
    accepted_no = response['accepted_no']
    accepted_pending = response['accepted_pending']
    accepted_canceled = response['accepted_canceled']
    confirmed_no = response['confirmed_no']
    confirmed_yes = response['confirmed_yes']
    confirmed_pending = response['confirmed_pending']
    checked_in = response['checked_in']
    event_rating_3 = response['event_rating_3']
    event_rating_4 = response['event_rating_4']
    event_rating_5 = response['event_rating_5']

    if checked_in is None:
        checked_in = 0


    print response['user_id'], confirmed_yes, checked_in

    score_event_ratings = (event_rating_3*3+event_rating_4*4+event_rating_5*5)
    Score_accepted = accepted_yes*5 - accepted_canceled*6
    score_confirmed = confirmed_yes*5 - (accepted_yes-(confirmed_yes+confirmed_no))*6
    score_checking = -(confirmed_yes-checked_in)*10
    final_score = score_event_ratings + Score_accepted + score_confirmed + score_checking
    print final_score

    sql = """UPDATE users SET score = %s WHERE id= %s """

    cursor.execute(sql, (final_score,  response['user_id']))

connection.commit()
