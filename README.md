# lab1_Distribuidos
------------------------------
Programa utilizado:
    Python 3.11.3
Librerias:
    Numpy = version 1.26.2
    MPI = version 10.1.3
-------------------------------
Para poder instalar la herramienta de MPI en Windows se debe realizar el siguiente comando:
    ->"python -m pip install mpi4py"
Luego se tiene que descargar e instalar MS-MPI del link:
    https://learn.microsoft.com/es-mx/message-passing-interface/microsoft-mpi
    Tendrá que seleccionar "msmpisetup.exe" y poner siguiente.
ATENCIÓN: Si aparece que no se reconoce el comando mpiexec debes agregar al PATH de tus variables de entorno el programa instalado anteriormente.
---------------------------------
Para poder Ejecutar los programas debe poner en el terminal los siguientes comandos dependiendo de la solución que desea implementar:
    ->lab1Eventos = python .\lab1Eventos.py
    ->lab1Monolitico = python .\lab1Monolitico.py
    ->lab1Servicios = mpiexec -n 4  python .\lab1Servicios.py

