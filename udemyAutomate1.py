import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login("from adress", "password")
conn.sendmail("from adress", "to adress", "Subject: Test \n\n Body: test message\n\n")
