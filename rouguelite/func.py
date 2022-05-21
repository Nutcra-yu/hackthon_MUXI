import random
import Node


def drawLine(screen, group, attr, start, end):
    nodes = [start]
    new_nodes = []
    pos = [20, 20]
    while True:

        # 生成行位置
        pos[0] = random.randint((pos[0] + attr[0] + 80), (pos[0] + attr[0] + 100))

        if pos[0] + attr[0] * 2 >= 1000:
            break

        # 一行对应多个，使用循环

        i = random.randint(2, 5)
        new_nodes = []
        while i > 0:
            pos[1] = random.randint((pos[1] + attr[1] + 20), (pos[1] + attr[1] * 5))
            if pos[1] + attr[1] >= 600:
                break

            new_node = Node.Node("../bullet.jpg", "", pos)
            group.add(new_node)
            new_nodes.append(new_node)
            i -= 1

        for front in nodes:
            for behind in new_nodes:
                front.judgeline(behind, screen,start)

        nodes = new_nodes
        pos[1] = 20

    group.add(end)
    nodes.append(end)
    for front in nodes:
        for behind in new_nodes:
            front.judgeline(behind, screen,start)


def checkLineFair(start, end):
    for node in start.behind:
        if node == end:
            return True
        ok = checkLineFair(node, end)

        if ok:
            return True
    return False


def restartDraw(ok,screen, group, attr, start, end):
    if ok:
        return
    for node in group:
        if node == start or node == end:
            continue
        node.kill()
    screen.fill('white')
    drawLine(screen, group, attr, start, end)