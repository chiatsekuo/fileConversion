
import excel2json

excel2json.convert_from_file('input/xlsToJson.xlsx')

'''
Limitations of excel2json-3 module

The plugin has very limited features.
There are no options to skip any sheet, rows, and columns. This makes it hard to use with bigger excel files.
The JSON is saved into files. Most of the times, we want to convert to JSON and use it in our program rather than saving it as a file.
The integers are getting converted to the floating point numbers.

The output json file will be generated in the current path which is the input folder.
'''