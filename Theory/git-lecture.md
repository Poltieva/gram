## Git

### Intro

**What is Git?**

Git is a distributed version control system. "Version control" is a system that records changes to a file or set of files over time so that you can recall specific versions later. "Distributed" means that every collaborator has a full local copy (clone) of the whole repository including all revision history, branches, etc. 

**What is GitHub (GitLab)?**

GitHub and GitLab are web-based Git repository hosting services.

![Image](images/git-vs-github.png)

**Why do we need Git?**

Even if you work on a project alone, it is useful to be able to keep track of the versions of your system. If you work with others, Git becomes indispensable: you can see who did what and when (and, if you are lucky, even why - which may be understandable from commit messages); you can work in different branches on different independent features and then merge them back into master; since you can create commits locally, you are not dependent on the central repository (i.e. the Internet connection) - in other words, you can do pretty much everything you need to do in a project together with other people. And don't forget: the fact that Git is a distributed system means that even if something happens to the server with the remote repository (e.g., a GitHub server), it will be easy to reconstruct the repository with full history as every collaborator has an exact copy of it.

### Three main sections of a Git project

These are the working directory, the staging area, and the Git directory.

The working directory is a local directory containing the files of the project you are working on.

The staging area (also known as "Index") is where git stores information about what will go into your next commit. You can think about it as a place with the file(s) that will go into one single commit.

The Git directory is where Git stores the metadata and object database for your project. This is the most important part of Git, and it is what is copied when you clone a repository from another computer.

1. You modify files in your working directory.
2. You stage the files, adding snapshots of them to your staging area.
3. You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.

### Configuring Git on your computer

After you have successfully installed Git on your computer, you will want to customize your Git environment.

To make Git remember your credentials (for a particular computer) run the following commands in shell:

$ `git config --global user.name "John Doe"`  
$ `git config --global user.email johndoe@example.com`

With the `--global` parameter you will have to do this only once, but you can change this configuration at any time.

If you want to check your settings, you can use the `git config --list` command to list all the settings Git can find at that point.

### Getting help

If you need help, there are three ways to get it from the Git manual:

$ `git help <command>`  
$ `git <command> --help`  
$ `man git-<command>`

### Initializing/cloning a repo

If you are the author of the project, you will have to **initialize** it. You can do it in the following way:

1. Create a folder on your computer. Give it the name you would like your repository to have. (E.g., you can do this by executing the `mkdir <directory_name>` command in the terminal).
2. Go to that directory: `cd <directory_name>`
3. Run `git init`.

The third command will create a `.git` directory in the current directory (`<directory_name>`). You have let Git know about the existence of your project.

You can accomplish this in one step by running

$ `git init <directory_name>`

Note that this will create a Git repository with no remote.

If you want to get a copy of an existing remote Git repository (**clone** it) – for example, a project you’d like to contribute to – the command you need is

$ `git clone <url>`

You can get the `<url>` from the project's main page on GitHub (this can be done via an `https` protocol, `ssh`, etc). 

### Recording changes to a repo

To check what has been changed since your last commit, use the following command:

$ `git status`

If you add a new file to your directory, Git will show it under the "Untracked files" heading. To begin tracking a new file or directory, use the following command:

$ `git add <file_name>`  
or  
$ `git add <directory_name>` (it will add all the files in this directory)

If you modify an existing file, it will appear under the name "Changes not staged for commit". To stage this file (move it to the staging area), use the same `git add` command.

Some more options with `git add` (these commands will work for the current directory):

$ `git add -u` - stages modified and deleted files (but not new ones)  
$ `git add .` - stages modified and new files (but not deleted ones)  
$ `git add -A` - adds all files to the staging area: tracked and untracked, new and deleted, modified

It happens sometimes that there are files that you don't want Git to see and track. These are often automatically generated files (e.g., the notorious `.DS_Store` files that Mac computers generate automatically, or log files). To resolve this, you can create a file called `.gitignore` and list you problematic files (including wildcards) there.

If you want to see the exact changes you've made between your working directory and your staging area, you should run

$ `git diff`

Running `git diff --staged` (or `git diff -cached`) will show what you’ve staged to go into your next commit.

Now that you have everything you need in your staging area (and just to make sure, run `git status`), you can proceed with the actual commit. To commit your staged changes, run

$ `git commit -m "Your commit message"`

If you only have tracked files in your status (no new files), you can combine the adding and committing steps into one by using the `-a` option:

$ `git commit -am "Your commit message"`

Run `git status` to see what is going on now.

If you want to remove a file from your repo, you can just physically remove the file from your working directory (e.g., by using the `rm <file_name>` command), but this is not the best option as the file will get into the unstaged section of your Git environment, and it will take some thinking to remove it from Git altogether. There is a proper Git command for that which will remove the file from your working directory AND stage it for commit:

$ `git rm <file_name>`  
$ `git rm -r <directory_name>` - removes an entire directory with all files and subdirectories in it

Run `git status` to see that your file IS staged for removal from Git.

You can rename a file in the following way (the renamed file will be staged for commit then):

$ `git mv <file_name1> <file_name2>`

And who knows if your renamed file has been staged? Right, `git status` does.

### Undoing things 

This is an area where you have to be extra careful. You have to know exactly what is happening behind each command as it may not always be possible to revert what you've done erroneously.

$ `git commit --amend` - allows you to amend your commit. If you have changes in the staging area, they will be added to the commit; if not, just the commit message will be changed  
$ `git reset <file_name>` - unstages a file  
$ `git checkout -- <file_name>` - discards changes in a modified file (that is, all your local changes to the file will disappear, so be careful!). You can do without the `--` part here, but if there is a branch or any other identifier with that name in your repo, Git may get confused.

