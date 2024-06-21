```mermaid
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