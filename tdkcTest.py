import re
fn = 'tdkc.txt'

def parseString2(string):
    pattern = '\d\d:\d\d'
    timeRule = re.compile(pattern)
    timeList= timeRule.findall(string)
    if timeList != None:
        print(f"時間:{timeList}")

def parseString3(string):
    pattern = '\d:\d\d:\d\d'
    timeRule = re.compile(pattern)
    timeList= timeRule.findall(string)
    if timeList != None:
        print(f"時間:{timeList}")


file_Obj = open(fn)
data = file_Obj.read()
parseString2(data)
parseString3(data)
file_Obj.close()
