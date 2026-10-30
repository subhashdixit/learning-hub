# Authorized cleanup

2026-10-30: Removed `02-mathematics-and-statistics/01-linear-algebra/dfd` at the user's request. This four-byte filler contained only `dfd` and a newline. Its original SHA-256 was `4643f988cee6b5dd070b511b0af519433792098f1032c98dbdf0dd082edb0c89`.

Moved the linear algebra handwritten PDF into its subject's `archive/` folder; its bytes and SHA-256 are unchanged. Updated the migration manifest to the new path. The other handwritten PDFs have not yet been moved or converted in this step.

## Document repository consolidation — 2026-10-30

Deleted only the four user-approved source repositories from GitHub: `Handwritten_Notes`, `Deployment_Notes`, `Economics`, and `Git_Tutorial`. Before deletion, verified unchanged source branch heads, the published Learning Hub commit, all 42 retained imported file hashes, and full-history Git backup bundles. The previously authorized four-byte `dfd` filler remains the sole excluded file from these sources.

GitHub returned HTTP 204 for each deletion. An authenticated repository listing confirmed that all four were absent, both `learning-hub` and `ineuron-bootcamp` remained, and every other repository in the pre-deletion inventory was retained. No iNeuron source repository was deleted in this operation. Original files in Learning Hub and their migration manifest remain unchanged.

## Learning/exercise repository consolidation — 2026-10-30

Following explicit user approval, deleted these 15 source repositories: `-FSDS-Bootcamp-at-iNeuron-Python-Programming-Assignments`, `Data_Science_Cheat_Sheet`, `DS_Interview_Preparation`, `FSDS-Bootcamp-at-iNeuron-Challenges`, `FSDS-Bootcamp-at-iNeuron-Python-Basic-Assignments`, `iNeuron_Assignment_PPT_Program`, `Machine_Learning`, `NLP_Bootcamp`, `pandas_data_for_practice`, `PySpark_Tutorial`, `Python_Programs_Notes`, `SQL_Training_Namaste_SQL`, `Statistics`, `Time_Series_Concepts_and_Practicals`, `VSCode_To_Github_FSDS`.

Before any deletion, verified all 347 original imported files against the Learning Hub manifest, unchanged source branch heads and full-history Git backup bundles. GitHub returned HTTP 204 for every deletion. An authenticated owner listing confirmed that all 15 were absent and all other previously listed repositories remained, including `learning-hub` and `ineuron-bootcamp`. Imported content and the migration manifest are unchanged.

## Remaining course/practice repository consolidation — 2026-10-30

Following explicit user approval, deleted these 17 source repositories: `claude-certification-architect-exam-prep`, `Ineuron_FSDS_Assignments`, `FSDS-Bootcamp-at-iNeuron-Tasks`, `Docker_Tutorial`, `Streamlit_Tutorial`, `Deep_Learning`, `NLP_Projects_and_Learning_Materials`, `Unsupervised_ML`, `Bagging`, `Boosting`, `Decision_Trees`, `Support_Vector_Machines`, `Regression_Model_Tasks`, `Linear_Regression`, `EDA`, `Logistics_Regression`, `Web_Scraping`.

All 548 imported files were already present in their subject folders in Learning Hub. Verified their manifest hashes against the published repository, unchanged source commits, and full-history backup bundles before deletion. GitHub returned HTTP 204 for each deletion; the authenticated owner listing confirmed all 17 were absent and every other previously listed repository remained. `learning-hub`, `ineuron-bootcamp`, `subhashdixit`, and `Resume` are retained. The imported learning files and migration manifest are unchanged.
