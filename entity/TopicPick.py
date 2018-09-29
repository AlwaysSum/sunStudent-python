import self
from entity.TopicOption import TopicOption


# 实体类
class TopicPick:
    # 内容
    content = ""
    # 解析
    errMsg = ""

    # 初始化方法
    def __init__(self):
        self.content = ""
        self.errMsg = ""
        # 分类:
        self.pid = 12281  # 12281 所属目录： 正数和负数
        self.type = 1  # 1 单选题
        self.easyNum = 0.00
        # 选项卡
        self.option1 = TopicOption()
        self.option2 = TopicOption()
        self.option3 = TopicOption()
        self.option4 = TopicOption()

    # 设置题目正确性
    def setAnswer(self, answer):
        if str(answer).find("A") > 0:
            self.option1.isTrue = 1
        if str(answer).find("B") > 0:
            self.option2.isTrue = 1
        if str(answer).find("C") > 0:
            self.option3.isTrue = 1
        if str(answer).find("D") > 0:
            self.option4.isTrue = 1

    # 设置选项卡
    def setOption(self, index, content):
        if index == 0:
            self.option1.content = content
        if index == 1:
            self.option2.content = content
        if index == 2:
            self.option3.content = content
        if index == 3:
            self.option4.content = content
