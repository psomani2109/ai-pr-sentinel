# 🤖 AI-Powered GitHub PR Sentinel

An automated CI/CD code review bot that intercepts GitHub Pull Requests in real time, inspects unified git diffs, and provides structured technical feedback using the Gemini API.

## 🚀 Features
- **Event-Driven CI/CD**: Automatically triggered via GitHub Actions on pull request events (`opened`, `synchronize`).
- **Diff Extraction**: Fetches unified code diffs using the GitHub REST API.
- **Automated Code Analysis**:
  - Critical Bugs & Edge Cases (null pointers, infinite loops, resource leaks)
  - Asymptotic Complexity & Efficiency ($O(N)$ bottlenecks)
  - Best Practices & Code Standards
- **Automated Feedback Loop**: Posts structured markdown reviews and merge verdicts (`APPROVE`, `COMMENT`, `REQUEST CHANGES`) directly into the PR discussion.

## 🛠️ Tech Stack
- **Language**: Python 3.11
- **APIs**: GitHub REST API, Google Gemini API
- **Automation / CI/CD**: GitHub Actions
