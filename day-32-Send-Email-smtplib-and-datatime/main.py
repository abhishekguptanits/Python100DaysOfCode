import smtplib

my_email = "raj.aryan.788010@gmail.com"
# my_password = "imjack@001"
my_app_password = 'izbyhaamyevvkrrb'

# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# connection.starttls()       # tls -> Transport Layer Security
# connection.login(user=my_email, password=my_app_password)
# connection.sendmail(from_addr=my_email, to_addrs='hsoemyardydgwvouwg@cwmxc.com',
#                     msg="Subject:Greeting\n\nHope you are doing fine!")
# connection.close()

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()       # tls -> Transport Layer Security
    connection.login(user=my_email, password=my_app_password)
    connection.sendmail(from_addr=my_email, to_addrs='hsoemyardydgwvouwg@cwmxc.com',
                        msg="Subject:Update\n\nWhat's the update on your current task!")
