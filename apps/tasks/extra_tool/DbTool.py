
import pymysql
# from tasks.models import TaskMsg
# from tasks.models import TaskMsg
from tasks.models import TaskMsg


def conn_mysql(msg):
    db = pymysql.connect(host=msg["host"], port=msg["port"], user=msg["user"], passwd=msg["password"], db=msg["database"], charset=msg["charset"])
    return db, db.cursor()


def conn_close(db,cursor):
    cursor.close()  # 关闭游标
    db.close()  # 关闭连接


def test():

    meg = TaskMsg.objects.all()
    print(meg)


if __name__ == '__main__':
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    conn_msg = {
        'db': 'InduceData',
        'USER': 'root',
        'port' : 3306,
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'charset' : 'utf8',
                }
    cursor = conn_mysql(conn_msg)
    sql = 'desc users_userprofile;'
    result = cursor.execute(sql)
    print(cursor.fetchall())
    # test()


