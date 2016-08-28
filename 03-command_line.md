# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

```pwd```` outputs the name of the current working directory.  
```ls``` lists all files and directories in the working directory.  
```cd``` switches you into the directory you specify.  
```mkdir``` creates a new directory in the working directory.  
```touch``` creates a new file inside the working directory.  
```ls -a``` lists all contents of a directory, including hidden files and directories  
```ls -l``` lists all contents in long format  
```ls -t``` orders files and directories by the time they were last modified  
```ls -alt``` combine -a/-l/-t into one command  
```cp``` copies files  
```mv``` moves and renames files  
```rm``` removes files  
```rm -r``` removes directories  
```*``` are wildcards  
```>``` redirects standard output of a command to a file, overwriting previous content.  
```>>``` redirects standard output of a command to a file, appending new content to old content.  
```<``` redirects standard input to a command.  
```|``` redirects standard output of a command to another command aka "pipes"  
```sort ``` sorts lines of text alphabetically.  
```uniq ``` filters duplicate, adjacent lines of text.  
```grep ``` searches for a text pattern and outputs it.  
```sed ``` searches for a text pattern, modifies it, and outputs it.  

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  : lists all contents of a directory, including hidden files and directories  
`ls -a`  : lists all contents of a directory, including hidden files and directories  
`ls -l`  : lists all contents in long format  
`ls -lh`  :  lists long format with readable file size  
`ls -lah`  : lists all contents (including hidden) with readable file size  
`ls -t`  : orders files and directories by the time they were last modified  
`ls -Glp`  : lists all contents long format add slash to directory and exclude Group/owner  

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

`-m` 	Displays the names as a comma-separated list.  
`-R` 	Displays subdirectories as well.  
`-x` 	Displays files as rows across the screen.  
`-q` 	Displays all nonprinting characters as ?  
`-L` 	Displays the file or directory referenced by a symbolic link.  

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` is a command on Unix and most Unix-like operating systems used to build and execute command lines from standard input:  
`find . -name foo* | xargs rm`
