import sys
def test():
    sal=-1
    try:
        if sal<0:
            raise Exception("Sal can't be less than zero")
    except Exception as Argu:
        print("inner class function :: "+str(sys.exc_info()[2].tb_lineno))
        print("In sub-traceback-exception :: "+str(Argu))
        raise

