def generate_access_token():
    # generates a random 256-bit token
    token = secrets.token_hex(32)

    #insert into the database
    mycursor = mydb.cursor()
    sql = "INSERT INTO personal_access_tokens (token, user_id) VALUES (%s, %s)"
    val = (token, user_id)
    mycursor.execute(sql, val)
    mydb.commit()
    
    return  token # 32 bytes = 256 bits

def token_destroy(token, user_id):
    # checks where token exists in database
    mycursor = mydb.cursor()
    sql = "SELECT * FROM personal_access_tokens user_id = %s"
    val = (user_id)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    if myresult:
        # delete from database
        mycursor = mydb.cursor()
        sql = "DELETE FROM personal_access_tokens WHERE user_id = %s"
        val = (user_id)
        mycursor.execute(sql, val)
        mydb.commit()
        return True
    else:
        return False

def token_validate(token, user_id):
    # checks where token exists in database
    mycursor = mydb.cursor()
    sql = "SELECT * FROM personal_access_tokens user_id = %s"
    val = (user_id)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    if myresult:
        return True
    else:
        return False