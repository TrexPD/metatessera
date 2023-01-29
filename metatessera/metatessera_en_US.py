from time import ctime, strptime, strftime
from support import extensions
from hashs import hash_calculation
from rich.panel import Panel
from re import sub, findall
from pathlib import Path
from rich import print
import click



APP_VERSION: str = '0.0.9 (2023-01-27)'

@click.group()
@click.version_option(APP_VERSION)
def cli_app():
    pass


def amount_of_characters(text: str) -> int: 
    return len(text)


def amount_of_letters(text: str) -> int:  
    letters: list = findall(r'[a-zA-ZÀ-ú]', text)
    return len(letters)


def amount_of_words(text: str) -> int:
    words: list = sub(r"\W+", " ", text)
    return len(words.split())


def amount_of_numbers(text: str) -> int:
    numbers: list = findall(r'\d', text)
    return len(numbers)


def number_of_lines(file: str) -> int:
    with open(f"{file}", 'rt', encoding='utf-8') as archive:
        lines = archive.readlines(4096)
        return len(lines)


@cli_app.command()
@click.argument('file', type=click.STRING, envvar='METAFILE')
def file(file: str) -> str:

    if Path(file).is_file():
        file_path = Path(file)
        created = strptime(ctime(file_path.stat().st_ctime))
        modified = strptime(ctime(file_path.stat().st_mtime))
        last_access = strptime(ctime(file_path.stat().st_atime))
        try:
            with open(file=file, mode='rt', encoding='utf-8') as archive:
                read_file: str = archive.read(4096)
        except FileNotFoundError:
            click.echo(f"The file {file} was not found!\n")
        except UnicodeDecodeError:
            click.echo('Unsupported file, run the command "meta --extensions" to see supported file types!\n')
        except:
            click.echo("Sorry, unknown error... :(\n")
        else:
            print(
Panel(f"""[yellow][bold]DETAILS:[/][/]

[blue]File name              [/]           [white][b]: {file_path.stem}                              [/]
[blue]File path              [/]           [white][b]: {file_path.absolute()}                        [/]
[blue]File size              [/]           [white][b]: {(int(file_path.stat()[6]) / 1024):.2f} KB    [/]
[blue]File extension         [/]           [white][b]: {file_path.suffixes}                          [/]
[blue]No. of characters      [/]           [white][b]: {amount_of_characters(read_file)}             [/]
[blue]No. of words           [/]           [white][b]: {amount_of_words(read_file)}                  [/]
[blue]No. of letters         [/]           [white][b]: {amount_of_letters(read_file)}                [/]
[blue]Quantity of No.        [/]           [white][b]: {amount_of_numbers(read_file)}                [/]
[blue]Quantity of lines      [/]           [white][b]: {number_of_lines(file)}                       [/]
[blue]Created (Date/Time)    [/]           [white][b]: {strftime('%d/%m/%Y %X %z', created)}         [/]
[blue]Modified (Date/Time)   [/]           [white][b]: {strftime('%d/%m/%Y %X %z', modified)}        [/]
[blue]Last Access (Date/Time)[/]           [white][b]: {strftime('%d/%m/%Y %X %z', last_access)}     [/]
{hash_calculation(file)}"""))

    elif Path(file).is_dir():
        click.echo(f'The "{file}" is a directory, and cannot be read!\n')
    else:
        click.echo(f'The "{file}" is an incorrect path or a non-existent file!\n')


if __name__ == '__main__':
    cli_app.add_command(file)
    cli_app.add_command(extensions)
    cli_app()