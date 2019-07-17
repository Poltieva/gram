## Terminal Cheat Sheet

### Checking where you are

`cd <dir_name>` - navigate to a directory.  
`cd ..` - navigate a level higher.

`ls` - list all files and directories. (Use `dir` for Windows.)  
`ls -l` - list all files and directories with more detailed info.

`mkdir <dir_name>` - create a directory.

### File manipulations

### Unix commands for Git

Unix and OS X:

`touch <file_name>` - create a file.  
`rm <file_name>` - remove the file.  
`cp <file_from_name> <file_to_name>` - create a file.  
`mv <file_from_name> <file_to_name>` - move (or rename) a file.

Windows:

`type nul > <file_name>` - create a file.  
`del <file_name>` - remove the file.  
`copy <file_from_name> <file_to_name>` - create a file.  
`move <file_from_name> <file_to_name>` - move (or rename) a file.

### Working with file content

Unix and OS X:

`printf "Text I am writing." > <file_name>` - print content to a file.  
`cat <file_name>` - get the content of a file.  
`head -n3 <file_name>` - show the first 3 lines of a file.

`wc <file_name>` - get the statistics of a file.

`sort <file_name>` - sort the lines in a file.

`uniq <file_name>` - show the unique lines in a sorted file.

`grep pattern <file_name>` - find all lines with a pattern in a file.

`diff <file_from_name> <file_to_name>` - compare the contents of two files line by line.

Windows:

`type "Text I am writing." > <file_name>` - print content to a file.  
`type <file_name>` - get the content of a file.

`sort <file_name>` - sort the lines in a file.

`find pattern <file_name>` - find all lines with a pattern in a file.

`fc <file_from_name> <file_to_name>` - compare the contents of two files line by line.


Use `>` to indicate the output file instead of printing to the Terminal.

### References

- https://learnbyexample.gitbooks.io/linux-command-line/content/Text_Processing.html#cmp
- https://www.computerhope.com/unix.htm
- https://skimfeed.com/blog/windows-command-prompt-ls-equivalent-dir/
