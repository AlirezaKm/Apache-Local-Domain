## Apache Local Domain
Create Local Domain for Apache Web Service

##### Description
    Create own Domain on Your Local System
    
##### Installation
    python3 -m pip install -U Apache-Local-Domain
    
##### Usage 1
    $ apacheld --help
    Usage: apacheld [OPTIONS] COMMAND [ARGS]...
    
    Options:
      --help  Show this message and exit.
    
    Commands:
      php   Initialize PHP Template
      wsgi  Initialize WSGI Template
      
-
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
-
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
    * Just Support Debian Base Distros
    
#### TODO
- [ ] Check enable http2 module or not
- [ ] link Configure file to /etc
- [ ] Builtin sudo Execute
