import bank.get_login_token
import common.requests_common
import unittest
from ddt import ddt,data,file_data,unpack
import logs.logger


logger = logs.logger.logs()   #日志实例化

token = bank.get_login_token.get_token()   #获取登录token
tokens = token[0]  #取到token
tokens_id = token[1]   #取到userid
logger.info("获取登录token：" + str(tokens))    #输出日志
logger.info("获取登录userid：" + str(tokens_id))  #输出日志

tset_1 = {"billNo": "",
             "refundNo": "",
             "payType": "",
             "refundStatus": [],
             "paymentId": "",
             "payerName": "",
             "payerAccount": "",
             "originalbizOrderType": "",
             "pageNumber": 1,
             "pageSize": 10,
             "beginTime": "2020-06-16 00:00:00",
             "endTime": "2020-06-17 23:59:59",
             "refundBeginTime": " ",
             "refundEndTime": "",
             "lastPageNumber": 0,
             "firstRecordTime": 0,
             "lastRecordTime": 0
             }
test_2 = {"billNo": "",
             "refundNo": "",
             "payType": "",
             "refundStatus": [],
             "paymentId": "",
             "payerName": "",
             "payerAccount": "",
             "originalbizOrderType": "",
             "pageNumber": 1,
             "pageSize": 10,
             "beginTime": "2020-07-30 00:00:00",
             "endTime": "2020-08-01 23:59:59",
             "refundBeginTime": " ",
             "refundEndTime": "",
             "lastPageNumber": 0,
             "firstRecordTime": 0,
             "lastRecordTime": 0
             }
@ddt #ddt装饰器
class TestDemo(unittest.TestCase):
    @data(tset_1,test_2) #指明需使用到的数据
    def test_payment_list(self,a):  # 银行端退款查询接口
        new_headers = {"Connection": "keep-alive",
                       "Referer": "https://gray3.ubank365.com/anhui/admin/bank/index.html",
                       "Content-Type": "application/json",
                       "userId": str(tokens_id),
                       "token": tokens
                       }
        url = "https://gray3.ubank365.com/api/bank/refund/bossPayment/list"
        res = common.requests_common.post_http(url=url,
                                                        headers=new_headers,
                                                        payload=a)
        try:
            self.assertIn("'message': '操作成功'",str(res))
            logger.info("退款查询接口，测试成功！")
        except AssertionError:
            logger.warning("测试失败！")
            raise

    def test_fundOrderId(self): #查看退款进度详情
        new_headers = {"Connection": "keep-alive",
                       "Referer": "https://gray3.ubank365.com/anhui/admin/bank/index.html",
                       "Content-Type": "application/json",
                       "userId": str(tokens_id),
                       "token": tokens
                       }
        url = "https://gray3.ubank365.com/api/bank/refund/auditDetails"
        x = {"refundOrderId":"9FEB7AD48000"}
        res = common.requests_common.get_http(url=url,
                                                       params= x,
                                                       headers=new_headers)
        try:
            self.assertIn("'reason': '商品破损已拒签'",str(res))
            logger.info("退款进度详情，测试成功！")
        except AssertionError:
            logger.warning("测试失败")
            raise
