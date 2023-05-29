from datetime import datetime
from pathlib import Path
import os

from cilogger import ciLogger
from test_child import childLogger

logger = ciLogger()
clogger = childLogger()

run_datetime = datetime.now()
logFilePath = Path( ".", "LOG_CITEST_" + run_datetime.strftime("%y%m%d_%H%M%S") + ".htm" )

logger.ciInitHtml( str( os.path.abspath( logFilePath ) ), encoding = 'iso-8859-15' )

logger.ciPrint( "cilogger integration test", colFormat = "datetime:20;80" )
logger.ciPrint( " " )
logger.ciInfo( "Column format: " + logger.colFormat )
logger.ciInfo( "Left column will now show message type (if using one of the standard message types)")
logger.ciPrint( " " )
logger.ciInfo( "Available foreground colors:" )
logger.ciPrint( "Black", fg = 'black', bg = 'white' )
logger.ciPrint( "Red", fg = 'red' )
logger.ciPrint( "Green", fg = 'green' )
logger.ciPrint( "Yellow", fg = 'yellow' )
logger.ciPrint( "Blue", fg = 'blue' )
logger.ciPrint( "Violet", fg = 'violet' )
logger.ciPrint( "Cyan", fg = 'cyan' )
logger.ciPrint( "White", fg = 'white', bg = 'black' )
logger.ciPrint( " " )
logger.ciInfo( "Available background colors:" )
logger.ciPrint( "Black", fg = 'white', bg = 'black' )
logger.ciPrint( "Red", fg = 'black', bg = 'red' )
logger.ciPrint( "Green", fg = 'black', bg = 'green' )
logger.ciPrint( "Yellow", fg = 'black', bg = 'yellow' )
logger.ciPrint( "Blue", fg = 'white', bg = 'blue' )
logger.ciPrint( "Violet", fg = 'white', bg = 'violet' )
logger.ciPrint( "Cyan", fg = 'black', bg = 'cyan' )
logger.ciPrint( "White", fg = 'black', bg = 'white' )

logger.ciPrint( " " )
logger.ciInfo( "Default style of standard message types" )
logger.ciInfo( "This is an info message" )
logger.ciDebug( "This is a debug message" )
logger.ciError( "This is an error message" )
logger.ciWarning( "This is a warning message" )
logger.ciSuccess( "This is a success message" )

logger.ciPrint( " " )
logger.colFormat = "msgtype:3;80"
logger.ciInfo( "Changing column format to " + str( logger.colFormat ) )
logger.ciWarning( "Message type in left column will now be truncated" )

logger.ciPrint( " " )
logger.colFormat = "datetime:20;80"
logger.ciInfo( "Changing column format to " + str( logger.colFormat ) )
logger.ciInfo( "Left column will now show current date and time" )
logger.ciInfo( "Current date and time format is " + logger.dateTimeFormat )

logger.ciPrint( " ", colFormat = "blank:20;80" )
logger.colFormat = "datetime:%m/%d/%y %-I:%M:%S %p:21;80"
logger.ciInfo( "Changing column format to " + str( logger.colFormat ) )
logger.ciInfo( "Left column will now show current date and time with custom date and time format" )

logger.ciPrint( " ", colFormat = "blank:20;80" )
logger.colFormat = "timer:runtime:6:10;80"
logger.ciInfo( "Changing column format to " + str( logger.colFormat ) )
logger.ciInfo( "Left column now show runtime of current script in seconds with 6 decimals" )

logger.ciPrint( " ", colFormat = "blank:20;80" )
logger.colFormat = "timer_ns:runtime:10;80"
logger.ciInfo( "Changing column format to " + str( logger.colFormat ) )
logger.ciInfo( "Left column now show runtime of current script in nanoseconds" )

clogger.printLog()

logger.ciPrint( " ", colFormat = "blank:20;80" )
logger.colFormat = "80;msgtype:10"
logger.ciInfo( "Changing column format to " + str( logger.colFormat ) )
logger.ciInfo( "The message type will now be printed to the right of the message itself")
logger.ciPrint( "This line shows how it would look with a red background color", bg = 'red', msgType = 'info' )

logger.ciPrint( " ", colFormat = "blank:20;80" )
logger.colFormat = "msgtype:10;wrap:50"
logger.ciInfo( "Changing column format to " + str( logger.colFormat ) )
logger.ciInfo( "The text will now automatically wrap to a new line if it exceeds the width of the wrap column, maintaining the left indent of any column preceeding the message column")

logger.ciFinalizeHtml()