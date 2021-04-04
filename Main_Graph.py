
import collections
import io
# import Bidirectional_Search
import ids
import eel
import json

eel.init("frontend")



mygraph = collections.defaultdict(list)
mynodes = list()



myinput = """5	5
2	2	2	x	2
2r	1	1	1	2
2	x	1b	1	x
2	1	x	1	2
2	2	2p	2	x"""



# address = "test1.txt"
# with open(address) as reader :
#     # print(reader.read())
#     myinput = reader.read()
# # print(myinput)


buf = io.StringIO(myinput)
n , m = map(int ,buf.readlines(1)[0].replace("\t" , " ").replace("\n" , "").split(" "))
for i in range(m):
    buffread = buf.readlines(1)[0].replace("\t" , " ").replace("\n" , "").split(" ")
    mynd = []
    for ii in range(n) : 
        mynd.append(buffread[ii])
    mynodes.append(mynd)

# x = n
# for i in mynodes :
#     print(i , end=" ")
#     if x == 1 :
#         x = n
#         print()
#     else:
#         x -= 1
      
for i in range(n):
    for ii in range(m) :
        pos = str(i) + str(ii)
        
        kind = 'o'
        if mynodes[i][ii].count('r') > 0 :
            kind = 'r'
        elif mynodes[i][ii].count('p') > 0 :
            kind = 'p'
        elif mynodes[i][ii].count('b') > 0 :
            kind = 'b'
        elif mynodes[i][ii].count('x') > 0 :
            kind = 'x'
        mygraph[pos].append(kind)

        if kind == 'x':
            mygraph[pos].append(-1)
            continue
        elif not mygraph[pos][0] == 'o' :
            mygraph[pos].append(mynodes[i][ii][:-1])
        else :
            mygraph[pos].append(mynodes[i][ii])

        if i > 0 and not mynodes[i-1][ii] == 'x' :
            cc = mynodes[i-1][ii]
            cc = cc.replace('r',"").replace('b',"").replace('p',"")
            mygraph[pos].append((str(i-1) + str(ii) , cc))

        if i < (n-1) and not mynodes[i+1][ii] == 'x' : 
            cc = mynodes[i+1][ii]
            cc = cc.replace("r","").replace("b","").replace("p","")
            mygraph[pos].append((str(i+1) + str(ii) , cc))

        if ii > 0 and not mynodes[i][ii-1] == 'x' : 
            cc = mynodes[i][ii-1]
            cc = cc.replace("r","").replace("b","").replace("p","")
            mygraph[pos].append((str(i) + str(ii-1) , cc))

        if ii < (m-1) and not mynodes[i][ii+1] == 'x' : 
            cc = mynodes[i][ii+1]
            cc = cc.replace("r","").replace("b","").replace("p","")
            mygraph[pos].append((str(i) + str(ii+1) , cc))


# print(mygraph)
# print(Bidirectional_Search.BidirectionalSearch(mygraph , "10" , "42"))

def get_json_result(results):
    return json.dumps(results)

@eel.expose
def runIDS():    
    q = ids.iterativeDeepening(mygraph , "10" , "42")
    print(q)
    return get_json_result({
        "graph" : mygraph,
        "path" : q,
    });

eel.start('index.html' ,size=(500,500))
