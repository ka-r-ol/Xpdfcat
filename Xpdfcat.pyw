"""
" GUI (tkinter) Tool to concatenate multiple pdf files
" Language:     Python
" Maintainer:   Karol Lemanski <karol.lemanski@wp.pl>
" Version:      python3
" URL:          http://github.com/ka-r-ol/Xpdfcat
"""

import os
import PyPDF2
import webbrowser
import re
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox


class PDFEntry(tk.Frame):
    def __init__(self, full_name, GT, master=None):
        super().__init__(master)
        self.GT = GT
        self.master = master
        self.full_name = full_name
        (dir_name, fil_name) = os.path.split(full_name)

        self.frame = tk.Frame(master)
        self.frame.pack(side="top", fill=tk.X)

        self.button_up = tk.Button(self.frame, text="\u1403",
                                   command=self.up_clicked)
        self.button_up.pack(side="left")

        self.button_down = tk.Button(self.frame, text="\u1401",
                                     command=self.down_clicked)
        self.button_down.pack(side="left")

        self.filename_label = tk.StringVar()
        self.filename_label.set(fil_name)
        self.pdf_name_label = tk.Label(self.frame,
                                       textvariable=self.filename_label)
        self.pdf_name_label.pack(side="left")

        self.button_del = tk.Button(self.frame, text="del",
                                    command=self.del_clicked)
        self.button_del.pack(side="right")

        self.INACTIVE = 1
        self.EDITABLE = 2
        self.CONFIRMED = 3
        self.slice_mode = self.INACTIVE
        self.slice_text = "*"
        self.sliced = [":"]
        self.button_slice_label = tk.StringVar()
        self.button_slice_label.set("Slice")
        self.button_slice = tk.Button(self.frame,
                                      textvariable=self.button_slice_label,
                                      command=self.slice_clicked)
        self.button_slice.pack(side="right")

        self.slice_entry = tk.Entry(self.frame, width=20)

    def swap_entries(self, idx1, idx2):
        # name of the file label
        o1_value = self.GT[idx1].filename_label.get()
        o2_value = self.GT[idx2].filename_label.get()
        self.GT[idx1].filename_label.set(o2_value)
        self.GT[idx2].filename_label.set(o1_value)
        # name and status of the slice button
        # name and status of the slice entry
        mode1 = self.GT[idx1].slice_mode
        text1 = self.GT[idx1].slice_text
        sliced1 = self.GT[idx1].sliced
        mode2 = self.GT[idx2].slice_mode
        text2 = self.GT[idx2].slice_text
        sliced2 = self.GT[idx2].sliced
        self.GT[idx1].set_slice_mode(mode2, text2, sliced2)
        self.GT[idx2].set_slice_mode(mode1, text1, sliced1)
        # swap full_names in the object
        o1_value = self.GT[idx1].full_name
        o2_value = self.GT[idx2].full_name
        self.GT[idx1].full_name = o2_value
        self.GT[idx2].full_name = o1_value

    def up_clicked(self):
        idx = self.GT.index(self)
        if idx == 0:
            return
        idx2 = idx-1
        self.swap_entries(idx, idx2)

    def down_clicked(self):
        idx = self.GT.index(self)
        if idx == len(self.GT)-1:
            return
        idx2 = idx+1
        self.swap_entries(idx, idx2)

    def set_slice_mode(self, mode, text, sliced):
        if mode == self.INACTIVE:
            self.button_slice_label.set("Slice")
            self.slice_text = "*"
            self.sliced = [":"]
            self.slice_entry.pack_forget()
            self.slice_mode = self.INACTIVE
        elif mode == self.EDITABLE:
            self.slice_text = text
            self.sliced = sliced
            self.button_slice_label.set("Confirm!")
            if not self.slice_entry.winfo_ismapped():
                self.slice_entry.pack(side="right")
            self.slice_entry['state'] = 'normal'
            self.slice_entry.delete(0, 'end')
            self.slice_entry.insert(0, self.slice_text)
            self.slice_mode = self.EDITABLE
        elif mode == self.CONFIRMED:
            self.slice_text = text
            self.sliced = sliced
            self.button_slice_label.set("Slice")
            if not self.slice_entry.winfo_ismapped():
                self.slice_entry.pack(side="right")
            self.slice_entry['state'] = 'normal'
            self.slice_entry.delete(0, 'end')
            self.slice_entry.insert(0, self.slice_text)
            self.slice_entry['state'] = 'readonly'
            self.slice_mode = self.CONFIRMED

    def convert(self, tmp_sliced):
        sliced = []
        if len(tmp_sliced) == 0:
            sliced = [":"]
        for s in tmp_sliced:
            if s == "*":
                sliced.append(":")
            else:
                m = re.match(r'(\d+)-(\d+)', s)
                if m:
                    t = m.groups()
                    v1 = max(0, int(t[0])-1)
                    v2 = max(0, int(t[1]))
                    if v2 > v1:
                        sliced.append(str(v1)+":"+str(v2))
                    elif v1 == v2:
                        sliced.append(str(v1))
                else:
                    t = int(s)
                    v = max(0, t-1)
                    sliced.append(str(v))
        return(sliced)

    def slice_clicked(self):
        def analize_text(entry_text):
            entry_text = entry_text.replace(" ", "")

            flag = False
            sliced = [":"]
            if entry_text == "":
                flag = True
            elif re.match(r'\A(\*|\d+-\d+|\d+)(,(\*|\d+-\d+|\d+))*\Z',
                          entry_text):
                flag = True
                tmp_sliced = re.findall(r'\*|\d+-\d+|\d+', entry_text)
                sliced = self.convert(tmp_sliced)
            return (flag, sliced)

        def provide_instructions():
            print("Instructions provided")
            message = """
        Please review your slice page range specyfication

        Slice page range expression examples:
            *     all pages.
            22    just the 22n page
            1-3   the first three pages
            4-5   page 4th and 5th
            4,5   page 4th and 5th
            5-10  pages from the 5th to 10th
            5,7-9 pages: 5th and from 7th to 9th
            1,1   first page repeated twice
            """
            tk.messagebox.showwarning(title="warning", message=message)
            pass

        if self.slice_mode == self.INACTIVE:
            self.slice_entry.pack(side="right")
            self.slice_entry.focus()
            self.slice_mode = self.EDITABLE
            self.slice_text = "*"
            self.sliced = [":"]
            self.slice_entry.delete(0, 'end')
            self.slice_entry.insert(0, self.slice_text)
            self.button_slice_label.set("Confirm!")
        elif self.slice_mode == self.EDITABLE:
            entry_text = self.slice_entry.get()
            (flag, sliced) = analize_text(entry_text)
            if flag:
                self.slice_text = entry_text
                self.sliced = sliced
                self.slice_entry['state'] = 'readonly'
                self.button_slice_label.set("Slice")
                self.slice_mode = self.CONFIRMED
            else:
                provide_instructions()
        elif self.slice_mode == self.CONFIRMED:
            self.slice_entry['state'] = 'normal'
            self.slice_mode = self.EDITABLE
            self.button_slice_label.set("Confirm!")

    def del_clicked(self):
        self.GT.remove(self)
        self.destroy()

    def destroy(self):
        self.frame.destroy()
        super().destroy()


