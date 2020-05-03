import mysql.connector
conn = None


try:
        conn = mysql.connector.connect(host='localhost', user='root', password='Sp00tyB00tie', database='classicmodels')
        print('Connected to MySQL database')
except Exception as ex:
        print("Cannot connect to MySQL : exception : " + str(ex))

cursor1 = conn.cursor()
cursor2 = conn.cursor()

query=("SELECT customers.customerName, payments.amount, payments.paymentDate FROM payments INNER JOIN customers ON customers.customerNumber=payments.customerNumber WHERE MONTH(paymentDate) = 12;")
cursor1.execute(query)

for (customer, amount, paymentDate) in cursor1:
    print("Customer: ", customer)
    print("Payment Date: ", paymentDate)
    print("Initial Payment: ", amount)
    print("Payment After Rebate: ", float(amount)* .99)

    print(". . .")
