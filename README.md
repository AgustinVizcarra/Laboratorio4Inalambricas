# Laboratorio4Inalambricas
Al momento de usar el script en python para la experiencia del laboratorio 4 se debe considerar realizar el comando de recepcion en el nodo #5
y derivarlo con un formato .txt de la siguiente manera
iperf -s -u -i 1 > prueba.txt
Sin embargo, dado que esto se almacenará dentro del contenedor para poder procesarla en python es necesario extraerlo para ello se ha añadido
ciertos comandos con respecto a LXC para enviar archivos desde el host al contenedor y viceversa. Luego se ha añadido un script adicional para
realizar las iteraciones por cada Bitrate configurado en experiencia4.sh con lo que se enviará de manera secuencial e iterando por cada bitrate
dado. Finalmente una vez que se extraiga el archivo .txt se deberá modificar el archivo en detector .py en funcion al nombre del archivo que se
tenga para que este pueda detectar el throughput por cada nodo y throughput general para así ir llenando la tabla por cada actividad dada.
Saludos,
Agustin
