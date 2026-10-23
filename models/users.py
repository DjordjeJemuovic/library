def add_users(con,name,age):
    cursor = con.cursor()

    users_query = "INSERT INTO users(name, dob) VALUES(%s, %s)"
    cursor.execute(users_query, (name, age))
    con.commit()
    user_id = cursor.lastrowid
    cursor.close()
    return user_id
