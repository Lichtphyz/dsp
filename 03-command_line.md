# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

- `ls` lists files and subdirectories of the current location
- `ls -a`  includes hidden files in the standard list
- `ls -l`  long form list of local files, including user, modificaiton date, etc. file sizes are in bytes
- `ls -lh`  same as ls -l, but file sizes show in B, Kb, Mb, etc.
- `ls -lah`  long form list, includes hidden files, shows abriaviated file sizes
- `ls -t`   sorts files by modification time
- `ls -Glp` -G colors directories (violet), long form list, with final slash after directories

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

*I found a more extensive (and useful!) [ls option list](http://www.rapidtables.com/code/linux/ls.htm#options)*, some of these are from there, hope you don't mind.

**My 5 favorite ls -options**
1. `ls -S` list files by size, largest to smallest
1. `ls -R` also lists contents of each subdirectory AND each of their subdirectories all the way down
1. `ls -X` list files y extension
1. `ls -1` limits output to 1 entry per line
1. `ls -u` sorts by time of last access

all of these support other useful modifications such as -l, -G, -lh, -a, etc.

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > The Unix command `xargs` is used to take the output of one command (such as grep, find, or ls) and individually pipe each returned result on to a second command to be run on *each* output of the first command.  Here's one silly example I just made up:

>>> `$find python | xargs du`

>>The `find python` part will generate a list of files containing "python" in their path and the `du` command will then estimate the file size of each one of them in turn.

 

