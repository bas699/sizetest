import os, tkinter, tkinter.filedialog, tkinter.messagebox, time

def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total

root = tkinter.Tk()
root.attributes("TopMost",1)
root.withdraw()
fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))

dir = tkinter.filedialog.askdirectory(initialdir = iDir)
sz = 0
psz = 0
zy = 0
en = 0
sz = get_dir_size(dir)
psz = sz
while zy == 0:
	sz = get_dir_size(dir)
	print(sz)
	if zy == 0 and sz > psz:
		print("start")
		zy = 1
	if zy == 1 :
            if sz == psz:
                ct += 1
                if ct == 0:
                    print("end")
                else:
                    ct = 0
	psz = sz
	time.sleep(10)
