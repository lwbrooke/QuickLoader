from pathlib import Path
from tkinter import filedialog
import glob
import os
import tkinter as tk

file_name = None
file_contents = None
path = Path('D:\\')
drive_written = False
drive_options = [
    'D:\\',
    'E:\\',
    'F:\\',
    'G:\\',
    'H:\\',
    'I:\\',
    'J:\\',
    'K:\\',
    'L:\\',
    'M:\\',
]

def _make_pick_file(callback):
    def pick_file():
        global file_name
        global file_contents
        file = filedialog.askopenfile(mode='rb')
        if file:
            file_name = Path(file.name).name
            file_contents = file.read()
            file.close()
            callback(f'File selected: {file_name}')
        else:
            file_name = None
            file_contents = None
            callback('File selected: ')
    return pick_file

def _make_label_updater(label):
    def update(text):
        label['text'] = text
    return update

def _make_loader(root, callback, wait_time, var_wipe):
    def load_usb():
        global drive_written
        try:
            if not file_name or not file_contents:
                callback('\u20E0   No file selected   \u20E0')
                return
            if not os.path.exists(path):
                drive_written = False
                callback('\u20E0   No usb drive detected   \u20E0')
                return
            if drive_written:
                callback('\u2714   File written, safe to eject drive   \u2714')
                return
            if var_wipe.get():
                callback("Wiping drive")
                for file in path.glob('*.*'):
                    file.unlink()
            drive_written = True
            callback('Opening file on drive')
            with open(path.joinpath(file_name), 'wb') as f:
                f.write(file_contents)
        finally:
            root.after(wait_time, load_usb)
    return load_usb

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Foulplay QuickLoader')

    root.rowconfigure([0, 3], minsize=50)
    root.columnconfigure(0, weight=1)

    row0 = tk.Frame(master=root)
    row0.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
    lbl_title = tk.Label(master=row0, text='Foulplay Quickloader', font=30, padx=5, pady=5)
    lbl_title.pack(padx=5, pady=5)

    row1 = tk.Frame(master=root)
    row1.grid(row=1, column=0, padx=5, pady=5)

    lbl_filename = tk.Label(master=row1, text='File selected: ', font=20, padx=5, pady=5, width=70, relief=tk.SUNKEN, anchor='w')
    file_updater = _make_label_updater(lbl_filename)
    lbl_filename.pack(padx=5, pady=5, side=tk.RIGHT)

    btn_picker = tk.Button(master=row1, text='Pick a new file', font=20, padx=5, pady=5, command=_make_pick_file(file_updater))
    btn_picker.pack(padx=5, pady=5, side=tk.RIGHT)
    
    row2 = tk.Frame(master=root)
    row2.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')

    var_wipe = tk.IntVar()
    chk_wipe_drive = tk.Checkbutton(master=row2, text="Wipe drive before writing", font=20, variable=var_wipe)
    chk_wipe_drive.pack(padx=5, pady=5, side=tk.LEFT)

    lbl_divider = tk.Label(master=row2, text='|', font=20, padx=5, pady=5)
    lbl_divider.pack(padx=5, pady=5, side=tk.LEFT)

    var_drive = tk.StringVar(value=drive_options[0])

    lbl_drive = tk.Label(master=row2, text='Drive Letter:', font=20, padx=5, pady=5)
    lbl_drive.pack(padx=5, pady=5, side=tk.LEFT)

    def drive_cmd(drive_letter):
        global path
        path = Path(drive_letter)

    mnu_drive = tk.OptionMenu(row2, var_drive, *drive_options, command=drive_cmd)
    mnu_drive.pack(padx=5, pady=5, side=tk.LEFT)

    row3 = tk.Frame(master=root, relief=tk.SUNKEN, borderwidth=1)
    row3.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')

    lbl_status = tk.Label(master=row3, text='\u20E0   No file selected   \u20E0', font=30, padx=5, pady=5)
    status_updater = _make_label_updater(lbl_status)
    lbl_status.pack(padx=5, pady=5)

    wait_time = 1 * 1000 # 1 sec
    loader = _make_loader(root, status_updater, wait_time, var_wipe)
    root.after(wait_time, loader)

    root.mainloop()