class XPDFConcat(tk.Frame):
    def __init__(self, master=None, text=""):
        super().__init__(master)
        self.GT = []
        self.master = master
        self.master.title("XPDFcat")
        self.topframe = tk.Frame(master)
        self.bottomframe = tk.Frame(master)
        self.topframe.pack(side="top", fill=tk.X)
        self.bottomframe.pack(side="bottom")
        self.create_widgets()
        self.GT = []
        self.output_pdf_trio = []

    def create_widgets(self):
        self.button_add = tk.Button(self.topframe, text="Add PDF file",
                                    command=self.button_add_clicked,
                                    pady=5, padx=10)
        self.button_startover = tk.Button(self.bottomframe,
                                          text="Del all",
                                          command=self.
                                          button_startover_clicked,
                                          pady=0, padx=10)
        self.button_close = tk.Button(self.bottomframe,
                                      text="Close",
                                      command=self.button_close_clicked,
                                      pady=0, padx=10)
        self.button_merge = tk.Button(self.bottomframe, text="Merge",
                                      command=self.button_merge_clicked,
                                      pady=12, padx=10)
        self.button_add.pack(side="top")
        self.button_merge.pack(side="left")
        self.button_close.pack(side="bottom")
        self.button_startover.pack(side="bottom")

    def button_add_clicked(self):
        full_name = askopenfilename(title="Select PDF file to be merged",
                                    filetypes={('PDF', '*.pdf')})
        if len(full_name) != 0:
            w = PDFEntry(full_name, self.GT, self.topframe)
            w.pack(side="top", fill=tk.X)
            self.GT.append(w)

    def button_startover_clicked(self):

        # if there are not pdfs selected (GT is empty), do nothing
        if len(self.GT) == 0:
            return

        decision = messagebox.askyesno(title="Start Over",
                                       message="Are you sure?")
        if decision:
            for w in self.GT:
                w.destroy()
            self.GT = []

    def button_close_clicked(self):
        self.master.destroy()

    def button_merge_clicked(self):
        if len(self.GT) < 1:
            messagebox.showinfo(title="No PDF files added",
                                message="Add at least one PDF file!")
            return

        all_slices_confirmed = True
        """
        self.INACTIVE = 1
        self.EDITABLE = 2
        self.CONFIRMED =3
        self.slice_mode = self.INACTIVE
        """
        for w in self.GT:
            if w.slice_mode == w.EDITABLE:
                all_slices_confirmed = False
                # break

        if all_slices_confirmed is False:
            messagebox.showinfo(title="Not all slices are confirmed!",
                                message="""
Not all slices are confirmed.

Confirm missing slices!

                                """)
            return

        full_name = asksaveasfilename(title="Select output file",
                                      filetypes={('PDF', '*.pdf')})
        if len(full_name) != 0:
            (dir_name, fil_name) = os.path.split(full_name)
            self.output_pdf_trio = [fil_name, dir_name, full_name]
            self.concatenate_pdfs()
            msg = "PDF files merged and saved in:\n\t\'"
            msg += fil_name+"\'\nat\n\t\'" + dir_name
            msg += "\'\ndirectory."
            messagebox.showinfo(title="PDF Merged",
                                message=msg)
            webbrowser.open('file://'+full_name, new=2)

    def concatenate_pdfs(self):

        output = open(self.output_pdf_trio[2], "wb")
        in_fs = []
        merger = PyPDF2.PdfFileMerger()
        for w in self.GT:
            filename = w.full_name
            f = open(filename, "rb")
            in_fs.append(f)
            for range in w.sliced:
                pr = PyPDF2.PageRange(range)
                merger.append(f, pages=pr)

        merger.write(output)
        output.close()
        for f in in_fs:
            f.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = XPDFConcat(master=root)
    app.mainloop()
