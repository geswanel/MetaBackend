## Prestudy

- Version Control
- Collaboration
- Linux
    - Command Line
- Git
- Github

## Time
(13 h on certificate page)
2h video + 3+ h reading = 5h material
4 graded + Labs

## 1 WEEK: Software collaboration

### Course introduction
- VC - system to track changes and modifications
- Program
    - Git and Github - basic commands
    - unix commands
    - exercises
- Collaboration
    - Communication
    - Adjust from person to person

### Introduction to VC
- What is VC
    - System to track changes and modifications: Add, Modify, Delete files
    - History of changes - roll back in time
    - Indentity - who made a feature
    - Collaboration
    - Automation
    - Efficiency
    - Peer review
    - AGILE methodology (2 week iteration)
- How meta engineers collaborate?
    - Gatekeepers?
    - Merge conflict
    - Monolitic or microservises
    - branches
- [Git terminology](git_commands.pdf)
- [Systems of VC and tools](https://www.linkedin.com/pulse/differentiate-between-centralized-distributed-version-control-ejv2c)
    - Centralized (CVCS)
        - one server with all history and codebase
        - easier to learn, more access control
        - slower
    - Distributd (DVCS)
        - each client is a server
        - speed and performance
    - pull changes from server and push them back
- History
    - CVS - Concurrent Version system
        - No integrity checking + only with text files
        - SVN (Subversion) - correct above problems
    - Bitkeeper - 2000 linux first VCS -> license was revoked 2005
        - Git by Linus Torvalds - 2007
        - Mercurial by Olivia Mackall
- VCS in professional software development. **CI/CD**
    - Workflow - rules how work is managed
    - Continuous Integration - small changes merged frequently -> compile and run tests automatically -> stable, less merge conflicts
    - Continuous Delivery - After CI, automatically packages the app and prepares for deployment. Avoid human error during packaging
    - Continuous Deployment - After prev step, automatically deploying to a test (staging) for validation and then to the live (production)
- History of revisions
    - Who, When, What reason and what code
    - Easy access to code of others
    - Solving merge conflicts
    - Feature -> development -> pull request -> peer review -> production
- Staging and production
    - Development environments - find any issues that may arise
        - Developer Environment
        - UAT or QA
        - Staging - mimic of production
            - New feature - flags to turn on/off and check effect
            - Testing
                - unit testing
                - integration testing
                - performance testing
            - Data migrations issues
            - Configuration changes
        - Production - for users -> any problem should be found in staging environment
            - Downtime
            - Vulnerabilities
            - Reputation

### Module Summary
- Collaboration
- VCS and its types
    - Centralized and Distributed
- History of VCS
- Conflict resolution
- Strategies for collaboration
    - Workflow
    - Continuous integration
    - Continuous Delivery
    - Continuous Deployment
- Staging and Production
    - Staging: New features, Testing, Migrations, Configuration changes
    - Production: Downtime, Vulnerabilities, Reputation

- Additional Reading
    - [About Version Control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)
    - [List of Version Control Software](https://en.wikipedia.org/wiki/List_of_version-control_software)
    - [The benefits of a distributed version control system](https://about.gitlab.com/topics/version-control/benefits-distributed-version-control-system/)
    - [What is Cloning?](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
    - [AGILE](https://www.geeksforgeeks.org/software-engineering-agile-software-development/)

## 2 WEEK: Command Line
### Unix commands
- Command line
    - Interact with computer = exchange information
        - Input: mouse, keyboard, mic
        - Output: Monitor, speakers
    - GUI - easier way to interact with computer
    - Command line - more powerful tool to interact with computer
        - Create, move, delete files and dirs
        - Unzip
        - Stop, start, restart programs
        - Download from the Internet
        - Manage access
        - Containerization
        - Aliases
        - Track software
        - Access and control remote server
        - Install upgrade uninstall software
        - Automation
        - Mount and Unmount computer drives
        - check disk space
    
- What is unix Commands?
    - Unix - 1969 => Linux 1990
    - Commands
        - `cd`, `touch` `mkdir`
        - `code` open in vs code
        - `pwd` - print working dir
        - `mv` `cp` `ls`
            - `mv what where`
        - `clear`
    - Flags - change command behavior
        - `ls -l`, `ls -a`
    - Helper
        - `man [command]`
- Git bash on windows
    - `vim`, `chmod`, `./script.sh`
    - `less` - show information in the file (cat)
    - Creating bash script using vim
    - rights (rwx)
    ```bash
    #!/bin/bash
    echo "Hello,World"
    ```
    - `cd ~/`
        - local and absolute path
    - .bashrc file - configurations (history, aliases etc). Executed at the beginning of cmd session
    - .profile - environment variables
- Pipes - combine commands `com1 | com2`
    - `wc file -w` - word count
    - `cat file` - print file in cmd
    - `cat file1 file2 | wc -w`
    - `ls | wc - w`
- [Redirections](https://mirror.apps.cam.ac.uk/pub/doc/redhat/AS2.1/rhl-gsg-en-7.2/s1-navigating-usingcat.html)
    - Standard input (0) `cat < input.txt`
    - Standard output (1) `com > output.txt`
    - Standard error (2) `com 2> error.txt`
        - combine with stdout `com > output.txt 2>&1`
- Grep - global RegEx print
    - `grep text file` - partial search
    - `-i` ignore case
    - `-w` exact pattern
    - `ls -l dir | grep pattern` - search file in directory

### Module Summary
- Grep
- Redirection and Pipes
- Commands
- unix -> linux

- Additional resources
    - [Agile methodologies](https://www.planview.com/resources/guide/agile-methodologies-a-beginners-guide/)
    - [Installing git on mac and windows, detailed instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
    - [Bash Reference Manual](https://www.gnu.org/software/bash/manual/html_node/index.html#SEC_Contents)
    - [Bash Redirections](https://www.gnu.org/software/bash/manual/html_node/Redirections.html#Redirections)
    - [Bash Cheatsheet](https://devhints.io/bash)
    - [Grep Cheatsheet](https://devhints.io/grep)
    - [Grep Manual](https://man7.org/linux/man-pages/man1/grep.1.html)
    - [History and Timeline of Unix](https://unix.org/what_is_unix/history_timeline.html)
    - [History of Vim](https://en.wikipedia.org/wiki/Vim_(text_editor))
    - [How to work with relative and absolute paths](https://www.geeksforgeeks.org/absolute-relative-pathnames-unix/)
    - [Unix Commands Cheatsheet](https://cheatography.com/jluis/cheat-sheets/bash-and-unix-commands/)
    - [Vim Cheatsheet](https://vim.rtorr.com/)

## 3 WEEK: Working with Git
### Git and Github
- Git - VCS that allows to keep track of changes in the project
    - Fast; Accessible; Open-Source; Reliable
- Github - cloud-based git repository management system
    - pull-requests; access-control; automation
    - security; profile features; open-source; other features
- Connection
    - HTTPS connection
        - creation of token
        - Git Credential Manager
    - SSH connection
        - creation of key
        - saving key to github account
- `git clone` remote repository to the local machine
- How git works
    - `git init`
    - Git workflow: modified -> staged -> committed -> remote
        - `git add` -> `git commit` -> `git push`
        - `git fetch`, `git pull`
    - other commands
        - `git status` - check changes
        - `git restore --staged` - make files untracked
    - Branches
        - `git branch`, `git branch name`, `git checkout name`, `git checkout -b name`
        - `git push -u origin br_name`
        - `git pull` on the branch will pull all changes
        - Branch is isolated and need to be merged into the main line
            - pull request is needed to obtain peer review and validate changes
    - Remote vs local
        - you can work at local machine offline and then push changes to remote repo
        - `git remote -v`, `git remote add name link`
        - `git clone`, `git init`
        - `git pull`
    - Push and pull
        - `git push` - pushes changes to remote repo by comparing them and changing updated files. (merge)
    - Resolving conflicts
        - conflicts appear when two developers work at the same files
        - pulling main before pushing
        - steps
            - `git log --merge`
            - resolving conflict
            - `git add` `git commit` `git push`
- Git workflow
    - feature workflow
        - checking out or pulling a project
        - create new branch from main line
        - work in the branch
        - commit changes
        - push changes and make pull request
        - peer review -> merging with main
- HEAD - reference to current commit (or branch)
    - .git folder
    - `cat HEAD`
    - `/refs/heads/branch` - commit ids for branch
- diff commands
    - status - filenames, diffs - changes inside files
    - `git diff HEAD filename`
    - `git diff commit1 commit2`
    - `git diff br1 br2`
- blame
    - `git log --pretty`
    - `git blame filename`
        - messages `id author date time linenum content`
        - `git blame -L 5,15 filename` lines
        - `git blame -l filename` format full id
    - `git log -p comid` - changes in commit
- forking

### Creating repo with forking