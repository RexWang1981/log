
# Git learning

* [Learning resource](https://www.youtube.com/watch?v=rH3zE7VlIMs)

## 1 Setup

Install and configure Git on your local machine

Shortcuts for the manual:

* q: quits the manual
* j: one line down
* k: one line up
* d: half page down
* u: half page up
* /<term>: search for term
* n: Next search term
* N: Previous search term
* rm -rf webflyx
* rm -rf webflyx-local
* mdr webflyx
* ls
* ls -a


Porcelain and plumbing

* git status
* git add
* git commit
* git push
* git pull
* git log
* git apply
* git commit-tree
* git hash-object

Assignment

* git config --get user.name
* git config --get user.email
* git config --add --global user.name "Rex Wang"
* git config --add --global user.email emailwangwei@gmail.com
* git config --list
* git config --list --local
* git stash list
* cat ~/.gitconfig
* cat .git/HEAD
* git config --global init.defaultBranch master
* git init
* content
* 

Status

* untracked
* staged: ready for commit
* committed:
* git status
* git add <file name or doc name>
* git add .
* git commit -m "<comment>"
* git log
* git --no-pager log -n 10
* git --no-pager log -n 10 --oneline --parents
* git --no-pager log -n 10 --oneline --parents --graph
* cat path/to/file
* xxd path/to/file
* git cat-file -p <filename>


## 2 Repositories

Learn about Git repositories, what they are, and how to work with commits

Terms

* HASH=HAC
* blob = Binary Large Object
* tree: git's way of storing a directory
* blob: git's way of storing a file

## 3 Internals

Learn how Git stores data on the files system and the plumbing commands that make it all work

## 4 Config

Learn how to configure Git and set up your user information

## 5 Branching

Practice creating and switching between branches

## 6 Merge

Merge changes from one branch into another and learn how merge commits work

## 7 Rebase

Learn about the cooler way to integrate changes from one branch into another

## 8 Reset

Learn how to undo changes with the reset command

## 9 Remote

Setup a remote repository and learn how to push and pull changes

## 10 GitHub

Learn how to use Git with GitHub, the most popular Git hosting service

## 11 Gitignore

Learn about using a .gitignore file to exclude files and directories from being tracked by Git.

## 12 Fork

Learn how to fork a repository and contribute to open source projects

## 13 Reflog

Work with the reference log to recover lost commits

## 14 Merge Conflicts

Understand merge conflicts, how they arise, and how to resolve them

## 15 Rebase Conflicts

Learn about rebase conflicts and how to safely keep the project history clean

## 16 Squash

Many teams require developers to squash commits, learn how and why you would do it

## 17 Stash

You don't always need to use branches to work on multiple things at once, learn how the stash can save time

## 18 Revert

Git reset is a bit of a blunt tool, learn about git revert and how to safely undo changes

## 19 Cherry Pick

Use git cherry pick to selectively move changes from one branch to another

## 20  Bisect

Slogging through git history can be time consuming, learn how git bisect can find bugs fast

## 21 Worktrees

Learn when git worktrees can be better than regular old branches when it comes to parallel development

## 22 Tags

Learn how to use git tags properly to version and release your code