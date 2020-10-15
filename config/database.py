import pymysql

dev3 =  pymysql.connect(
        host="10.46.7.200",
        user="ubankdev",
        port=3306,
        password="123456",
        database="froad_cbank_dev_anhui",
        charset="utf8")

anhuiuat =  pymysql.connect(
        host="10.46.8.200",
        user="ubanktest",
        port=3306,
        password="123456",
        database="froad_cbank_gray_anhui",
        charset="utf8")

gray3 = pymysql.connect(
        host="10.46.8.200",
        user="ubanktest",
        port=3306,
        password="123456",
        database="froad_cbank_gray_anhui_0503",
        charset="utf8")
