#a = 5
try:
    print(a)
except Exception as e:
    print(e)
else:
    print("This is else block.")
finally:
    print("This is finally block.")
