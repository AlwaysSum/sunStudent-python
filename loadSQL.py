import loadHtml
import pymysql


# 插入数据库语句
def insertTopic():
    # 连接数据库
    db = pymysql.Connect(host='localhost',
                         port=3306,
                         user='sunflower816',
                         passwd='0.0.0.',
                         db='sunstudent',
                         charset='utf8')
    # 获取游标
    cursor = db.cursor()

    # 获取数据实体类
    topicSet = loadHtml.getTopicPicks()
    for idx, topic in enumerate(topicSet):
        idx = idx + 1
        # 插入数据
        sqlTopic = "INSERT INTO `sunstudent`.`tb_topic`(`ID`,`PID`,`type`,`content`,`errMsg`,`easyNum`)" \
                   "VALUES (%s,%s,%s,'%s','%s',%s)" % \
                   (idx, topic.pid, topic.type, topic.content, topic.errMsg, topic.easyNum)

        sqlOption1 = "INSERT INTO `sunstudent`.`tb_option`(`topicID`,`content`,`isTure`) " \
                     "VALUES (%s,'%s',%s)" % \
                     (idx, topic.option1.content, topic.option1.isTrue)
        sqlOption2 = "INSERT INTO `sunstudent`.`tb_option`(`topicID`,`content`,`isTure`) " \
                     "VALUES (%s,'%s',%s)" % \
                     (idx, topic.option2.content, topic.option2.isTrue)
        sqlOption3 = "INSERT INTO `sunstudent`.`tb_option`(`topicID`,`content`,`isTure`) " \
                     "VALUES (%s,'%s',%s)" % \
                     (idx, topic.option3.content, topic.option3.isTrue)
        sqlOption4 = "INSERT INTO `sunstudent`.`tb_option`(`topicID`,`content`,`isTure`) " \
                     "VALUES (%s,'%s',%s)" % \
                     (idx, topic.option4.content, topic.option4.isTrue)
        # 执行sql
        cursor.execute(sqlTopic)
        cursor.execute(sqlOption1)
        cursor.execute(sqlOption2)
        cursor.execute(sqlOption3)
        cursor.execute(sqlOption4)
    # 提交事务
    try:
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
    # 关闭数据库连接
    db.close()


# 查询数据库
def queryTopic():
    # 连接数据库
    db = pymysql.Connect(host='localhost',
                         port=3306,
                         user='sunflower816',
                         passwd='0.0.0.',
                         db='sunstudent',
                         charset='utf8')
    # 获取游标
    cursor = db.cursor()
    # 查询数据
    sql = "SELECT ID,content,errMsg,easyNum FROM sunstudent.tb_topic"
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(str(row[0]) + "===" + str(row[1]) + "===" + str(row[2]) + "===" + str(row[3]))
    print('共查找出', cursor.rowcount, '条数据')
    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    insertTopic()
    # queryTopic()
