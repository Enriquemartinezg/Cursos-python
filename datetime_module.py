from datetime import datetime

birthday = datetime (1995, 5, 14, 15, 36, 33) #año/mes/dia/hora/minuto/segundo/microsegundo/zonahoraria
birthday.year
birthday.weekday

datetime.now() - birthday

mi_cumple = datetime.strptime("May 14, 1995", "%b %d, %Y") # el formato se encuentra en internet (datetime python3)
date_now_string = datetime.strftime(datetime.now(), '%b %d, %Y') #convierte una fecha en string