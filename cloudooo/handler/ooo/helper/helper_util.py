import sys
import os

def getServiceManager(host, port, uno_path, office_binary_path):
  """Get the ServiceManager from the running OpenOffice.org.
  """
  # Add in sys.path the path of pyuno
  if uno_path not in sys.path:
    sys.path.append(uno_path)
  fundamentalrc_file = '%s/fundamentalrc' % office_binary_path
  if os.path.exists(fundamentalrc_file) and \
      'URE_BOOTSTRAP' not in os.environ:
    os.putenv('URE_BOOTSTRAP', 'vnd.sun.star.pathname:%s' % fundamentalrc_file)
  import uno
  # Get the uno component context from the PyUNO runtime
  uno_context = uno.getComponentContext()
  # Create the UnoUrlResolver on the Python side.
  url_resolver = "com.sun.star.bridge.UnoUrlResolver"
  resolver = uno_context.ServiceManager.createInstanceWithContext(url_resolver,
                                                                  uno_context)
  # Connect to the running OpenOffice.org and get its
  # context.
  uno_connection = resolver.resolve("uno:socket,host=localhost,port=4062;urp;StarOffice.ComponentContext")
  # Get the ServiceManager object
  return uno_connection.ServiceManager
