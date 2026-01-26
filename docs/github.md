# Git and GitHub Guide

Essential commands and workflows for version control with Git and hosting on GitHub.

## Getting Started
```bash
# Initialize a local repository
git init

# Add files to staging
git add .
git add path/to/file

# Commit changes
git commit -m "Your commit message"

# Set branch name to main
git branch -M main

# Add remote origin
git remote add origin https://github.com/username/repository.git

# Push to GitHub
git push -u origin main
```

## Branching & Merging
```bash
# Create and switch to a new branch
git checkout -b feature-name

# Switch to an existing branch
git checkout main

# Merge a branch into current branch
git merge feature-name

# Delete a branch
git branch -d feature-name
```

## Synchronizing
```bash
# Pull latest changes from remote
git pull origin main

# Fetch changes without merging
git fetch origin

# Stash temporary changes
git stash
git stash pop
```

## Useful Tips
- Use `.gitignore` to exclude sensitive or unnecessary files.
- Write clear, concise commit messages.
- Use Pull Requests (PRs) for code reviews on GitHub.