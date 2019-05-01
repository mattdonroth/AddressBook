import pymysql.cursors
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

def connect():
  mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd="skipswife",
  db='python_DB'
  )
  return mydb

def check(username, password):
  try:
    db = connect()
    with db.cursor() as cursor:
      sql = """SELECT `username` from `python_DB`.`login` as `login` WHERE (`username` = %s) AND (`password` = %s);"""
      digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
      
      digest.update(password.encode())
      sendpass = str(digest.finalize())
      tuple = (username, sendpass)
      cursor.execute(sql, tuple)
      result = cursor.fetchall()
      if len(result) == 0:
        return False
      else:
        return True
  finally:
    db.commit()
    db.close()

def add(name, address, zipcode, email, phone_number, username):
  try:
    db = connect()
    with db.cursor() as cursor:
      sql = """ INSERT INTO contacts (name, address, zip_code, email, phone_number, username) VALUES (%s, %s, %s, %s, %s, %s);"""
      tuple = (name, address, zipcode, email, phone_number, username)
      cursor.execute(sql, tuple)
  finally:
    db.commit()
    db.close()

def delete(name, username):
  try:
    db = connect()
    with db.cursor() as cursor:
      sql = """DELETE FROM `python_DB`.`contacts` WHERE (`name` = %s) and (`username` = %s);"""
      tuple = (name, username)
      cursor.execute(sql, tuple)
  finally:
    db.commit()
    db.close()

def show(name):
  try:
    db = connect()
    with db.cursor() as cursor:
      sql = """SELECT `name`, `address`, `zip_code`, `email`, `phone_number` from `python_DB`.`contacts` as `contacts` WHERE (`username` = %s);"""
      tuple = name
      cursor.execute(sql, tuple)
      addresses = cursor.fetchall()
  finally:
    db.commit()
    db.close()
    return addresses


#add('pythontest', '123 fake', '92110', 'mail.com', '9165178084', 'pythonhack')
#delete('pythontest')
#show('jeff')



