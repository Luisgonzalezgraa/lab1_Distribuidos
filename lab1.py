from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
#Se crean unos datos en el worker RANK_0
if rank == 0:
    data = {'key1': [7, 2.72, 2+3j], 'key2': ('abc','xyz')}
else:
    data = None

# Transmitir los datos de RANK_0 a todos los workers
data = comm.bcast(data, root=0)

# Agregar el RANK id a los datos para el print
data['key1'].append(rank)

print(f"Rank: {rank}, data: {data}")