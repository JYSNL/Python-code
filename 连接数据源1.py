import json
jsonarray = '[{"word":"hello","count:55"},{“word”:"som","count":"12"}]'
print(jsonarray)
#字符串数组
jsonobj = '{"word":"seven","count":"2"}'
print(jsonobj)
print('')
#将json数据解码成python数据
json1 = json.loads(jsonobj)
print("json->python")
print(json1)
print(json1["word"])
print(json1["count"])
print('')
#将python数据编码成为json数据
python1 = {'name':'mike','password':'11111'}
print("python->json")
json2 = json.dumps(python1)
print(json2)
print(type(json2))
print('')