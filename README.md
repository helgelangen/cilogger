# cilogger
Utility for producing beautiful formatted console output when running continous integration tests

## Colspec field

The colspec defines the columns of information to be printed. Each column is separated by semicolons, the fields within each column separated by colons.

'80' (just a number): this column contains the message to print. Note: Message will _not_ be truncated, even if exceeding the column width.
'wrap:80': this column will also contain the message to print. If the message exceeds the column width, it will wrap to a new line.
'msgtype:10': this column contains the message type, if using a built in message type, with column width 10. Field will be truncated if exceeding the column width. Field will be blank if the message type is invalid.
'datetime:20': Current date and time formatted using the current set datetime format string. Field will be truncated if exceeding the column width.
'datetime:%d.%m.%y %H:%M:%S:20': Current date and time formatted using the datetime format string given in the middle field. Semicolons must not be used. Field will be truncated if exceeding the column width
'timer:runtime:6:10': prints the current runtime since the cilogger object was initiated, in seconds, with a precision of 6 decimals and column width 10. Field will be truncated if exceeding the column width
'timer:mytimer:6:10': prints the current time of custom timer mytimer, if mytimer has been initiated, in seconds with a precision of 6 and column width 10. Field will be truncated if exceeding the column width. Field will be blank if a timer with the given timer name has not been initiated.
'timer_ns:mytimer:11': prints the current time of custom timer mytimer, if mytimer has been initiated, in nanoseconds with column width 11. Field will be truncated if exceeding the column width. Field will be blank if a timer with the given timer name has not been initiated.