from rich.text import Text
import hashlib


def hash_calculation(file_name: str) -> str:
    with open(f'{file_name}', 'rb') as archive:
        hash_md5 = hashlib.md5()
        hash_sha1 = hashlib.sha1()
        hash_sha224 = hashlib.sha224()
        hash_sha256 = hashlib.sha256()
        hash_sha384 = hashlib.sha384()
        hash_sha512 = hashlib.sha512()
        while True:
            data: bytes = archive.read(4096)
            if not data:
                break
            hash_md5.update(data)
            hash_sha1.update(data)
            hash_sha224.update(data)
            hash_sha256.update(data)
            hash_sha384.update(data)
            hash_sha512.update(data)
        return str(Text(f"""
[yellow][b]CHECKSUM:[/][/]

[blue]MD5   [/]                            [white][b]: {hash_md5.hexdigest()}[/][/]
[blue]SHA1  [/]                            [white][b]: {hash_sha1.hexdigest()}[/][/]
[blue]SHA224[/]                            [white][b]: {hash_sha224.hexdigest()}[/][/]
[blue]SHA256[/]                            [white][b]: {hash_sha256.hexdigest()}[/][/]
[blue]SHA384[/]                            [white][b]: {hash_sha384.hexdigest()}[/][/]
[blue]SHA512[/]                            [white][b]: {hash_sha512.hexdigest()}[/][/]"""))


if __name__ in "__main__":
    print(hash_calculation('setup.py'))