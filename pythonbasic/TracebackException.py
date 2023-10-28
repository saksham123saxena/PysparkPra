import traceback as tb
import SubTracebackEx as sb
import sys

# print(help(tb))
# print(dir(tb))
# '''
# ['FrameSummary', 'StackSummary', 'TracebackException', '_RECURSIVE_CUTOFF', '_Sentinel', '__all__', '__builtins__',
# '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_cause_message',
# '_context_message', '_format_final_exc_line', '_parse_value_tb', '_sentinel', '_some_str', 'clear_frames',
# 'collections', 'extract_stack', 'extract_tb', 'format_exc', 'format_exception', 'format_exception_only', 'format_list',
#  'format_stack', 'format_tb', 'itertools', 'linecache', 'print_exc', 'print_exception', 'print_last', 'print_list',
#   'print_stack', 'print_tb', 'sys', 'walk_stack', 'walk_tb']
#
# '''

def main():
    try:
        sb.test()
    except:
        print("it is the main class, which is using sub class for raising the exception!!")
        # print(tb.print_exc())
        print(tb.print_exc())
        print(sys.exc_info())
        print(sys.exc_info()[2].tb_lineno)
        sys.exit(1)

if __name__ == "__main__":
    main()

