# HARSH

Private auto-commit repository. A GitHub Actions workflow runs multiple times
daily at randomised intervals, generating commits with varied file types,
directory structures, and commit messages — no two days look the same.

## How it works

| Layer            | Randomisation                                        |
| ---------------- | ---------------------------------------------------- |
| **Schedule**     | 3 cron triggers spread across the day (UTC)          |
| **Delay**        | Each run sleeps 0 – 50 min before committing         |
| **File count**   | 1 – 3 files per commit                               |
| **File type**    | `.md`, `.txt`, `.json`, `.yaml`, `.py`, `.sh`, etc.  |
| **Directory**    | Random nesting up to 2 levels deep                   |
| **Content**      | Contextual content matching the file extension        |
| **Commit msg**   | Randomly selected conventional-commit message         |

## Manual trigger

You can also trigger a commit manually from the **Actions** tab → **Daily Auto Commit** → **Run workflow**.
