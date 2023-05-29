import sys
import os
from pathlib import Path
from datetime import datetime
import time
import math
import textwrap

class ciLogger:

   def __init__( self,
                 colFormat = 'msgtype:10;80',
                 silent = True,
                 dateTimeFormat = "%d.%m.%Y %H:%M:%S" ):

      self.colFormat = colFormat

      self.msgTypeStrings = { 'success': "SUCCESS",
                              'error': "ERROR",
                              'warning': "WARNING",
                              'info': "INFO",
                              'debug': "DEBUG" }

      self.msgTypeFg = { 'success': 'green',
                             'error': 'red',
                             'warning': 'yellow',
                             'info': 'cyan',
                             'debug': 'violet' }
      
      self.logFilePath = ''
      self.logFileEncoding = ''

      self.silent = silent

      self.dateTimeFormat = dateTimeFormat

      self.timers = {}
      self.timers['runtime'] = time.perf_counter_ns()
   
      # Foreground (text) color codes
      self.fg = { 'black'  : '\33[30m',
                  'red'    : '\33[31m',
                  'green'  : '\33[32m',
                  'yellow' : '\33[33m',
                  'blue'   : '\33[34m',
                  'violet' : '\33[35m',
                  'cyan'   : '\33[36m',
                  'white'  : '\33[37m' }
      
      self.fgHtml = { 'black'  : '000000',
                  'red'    : 'C50F1F',
                  'green'  : '14A10E',
                  'yellow' : 'C19B00',
                  'blue'   : '0037DA',
                  'violet' : '881798',
                  'cyan'   : '00AAAA',
                  'white'  : 'FFFFFF' }
      
      # Background color codes (omit for terminal default)
      self.bg = { 'black'  : '\33[40m',
                  'red'    : '\33[41m',
                  'green'  : '\33[42m',
                  'yellow' : '\33[43m',
                  'blue'   : '\33[44m',
                  'violet' : '\33[45m',
                  'cyan'   : '\33[46m',
                  'white'  : '\33[47m' }
      
      # Text styles                  
      self.st = { 'bold'    : '\33[1m',
                  'faint'   : '\33[2m',
                  'italic'  : '\33[3m',
                  'underline': '\33[4m',
                  'inverted': '\33[7m' }
                        
      self.term = '\33[0m'
      
      if ( 'win32' in sys.platform ):
         os.system( 'color' )
   
   def is_number(self, s):
      '''
      Simple test of whether a string is a number
      '''
      try:
         float(s)
         return True
      except (ValueError, TypeError) as e:
         return False

   ##################################################
   # Regular print with text formatting
   ##################################################
   def ciPrint( self,
                s,
                msgType = '',
                end = '\n',
                colFormat = 'default',
                fg = '',
                st = '',
                bg = '' ):
   
      outStr = ""
      htmlStyle = ""

      if (fg in self.fg):
         outStr = outStr + self.fg[fg]
         htmlStyle = htmlStyle + "color: #" + self.fgHtml[fg] + ";"
      if (st in self.st):
         outStr = outStr + self.st[st]
      if (bg in self.bg):
         outStr = outStr + self.bg[bg]
         htmlStyle = htmlStyle + "background-color: #" + self.fgHtml[bg] + ";"
      
      formatLength = len( outStr )
      
      htmlOpen = "<span style='" + htmlStyle + "'>"
      htmlClose = "</span><br />\r\n"
      outHtml = "<span style='" + htmlStyle + "'>"
      outResidue = []
      outResidueHtml = []
      
      if ( colFormat == 'default' ):
         cols = self.colFormat.split(";")
      else:
         cols = colFormat.split(";")
      
      if ( len(cols) > 0 ):

         for col in cols:

            colspec = col.split(":")
            colStr = ""

            if ( self.is_number( colspec[-1] ) ):

               colWidth = int( colspec[-1] )

               if ( len( colspec ) > 1 and colWidth > 0 ):

                  if ( colspec[0] == 'msgtype' ):
                     if ( msgType in self.msgTypeStrings ):
                        colStr = ("{:<" + str( colWidth ) + "}:").format( self.msgTypeStrings[msgType] )[:colWidth]
                     else:
                        colStr = " " * colWidth
                     
                  elif ( colspec[0] == 'datetime' ):
                     if ( len( colspec ) == 2 ):
                        colStr = ("{:<" + str( colWidth ) + "}:").format( datetime.now().strftime( self.dateTimeFormat ) )[:colWidth]
                     elif ( len( colspec ) > 2 ):
                        customFormat = ":".join( colspec[1:-1] )
                        try:
                           colStr = ("{:<" + str( colWidth ) + "}:").format( datetime.now().strftime( customFormat ) )[:colWidth]
                        except:
                           colStr = " " * colWidth
                  elif ( colspec[0] == 'timer' ):
                     if ( len( colspec ) > 3 ):
                        if ( colspec[1] in self.timers and self.is_number( colspec[2] ) ):
                           colStr = ("%" + str( colWidth - 1 ) + "." + colspec[2] + "f" ) % ( ( time.perf_counter_ns() - self.timers[ colspec[1] ] )/1e9 )
                           colStr = ("{:<" + str( colWidth ) + "}:").format( colStr )[:colWidth]
                        else:
                           colStr = " " * colWidth
                  elif ( colspec[0] == 'timer_ns' ):
                     if ( len( colspec ) > 2 ):
                        if ( colspec[1] in self.timers ):
                           colStr = ("{:<" + str( colWidth ) + "}:").format( str( time.perf_counter_ns() - self.timers[ colspec[1] ] ) )[:colWidth]
                        else:
                           colStr = " " * colWidth
                  elif ( colspec[0] == 'blank' ):
                     colStr = " " * colWidth
                  elif ( colspec[0] == 'wrap' ):
                     if ( len ( s ) <= colWidth ):
                        colStr = s
                     else:
                        prepend = " " * ( len( outStr ) - formatLength )
                        rows = textwrap.wrap( s, colWidth )
                        outStr = outStr + rows[0]
                        for row in rows[1:]:
                           outResidue.append( prepend + row)
                           outResidueHtml.append( htmlOpen + outResidue[-1] + htmlClose )
                  
                  outStr = outStr + colStr
                  outHtml = outHtml + colStr.replace(' ', '&nbsp;')

               else:

                  outStr = outStr + ( "{:<" + str( colWidth ) + "}" ).format( s )
                  outHtml = outHtml + ( "{:<" + str( colWidth ) + "}" ).format( s ).replace( " ", "&nbsp;" )
   
      if ( end == '\n' ):
         # If end is set to newline, omit end parameter
         # to force use of OS default line ending
         if ( len( outResidue ) ):
            print( outStr )
            for line in outResidue:
               print( line )
            print( self.term, end = "" )
         else:
            print( outStr + self.term )
      else:
         if ( len( outResidue ) ):
            print( outStr, end = end )
            for line in outResidue:
               print( line, end = end )
            print( self.term, end = "" )
         else:
            print( outStr + self.term, end = end )
      
      if 'CI_LOGFILE' in os.environ:
         with open( os.environ['CI_LOGFILE'], 'a', encoding = os.environ['CI_ENCODING'] ) as logFile:
            logFile.write( outHtml + htmlClose )
            logFile.close()
   
   ##################################################
   # Short print aliases with preset color codes
   ##################################################
   
   def ciError( self, s ):
      self.ciPrint( s, msgType = 'error', fg = self.msgTypeFg['error'] )
   
   def ciWarning( self, s ):
      self.ciPrint( s, msgType = 'warning', fg = self.msgTypeFg['warning'] )
   
   def ciInfo( self, s ):
      self.ciPrint( s, msgType = 'info', fg = self.msgTypeFg['info'] )
   
   def ciDebug( self, s):
      self.ciPrint( s, msgType = 'debug', fg = self.msgTypeFg['debug'] )
   
   def ciSuccess( self, s ):
      self.ciPrint( s, msgType = 'success', fg = self.msgTypeFg['success'] )
   
   def ciInitHtml( self, filePath, encoding = 'iso-8859-15', useGlobally = True ):
      '''
      Initialize logging output to HTML file in addition to console output
      if useGlobally is set to true, Python class objects called by the current file,
      which also uses the cilogger module, will log to the same HTML file.
      '''

      self.logFilePath = Path( filePath )
      self.logFileEncoding = encoding
      with open( self.logFilePath, 'w', encoding = encoding) as logFile:
         logFile.write('<html>')
         logFile.write('<head>')
         logFile.write('<style>')
         logFile.write('body { background-color: #FFFFFF; font-family: "Lucida Console", "Ubuntu Mono", Courier, monospace; }')
         logFile.write('</style>')
         logFile.write('</head>')
         logFile.write("<body>")
         logFile.close()
      if ( useGlobally ):
         os.environ['CI_LOGFILE'] = str( os.path.abspath( self.logFilePath ) )
         os.environ['CI_ENCODING'] = encoding
   
   def ciFinalizeHtml( self, filePath = '', encoding = '' ):
      '''
      Finalize HTML log file by appending closing HTML tags to the end of the file
      '''

      if ( encoding == '' ):
         if ( self.logFileEncoding != '' ):
            encoding = self.logFileEncoding
         elif 'CI_ENCODING' in os.environ:
            encoding = os.environ['CI_ENCODING']


      if ( filePath == '' ):
         if ( not self.logFilePath.is_file() ):
            if 'CI_LOGFILE' in os.environ:
               self.logFilePath = Path( os.environ['CI_LOGFILE'] )
      else:
         self.logFilePath = Path( filePath )
      
      if ( self.logFilePath.is_file() ):
         with open( self.logFilePath, 'a', encoding = encoding ) as logFile:
            logFile.write("</body>")
            logFile.write("</html>")
            logFile.close()

