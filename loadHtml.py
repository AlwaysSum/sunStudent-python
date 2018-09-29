from bs4 import BeautifulSoup
from selenium import webdriver
import ssl  # 导入ssl认证东西
import time
from entity.TopicPick import TopicPick
import json

ssl._create_default_https_context = ssl._create_unverified_context  # 访问https证书失败，加上全局取消认证

# 单选题链接
urls = [
    "http://www.tiku.cn/index/index/questions?cid=10&cno=1&unitid=800253&thrknowid=709362&typeid=600012&page={}".format(
        str(i)) for i in
    range(1, 3)]  # 页码 1~2

# 页码
index = 0


# 获取单项选择题列表
def getTopicPicks():
    # 初始化一些设置
    # chromedriver 的路径
    driver = webdriver.Chrome(r"D:\CodePython\chromedriver_win32\chromedriver.exe")
    global index
    keep_request = True  # while_true=True 变量命名更清晰点
    isLogin = False  # 是否登录
    topicSet = set()

    # 遍历urls：分页数据
    for url in urls:
        # 通过selenium调用答案的点击事件
        driver.get(url)

        # 等待登录OK
        if isLogin == False:
            inputStr = input("请先登录，登录成功请输入OK继续~:")
            isLogin = inputStr == "ok"
        # 登录过的则不登录了
        if isLogin:
            # 调用所有的答案点击事件
            for ele in driver.find_elements_by_xpath("//i[@class='fa fa-list']/parent::a"):
                ele.click()
                time.sleep(1.5)
        else:
            return
        # 加载网页源码进行遍历
        while keep_request:
            try:
                # page = urllib.request.urlopen(driver.page_source).read()  # 加载网页
                keep_request = False
                main = BeautifulSoup(driver.page_source, "html.parser")
                # print(school.title.string)
            except:
                print("reconnect to web..")  # print("重新连接")
                time.sleep(1)
        # 题目最外层
        for list_data in main.find_all('div', "card mb-3 q-detail rounded-0"):
            index = index + 1
            # 实例化一个题目对象
            topic = TopicPick()
            # 得到题目数据
            content = str(list_data.find("section", class_="card-text mb-3"))
            content = content.replace("<section class=\"card-text mb-3\">", "")
            content = content.replace("</section>", "").strip()
            print("第" + str(index) + "题：" + content)
            # 添加题目内容
            topic.content = content
            # 得到四个选项卡
            for idxOption, option in enumerate(list_data.find_all('div', class_="col-lg-6")):
                opStr = str(option)
                opStr = opStr.replace("<div class=\"col-lg-6\">", "")
                opStr = opStr.replace("</div>", "").strip()
                print("选项：" + str(idxOption) + "：" + opStr)
                topic.setOption(idxOption, opStr)
            # 获取难度
            nandu = str(list_data.find("span", class_="align-self-center text-muted text-nowrap"))
            nandu = nandu.replace("<span class=\"align-self-center text-muted text-nowrap\">", "")
            nandu = nandu.replace("</span>", "")
            nandu = nandu.replace("难度:", "").strip()
            print(nandu)
            topic.easyNum = float(nandu)
            # 获取答案
            answer = str(list_data.find("p", class_="answer-detail"))
            answer = answer.replace("<p class=\"answer-detail\">", "")
            answer = answer.replace("</p>", "").strip()
            print(answer)
            topic.setAnswer(answer)
            # 获取解析
            anaylis = str(list_data.find("p", class_="anaylis-detail"))
            anaylis = anaylis.replace("<p class=\"anaylis-detail\">", "")
            anaylis = anaylis.replace("</p>", "")
            anaylis = anaylis.replace("解析 :", "").strip()
            print(anaylis)
            topic.errMsg = anaylis
            topicSet.add(topic)
    # 退出浏览器
    driver.quit()
    return topicSet


if __name__ == '__main__':
    topics = getTopicPicks(urls)
    for top in topics:
        dict = top.__dict__
        print(dict)
