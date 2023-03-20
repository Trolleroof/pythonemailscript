import csv
from email.message import EmailMessage
import smtplib
import ssl
import os

context = ssl.create_default_context()
email_sender = "nikhilprabhu06@gmail.com"
password = "kfhhjghkuouxnxyw"
email_reciever = ""
subject = "Testemailv3"

email_reciever_list = []

em = EmailMessage()
em['From'] = email_sender
em['Subject'] = subject
em['To'] = email_reciever

with open('50-contacts.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        email_reciever_list.append(line[1])
        ## TODO: Change indexing just in case, and find a way to attach resume and links
        print(email_reciever_list)
        ## TODO: Fix email template and formatting because it looks bad
        body1 = "Dear Professor " + line[0] + ","
        body2 = """
        
        My name is Nikhil Prabhu and I am a high school sophomore from Dublin High School, California and I am passionate about applying my mobile and cloud computing skills to solve problems and contribute to projects.

        I have plenty of experience in this field, as I worked to co-found a startup that implements complex database architecture that follows the best ACID practices and implements sustainable API architecture that works in cohesion with the database architecture and optimizes the most efficient queries.

        I also have experience in web and app development where I manage a team of application developers to consistently improve client side performance through client side caching, frame janks, pagination, and other best practices. I have also built a plethora of mobile and web apps, which can be seen on my GitHub.

        Thus, in order to expand my knowledge in mobile computing, software engineering, and cloud computing, I am looking to conduct research and contribute to your lab this fall/summer if possible. I have attached my resume for your reference to verify my academic progress and interests.

        Most importantly I am willing to learn more and grow my knowledge. I may be just a high school student, but I am ambitious and being able to teach me would be an investment in my future as well as the future engineers of tomorrow. Please give my request some thought before considering a rejection, as I am a passionate student and an ambitious learner, and this opportunity would mean the world to me.

        Sincerely,
            Nikhil Prabhu
        """
        em.set_content(body1+body2)

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, password)
    for x in range(len(email_reciever_list)):
        smtp.sendmail(email_sender, email_reciever_list[x], em.as_string())
        x += 1









