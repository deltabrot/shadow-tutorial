# reminds me of the /vanish you used on minecraft to make challenges and then blew up my base

# Welcome to deltabrot shadow-tutorial.
#
# shadow: user = does not know how to use vim
# deltabrot: don't worry about that, we'll train you up
# deltabrot: you still ther?
# shadow: yes why do you do this 2 beers in when i'm impaired?
# deltabrot: best way to learn = !false
# deltabrot: ;)
# deltabrot: let's start with the absolute basics of how to use vim, what you need to know is there are 2 primary modes, normal mode, and insert mode.
# deltabrot: normal mode is where you can use a wide variety of vim "bindings" (or hotkeys) to quickly navigate portions of text, we will come to that later.
# deltabrot: insert mode is where vim basically behaves like any other text editor that you're familiar with.
#
# == VIM ==
# When you initially open a file using vim, you will find yourself in NORMAL mode.
# To enter INSERT mode, simply press i, to exit insert mode press ESC.
# Give this a try now
# To enter INSERT mode, simply press i, to exit insert mode press ESC.
# Give this a try now
# Notice the -- INSERT -- sign show on the bottom left? yes
# All you really need to know is how to get into insert mode, and how to natigate text in the most rudimentary form, you can do this using arrow keys.
# Now attempt to enter INSERT mode and navigate to the top of the file and type something.
#
# The other important part of vim is being able to save files and exit files.
# To do this you need to be in NORMAL mode.
# You then need to enter a "command".
# To enter a command, while in NORMAL mode, type a colon (:).
# Then you will be able to type a command.
# Now let's try saving this file using the command :w.
# Give it a try.
# Notice the text on the bottom left that read:
# "example.py" 39L, 1935B written
# That means you successfully saved the file.
# Now let's try exiting the file using :q
# Give it a try.
# Boom, you are now a fully qualified vim consultant. bullshit, i looked at the vim interactive tutorial and it was a lot more complex and hard to understand, hence why i don't use it
# Okay, well let's put that to the test shall we?
# I'm going to create a file, I want you to create the exact same file using what you know.
#
# Another useful command is :wq which saves and exits the file.
# Give it a go, save and exit this file, and add a line of text that reads:
# deltabrot is writing a tutorial
# To shadows-file.txt
#
# You can include line numbers using the following command:
# :set number
#
# You can include relative line numbers using the following command:
# :set relativenumber
#
# Not as hard as it seems right? sure but the tutorial makes it out to be a lot harder.
# Nah I'm not gonna carry on much longer, I just want to go over some basic python, but then we'll call it quits, I just want to focus on basic VIM usage really. I'll teach you some really basic VIM commands.
#
# i'm back like a heart attack, no slack or you'll get a smack
# very cool
# So let's do some basic VIM commands
#
# First off you're going to want to know how to copy and paste
# COPY in VIM is not called copy, it's called YANK
# you need to press yy in NORMAL mode to copy a line of text
# Then you can press p to paste, like so:

print("Hello, world")
print("Hello, world")
print("Hello, world")

# You give it a go:


# also once a line is copied you can paste it multiple times by just pressing p again.
# huh? didn't do anything is it :yy? and 
# don't forget the # so the line is treated as a comment in python
# you need to press yy while on the line you want to copy, watch
# you need to press yy while on the line you want to copy, watch
# also once a line is copied you can paste it multiple times by just pressing p again.
# also once a line is copied you can paste it multiple times by just pressing p again.
# also once a line is copied you can paste it multiple times by just pressing p again.

# Try it


# Next you're going to want to delete all that shit
# Do so by pressing dd

# Another cool trick is you can repeat the last command you executed by pressing .
# watch this:

# Give it a try:wait, dd does that delete the line above below or you're on
# It deletes the line you're on, look:

# Try writing a line of random text, paste it 10 times then delete them using . after deleting the first one using dd

# Nice, another useful thing to know, if you think you've typed the command wrong, just tap ESC a couple of times, that will reset NORMAL mode.

# Next we can talk about repeating in VIM, so if I wanted to copy and paste a line 5 times, I could literally type:
# yyppppp
# Alternatively I could type:
# yy5p
#
# Watch this:

# deltabrot is writing a tutorial
# deltabrot is writing a tutorial
# deltabrot is writing a tutorial
# deltabrot is writing a tutorial
# deltabrot is writing a tutorial
# deltabrot is writing a tutorial

# You need to type the command in normal mode, not insert mode
# Similarly I can do it with delete, so: 5dd

# see? in normal mode doesn't work, because there was nothing to delete, first try pasting a line 5 times

# see? it's on the line i want but 5yy doesn't work either
# Because you YANKed the line 5 times
# Because you YANKed the line 5 times

# Okay last thing, how do undo and redo?
# Undo is the hotkey u
# Redo is the hotkey ctrl+r

# Wow something else
# This is some text
# This is more text
# This is more text

# Did you get the hang of that? yes

# Great let's make a cheatsheet
