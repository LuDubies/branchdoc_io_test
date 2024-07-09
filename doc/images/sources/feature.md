```mermaid
%%{init: { 'gitGraph': {'showCommitLabel': false}} }%%
gitGraph
   commit tag: "v1.0.0"
   branch release/v2.0.x
   branch feature/multiuser_support
   commit
   checkout release/v2.0.x
   branch feature/client_rework
   commit
   checkout feature/multiuser_support
   commit
   checkout feature/client_rework
   commit
   checkout release/v2.0.x
   merge feature/multiuser_support
   merge feature/client_rework
   checkout main
   merge release/v2.0.x tag: "v2.0.0"
```