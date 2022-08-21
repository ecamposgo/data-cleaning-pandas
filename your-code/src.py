##Limpiar fechas

def fechas(date):
    
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    
    for i in months: 
        if date.find(i) >= 0:
            date = date.strip()
            date = date.replace('Reported','')
            
            if len(date) == 11:
                return date 
    
    return "01-01-1900"


#clasificacion de especies

def especies(species):
    
    species = species.lower()
    
    clases = ["white","blue","bull","grey","tiger","blacktip","zambesi","dusky","hammerhead","whaler","wobbegong","caribbean"]
    
    for clase in clases: 
        if species.find(clase) >= 0:
            
            return clase 
    
    return "unidentified species"

#formateo horas

def hora(time):
    
    import re
    
    patron = r'^[0-9]{2}h[0-9]{2}$'
    
    if re.match(patron, time):
        
        time = time.replace('h',':')    
        
        return time
    else:
        
        return "Unknown"


