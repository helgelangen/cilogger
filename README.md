[![Build Status](https://jenkins.nadbygg.no/buildStatus/icon?job=cilogger%2Fmain&style=plastic)](https://jenkins.nadbygg.no/job/cilogger/job/main/)

# cilogger
Utility for producing beautiful formatted console output when running continous integration tests

## Invoking the cilogger in your script
To invoke the cilogger, create a ciLogger object:
```python
logger = ciLogger()
```

Then use the ciPrint function or the other shorthands to directly print using predefined message types:
```python
logger.ciPrint("This will be printed using the terminals default color")
logger.ciWarning("This will be printed using the warning color, default yellow text")
logger.ciError("This will be printed using the error color, default red text")
```

## Creating a HTML logfile
It is possible to create a HTML logfile that will contain all output generated by the cilogger instance. The HTML file will have the same colors and formatting as the console output. By default, the HTML file will have a white background color.

To initiate a new HTML log file, call the ciInitHtml() function:
```python
logger.ciInitHtml( filepath, encoding, useGlobally)
```
ciInitHtml() takes the following arguments:
* filepath: str or pathlib.Path, required: filename of the HTML file. should have .htm or .html extension
* encoding: str, optional, default iso-8859-15: character encoding of the HTML file. See Python supported text codecs here: https://docs.python.org/3/library/codecs.html#standard-encodings
* useGlobally: bool, optional, default True: if set to True, the filepath and encoding will be saved to an environment variable that will be inherited by all Python files called from the file where ciInitHtml() was first invoked. if a ciLogger object is initiated in Python files descending from this file, HTML logging will already be enabled.

If a Python file that should log to the same HTML file does not inherit the environment variable set by the ciInitHtml() function, e.g. in a Jenkins pipeline with several steps, you can set the ciLogger object to use an existing HTML log file by calling the ciRecoverOpenHtmlFile() function:
```python
logger.ciRecoverOpenHtmlFile( searchPath, encoding, useGlobally , forceSearch )
```
ciRecoverOpenHtmlFile() takes the following arguments:
* searchPath: str or pathlib.Path, required: filename of the HTML file to keep working on, or a folder to search for open HTML files. If a path to a file with extension .htm or .html is given, the function checks if the file with the given name exists, and if it has not been closed by the ciFinalizeHtml() function. If an open file is found, ciLogger will log to this file, and the function returns True. If a path to a folder is given, the function browse the folder searching for .htm and .html files, checking if these files were created by ciLogger and that they have not been closed by the ciFinalizeHtml() function. If an open file is found, ciLogger will log to this file, and the function returns true. If multiple open files are found, the last modified file is chosen. If none of the methods find an open file, the function returns false (in which you might consider creating a new file using ciInitHtml()).
* encoding: str, optional, default iso-8859-15. See Python supported text codecs here: https://docs.python.org/3/library/codecs.html#standard-encodings
* useGlobally: bool, optional, default True: if set to True, the filepath and encoding will be saved to an environment variable that will be inherited by all Python files called from the file where ciInitHtml() was first invoked. if a ciLogger object is initiated in Python files descending from this file, HTML logging will already be enabled.
* forceSearch: bool, optional, default False: if a HTML log file has already been specified for the current ciLogger object, e.g. if it has inherited the environment variables from a parent script, or if ciInitHtml() or ciRecoverOpenHtmlFile() has already been performed, no search for existing files is performed. if forceSearch is set to True, however, a search for an existing HTML log file is performed in any case, and if the search finds an existing file, that file will replace the current specified HTML log file.

At the end of the script using ciLogger to log to a HTML file, or at the end of the final script in a multi-script test pipeline, the HTML file should be finalized. This means adding the closing </body> and </html> tags at the end of the file, as well as setting the status of the file to closed by changing a special HTML comment at the beginning of the file. This is done by calling the ciFinalizeHtml() function:
```python
logger.ciFinalizeHtml( filePath, encoding )
```
ciFinalizeHtml() takes no arguments and relies on the ciLogger object to already point to a valid, open ciLogger HTML log file.

## colFormat specification

The colFormat defines the columns of information to be printed. Each column is separated by semicolons, the fields within each column separated by colons.

'80' (just a number): this column contains the message to print. Note: Message will _not_ be truncated, even if exceeding the column width  
'wrap:80': this column will also contain the message to print. If the message exceeds the column width, it will wrap to a new line  
'msgtype:10': this column contains the message type, if using a built in message type, with column width 10. Field will be truncated if exceeding the column width. Field will be blank if the message type is invalid  
'datetime:20': Current date and time formatted using the current set datetime format string. Field will be truncated if exceeding the column width  
'datetime:%d.%m.%y %H:%M:%S:20': Current date and time formatted using the datetime format string given in the middle field. Semicolons must not be used. Field will be truncated if exceeding the column width  
'timer:runtime:6:10': prints the current runtime since the cilogger object was initiated, in seconds, with a precision of 6 decimals and column width 10. Field will be truncated if exceeding the column width  
'timer:mytimer:6:10': prints the current time of custom timer mytimer, if mytimer has been initiated, in seconds with a precision of 6 and column width 10. Field will be truncated if exceeding the column width. Field will be blank if a timer with the given timer name has not been initiated.  
'timer_ns:mytimer:11': prints the current time of custom timer mytimer, if mytimer has been initiated, in nanoseconds with column width 11. Field will be truncated if exceeding the column width. Field will be blank if a timer with the given timer name has not been initiated.  
