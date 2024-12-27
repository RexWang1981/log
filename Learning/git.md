
# Git learning

* [Learning resource](https://www.youtube.com/watch?v=rH3zE7VlIMs)

## 1.1 Setup

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
* find .git in foldername
* cat .git in foldername
* cat filename
* echo "* The Intership" > titles.md
* cd ..
* cd ~/desktop/xxx
* mkdir

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

## 1.2 Repositories

Learn about Git repositories, what they are, and how to work with commits

## 1.3 Internals

Learn how Git stores data on the files system and the plumbing commands that make it all work

Terms

* HASH=HAC
* blob = Binary Large Object
* tree: git's way of storing a directory
* blob: git's way of storing a file

## 1.4 Config

Learn how to configure Git and set up your user information

* git config --add --global user.name "Rex Wang"
  * git config: the commend that interact with your Git configuration
  * --add: flag starting you want to add a configuration
  * --global: flag starting you want this configuration to be stored globally in your ~/gitconfig file. The opposite is "local". which stores the configuration in the current repository only.
  * user: the section
  * name: the key within the section
  * “RexWang”：the value you want to set for the key
* git config --list --local
* git config --list --global
* git config --get user.name
* git config --get user.email
* git --unset
* git --unset-all example.key
* git config --remove-section section

## 1.5 Branching

Practice creating and switching between branches

* git branch
* git branch -m oldname newname
* git branch -m master main
* git config --add --global init.defaultBranch main
* git config --unset-all init.defaultBranch
* git config --list
* git branch my_new_branch
* git switch -c my_new_branch
* git checkout my_new_branch
* git branch -m existing_branch_name to new_branch_name

Log flag

* git log decoration=full
* git log decoration=no
* git log --graph
* git log --graph
* short: the default
* full: shows the full ref name
* no: no decoration

## 1.6 Merge

Merge changes from one branch into another and learn how merge commits work

* git merge branch_name
* git log --oneline --graph --decorate --parents
* git branch -d branch_name

Terms

* merge base
* rebase
* pointer

## 1.7 Rebase

Learn about the cooler way to integrate changes from one branch into another.  
You should never rebase a public branch (like main or master) onto anything else.

* git rebase main
* if conflict there options:
  * modify
  * delete
  * xx

## 1.8 Reset

Learn how to undo changes with the reset command

* git reset --soft COMMITHASH
* git reset --hard COMMITHASH  # _this is an danger operation, avoid to do it_
* git reset --soft HEAD~1
* git diff --staged
* git log --oneline -1
* git log -p --oneline -1

## 1.9 Remote

Setup a remote repository and learn how to push and pull changes

* git remote add <name> <url>
* git fetch
* git log origin/branch --oneline

Terms

* remote: in Git, the another repo is called remote. Not necessarily to be GitHub or other remote server, it can be local repo.
* origin: the standard convention is that when you're treating the remote as the "authoritative source of truth" (such as GitHub) you would name it the "Origin".
* upstream

## 1.10 GitHub

Learn how to use Git with GitHub, the most popular Git hosting service

* git push origin main
* git pull [<remote|origin>/<branch>]
* git pull origin master
* git config --global pull.rebase true

## 1.11 Gitignore

Learn about using a .gitignore file to exclude files and directories from being tracked by Git.

* xxx

## 2.1 Fork

Learn how to fork a repository and contribute to open source projects

* git fork
* git clone http://github.com/thePrimeagen/megacorp
* git remote add upstream https://github.com/ORIGINAL-OWNER/ORIGIN
* git add . && git commit -m "add myself as a contributor"
* git checkout -b add_contrib
* git push origin add_contrib
* git remote -v
* git remote rm origin

Fork Work flow:

1. Fork the main repo
2. Clone down forked repo to own environment
3. Make the changes to the main branch in the forked repo
4. Push change to the main branch in the forked repo
5. Open a pull request with the changes from the fork onto the original repo

After fork the other people's repo, normally set new remote to the original repo incase to get the new update from the original repo. Also help to eliminate the conflict with the pull request.

## 2.2 Reflog

Work with the reference log to recover lost commits

* cat .git/HEAD
* git reflog HEAD@{0} : where HEAD is now
* git reflog HEAD@{1} : where HEAD was 1 move ago
* git reflog HEAD@{2} : where HEAD was 2 move ago
* git reflog HEAD@{n} : where HEAD was n move ago
* git cat-file -p e6134a2
* git merge HEAD@{1}

## 2.3 Merge Conflicts

Understand merge conflicts, how they arise, and how to resolve them

## 2.4 Rebase Conflicts

Learn about rebase conflicts and how to safely keep the project history clean

* git rebase main
* git checkout --theirs
* git checkout --ours
* git rebase --continue: handle multi conflicts
* git config --local rerere.enable false
* re -rf .git/rr-cache
* git rerere: remember how you solve the conflict and deal with the same kind of conflict automatically.
* git config --unset --local rerere.enable
* git config --list | grap rerere
* git reset --soft HEAD~1

## 2.5 Squash

Many teams require developers to squash commits, learn how and why you would do it

* git push origin master
* git push origin master --force  # dangerous but useful.
* never squash main/master

## 2.6 Stash

You don't always need to use branches to work on multiple things at once, learn how the stash can save time

* git stash
* git stash list
* git stash pop
* git stash@{0}
* git stash --message "xxx"
* git stash apply
* git stash drop
* git stash apply stash@{2}
* git stash drop stash@{2}

## 2.7 Revert

Git reset is a bit of a blunt tool, learn about git revert and how to safely undo changes

* git log
* git reverse <commit-hash>
* git diff
* git diff HEAD~1
* git diff COMMIT_HASH_1 COMMIT_HASH_2

## 2.8 Cherry Pick

Use git cherry pick to selectively move changes from one branch to another

* git cherry-pick <commit-hash>
* git cherry-pick --abort

## 2.9  Bisect

Slogging through git history can be time consuming, learn how git bisect can find bugs fast

* git bisect start
* git bisect good <commitish>
* git bisect bad <commitish>
* git bisect reset
* git show HASH

## 2.10 Worktrees

Learn when git worktrees can be better than regular old branches when it comes to parallel development

* git worktree list
* git worktree add <path> [<branch>]

## 2.11 Tags

Learn how to use git tags properly to version and release your code

* git tag
* git tag -a "2024-12-26 milestone" -m "message"
* git tag -a v3.10.2 -m "fixed a lil bug"
* git push origin --tags

Term:

* Semver
  * v
  * Major (breaking change)
  * .
  * Minor (safe feature)
  * .
  * Patch (safe bug fixes)
* Example: **v3.12.5**

## Example to start a repo

* git init
* git config --add --global user.name "Rex Wang"
* git config --add --global user.email emailwangwei@gmail.com
* git remote add origin https://github.com/RexWang1981/website.git
* git config --global init.defaultBranch master
* git add .
* git commit -m "1st change, tidy the folder tree"
* git status

---
Done 2024-12-26