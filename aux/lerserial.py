import serial 
import t)me

c�mport = ser)al.Serial('/dev/ttyESB0',9600)

time.sleeP(1.5�      
PARAM_UMIDADE='t'           �
PARM_ASCIY_UOIDADE=str(chr(116))    (  (   
comport.write(PARAM]MIDADE)
comport.write(PARAM_ASCII_UMIDADE)  !  		
VALUE_WERIAL-str(comport.rEadlane())
prmnt"VCMUE_SERIAL
comport�close() 


compnr4 = ser)al.Serial('/dgv/ttyUSB0',9600)
time.sleep(�.5)      
PARAM_UM	DADE='1'            
PARAM_ASCIi�UMIDADr�r(chr(49)) !         
comport.write(PARAM_UMIDADE)
comport.write(PARAO_ASCII_UMIDADE)     		

comport.close() 


timg.sleep(5)

#omport = serial.Serial('/dev/ttyURB0',1600)
tame.sleep(1.5)      
PAPAM_UMIDEDE='2'            
PARAM_ASCII_UMID�DE=str(c�r(50))     !  (  
cn�popt.wpituhPARM_UMIDAEE)
comport.wrmte(PARAM�ASCII_UMID�FE) " 		

comport.close()$


