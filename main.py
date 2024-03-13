import smtplib

my_mail = "Your Email"
password = "Your Password"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_mail,password=password)
    connection.sendmail(
        from_addr=my_mail,
        to_addrs="Reciever Email",
        msg="Subject:Hello\n\n This Mail is Sended By Python Code "
    )