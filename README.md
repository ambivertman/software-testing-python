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

### 正则表达式

查询教程:[python进阶|正则表达式](https://www.byhy.net/tut/py/extra/regex/)

`re.sub()`可以的参数设置:

- `pattern`: 要查找的正则表达式模式。
- `replacement`: 要替换匹配到的模式的字符串。
- `string`: 要在其中执行替换操作的输入字符串。
- `count`: 可选参数，指定最大替换次数。默认值为 0，表示替换所有匹配项。
- `flags`: 可选参数，用于指定正则表达式的匹配标志。

其中`replacement`可以将**自定义的替换规则`subfunc()`**作为函数对象传递给函数. 其作用过程是一发现可以匹配的内容时就向函数一个match对象作为参数, 然后在subFunc()中完成替换后,返回给`re.sub()`

## 2023-8-27

### excel读写

将含有多个键值对的字典列表写入excel

```python
header_row = sheet.append(list(target_info[0].keys()))

for info in target_info:
    row = [info[key] for key in info]
    sheet.append(row)
```

## 2023-8-28

今天学到的小技巧:

1. 快速将字典的简直互换:

   ```python
   swapped_dict = {value: key for key, value in original_dict.items()}
   ```

2. 将列表连接成字符串

   ```python
   list_str = ','.join(list)
   ```

   

   
