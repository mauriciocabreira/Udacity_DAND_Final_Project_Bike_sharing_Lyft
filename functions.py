import math

def haverccsine2(lat1, lon1, lat2, lon2):
    R = 6372800  # Earth radius in meters
    #lat1, lon1 = coord1
    #lat2, lon2 = coord2
       
    phi1, phi2 = math.radians(lat1), math.radians(lat2) 
    dphi       = math.radians(lat2 - lat1)
    dlambda    = math.radians(lon2 - lon1)
    
    a = math.sin(dphi/2)**2 + \
        math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    
    #return 2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a))
    #return values in KM, 2 decimals
    return 2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a)) 
    


def haversine(coord1, coord2):
    R = 6372800  # Earth radius in meters
    lat1, lon1 = coord1
    lat2, lon2 = coord2
       
    phi1, phi2 = math.radians(lat1), math.radians(lat2) 
    dphi       = math.radians(lat2 - lat1)
    dlambda    = math.radians(lon2 - lon1)
    
    a = math.sin(dphi/2)**2 + \
        math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    
    return 2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a))