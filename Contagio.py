import click

@click.group()
@click.option('--matriz',
              default='matriz',
               help='Matriz de adyacencia')
@click.pass_context
def cli(ctx,matriz):
    ctx.obj = matriz

@cli.command(name='ejecutarAlgoritmo')
@click.option('--semillauno',
              default=1,
              help='Semilla numero 1')
@click.option('--semillados',
              default=2,
              help='Semilla numero 2')
@click.option('--umbral',
              default=0.4,
              help='Umbral para establecer contagio')
@click.pass_context
def ejec_algoritmo(ctx,semillauno,semillados,umbral):

     matriz = ctx.obj
     click.echo(matriz)
     click.echo(semillauno)
     click.echo(semillados)
     click.echo(umbral)



if __name__ == '__main__':
    cli()