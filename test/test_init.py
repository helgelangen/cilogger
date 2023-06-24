from datetime import datetime
from pathlib import Path
import os
import sys

ciLoggerDir =  Path(__file__).resolve().parents[1]
sys.path.append( str( ciLoggerDir ) )
from cilogger import ciLogger

logger = ciLogger()

run_datetime = datetime.now()
logFilePath = Path( ".", "LOG_CITEST_" + run_datetime.strftime("%y%m%d_%H%M%S") + ".htm" )

logger.ciInitHtml( str( os.path.abspath( logFilePath ) ), encoding = 'iso-8859-15' )

logger.ciPrint( "=============================================", colFormat = "80" )
logger.ciPrint( "cilogger integration test", colFormat = "datetime:20;80" )
logger.ciPrint( "=============================================", colFormat = "80")
logger.ciPrint( " " )
logger.ciDebug( "Creating HTML log file " + str( os.path.relpath( logFilePath ) ) )