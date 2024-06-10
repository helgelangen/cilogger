from datetime import datetime
from pathlib import Path
import os
import sys
import argparse

from cilogger import ciLogger

parser = argparse.ArgumentParser()
parser.add_argument( "-b", type = int, help = "Jenkins build number", default = 0, required = False )
args = parser.parse_args()

logger = ciLogger()

run_datetime = datetime.now()
logBuildNum = ''
if ( args.b > 0 ):
    logBuildNum = f"b{ args.b }_"
logFilePath = Path( ".", "LOG_CITEST_" + logBuildNum + run_datetime.strftime("%y%m%d_%H%M%S") + ".htm" )
errorLogFilePath = Path( "error.log" )

logger.ciInitHtml( str( os.path.abspath( logFilePath ) ), encoding = 'iso-8859-15' )
logger.ciInitErrorLog( str( os.path.abspath( errorLogFilePath ) ), encoding = 'iso-8859-15', useGlobally = True )

logger.ciPrint( "=============================================", colFormat = "80" )
logger.ciPrint( "cilogger integration test", colFormat = "datetime:20;80" )
logger.ciPrint( "=============================================", colFormat = "80")
logger.ciPrint( " " )
logger.ciDebug( "Creating HTML log file " + str( os.path.relpath( logFilePath ) ) )
logger.ciDebug( "Creating Error log file "+ str( os.path.relpath( errorLogFilePath ) ) )