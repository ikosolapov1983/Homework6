import smtplib              # отправка письма

with smtplib.SMTP('smtp.gmail.com', 587) as my_smtp:
    my_smtp.starttls()
    my_smtp.login('iloykos83@gmail.com', 'dremora1000')
#    help(my_smtp.sendmail)
    my_smtp.sendmail(from_addr='iloykos83@gmail.com', to_addrs='el.piankova@gmail.com', msg='Test message')
    my_smtp.quit()
