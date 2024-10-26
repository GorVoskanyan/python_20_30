import time
from task_100 import password_generator
from task_102 import is_valid_password

start = time.time()

password = password_generator()
if is_valid_password(password):
    print(password, 'is valid.')
else:
    print(password, 'is not valid.')
# l = sum(i ** j for i in range(1000) for j in range(1000))

runtime = time.time() - start
print(runtime, 'seconds')
