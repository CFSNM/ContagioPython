import click
import numpy as np

@click.group()
@click.option('--archivomatriz',
              prompt=True,
              help='Ruta donde se encuentra definida la matriz de adyacencia')
@click.pass_context
def cli(ctx,archivomatriz):
    ctx.obj = archivomatriz

@cli.command(name='ejecutarAlgoritmo')
@click.option('--semillauno',
              default=6,
              help='Semilla numero 1')
@click.option('--semillados',
              default=7,
              help='Semilla numero 2')
@click.option('--umbral',
              default=0.4,
              help='Umbral para establecer contagio')
@click.pass_context
def ejec_algoritmo(ctx,semillauno,semillados,umbral):

     A = extraer_matriz(ctx.obj)
     numero_nodos = len(A)
     print('La matriz de adyacencia A es ')
     print(A)
     print('Los nodos contagiados inicialmente son '+str(semillauno)+' y '+str(semillados))
     print('El umbral de contagio es '+str(umbral))

     nodos_contagiados = np.zeros((1, numero_nodos))
     nodos_contagiados[0][semillauno] = 1
     nodos_contagiados[0][semillados] = 1

     print('**********************************************')
     print('EMPIEZA EL ALGORITMO')

     iter = 1
     while(True):
         nuevos_nodos_contagiados = []
         print('**********************************************')
         print('**********************************************')
         print('Iteración nº'+str(iter))
         print('**********************************************')
         for nodo in range(numero_nodos):
            if(nodos_contagiados[0][nodo] == 1):
                continue
            fila = A[nodo, :]
            nodos_totales_nodo = sum(fila)
            nodos_contagiados_nodo = sum(np.multiply(fila, nodos_contagiados[0, :]))
            umbral_nodo = nodos_contagiados_nodo/nodos_totales_nodo
            if(umbral_nodo >= umbral):
                nuevos_nodos_contagiados.append(nodo)
                print('El nodo '+str(nodo)+' ha sido contagiado')


         if (len(nuevos_nodos_contagiados) == 0):
             print('No hay nuevos nodos contagiados en la iteración nº'+str(iter))
             print('El algoritmo ha terminado...')
             break

         iter = iter + 1
         nodos_contagiados = actualizar_nodos_contagiados(nodos_contagiados, nuevos_nodos_contagiados)



def extraer_matriz(path):

    file = open(path,'r')
    filas = file.readlines()
    num_nodos = len(filas)
    matriz = np.zeros((num_nodos, num_nodos))
    cont_fila = 0
    cont_col = 0
    for fila in filas:
        elementos = fila.split()
        cont_col = 0
        for elem in elementos:
            matriz[cont_fila][cont_col] = elem
            cont_col = cont_col + 1
        cont_fila = cont_fila + 1

    return matriz

def actualizar_nodos_contagiados(nodos_contagiados_actuales, nuevos_nodos_contagiados):

    nodos_contagiados = nodos_contagiados_actuales

    for index in nuevos_nodos_contagiados:
        nodos_contagiados[0][index] = 1

    return nodos_contagiados


if __name__ == '__main__':
    cli()