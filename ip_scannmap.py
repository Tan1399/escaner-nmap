import nmap 

#se escanea el puerto insertado
scanner= nmap.PortScanner()


#se pide al usuario que ingrese la ip

ip= input("Insert the ip andress ")

#se imprime la ip que se ha ingresado
print(" this is the ip you have entered ", ip)

#se escanea la ip
scanner.scan(ip)

#se imprime el estado de la ip
print(scanner.all_hosts())

