import sys
from tkinter import Tk

r = Tk()
r.withdraw()
try:
    # r.clipboard_append("hi stat")
    # result = r.clipboard_get()
    # print(result, file=sys.stderr)
    print("hello", file=sys.stderr)
    # print("hello", file=sys.stdout)
    # sys.stdout.write(result)
    # sys.stderr.write(result)
    # sys.stdout.flush()
except Tk.TclError:
    pass
finally:
    r.destroy()

