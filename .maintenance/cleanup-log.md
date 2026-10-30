# Authorized cleanup

2026-10-30: Removed `02-mathematics-and-statistics/01-linear-algebra/dfd` at the user's request. This four-byte filler contained only `dfd` and a newline. Its original SHA-256 was `4643f988cee6b5dd070b511b0af519433792098f1032c98dbdf0dd082edb0c89`.

Moved the linear algebra handwritten PDF into its subject's `archive/` folder; its bytes and SHA-256 are unchanged. Updated the migration manifest to the new path. The other handwritten PDFs have not yet been moved or converted in this step.

## Document repository consolidation — 2026-10-30

Deleted only the four user-approved source repositories from GitHub: `Handwritten_Notes`, `Deployment_Notes`, `Economics`, and `Git_Tutorial`. Before deletion, verified unchanged source branch heads, the published Learning Hub commit, all 42 retained imported file hashes, and full-history Git backup bundles. The previously authorized four-byte `dfd` filler remains the sole excluded file from these sources.

GitHub returned HTTP 204 for each deletion. An authenticated repository listing confirmed that all four were absent, both `learning-hub` and `ineuron-bootcamp` remained, and every other repository in the pre-deletion inventory was retained. No iNeuron source repository was deleted in this operation. Original files in Learning Hub and their migration manifest remain unchanged.
