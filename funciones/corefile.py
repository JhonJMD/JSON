import json
MI_DATABASE =" "
def NewFile(data:dict):
    with open(MI_DATABASE,"w") as wf:
        json.dump(data,wf,indent=3)
        wf.close()
def checkFile(archivo:str)->bool:
    try:
        with open(archivo,"r") as wf:
                        return True
    except FileNotFoundError:
        return False
    except IOError as e:
        return False