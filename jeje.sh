#!/bin/bash

# URL que deseas abrir
URL="https://www.youtube.com/watch?v=tWklp-YFQgQ"

# Bucle para abrir la URL 100 veces
for i in {1..100}
do
  xdg-open $URL
  sleep 1 # Opcional: Pausa de 1 segundo entre cada apertura
done

