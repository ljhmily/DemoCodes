#!/usr/bin/python3
# coding=utf-8

import smtplib
import socket
import email.mime.multipart

user = 'zabbix@midea.com'
passwd = 'z5KNp4'
server = 'smtp.midea.com'
port = '25'

smtp = smtplib.SMTP(host=server, port=port, timeout=socket._GLOBAL_DEFAULT_TIMEOUT)

msg = email.mime.multipart.MIMEMultipart()
msg['From'] = 'zabbix@midea.com'
msg['To'] = 'hao7.liu@midea.com'
msg['Subject'] = 'Helloworld'
msg.attach(r'This is a test')

smtp.login(user, passwd)

smtp.send(msg)
