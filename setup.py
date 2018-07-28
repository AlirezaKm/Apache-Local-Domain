from setuptools import setup, find_packages, Command
import os

currentPath = os.path.dirname(os.path.abspath(__file__))


def readme():
    with open(os.path.join(currentPath, 'README.md'), 'r') as file:
        return file.read()


class CustomizeConfigurations(Command):
    """
    Run my command.
    """
    description = 'Customize Configurations'

    user_options = [
        ('debug-mode=', 'd', 'Debug mode [False]'),
        ('apache-modules-path=', 'm', 'Apache Modules Path[/etc/apache2/mods-enabled/]'),
        ('hosts=', 'h', 'Hosts file [/etc/hosts]'),
        ('virtual-hosts-available-path=', 'a', 'VirtualHosts available Path [/etc/apache2/sites-available/]'),
        ('virtual-hosts-enabled-path=', 'v', 'VirtualHosts Enabled Path [/etc/apache2/sites-enabled/]'),
        ('extension=', 'e', 'VirtualHosts extension [.conf]'),
        ]

    def initialize_options(self):
        self.debug_mode = 'False'
        self.apache_modules_path = '/etc/apache2/mods-enabled/'
        self.hosts = '/etc/hosts'
        self.virtual_hosts_available_path = '/etc/apache2/sites-available/'
        self.virtual_hosts_enabled_path = '/etc/apache2/sites-enabled/'
        self.extension = '.conf'

    def finalize_options(self):
        # if self.debug_mode is None:
        #     raise Exception("Parameter --debug-mode is missing")
        # if self.apache_modules_path is None:
        #     raise Exception("Parameter --apache-modules-path is missing")
        # if self.hosts is None:
        #     raise Exception("Parameter --hosts is missing")
        # if self.virtual_hosts_available_path is None:
        #     raise Exception("Parameter --virtual-hosts-available-path is missing")
        # if self.virtual_hosts_enabled_path is None:
        #     raise Exception("Parameter --virtual-hosts-enabled-path is missing")
        # if self.extension is None:
        #     raise Exception("Parameter --extension is missing")

        if not os.path.isdir(self.apache_modules_path):
            raise Exception("directory does not exist: {0}".format(self.apache_modules_path))
        if not os.path.isdir(self.virtual_hosts_available_path):
            raise Exception("directory does not exist: {0}".format(self.virtual_hosts_available_path))
        if not os.path.isdir(self.virtual_hosts_enabled_path):
            raise Exception("directory does not exist: {0}".format(self.virtual_hosts_enabled_path))

    def run(self):
        # Create Configuration file
        with open(os.path.join(currentPath, 'ApacheLocalDomain/templates/configuration.template'), 'r') as file:
            content = file.read()
            content = content \
                .replace('{DEBUG}', self.debug_mode.title()) \
                .replace('{APACHE2_MODULES_PATH}', self.apache_modules_path) \
                .replace('{HOSTS}', self.hosts) \
                .replace('{VIRTUAL_HOSTS_AVAILABLE_PATH}', self.virtual_hosts_available_path) \
                .replace('{VIRTUAL_HOSTS_ENABLED_PATH}', self.virtual_hosts_enabled_path) \
                .replace('{EXTENSION}', self.extension if self.extension.startswith(".") else "." + self.extension)

        # Create Backup from old config file
        with open(os.path.join(currentPath, 'ApacheLocalDomain/app/configs.py'), 'r') as old:
            with open(os.path.join(currentPath, 'ApacheLocalDomain/app/configs-bk.py'), 'w') as bk:
                bk.write(old.read())

        # Create Config file
        with open(os.path.join(currentPath, 'ApacheLocalDomain/app/configs.py'), 'w') as file:
            file.write(content)


setup(
    name='Apache-Local-Domain',
    version='1.1.2',
    packages=find_packages(exclude=['.venv', 'build', 'dist', 'Apache_Local_Domain.egg-info']),
    url='https://gitlab.com/toys-projects/Apache-Local-Domain',
    license='GPLv3',
    author='Alireza Km',
    author_email='alitm28@gmail.com',
    description='Create Domain in Localhost on Apache2',
    long_description=readme(),
    long_description_content_type="text/markdown",
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
    },
    cmdclass={
        'customize_configs': CustomizeConfigurations
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)