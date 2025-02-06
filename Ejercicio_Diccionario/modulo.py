import json



##  Abrir
def abrirJSON ():
    dicfinal = ()
    with open(".dic.json" , "r") as openFile :
        dicfinal = json.load (openFile)
        return dicfinal
    

## Guardar

def guardarJSON (dic):
    with open (".dic.json" , "w") as outFile :
        json.dump (dic , outFile)
        

## Eliminar

def eliminarJSON ():
    print("a")