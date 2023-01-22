from click import group
from metatessera.metatessera_en_US import main


@group('cli')
def cli():
    pass


cli.add_command(main())
cli()