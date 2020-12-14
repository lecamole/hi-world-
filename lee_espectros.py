#Librerias genericas
import numpy as np
import matplotlib.pyplot as plt

#Libreria manejo de fits
from astropy.io import fits

#nombre del archivo
archivo= "spSpec-51789-0398-288.fits"

#abrir archivo
hdu=fits.open(archivo)
#cargar seccion de datos del archivo
datos=hdu[0].data
#encabezado
encabezado = hdu[0].header
#seleccionar informacion de espectros
espectro=datos[0,:]
coeff0=encabezado['COEFF0']
coeff1=encabezado['COEFF1']
Z=encabezado['Z']

#corrección por longitud de onda
j=np.arange(0,len(espectro)) #índice pixeles
lam=10**(coeff0+coeff1*j) #eje x corregido por longitud de onda

#correción por redshift
lamb_orig=lam/(Z+1)

#graficar
#plt.plot(espectro)
#plt.plot(lam,espectro,label='Espectro corregido por $\lambda$')
plt.plot(lamb_orig,espectro,label='Espectro corregido por Z')
#plt.vlines()
plt.text(6550,max(espectro)+90,r'$H\alpha 6564\AA$',rotation=90)
plt.text(4990,250,r'$[OIII] 5007\AA$',rotation=90)
plt.ylim(0,450)
plt.legend(loc='best')
plt.savefig('Líneasbullcrap.png')
plt.show() 


#Agregar informacion de lambda
#Leer 

#hdr=hdu[0].header
#corrimiento=hdr["Z"]
