from cilogger import ciLogger

class childLogger:

   def __init__( self ):
      
      self.logger = ciLogger()

   def printLog( self ):

      self.logger.ciPrint( " " )
      self.logger.ciInfo( "This message is printed from a child class" )
      self.logger.ciInfo( "Output is saved to HTML even if HTML logging was not initialized by the child class" )
      self.logger.ciInfo( "Note however that other settings are not inherited and are set to default values" )
