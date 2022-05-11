# Vim Cheatsheet
When you boot VIM you enter NORMAL mode
To enter INSERT mode type: `i`
To exit INSERT mode type: `ESC`

Note: When you are insert mode, you will see `-- INSERT --` on the bottom
left corner

## INSERT Mode
When you're in insert mode, Vim will behave like most other text editors, you
will be able to use the arrow keys to navigate, and you can type as normal

## NORMAL Mode
Normal mode allows you to take advantage of Vim's shortcuts.
Some useful shortcuts:
- `yy` (yank (copy))
- `p` (paste)
- `dd` (delete)
- `.` (repeat the last command)
- `u` (undo)
- `ctrl + r` (redo)

In normal mode you can repeat a command multiple times, suppose you wanted to the
following 10 lines, you could write:
- `10dd`

## COMMANDS
To write a commnd you must first type : in NORMAL mode
Some useful commands:
- `:w` (save the current file)
- `:q` (exit the current file)
- `:wq` (save and exit the current file)
- `:!q` (exit without saving (DANGEROUS))
- `:set number` (show line numbers)
- `:set relativenumber` (show relative line numbers)
