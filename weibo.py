from bs4 import BeautifulSoup
import re

class Player:
    def __init__(self, name, forward, comment, like, sum):
        self.name = name
        self.forward = forward
        self.comment = comment
        self.like = like
        self.sum = sum

    def print(self):
        print("{},转发数: {}, 评论数: {}, 点赞数: {}。总数: {}".format(self.name, self.forward, self.comment, self.like, self.sum))

path = '麻鸡拿指_01.html'
htmlfile = open(path, 'r', encoding='utf-8')
htmlhandle = htmlfile.read()
soup = BeautifulSoup(htmlhandle, 'html.parser')
# 1.获取所有的微博内容<div class="weibo-text">
texts = soup.find_all("div", "weibo-text")
players = []

for text in texts:
    allText = text.get_text()
    # 2.过滤关键字“位参赛选”
    forward = 0
    comment = 0
    like = 0
    if allText.find("位参赛选") != -1:
    	# 3.拼接筛选出的内容
        name = re.findall('[第|滴]\S{1,3}位参赛选', allText)[0] + "手"
        # 4.获取转发数、评论数、点赞数
        footer = text.parent.parent.next_sibling
        h4 = footer.find_all("h4")
        forward = forward + int(h4[0].get_text())
        comment = comment + int(h4[1].get_text())
        like = like + int(h4[2].get_text())
        sum = forward + comment + like
        player = Player(name, forward, comment, like, sum)
        players.append(player)

# 排序
sorted_player = sorted(players, key=lambda player: player.sum, reverse=True)
# 输出所有选手信息
for player in sorted_player:
    player.print()