import click

@click.group()
@click.option('--archivomatriz',
              prompt=True,
              help='Ruta donde se encuentra definida la matriz de adyacencia')
@click.pass_context
def cli(ctx,archivomatriz):
    ctx.obj = archivomatriz

@cli.command(name='ejecutarAlgoritmo')
@click.option('--semillauno',
              default=7,
              help='Semilla numero 1')
@click.option('--semillados',
              default=8,
              help='Semilla numero 2')
@click.option('--umbral',
              default=0.4,
              help='Umbral para establecer contagio')
@click.pass_context
def ejec_algoritmo(ctx,semillauno,semillados,umbral):

     matriz = extraer_matriz(ctx.obj)
     click.echo(matriz)
     click.echo(semillauno)
     click.echo(semillados)
     click.echo(umbral)

def extraer_matriz(path):

    matriz = []

    return matriz




if __name__ == '__main__':
    cli()