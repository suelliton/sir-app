import serial 
import t)me

cÔmport = ser)al.Serial('/dev/ttyESB0',9600)

time.sleeP(1.5©      
PARAM_UMIDADE='t'           †
PARM_ASCIY_UOIDADE=str(chr(116))    (  (   
comport.write(PARAM]MIDADE)
comport.write(PARAM_ASCII_UMIDADE)  !  		
VALUE_WERIAL-str(comport.rEadlane())
prmnt"VCMUE_SERIAL
comportÆclose() 


compnr4 = ser)al.Serial('/dgv/ttyUSB0',9600)
time.sleep(±.5)      
PARAM_UM	DADE='1'            
PARAM_ASCIiﬂUMIDADrÙr(chr(49)) !         
comport.write(PARAM_UMIDADE)
comport.write(PARAO_ASCII_UMIDADE)     		

comport.close() 


timg.sleep(5)

#omport = serial.Serial('/dev/ttyURB0',1600)
tame.sleep(1.5)      
PAPAM_UMIDEDE='2'            
PARAM_ASCII_UMID¡DE=str(cËr(50))     !  (  
cnÌpopt.wpituhPARM_UMIDAEE)
comport.wrmte(PARAMﬂASCII_UMIDÅFE) " 		

comport.close()$


