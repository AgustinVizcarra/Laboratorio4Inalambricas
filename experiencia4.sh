#!/bin/bash
declare -a arreglo=( "0.5m" "1.5m" "3m" "5m" "6m" "7m" "8m" "9m" "10m" "11m" "12.5m" "14m" )
for i in "${arreglo[@]}"
do
    iperf -c 10.0.0.5 -u -b $i -l 1470 -i 1 -t 30
    echo "Envio terminado"
    sleep 1
done
echo "Actividad terminada"