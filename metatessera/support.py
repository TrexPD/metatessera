from rich import print
import click


@click.command()
@click.option('-e', '--extensions', is_flag=True, default=True, type=click.BOOL, help='Supported extensions of metatessera!')
def extensions(extensions: bool) -> str:
    if extensions:
        print("""
 Supported extensions:
   
 [blue].bat  [/] -> Batch Files                                      [blue].php[/]   -> Hypertext Preprocessor
 [blue].csv  [/] -> Comma Separated Values                           [blue].py [/]   -> Python File
 [blue].html [/] -> Hypertext Markup Language                        [blue].r  [/]   -> R File
 [blue].json [/] -> JavaScript Object Notation                       [blue].rs [/]   -> Rust File
 [blue].js   [/] -> JavaScript File                                  [blue].rtf[/]   -> Rich Text Format
 [blue].lock [/] -> Lock File                                        [blue].sh [/]   -> Shell Script
 [blue].toml [/] -> Tom's Obvious, Minimal Language                  [blue].txt[/]   -> Plain Text File
 [blue].md   [/] -> Markdown Documentation File                      [blue].xml[/]   -> eXtensible Markup Language
""")