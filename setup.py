from setuptools import setup, find_packages

setup(
    name='Apache-Local-Domain',
    version='1.0.3',
    packages=find_packages(exclude=['.venv', 'build', 'dist', 'Apache_Local_Domain.egg-info']),
    url='',
    license='GPLv3',
    author='Alireza Km',
    author_email='alitm28@gmail.com',
    description='Create Domain in Localhost on Apache2',
    install_requires=[
        'click',
        'decorator',
        'six',
        'validators',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'apacheld=ApacheLocalDomain.app.cli:cli'
        ]
    }
)
