---
layout: "default"
title: "git"
word_count: 154
created: "2024-11-28T18:24:53.203109"
modified: "2024-11-28T18:24:53.203109"
---
# git

## Git commands

| Action                                    | command                                      | details            |
| ----------------------------------------- | -------------------------------------------- | ------------------ |
| diff between branches                     | git diff {branch1}...{branch2}               | Na                 |
| revert a committed and merged file        | 1. git checkout {their_branch} -- {filename} | NA                 |
| ------- continued  ----------             | 2. git restore --staged {filename}           | NA                 |
| revert to prev commit, ignore any changes | git reset --hard HEAD                        | Head - Prev commit |

## References

### How do I revert a Git repository to a previous commit?

[How do I revert a Git repository to a previous commit](https://stackoverflow.com/questions/4114095/how-do-i-revert-a-git-repository-to-a-previous-commit)

## revert a committed and merged file

Example:

```console
    git checkout gl/8000/main -- manageability/yang/framework/rpc/yang/Cisco-IOS-XR-ipv6-ping-act.yang
    git restore --staged manageability/yang/framework/rpc/yang/Cisco-IOS-XR-ipv6-ping-act.yang
```

## Using submodules

[How to create a git submodule](https://www.vogella.com/tutorials/GitSubmodules/article.html#:~:text=Git%20allows%20you%20to%20include,the%20parent%20repository's%20working%20directory.)