Don't forget to run `git status` after each of these - just for the sport of it.

![Image](images/Octocat.png)

### Viewing the commit history

$ `git log` - lists the commits made in that repository in reverse chronological order – that is, the most recent commits show up first

This command has a lot of options. Some of them are listed below.

$ `git log --summary` - additionally provides the list of added, deleted and modified files for each commit  
$ `git log -p` - shows the difference introduced in each commit. You can add the `-<number>` parameter at the end to see details for the last `number` of commits only  
$ `git log --pretty=oneline` - prints each commit on a single line. The `--pretty` option has several other parameters.

You can also use the time-limiting options such as `--since` and `--until`, e.g.:

$ `git log --since=2.weeks`

To see the commits of a particular author only, you can run

$ `git log --author=bob`

You can explore other options on your own.

### Working with remotes

$ `git remote` - allows you to see which remote servers you have configured  
$ `git remote -v` - shows you the URLs that Git has stored for the shortname to be used when reading and writing to that remote  
$ `git remote add <shortname> <url>` - adds a new remote Git repository as a shortname you can reference later  
$ `git remote show <remote-name>` - allows you to see more information about a particular remote  
$ `git remote rename <shortname1> <shortname2>` - allows you to rename a remote  
$ `git remote rm <shortname>` - allows you to remove a remote

The most commonly used commands are as follows:

$ `git pull` - automatically fetches and merges the data from the remote repo into your local one  
$ `git push <remote-name> <branch-name>` (or just `git push` if you are working with the remote `origin` and in branch `master`) - pushes your changes into the remote repo. This command will work only if you have the write rights for this repo

And don't be surprised if I ask you to run `git status` now. It's a useful command, you know.

To set the default remote and branch as "origin/master" (so that you can just write `git push` from now on), perform the `git push -u origin master` command.

### Branching, merging, and conflicts

Sometimes you need a sandbox to play in - that's where branches come in useful. The main (default) branch is called `master`. You may want to have a separate branch to work on an independent feature which will be merged into `master` later on. You may also want to have a separate branch for each collaborator (who will presumably be working on a separate issue). The main thing is that branches allow you to work independently for some time without interruptions and then merge your [fully functional] work into the main branch.

$ `git branch` - returns a list of your branches  
$ `git branch <branch_name>` - creates a new branch  
$ `git checkout <branch_name>` - switches to an existing branch. Note that Git won't allow you to do this if you have changes in your working directory or staging area - you will have to commit or stash them before you can switch branches. At this point, you may also run `git status` if you feel like it  
$ `git checkout -b <branch_name>` - creates a new branch AND switches to it  
$ `git merge <branch_name>` - merges branch `<branch_name>` into your current branch  
$ `git branch -d <branch_name>` - deletes branch `<branch_name>`

When you try to merge two branches in which the same file(s) was(were) modified in roughly the same place, Git will not be able to make an automatic merge commit for you. It will show a message similar to the following:

    Auto-merging index.html
    CONFLICT (content): Merge conflict in index.html
    Automatic merge failed; fix conflicts and then commit the result.

![Image](images/Yoda.png)

When you run `git status`, you will see a file(s) under the "Unmerged paths" header. You now have to open these files and resolve the conflict manually (i.e., look at the changed segments and decide which one - or maybe a combination of both - to keep). In the file, this will look similar to the following:

    <<<<<<< HEAD:index.html
    <div id="footer">contact : email.support@github.com</div>
    =======
    <div id="footer">
    please contact us at support@github.com
    </div>
    >>>>>>> iss53:index.html

After that, you have to add the corresponding file(s) to the staging area (`git add`). The conflict has been resolved.

Run `git commit`. It is better to run it without the `-m` argument as it will automatically provide a draft of the message for you. In this case it will contain some useful information: the files you have had a conflict in. All you need to do is save the file and close the editor. If your default editor happens to be Vim, typing `ZZ` will do the job.

### Stashing your changes

If you are working on a branch and then suddenly need to switch to another branch, you don't always want to commit your changes (maybe, you are being messy, and you don't want everyone to see your mess in the commit later). Git won't allow you to switch branches when you have uncommitted changes. The solution to this situation is stashing your changes.

$ `git stash` - stashes your changes leaving your working directory clean (and allowing you to switch branches seamlessly). Time to use `git status` for a 100% guarantee  
$ `git stash list` - shows a list of all your stashes (there may easily be more than one)

When you are done with the other branch, you return to your original branch and want to continue with your stashed changes. In order to do this, you have to apply your stashed changes.

$ `git stash apply` - applies your latest stash (keeping it in the stash list)  
$ `git stash pop` - applies your latest stash (and drops it from the stash list)

And guess what? No time like the present; no command like `git status` - to see your stashed changes back!

P.S. Already executing `git status` after each command? Don't worry: that was the objective of this class.

### Useful info

Whenever you execute a Git command, read whatever Git has to tell you: it sometimes gives you useful tips as to how to proceed in a particular situation (this refers in particular to the `git status` command).

![Image](images/GitFiredUp.jpg)

### References

1. Git documentation, available at http://git-scm.com/docs
2. Pro Git by Scott Chacon, available at http://git-scm.com/book/en/v2
3. A tiny course on Git from Code Academy, available at https://try.github.io/levels/1/challenges/1
4. A course on Udacity, available at https://www.udacity.com/course/ud775

