fo = open("test.txt", "r+")


line = fo.readline()
print("读取的数据为: %s" % (line))

# 重新设置文件读取指针到开头
fo.seek(4, 0)
line = fo.readline()
print("读取的数据为: %s" % (line))