# Python and Programming — questions and worked answers

[Subject home](../README.md) · [Theory map](../01-theory/README.md) · [Practicals](../02-practicals/README.md)

Try each answer first, then expand the explanation. Questions follow the lesson order. Programming and SQL practice sets include additional runnable solutions in Practicals.

- [01 — Run Python, read syntax and write clear names](#lesson-01)
- [02 — Numbers, strings, booleans and operators](#lesson-02)
- [03 — Lists, tuples, sets, dictionaries and mutation](#lesson-03)
- [04 — Decisions, loops, comprehensions and pattern matching](#lesson-04)
- [05 — Functions, arguments, scope and docstrings](#lesson-05)
- [06 — Iterables, iterators, generators and lazy pipelines](#lesson-06)
- [07 — Files, paths, CSV, JSON, dates and regular expressions](#lesson-07)
- [08 — Exceptions, context managers, logging and debugging](#lesson-08)
- [09 — Classes, dataclasses, composition and protocols](#lesson-09)
- [10 — Modules, packages, environments, typing and tests](#lesson-10)
- [11 — Closures, decorators, context managers and concurrency](#lesson-11)
- [12 — NumPy, pandas, vectorization and data cleaning](#lesson-12)

<a id="lesson-01"></a>

## 01 — Run Python, read syntax and write clear names

[Read the lesson](../01-theory/lesson-01-first-program.md)

### Q001. Does assigning a different type change the old object?

<details>
<summary>Answer</summary>

No. A name is rebound; the old object is unchanged unless separately mutated.

</details>

### Q002. Print or return?

<details>
<summary>Answer</summary>

Print produces display output; return gives the caller a value for further computation.

</details>

### Q003. Why use an environment per project?

<details>
<summary>Answer</summary>

Dependency versions can differ across projects without one upgrade silently changing them all.

</details>

<a id="lesson-02"></a>

## 02 — Numbers, strings, booleans and operators

[Read the lesson](../01-theory/lesson-02-values-and-operators.md)

### Q004. Why is bool("False") True?

<details>
<summary>Answer</summary>

It is a nonempty string; its characters are not interpreted as a boolean literal.

</details>

### Q005. What does a slice stop mean?

<details>
<summary>Answer</summary>

The stop index is excluded, so positions 1,2,3 appear in a[1:4].

</details>

### Q006. When is `is` appropriate?

<details>
<summary>Answer</summary>

For identity, especially singleton sentinels such as None; ordinary values usually need ==.

</details>

<a id="lesson-03"></a>

## 03 — Lists, tuples, sets, dictionaries and mutation

[Read the lesson](../01-theory/lesson-03-collections-and-mutation.md)

### Q007. Does a shallow copy isolate nested lists?

<details>
<summary>Answer</summary>

No. The outer list is new but nested objects remain shared.

</details>

### Q008. Why can a set not contain a list?

<details>
<summary>Answer</summary>

List is mutable and unhashable; set elements must be hashable.

</details>

### Q009. Dictionary or list for lookup by unique customer ID?

<details>
<summary>Answer</summary>

Usually a dictionary, after validating that duplicate IDs are handled deliberately.

</details>

<a id="lesson-04"></a>

## 04 — Decisions, loops, comprehensions and pattern matching

[Read the lesson](../01-theory/lesson-04-decisions-and-loops.md)

### Q010. When does a for-loop else run?

<details>
<summary>Answer</summary>

When the iterator is exhausted without a break, including an initially empty iterator.

</details>

### Q011. What happens when zip inputs have different lengths?

<details>
<summary>Answer</summary>

Ordinary zip stops at the shortest; explicitly validate or use an appropriate strict option on supported Python versions.

</details>

### Q012. What is an off-by-one error?

<details>
<summary>Answer</summary>

A boundary is included/excluded incorrectly, often from confusing a range or slice stop with an included endpoint.

</details>

<a id="lesson-05"></a>

## 05 — Functions, arguments, scope and docstrings

[Read the lesson](../01-theory/lesson-05-functions-and-scope.md)

### Q013. Why use None instead of [] as a default?

<details>
<summary>Answer</summary>

A default list is created once and reused; a None sentinel allows a fresh list per call.

</details>

### Q014. Do type hints validate runtime inputs?

<details>
<summary>Answer</summary>

Not ordinarily. Add explicit validation where required.

</details>

### Q015. Why separate printing from calculation?

<details>
<summary>Answer</summary>

Returned values can be reused, tested and displayed in different contexts without capturing output.

</details>

<a id="lesson-06"></a>

## 06 — Iterables, iterators, generators and lazy pipelines

[Read the lesson](../01-theory/lesson-06-iteration-and-generators.md)

### Q016. Why is the second list(stream) empty?

<details>
<summary>Answer</summary>

The same generator has already been exhausted; it is not automatically restarted.

</details>

### Q017. Does lazy evaluation remove the need for memory in sorting?

<details>
<summary>Answer</summary>

No. Global operations such as a full sort still need to retain or externally organize data.

</details>

### Q018. Iterable versus iterator?

<details>
<summary>Answer</summary>

An iterable produces an iterator; an iterator is the stateful object that advances through values.

</details>

<a id="lesson-07"></a>

## 07 — Files, paths, CSV, JSON, dates and regular expressions

[Read the lesson](../01-theory/lesson-07-files-and-formats.md)

### Q019. Why not split CSV on commas?

<details>
<summary>Answer</summary>

Quoted fields may contain commas and newlines; a CSV parser understands those rules.

</details>

### Q020. Does valid JSON imply valid business data?

<details>
<summary>Answer</summary>

No. Required fields, ranges, relationships and types still need validation.

</details>

### Q021. Why timezone-aware timestamps?

<details>
<summary>Answer</summary>

They can represent instants unambiguously, whereas a local clock reading alone may be ambiguous.

</details>

<a id="lesson-08"></a>

## 08 — Exceptions, context managers, logging and debugging

[Read the lesson](../01-theory/lesson-08-errors-and-logging.md)

### Q022. Why catch a narrow exception?

<details>
<summary>Answer</summary>

It avoids hiding unrelated bugs and makes the intended recovery explicit.

</details>

### Q023. What does `raise ... from exc` preserve?

<details>
<summary>Answer</summary>

The causal relationship to the underlying exception, improving diagnosis.

</details>

### Q024. Are assertions sufficient for production input validation?

<details>
<summary>Answer</summary>

No. They may be disabled and are intended for internal invariants, not required user validation.

</details>

<a id="lesson-09"></a>

## 09 — Classes, dataclasses, composition and protocols

[Read the lesson](../01-theory/lesson-09-classes-and-dataclasses.md)

### Q025. Why default_factory for a list field?

<details>
<summary>Answer</summary>

Each instance receives its own new list instead of sharing mutable state.

</details>

### Q026. Does frozen make nested lists immutable?

<details>
<summary>Answer</summary>

No. Preventing field rebinding does not recursively freeze contained objects.

</details>

### Q027. When prefer composition?

<details>
<summary>Answer</summary>

When one component uses another capability without being a true substitutable subtype of it.

</details>

<a id="lesson-10"></a>

## 10 — Modules, packages, environments, typing and tests

[Read the lesson](../01-theory/lesson-10-modules-packaging-and-quality.md)

### Q028. Why guard a script entry point?

<details>
<summary>Answer</summary>

Importing the module can then expose functions without running the script workflow.

</details>

### Q029. Unit versus integration test?

<details>
<summary>Answer</summary>

A unit test focuses on a small contract; an integration test checks interacting components.

</details>

### Q030. Why profile first?

<details>
<summary>Answer</summary>

It identifies real bottlenecks so optimization effort targets the dominant cost.

</details>

<a id="lesson-11"></a>

## 11 — Closures, decorators, context managers and concurrency

[Read the lesson](../01-theory/lesson-11-advanced-functions.md)

### Q031. What does a closure retain?

<details>
<summary>Answer</summary>

Access to enclosing bindings; it does not necessarily freeze each value at function creation.

</details>

### Q032. Does async mean parallel CPU computation?

<details>
<summary>Answer</summary>

No. It mainly enables cooperative concurrency around awaited operations.

</details>

### Q033. Why functools.wraps?

<details>
<summary>Answer</summary>

It preserves metadata such as the wrapped function name and documentation for inspection and tooling.

</details>

<a id="lesson-12"></a>

## 12 — NumPy, pandas, vectorization and data cleaning

[Read the lesson](../01-theory/lesson-12-arrays-and-dataframes.md)

### Q034. Matrix multiplication versus elementwise multiplication?

<details>
<summary>Answer</summary>

@ combines inner dimensions as a linear algebra product; * multiplies corresponding broadcast-compatible elements.

</details>

### Q035. Why can a merge inflate totals?

<details>
<summary>Answer</summary>

Duplicate keys can create multiple matches, repeating records at a finer grain.

</details>

### Q036. Why inspect shape after each major step?

<details>
<summary>Answer</summary>

It catches lost/duplicated rows, unexpected broadcasting and unintended dimensional changes early.

</details>
