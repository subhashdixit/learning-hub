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


## Remaining-subject expansion — 2026-10-30

- Added 78 ordered lessons across eleven subjects, approximately 25,000 words, 234 answered lesson questions, 40 executable Python problems and 20 worked SQLite queries. The existing 40-lesson ML course remains unchanged.
- Added 26 static plots, 89 Mermaid diagrams and 3 animations across those subjects; retained previous detailed visual guides and source materials.
- All eleven standard-library guided labs, 40 Python solutions, 20 SQLite query cases, 12 inline Python lesson examples and 5 inline SQL examples executed successfully.
- All 1,036 original imported files matched the migration manifest SHA-256 hashes. Original handwritten PDFs remain in archive. No source repository was deleted.
- Checked 504 authored Markdown pages for local links with no missing targets. Parsed 97 new/authored-page math expressions with KaTeX and 89 diagrams with Mermaid without syntax errors. Inspected the new figures as a contact sheet and refined the Python object-reference diagram.
- Historical imported notebooks were retained; this check does not claim to have re-executed every notebook or a full cloud/Spark/LLM deployment. New AI/deployment labs clearly identify their local simulations.
- Detailed outputs: `.maintenance/expansion-validation.json` and `.maintenance/expansion-render-validation.json`.


## Algorithm progression update — 2026-10-30

- Added 25 worked algorithm chapters (13 forecasting, 12 deep learning), twelve subject progression stories, 37 new flowcharts and 7 static scientific figures. Foundation lessons and imported material were retained.
- Every worked chapter covers the motivating limitation, mechanism/training, numerical example, trade-offs, related alternatives and validation. Main ML story links its existing worked algorithm lessons; other subject maps distinguish survey families from full worked chapters.
- Fitted seasonal naive, ARIMA, SARIMA, SARIMAX, Holt–Winters and Prophet on one identical synthetic temporal holdout. The exercise records actual metrics, fixed model settings, package versions and starting-parameter warnings; it does not claim a universal winner or trained implementations for every surveyed neural method.
- Arithmetic checks passed for the worked forecasting/deep-learning calculations. Parsed 59 math expressions and 50 diagrams in touched pages without errors. These totals include existing diagrams on updated route/index pages; 37 flowcharts are new.
- Checked 546 authored Markdown pages for local links with no missing targets. All 1,036 imported originals still matched manifest hashes. Inspected all seven new figures and corrected a misleading floating-point axis scale in the seasonal-difference illustration.
- Detailed results: `.maintenance/algorithm-validation.json`, `.maintenance/algorithm-render-validation.json`, and the forecasting practical’s `model-comparison/example-results.json`.
