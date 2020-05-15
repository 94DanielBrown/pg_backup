from setuptools import setup, find_packages

with open('README.md', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    description='Database backups locally or to AWS S3.',
    long_description=readme,
    author='Daniel',
    author_email='94daniel.brown@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
)