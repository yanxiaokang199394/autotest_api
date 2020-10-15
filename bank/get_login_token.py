import requests
import json
import config.database

def verification_code():
    url = "https://gray3.ubank365.com/api/bank/login/gic"
    new_herad = {"Connection" : "keep-alive",
                "Referer" : "https://gray3.ubank365.com/anhui/admin/bank/index.html",
                "Content-Type" : "application/json"}
    res = requests.post(url,headers = new_herad)
    r = json.loads(res.text)
    global tokens
    tokens = (r["token"])

def database_connection():
    db = config.database.gray3
    cursor = db.cursor()
    sql = "SELECT `code` FROM `cb_sms_log`WHERE token=%s"
    cursor.execute(sql,tokens)
    data = cursor.fetchone()
    global code
    code = data[0]
    db.close()

def bank_login():
    new_headers = {"Connection" : "keep-alive",
                "Referer" : "https://gray3.ubank365.com/anhui/admin/bank/index.html",
                "Content-Type" : "application/json"}
    url = "https://gray3.ubank365.com/api/bank/login/ve"
    x = {"userName":"yanxiaokang1",
                 "password":"44a6ae520b8df21cb9ba3249c8c2414046d9df0d1e4c1e0f04e75604a110dadd",
                 "loginFailureCount":0,
                 "code":int(code),   #### 图片验证码
                 "token":"{}".format(tokens)  #####获取图片验证码接口返回token
                 }
    y = json.dumps(x)
    res = requests.post(url,data = y,headers = new_headers)
    r = json.loads(res.text)
    token = (r["token"])
    userId = (r["userId"])
    return token,userId


def get_token():
    verification_code()
    database_connection()
    data = bank_login()
    return data
