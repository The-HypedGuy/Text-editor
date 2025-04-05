import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('Zpad text editor')

#_________________main_menu__________________#
#_____________&&&&End_main_menu&&&&__________#
main_menu = tk.Menu()

#file icons
file = tk.Menu(main_menu,tearoff=False)#file_menu
new_icons = tk.PhotoImage(file="/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/new.png")
open_icons = tk.PhotoImage(file="/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/open.png")
save_icons = tk.PhotoImage(file="/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/save.png")
save_as_icons = tk.PhotoImage(file="/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/save_as.png")
exit_icons = tk.PhotoImage(file="/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/exit.png")

#edit_icons
edit = tk.Menu(main_menu,tearoff=False)#edit_menu
copy_icon = tk.PhotoImage(file=('/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/copy.png'))
paste_icon = tk.PhotoImage(file=('/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/paste.png'))
cut_icon = tk.PhotoImage(file=('/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/cut.png'))
clear_all_icon = tk.PhotoImage(file=('/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/clear_all.png'))
find_icon = tk.PhotoImage(file=('/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/find.png'))

#view_icons
tool_bar_icon = tk.PhotoImage(file='/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/status_bar.png')

view = tk.Menu(main_menu,tearoff=False)

#color_theme_icons
light_default_icon = tk.PhotoImage(file='/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/dark.png')
red_icon = tk.PhotoImage(file='/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/red.png')
monokai_icon = tk.PhotoImage(file='/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/night_blue.png')

#color_theme_menu
color_theme = tk.Menu(main_menu,tearoff=False)
theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {
    'Light Default' : ('#00000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#d3b774', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' : ('#ededed', '#6b9dc2')
}

#cascade
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color_theme)

#_________________tool_bar__________________#
#_____________&&&&End_tool_bar&&&&__________#

tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

#font_box
font_tuples = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuples
font_box.current(7)
font_box.grid(row=0, column=0, padx=5)

#size_box
size_var = tk.IntVar()
font_size =ttk.Combobox(tool_bar, width=14, textvariable=size_var, state='readonly')
font_size['values'] = tuple(range(8,80,2))
font_size.current(4)
font_size.grid(row=0, column=1, padx=5)

#blod_buttom
bold_icon = tk.PhotoImage(file='/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

#italic_button
italic_icon = tk.PhotoImage(file='/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

#underline_button
underline_icon = tk.PhotoImage(file='/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/underline.png')
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

#font_color_button
font_color_icon = tk.PhotoImage(file='/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/font_color.png')
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=5, padx=5)

#align_button
align_left_icon = tk.PhotoImage(file='/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/align_left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

align_right_icon = tk.PhotoImage(file='/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/align_right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)

align_center_icon = tk.PhotoImage(file='/home/hypedg/Documents/Code/Python/Text-editor/ZPad/icons2/align_center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)

#_________________text_editor__________________#

text_editor = tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#font_family and font_functionality
current_font_family = 'Arial'
current_font_size = 12

def change_font(bind=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))

def change_fontsize(bind=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))

font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)\

#button_funcatonality

#bold button functinality
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

bold_btn.configure(command=change_bold)

#italic button functionality
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

italic_btn.configure(command=change_italic)

#underline button functonality
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

underline_btn.configure(command=change_underline)

#font colour functionality
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=change_font_color)

#align functionality
#align left
def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

align_left_btn.configure(command=align_left)

#align center
def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

align_center_btn.configure(command=align_center)

#align right
def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

align_right_btn.configure(command=align_right)

text_editor.configure(font=('Arial', 12))

#_____________&&&&End_text_editor&&&&__________#

#_________________status_bar_________________#

status_bar = ttk.Label(main_application, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c').replace(' ', ''))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>', changed)

#_____________&&&&End_status_bar&&&&__________#

#_________________main_menu_functionality__________________#

url = ''

#new_functionality
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)

file.add_command(label='New', image = new_icons, compound=tk.LEFT, accelerator='CTRL+N', command=new_file)

#open_functionality
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))

file.add_command(label='Open', image = open_icons, compound=tk.LEFT, accelerator='CTRL+O', command=open_file)

#save_functionality
def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return
    
file.add_command(label='Save', image = save_icons, compound=tk.LEFT, accelerator='CTRL+S', command=save_file)

#save_as_functionality
def save_as(event=None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return

file.add_command(label='Save as', image = save_as_icons, compound=tk.LEFT, accelerator='CTRL+SHIFT+S', command=save_as)

#exit_functionality
def exit_file(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw: 
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

file.add_command(label='Exit', image = exit_icons, compound=tk.LEFT, accelerator='CTRL+W', command=exit_file)

#find_funtionality
def find_func(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='blue')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialouge = tk.Toplevel()
    find_dialouge.geometry('450x250+500+200')
    find_dialouge.title('Find')
    find_dialouge.resizable(0,0)

    #frame
    find_frame = ttk.LabelFrame(find_dialouge, text='Find/Replace')
    find_frame.pack(pady=20)

    #label
    text_find_label = ttk.Label(find_frame, text='Find: ')
    text_replace_label = ttk.Label(find_frame, text='Replace')

    #entry
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    #button
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text='Replace', command=replace)

    #label_grid
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    #entry_grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    #button_grid
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=1, column=0, padx=8, pady=4)

    find_dialouge.mainloop()

#edit_commands
edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='CTRL+C', command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator='CTRL+V', command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='CTRL+X', command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear all', image=clear_all_icon, compound=tk.LEFT, accelerator='CTRL+SHIFT+C', command=lambda:text_editor.delete(1.0, tk.END))
edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='CTRL+F', command=find_func)

#view_check button
view.add_checkbutton(label='Tool Bar', onvalue=True, offvalue=False, image=tool_bar_icon, compound=tk.LEFT)
view.add_checkbutton(label='Status Bar',onvalue=True, offvalue=False, image=status_bar_icon, compound=tk.LEFT)

#color_theme
count = 0
for i in color_dict:
    color_theme.add_radiobutton(label = i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT)
    count += 1

#_____________&&&&End_main_menu_functionality&&&&__________#

main_application.config(menu=main_menu)
#main_application.iconphoto()
main_application.mainloop()