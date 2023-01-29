# Metatessera

#### Metatessera is a cli app, which shows the whole summary of a file!

### Libraries used:

```click```
```hashlib```
```pathlib```
```re```
```rich```
```time```

### Installation:

#### Clone the project to the local repository (your PC).

```git clone https://github.com/TrexPD/metatessera.git```

#### Enter the metatessera folder/directory and type the command below as ADM on windows or root on linux and the like (if you need it).

```python setup.py install```


### Use in practice:

#### Optional parameters:

```
--version   Show the version and exit.
--help      Show this message and exit.
```

#### Calling the app and entering data!

###### Command 'file':

```daniel@nix-os: $ meta file teste.txt```

###### Ouput:
```
DETAILS:

File name                         : teste
File path                         : /tmp/teste.txt
File size                         : 72.92 KB
File extension                    : ['.txt']
No. of characters                 : 4096
No. of words                      : 675
No. of letters                    : 3173
Quantity of No.                   : 166
Quantity of lines                 : 83
Created (Date/Time)               : 28/01/2023 21:36:13 -0300
Modified (Date/Time)              : 28/01/2023 21:00:33 -0300
Last Access (Date/Time)           : 28/01/2023 21:36:16 -0300

CHECKSUM:

MD5                               : 858684252b377d8937dbe24c5c2b0017
SHA1                              : 3ddb912c428b2325cd09696ddf5f2cd7ba7d65cf
SHA224                            : fe29130b0d37771a06c83f227c6fc218cecdd1bf00f19b466a9cd063
SHA256                            : 4fcb6a783ae04e6193567b7794f184522cbc54f850108e565be61c1efedbcb38
SHA384                            :
dfbe120525e28ac50a34eff9c656089cbf869f14764b7efc6397743b2dde2cae3e52165ee617cd70956dc86bd1be2aa9
SHA512                            :
eac3db359f671c050374c0b2d5101d529f7997b4b33ff1a068b80efa463c23fbba05e7107d35dd6866fd0bc0d7789841bd0fc6a317066ece6f62ba8458391731
```


###### Command 'extensions':

```daniel@nix-os: $ meta extensions```

###### Ouput:
```
Supported extensions:

.bat   -> Batch Files                                      .php   -> Hypertext Preprocessor
.csv   -> Comma Separated Values                           .py    -> Python File
.html  -> Hypertext Markup Language                        .r     -> R File
.json  -> JavaScript Object Notation                       .rs    -> Rust File
.js    -> JavaScript File                                  .rtf   -> Rich Text Format
.lock  -> Lock File                                        .sh    -> Shell Script
.toml  -> Tom's Obvious, Minimal Language                  .txt   -> Plain Text File
.md    -> Markdown Documentation File                      .xml   -> eXtensible Markup Language
```


<h2 align="center">
    <strong>🌟
        Favorite este repositório 
    </strong>🌟
</h2>


<p align="center">
    Criado com ❤️ e python por
        <a href="https://github.com/TrexPD">
            Paulo Daniel (TrexPD)!
        </a>
</p> 