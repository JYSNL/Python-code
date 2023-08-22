from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()  # 创建一个队列
    search_queue += graph[name]  # 将你的邻居都加入到这个搜索队列中
    print(search_queue)

    searched = []  # 这个数组用于记录检查过的人
    while search_queue:  # 只要队列不为空
        person = search_queue.popleft()  # 取出队列中的一个人
        print(person)
        print(search_queue)
        if person not in searched:  # 仅当这个人未检查过时才检查
            if person_is_seller(person):  # 检查这个人是否是芒果销售商
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]  # 不是芒果销售商，将这个人的朋友都加入搜索队列
                print(search_queue)
                searched.append(person)  # 将这个人标记为检查过
                print(searched)
    return False  # 如果到达了这里，就说明队列中没人是芒果销售商


search("you")