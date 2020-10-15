import smtplib
from email.mime.text import MIMEText
from email.header import Header
import logging
import os
import time

smtpserver = "smtp.qq.com"  # 发送邮箱服务器
user = "653847252@qq.com"  #发送邮箱用户名
password = "eidoohnwljqybbjj"  #授权码
sender = "653847252@qq.com"  # 发送邮箱
receiver = ["yanxiaokang@f-road.com.cn"]  # 接收邮箱


# 连接服务器并发送邮件
def send_mail():
    '''读取测试报告文件,设置邮件格式'''
    # 获取项目根目录
    root_path = os.path.abspath(os.path.dirname(__file__)).split('test_api')[0]
    # 指明测试报告路径
    base_dir = root_path + "test_api/report"
    # 列出目录下所有文件
    lists = os.listdir(base_dir)
    # 目录下的文件让时间排序
    lists.sort(key=lambda fn: os.path.getmtime(base_dir + "/" + fn))
    # 获取最新文件
    new_file = os.path.join(base_dir, lists[-1])
    logging.info("获取报告文件名为" + new_file)
    # 将文件打开并存放在mail_body中
    f = open(new_file, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['From'] = Header('zhtest', 'utf-8')
    msg['To'] = Header('yanxiaokang@f-road.com.cn', 'utf-8')
    # msg['To'] = Header('人员2','utf-8')
    now = time.strftime("%Y-%m-%d")
    subject = now + "接口自动化报告"  # 邮件主题
    msg['Subject'] = Header(subject, 'utf-8')
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, 587)
    smtp.login(user, password)

    try:
        smtp.sendmail(sender, receiver, msg.as_string())
    except:
        logging.warning("邮件发送失败！！！")
    else:
        logging.info("邮件发送成功！")
    finally:
        smtp.close()

if __name__ == '__main__':
    send_mail()

