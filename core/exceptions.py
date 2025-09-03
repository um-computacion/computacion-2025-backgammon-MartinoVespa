def exceptions(response):
    if response == "l" or response == "t" or response == "listo" or response == "terminado":
        return(100, 100)
    
    