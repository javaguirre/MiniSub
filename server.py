#!/usr/bin/env python2

import SimpleHTTPServer
import SocketServer
# TODO use argparse for 2.7
from optparse import OptionParser


parser = OptionParser()
parser.add_option('-p', '--port', dest='port',
                  help='Server port', metavar='PORT')
(options, args) = parser.parse_args()

PORT = 8000
if options.port is not None:
    PORT = int(options.port)

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
