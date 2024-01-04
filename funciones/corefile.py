import json
import os
MY_DATABASE =" "
def NewFile(data:dict):
    with open(MY_DATABASE,"w") as wf:
        json.dump(data,wf,indent=3)
        wf.close()
def checkFile(archivo:str)->bool:
    return os.path.isfile(MY_DATABASE)

# def checkFile(archivo:str)->bool:
#     try:
#         with open(archivo,"r") as wf:
#                         return True
#     except FileNotFoundError:
#         return False
#     except IOError as e:
#         return False