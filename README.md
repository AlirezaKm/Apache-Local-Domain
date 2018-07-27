## Apache Local Domain
Create Local Domain for Apache Web Service

#### Description
    Create own Domain on Your Local System
    
#### Installation

##### Debian Base Distros (Debian,Ubuntu,...)
    python3 -m pip install -U Apache-Local-Domain
    
##### Other Distros (Arch , Fedora , ...)
    $ git clone https://gitlab.com/toys-projects/Apache-Local-Domain.git
    $ cd Apache-Local-Domain
    $ python3 setup.py --help customize-configs    
    ...
    Options for 'CustomizeConfigurations' command:
      --debug-mode (-d)                    Debug mode [False]
      --apache-modules-path (-m)           Apache Modules Path
                                            [/etc/apache2/mods-enabled/]
      --hosts (-h)                         Hosts file [/etc/hosts]
      --virtual-hosts-available-path (-a)  VirtualHosts available Path
                                           [/etc/apache2/sites-available/]
      --virtual-hosts-enabled-path (-v)    VirtualHosts Enabled Path
                                           [/etc/apache2/sites-enabled/]
      --extension (-e)                     VirtualHosts extension [.conf]
    ...
##### example Customize Configuration
    $ python3 setup.py customize_configs \
        --debug-mode False \
        -m /etc/httpd/modules/ \          
        -a /etc/httpd/vhosts-available/ \
        -v /etc/httpd/vhosts-enabled/ \
        -e .dom

after of Generate New file Configuration Complete , run:

    $ sudo python3 setup.py install
   
#### Usage 1
    $ apacheld --help
    Usage: apacheld [OPTIONS] COMMAND [ARGS]...
    
    Options:
      --help  Show this message and exit.
    
    Commands:
      php   Initialize PHP Template
      wsgi  Initialize WSGI Template
      
##### Usage 2
    $ apacheld wsgi --help
    Usage: apacheld wsgi [OPTIONS]
    
      Initialize WSGI Template
    
    Options:
      -d, --domain TEXT               This Domain is Created (ServerName)  ,
                                      example: example.com  [required]
      -r, --root TEXT                 DocumentRoot of Your website (DocumentRoot)
                                      , example: /srv/http/MyWebSite/  [required]
      -w, --wsgiscript TEXT           WSGIScriptAlias of Your website
                                      (WSGIScriptAlias) , example:
                                      /srv/http/MyWebSite/wsgi.py  [required]
      -v, --virtualenv-folder-name TEXT
                                      Virtualenv Folder name in Project PATH
                                      (default: .venv)  [required]
      -e, --email TEXT                Your Email (ServerAdmin) , example:
                                      example@example.com
      --http2                         Enable HTTP2 Protocol
      --enable-static                 Enable using static files
      -s, --static-folder-name TEXT   static folder name in Project PATH (default:
                                      static)  [required with enable_static]
      --help                          Show this message and exit.
      
##### Usage 3
    $ apacheld php --help 
    Usage: apacheld php [OPTIONS]
    
      Initialize PHP Template
    
    Options:
      -d, --domain TEXT  This Domain is Created (ServerName)  , example:
                         example.com  [required]
      -r, --root TEXT    DocumentRoot of Your website (DocumentRoot) , example:
                         /srv/http/MyWebSite/  [required]
      -e, --email TEXT   Your Email (ServerAdmin) , example: example@example.com
      --http2            Enable HTTP2 Protocol
      --help             Show this message and exit.
      
#### Note
    * To use This Program You should Run it with `sudo`
    
#### TODO
- [x] Check enable http2 module or not
- [x] add new Validations for inputs (documentroot , wsgiscript , virtualenv ,...)
- [ ] link Configure file to /etc
- [ ] Builtin sudo Execute
