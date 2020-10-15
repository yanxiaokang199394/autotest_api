import bank.get_login_token,bank.bank_test_case
import common.requests_common
import unittest,time
from HTMLTestRunner import HTMLTestRunner
import common.send_mail

def run():
    '''执行测试用例,并生成测试报告，'''
    testunit = unittest.TestSuite()#初始化测试用例集合对象，构建测试套件
    testunit.addTest(bank.bank_test_case.TestDemo("test_payment_list_1"))
    testunit.addTest(bank.bank_test_case.TestDemo("test_payment_list_2"))
    testunit.addTest(bank.bank_test_case.TestDemo("test_fundOrderId"))#把测试用例加入到测用例集合中去，将用例加入到检测套件中
    now = time.strftime("%Y-%m-%d_%H_%M_%S") #获取当前时间戳
    fp = open("/home/yanxiaokang/test_api/report/"+ now +"report.html", 'wb')#命名测试报告并告知存放路径
    runner = HTMLTestRunner(stream=fp,title='银行端',description='用例执行情况')#定义测试报告
    runner.run(testunit)#执行测试用例
    fp.close() #关闭报告
    bank.bank_test_case.logger.info("测试报告已生成")
    common.send_mail.send_mail()   #发送邮件

if __name__ == '__main__':
    run()
