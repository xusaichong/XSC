# 打开文件并读取内容
with open('word.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# 将内容转换为小写，以确保统计时不区分大小写
content = content.lower()

# 替换可能的标点符号，确保单词的准确性
import re
content = re.sub(r'[^\w\s]', '', content)

# 统计 "python" 单词的出现次数
count = content.count('python')

print(f"'python' 出现了 {count} 次。")