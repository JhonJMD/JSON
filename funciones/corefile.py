import json
import os
MY_DATABASE = ''

def NewFile(*param):
    with open(MY_DATABASE,"w") as wf:
        json.dump(param[0],wf,indent=4)
def checkFile(*param):
    if (os.path.isfile(MY_DATABASE)):
        print('Lo encontre')
    else:
        if(len(param)>0):
            NewFile(param[0])

# def checkFile(archivo:str)->bool:
#     try:
#         with open(archivo,"r") as wf:
#                         return True
#     except FileNotFoundError:
#         return False
#     except IOError as e:
#         return False