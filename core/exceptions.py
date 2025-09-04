def exceptions(response):
    if response == "l" or response == "t" or response == "listo" or response == "terminado":
        return(100, 100)
    if response in exitTerms:
        return(101, 101)
    
    loc = findSeparation(response)
    return(int(response[:loc]), int(response[loc+1:]))

def findSeparation(value):
    for i in range(len(value)):
        if (value[i] == ' ' or value[i] == ','):
            return i
        return 0
    
exitTerms = ("exit", "salir", "s")
