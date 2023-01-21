from setuptools import setup, find_packages

setup(
    name='metatessera',
    version='0.0.5',
    license='BSD 3-Clause',
    author='Paulo Daniel',
    platforms=['Windows', 'Linux', 'BSD'],
    url='https://github.com/TrexPD/metatessera.git',
    download_url='https://github.com/TrexPD/metatessera.git',
    description='metatessera is a cli app, which shows the whole summary of a file!',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click', 'rich', 'hashlib'
    ],
    entry_points="""
    [console_scripts]
    meta = metatessera_en-US:main
    """
)