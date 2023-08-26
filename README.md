# software-testing-python
记录学习自动化软件测试的过程
## 2023-8-26
### json
1. json.load()与json.loads()的区别
    >前者用于解析文件,后者用于的解析json格式的字符串
2. json.loads()的注意事项
    >如果字符串中 JSON 对象之间没有逗号分隔，或者没有包含在一个数组（[]）中，就会导致 "Extra data" 错误
3. 深拷贝
    > ``````python
    > team1 =[
    > {'name':'乔丹',
    > 'height':198},
    > {name':‘姚明',
    > 'height':223}
    > ]
    > #如果直接使用team2 = team1 两个变量实际上是同一个
    > #可以使用以下方式进行深拷贝
    > team2 = json.loads(json.dumps(team1))