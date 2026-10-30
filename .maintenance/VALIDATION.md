# Visual Learning Hub validation

- All 1,036 imported source-file records resolve and match their original SHA-256 hashes.
- All 204 original PDFs are retained; identified handwritten PDFs are in subject archives, including duplicate ANOVA material.
- 28 handwritten note files plus four typed NLP note files are mapped to concept-based guides in `note-coverage.csv`.
- 22 theory chapters (including the reviewed linear-algebra guide) and 12 worked-question guides form the main learning sequence.
- 34 repeated Python notebooks, compared using ordered Markdown/code cell text, are preserved outside the main reading path.
- Authored Markdown local-file links, fences, math delimiters and control characters were checked.
- Twenty self-contained Python blocks and thirteen SQL queries execute successfully. Representative hand calculations were independently recomputed.
- Twenty added static figures were visually inspected. Existing algebra figures/animation were retained.
- Representative chapters were accepted by GitHub's Markdown renderer.

Historical notebook applications, cloud deployment, Spark sessions, external services and model-training experiments were not all rerun. Their original files are retained as study practicals; new standalone examples have their own checked results. The guides are reorganized teaching explanations, not literal line-by-line PDF transcriptions.


## Machine Learning course expansion — 2026-10-30

- Added 40 ordered teaching lessons (about 19,000 words), 200 answered questions, 32 new static plots and one animated k-means illustration; retained the existing useful figures.
- Added ten self-contained executable labs with pinned dependencies and recorded outputs in `04-machine-learning/02-practicals/labs/VALIDATION.md`.
- Moved the complete course-assignment tree to Machine Learning practicals. Updated 33 imported-file destinations in the migration manifest; every one of the 1,036 original files still matches its recorded SHA-256.
- Checked local links across authored hub Markdown, course math/fence syntax, worked arithmetic and every new lab. Original PDFs remain intact in archive. Historical imported notebooks were preserved, not all re-executed.

- Parsed all 335 course math expressions with KaTeX and all 46 Mermaid diagrams with Mermaid; no syntax errors. Checked the PCA chapter through GitHub's Markdown renderer. Inspected a contact sheet of the plotted figures.
