f = open('python.text','r')
content = f.readlines()
print(f'第一行：{content}')

content = f.readlines()
print(f'第二行：{content}')
# ['hello world\n','abcdefg\n','aaa\n','bbb\n','ccc']
# print(content)

for line in open("python.text","r"):
    print(line)
 #关闭文件
f.close()