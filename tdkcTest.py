import re
fn = 'tdkc.txt'

def parseString2(string):
    pattern = '\d\d:\d\d'
    timeRule = re.compile(pattern)
    timeList= timeRule.findall(string)
    if timeList != None:
        print(f"時間2:{timeList}")

def parseString3(string):
    pattern = '\d:\d\d:\d\d'
    timeRule = re.compile(pattern)
    timeList= timeRule.findall(string)
    if timeList != None:
        print(f"時間3:{timeList}")

def parseString4(string):
    pattern = 'The Dark Knight Rises'
    timeRule = re.compile(pattern)
    timeList= timeRule.findall(string)
    if timeList != None:
        print(f"TDKR:{timeList}")

file_Obj = open(fn)
data = file_Obj.read()
parseString2(data)
parseString3(data)
parseString4(data)

file_Obj.close()
