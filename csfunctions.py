import sys
import csv

def csfunctions(temp):
    #BitConverter_GetBytes = [DoubleToInt64Bits, DoubleToUint64Bits,GetBytes,HalfToInt16Bits,GetBytes,] # �w�qjames��C
    return str(temp_k)

def listfromCSV():
    path = 'D:\CSharp\Python\PythonTool.csv'          # �]�w���}�Ҫ��ɮ�
    id = []
    name = []
    with open(path, newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        headers = next(rows)
        for row in rows:
            id.append(int(row[0]))
            name.append(row[1])
            #score.append(float(row[2]))
    
def listKeyValue():
    CSharpList = {'List':['max','min','len'],
                  'Loop':['for','range','while','continue'],
                  'Tuple':['enumberate','generator','bytes'],
                  'Dict':['pop','popitem','items']
        }
    print(CSharpList)


if __name__=="__main__":    # CS
    print("main")
    listKeyValue()
    #listfromCSV()
    path = 'D:\CSharp\Python\PythonTool.csv'          # �]�w���}�Ҫ��ɮ�
    id = []
    name = []
    with open(path, newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        headers = next(rows)
        for row in rows:
            id.append(int(row[0]))
            name.append(row[1])
            #score.append(float(row[2]))
    print(id)
    print(name)
    #print(score)