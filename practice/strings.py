from timeit import default_timer


start = default_timer()

print("hello world")

stop = default_timer()


print(stop-start)

print(f"formatting:{start} and {stop}" )