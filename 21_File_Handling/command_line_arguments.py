import sys

# all_command_line_arguments = sys.argv
# print(all_command_line_arguments)



def fibo(n): return fibo(n-1) + fibo(n-2) if n > 2 else n
print(fibo(int(sys.argv[1])))

# try:
#     n = int(sys.argv[1])
#     print(fibo(n))
# except IndexError:
#     print('Arguments must be provided as command line...')
