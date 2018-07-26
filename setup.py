from setuptools import setup, find_packages

setup(
    name='Apache-Local-Domain',
    version='1.0.0',
    packages=find_packages(exclude=['.venv']),
    url='',
    license='MIT',
    author='Alireza Km',
    author_email='alitm28@gmail.com',
    description='Create Domain in Localhost on Apache2',
    install_requires=[
        'click',
        'decorator',
        'six',
        'validators',
    ],
    entry_points={
        'console_scripts': [
            'aldomain=ApacheLocalDomain.app.cli:cli'
        ]
    }
)
