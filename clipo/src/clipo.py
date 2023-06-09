import sys
from tkinter import Tk

print('start')
r = Tk()
r.withdraw()
print(r.withdraw())
r.clipboard_clear()

if len(sys.argv) < 2:
    data = sys.stdin.read()
else:
    data = ' '.join(sys.argv[1:])

# r.clipboard_append(data)
r.clipboard_append("hi stat")

if sys.platform != 'win32':
    if len(sys.argv) > 1:
        raw_input('Data was copied into clipboard. Paste and press ENTER to exit...')
    else:
        # stdin already read; use GUI to exit
        print('Data was copied into clipboard. Paste, then close popup to exit...')
        r.deiconify()
        r.mainloop()
else:
    r.destroy()
