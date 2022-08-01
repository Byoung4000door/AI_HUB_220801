import sqlite3
con = sqlite3.connect('../opentutorials.db')
cur = con.cursor()

result_id = input('id ? ')
result = cur.execute('SELECT * FROM topics WHERE id = ?', (result_id,))
rows = result.fetchone()
print(rows)
con.close()

