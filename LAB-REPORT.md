# Lab Report: DevOps for Cloud Computing (CSC418)
**Student Name:** Fatima Khalid  
**Registration Number:** FA23-BSE-049  
**Course:** DevOps for Cloud Computing  
**Assignment:** Student Task Manager Development and Version Control Using Git and GitHub  

---

## 1. Executive Summary
This lab assignment focused on implementing a Python-based command-line Student Task Manager while applying professional DevOps practices, including Git version control, branching strategies, collaborative workflows through Issues and Pull Requests, merge conflict resolution, automated testing via GitHub Actions, and structured documentation and release management.

## 2. Key Accomplishments & Implementation Details
- **Repository Setup & Version Control:** Initialized a public GitHub repository with a proper `.gitignore`, `LICENSE`, and `README.md`. Tracked development using descriptive commits and pushed changes successfully.
- **Branching & Feature Development:** Created separate feature branches (`feature/add-task`, `feature/complete-task`, `feature/delete-task`) to isolate code changes, maintaining a clean and functional `main` branch.
- **Collaboration & PRs:** Managed development workflows using GitHub Issues, linked Pull Requests, code reviews, and proper merge strategies.
- **Merge Conflict Resolution:** Successfully simulated, identified, and resolved merge conflicts in `README.md` resulting from concurrent branch modifications.
- **Automated Testing & CI:** Integrated an automated test suite using Python's `unittest` framework and configured a GitHub Actions CI workflow (`.github/workflows/tests.yml`) to run tests automatically on pushes and pull requests.
- **Documentation & Releases:** Provided comprehensive user documentation, updated the project README, and published the official `v1.0.0` stable release.

## 3. Challenges Faced and Solutions
- **Merge Conflicts:** Encountered conflicts when merging branches modifying the same line in `README.md`. Resolved by inspecting the conflict markers in VS Code, selecting the appropriate changes, and completing the commit process.
- **CI/CD Pipeline Errors:** Initially faced an `IndentationError` and a test loading failure during automated CI runs. Fixed code formatting locally, verified tests using `python -m unittest discover -s tests -v`, and successfully re-triggered the GitHub Actions pipeline.

## 4. Conclusion
This lab provided hands-on experience with core DevOps tools and workflows. By combining version control, automated testing, and CI/CD pipelines, I successfully built and delivered a robust, production-ready Student Task Manager application.