# Threadsafe Printing to Screen
This example ensures that printing (to screen in the example) is serialised such that different threads do not overlap one another.

This is particularly useful for error logging, notifications and writing to files when using multi-threaded code.

This is based on the discussion at [Stack Overflow](http://stackoverflow.com/questions/3029816/how-do-i-get-a-thread-safe-print-in-python-2-6).