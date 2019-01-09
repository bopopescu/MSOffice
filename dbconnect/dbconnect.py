from mysql.connector import connect


def select_all():
    cnx = connect(user='root', password='******', host='localhost', database='exceldb')
    cursor = cnx.cursor()
    query = ("SELECT DISTINCT firstname, lastname, address, email, phone FROM Contact ORDER BY lastname")
    cursor.execute(query)
    items = cursor.fetchall()
    cnx.commit()
    cnx.close()
    return items


def insert_contact(first, last, address, phone, email):
    cnx = connect(user='root', password='*****', host='localhost', database='exceldb')
    cursor = cnx.cursor()
    try:
        query = ("INSERT INTO Contact(firstname, lastname, address, phone, email) VALUES(%s,%s,%s,%s,%s)")
        insertUser = (first, last, address, phone, email)
        cursor.execute(query, insertUser)
        cnx.commit()
        cnx.close()
        return True

    except Exception as e:
        print(e)
        return False


def insert_rates(company, one, two, three, four, five):
    cnx = connect(user='root', password='******', host='localhost', database='exceldb')
    cursor = cnx.cursor()
    try:
        query = ("INSERT INTO Rate(company, one, two, three, four, five) VALUES(%s,%s,%s,%s,%s,%s)")
        insert_rate = (company, one, two, three, four, five)
        cursor.execute(query, insert_rate)
        cnx.commit()
        cnx.close()
        return True

    except Exception as e:
        print(e)
        return False

