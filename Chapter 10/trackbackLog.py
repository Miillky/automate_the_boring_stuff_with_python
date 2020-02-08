import traceback
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('./Chapter 10/errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt')