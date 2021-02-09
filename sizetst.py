import os,sys,io
import tkinter.filedialog,tkinter,tkinter.messagebox,time,shutil,pathlib,logging
part = [
	[1,1,0],
	[2,2,1],
	[2,3,1],
	[2,4,1],
	[2,5,1],
	[2,6,1],
	[2,7,1],
	[2,8,1],
	[2,9,1],
	[2,10,1],
	[2,11,1],
	[2,12,1],
	[2,13,1],
	[2,14,1],
	[2,15,1],
	[0,99,99]
]
def get_dir_size(path='.'):
	total=0
	try:
		with os.scandir(path) as it:
			for entry in it:
				if entry.is_file():
					total += entry.stat().st_size
				elif entry.is_dir():
					total += get_dir_size(entry.path)
	except OSError as err:
		print(err)
		pass
	return total

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
logging.basicConfig(level='DEBUG')
root = tkinter.Tk()
root.wm_attributes("-topmost", 1)
root.withdraw()
iDir = os.path.abspath(os.path.dirname(__file__))
dir = tkinter.filedialog.askdirectory(initialdir = iDir)
sz = get_dir_size(dir)
temp = 0
logging.info(shutil.disk_usage(dir[0:2]))
logging.info(dir)
logging.info("フォルダの監視を始めます")
while part[temp][0]!=0:
	psz = sz
	time.sleep(2)
	if shutil.disk_usage(dir[0:2]).total > shutil.disk_usage(dir[0:2]).free*100:
		logging.info("ドライブ容量がわずかです")
	sz = get_dir_size(dir)
	logging.info(sz)
	if part[temp][0]==1:
		if sz > psz:
			logging.info("フォルダサイズの増加を確認")
			temp = part[temp][1]
			continue
		else:
			temp = part[temp][2]

			continue
	elif part[temp][0]==2:
		if sz == psz:
			temp = part[temp][1]
			continue
		else:
			temp = part[temp][2]
			continue
tkinter.messagebox.showinfo("完了","フォルダサイズの増加が完了しました。監視を終了します。")
