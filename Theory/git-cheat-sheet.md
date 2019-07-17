## Git Cheat Sheet

### Some useful commands

`git init` - create a repository

`git config --list` - list all user settings that Git knows about.

`git status` - check the state of the files in your working directory.  
`git diff` - check the exact line-by-line changes in the files in your working directory.  
`git log` - check the history of commits in your repository.  
`git log --pretty=oneline` - check the history of commits in your repository in a pretty way.

`git checkout -- <file_name>` - cancel all changes in `<file_name>`.  
`git checkout -- .` - cancel all changes in the directory.

`git add <file_name>` - add `<file_name>` to the staging area.  
`git reset <file_name>` - remove `<file_name>` from the staging area.

`git commit -m "Your commit message"` - record the changes in the staging area with the given message.  
`git commit --amend -m "Your commit message"` - fix the commit message or the changes in your last commit.

`git pull <remote> <branch>` - fetch the data from the remote repository and merge it into your local one.  
`git push <remote> <branch>` - push new data to a branch in the remote repository.

`git branch` - check which branch you are using.  
`git checkout -b <branch_name>` - create a new branch `<branch_name>` and switch to it.  
`git checkout <branch_name>` - switch to `<branch_name>`.

### How to push your results to the repository

1. Run `git add <file_name>` on the files with changes that you want recorded. If all files have to be added, run `git add -A`.
2. Run `git commit -m "Your commit message"` to record your changes with a clear message.
3. Run `git push` to push your changes to the remote branch.

To pull the latest changes from `master`, run `git pull origin master`.
