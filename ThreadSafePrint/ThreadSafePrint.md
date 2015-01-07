# Threadsafe Printing to Screen
This example ensures that printing (to screen in the example) is serialised such that different threads do not overlap one another.

This is particularly useful for error logging, notifications and writing to files when using multi-threaded code.
