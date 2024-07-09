# NewTec GIT branching guidelines

```{note}
This whole documentation is a draft and work in progress. It does not represent the current guidelines of the company.
```

## Introduction

[Git](https://git-scm.com/) is a Version Control System (VCS) used in a huge amount of projects, not only open-source but also private and in the industry. It works by creating "snapshots" of your files, so you can share them with others or come back to an old version if something is not working right. It allows efficient cooperative work and a traceable lifecycle for software projects, which is a great advantage for developers. To learn more about using Git, you can visit this [cool website](https://learngitbranching.js.org/).

Git is not restrictive on how the project structure shall look like, or how each repository shall be configured, making it the responsibility of users that work together to agree on the conventions and structures to be used. Depending on the project complexity and team size, different rulesets ensure either light overhead and flexibility or a tight harness around each developer.

This documentation is intended to introduce the overall branching strategy to be used in all NewTec projects, specifically those hosted in [GitHub](https://github.com/NewTec-GmbH). It will serve as a starting point for new project members to get up to speed with the existing workflow and a reference manual for developers.

## Content

Below is a visualization of an example workflow in a project. More information can be found on the following pages:

- [Branch types](branch_types.md): Details on the different types of branches that are found in a project.
- [Pull Requests](pull_request.md): What is a PR and why are these mandatory.
- [Continuous Integration](ci.md): Introduction to the CI/CD workflows.

```{mermaid}
%%{init: { 'gitGraph': {'showCommitLabel': false}} }%%
gitGraph
    commit tag: "v1.0.0"
    branch release/v2.0.x
    branch feature/UI
    commit
    checkout release/v2.0.x
    branch feature/AJAX
    commit
    checkout release/v2.0.x
    merge feature/AJAX
    checkout feature/UI
    commit
    checkout release/v2.0.x
    merge feature/UI
    checkout main
    merge release/v2.0.x tag: "v2.0.0"
    branch release/v3.0.x
    branch feature/DB
    commit
    checkout release/v3.0.x
    merge feature/DB
    checkout main
    checkout release/v2.0.x
    branch bugfix/Button
    commit
    checkout release/v2.0.x
    merge bugfix/Button tag: "v2.0.1"
    checkout release/v3.0.x
    branch feature/UI_rework
    commit
    checkout release/v3.0.x
    merge feature/UI_rework
    merge bugfix/Button
    checkout main
    merge release/v3.0.x tag: "v3.0.0"
```
