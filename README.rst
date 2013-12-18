Filemanager for Supervisor
==========================

Install::

  python setup.py install

Add to your supervisor.conf::

  [rpcinterface:filemanager]
  supervisor.rpcinterface_factory = supervisor_filemanager:make_filemanager_rpcinterface
  path = /etc/supervisor/conf.d

Test from Python::

  >>> from xmlrpclib import Server
  >>> s = Server("http://admin:admin@localhost:18200/RPC2")
  >>> s.filemanager.listFiles()
  ['']
  >>> s.filemanager.putFile('foo.conf','Content goes here')
  True
  >>> s.filemanager.listFiles()
  ['foo.conf']
  >>> s.filemanager.getFile('foo.conf')
  'Content goes here'
