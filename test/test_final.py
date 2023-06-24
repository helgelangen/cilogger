from datetime import datetime
from pathlib import Path
import os
import sys

ciLoggerDir =  Path(__file__).resolve().parents[1]
sys.path.append( str( ciLoggerDir ) )
from cilogger import ciLogger

logger = ciLogger()

if ( logger.ciRecoverOpenHtmlFile( "." ) ):
    logger.ciPrint( " " )
    logger.ciDebug( "Finalizing open HTML log file " + str( os.path.relpath( logger.logFilePath ) ) )
else:
    logger.ciError( "An open HTML log file was not found. Build will terminate" )
    sys.exit(1)

logger.ciFinalizeHtml()