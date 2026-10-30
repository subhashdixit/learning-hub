# Git, Docker and Deployment — questions and worked answers

[Subject home](../README.md) · [Theory map](../01-theory/README.md) · [Practicals](../02-practicals/README.md)

Try each answer first, then expand the explanation. Questions follow the lesson order. Programming and SQL practice sets include additional runnable solutions in Practicals.

- [01 — Git working tree, staging, commits, branches and history](#lesson-01)
- [02 — Remotes, pull requests, merges, rebases and conflict resolution](#lesson-02)
- [03 — Docker images, containers, builds, volumes and configuration](#lesson-03)
- [04 — APIs, schemas, errors, authentication and application design](#lesson-04)
- [05 — CI/CD, quality gates, environments and release strategies](#lesson-05)
- [06 — Monitoring, reliability, secrets and incident response](#lesson-06)

<a id="lesson-01"></a>

## 01 — Git working tree, staging, commits, branches and history

[Read the lesson](../01-theory/lesson-01-git-mental-model.md)

### Q001. What goes in the next commit?

<details>
<summary>Answer</summary>

The staged/index snapshot, which can differ from current working files.

</details>

### Q002. Does .gitignore remove a tracked secret?

<details>
<summary>Answer</summary>

No. It does not erase existing tracking/history or revoke the secret.

</details>

### Q003. What is a branch?

<details>
<summary>Answer</summary>

A named movable reference to a commit, not a separate copy of every file.

</details>

<a id="lesson-02"></a>

## 02 — Remotes, pull requests, merges, rebases and conflict resolution

[Read the lesson](../01-theory/lesson-02-collaboration-and-recovery.md)

### Q004. Fetch versus pull?

<details>
<summary>Answer</summary>

Fetch updates remote-tracking refs; pull additionally integrates according to a merge/rebase strategy.

</details>

### Q005. Revert versus reset?

<details>
<summary>Answer</summary>

Revert adds an inverse commit; reset moves a reference and can affect staged/working content depending on mode.

</details>

### Q006. Does no textual conflict prove compatibility?

<details>
<summary>Answer</summary>

No. Behavioural interactions can fail even when files merge cleanly.

</details>

<a id="lesson-03"></a>

## 03 — Docker images, containers, builds, volumes and configuration

[Read the lesson](../01-theory/lesson-03-docker-and-environments.md)

### Q007. Image versus container?

<details>
<summary>Answer</summary>

The image is the packaged artifact; a container is a running instance with runtime state/configuration.

</details>

### Q008. Why use a volume?

<details>
<summary>Answer</summary>

For deliberately persistent or shared data outside the ephemeral container writable layer.

</details>

### Q009. Does build success prove service correctness?

<details>
<summary>Answer</summary>

No. Exercise the running application and its failure paths.

</details>

<a id="lesson-04"></a>

## 04 — APIs, schemas, errors, authentication and application design

[Read the lesson](../01-theory/lesson-04-apis-and-applications.md)

### Q010. Authentication versus authorization?

<details>
<summary>Answer</summary>

Identity verification versus permission to perform a specific action on a specific resource.

</details>

### Q011. Why version an API?

<details>
<summary>Answer</summary>

Callers depend on semantics and shape; changes need a compatibility/migration strategy.

</details>

### Q012. Why a request ID?

<details>
<summary>Answer</summary>

To trace a request across components and, when designed appropriately, support idempotent handling.

</details>

<a id="lesson-05"></a>

## 05 — CI/CD, quality gates, environments and release strategies

[Read the lesson](../01-theory/lesson-05-ci-cd-and-releases.md)

### Q013. CI versus deployment?

<details>
<summary>Answer</summary>

CI validates integrated changes; deployment changes a running environment. They can be connected but are distinct actions.

</details>

### Q014. Why artifact identity?

<details>
<summary>Answer</summary>

It ties the running version to the code, dependencies and checks that produced it.

</details>

### Q015. Why consider database compatibility?

<details>
<summary>Answer</summary>

Old and new application instances may coexist, and data/schema changes may not be reversible by code rollback.

</details>

<a id="lesson-06"></a>

## 06 — Monitoring, reliability, secrets and incident response

[Read the lesson](../01-theory/lesson-06-production-operations.md)

### Q016. Health endpoint versus model quality?

<details>
<summary>Answer</summary>

A health endpoint may show process availability while predictions remain wrong.

</details>

### Q017. Why test restoration?

<details>
<summary>Answer</summary>

It verifies backups, procedure, credentials and recovery timing actually work together.

</details>

### Q018. What makes an incident follow-up useful?

<details>
<summary>Answer</summary>

A specific system improvement with ownership and a check that it reduces the observed failure mode.

</details>
