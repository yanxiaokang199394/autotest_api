import requests
import logging
import json

def get_http(url, headers, params, **kwargs):
    # params = json.dumps(params)
    response = requests.request("GET", url, headers=headers, params=params, **kwargs)
    res = json.loads(response.text)
    print(res)
    logging.info("get_res==>"+json.dumps(res))
    return res

def post_http(url, headers, payload, **kwargs):
    payload = json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data=payload, **kwargs)
    res = json.loads(response.text)
    print(res)
    logging.info("post_res==>" + json.dumps(res))
    return res

if __name__ == "__main__":
    new_head = {"Connection": "keep-alive",
                       "Referer": "https://gray3.ubank365.com/anhui/admin/bank/index.html",
                       "Content-Type": "application/json",
                       "userId": "100005121",
                       "token": "4395659050734e72aa2c41345d73252d"
                       }
    data = {"refundOrderId":"9FEB7AD48000"}
    res = get_http(url="https://gray3.ubank365.com/api/bank/refund/auditDetails?refundOrderId=9FEB7AD48000",
             params=data,headers=new_head)