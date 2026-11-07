---
title: "Testing Principles"
date: "2026-05-05"
type: "permanent"
category: "Computer Science/Coding Practices"
tags: ["testing", "quality", "maintainability"]
status: "complete"
related: ["[[Testing Pyramid]]", "[[Test Driven Dev]]"]
---

# Testing Principles

## Code writing Principles
1. ALWAYS write code that you can test.
2. Prioritize Readability over clever or concise code
3. ALWAYS prioritize writing "Clean Code" over completing the task FAST
   - Ask yourself
     - is it more readable
     - can you make it more readable and maintainable
4. ALWAYS Document the process
   - Readme
   - Meaningful Commit messages
5. Quality metrics are just side effect of a "Good Code-base"

### To Achieve
1. Code base which is
   - Readable
   - Easy to Change/Extend
   - Maintainable
   - Modular
   - Testable (UT/IT)
2. Operational state
   - Bug turn around time is less
   - Any change could be tested by Automated Test suites (including Unit and Module testing)
   - Team can spend more time in building New Features
   - Most of the Bugs are caught in Automation runs (pre-commit, nightly)
3. Achieve 100% "[[State Coverage]]"
   - As a side effect Line and Branch coverage will be up

## Dev Workflows
1. Automate workflows
   - Add Linters and Static code analyzers
   - Add Automated Code formatters
   - Automated testing UT, IT
   - Automate your deployments

### PR Guidelines

#### Accountability on Peer Reviews
1. With every PR, Add Automated UT for the changes done in the PR
2. If Automation is present, Attach Automation
   - Why the Automation Didn't catch this issue
   - [if needed] Fix the Automation
3. Improve the quality of the code by 1% by each commit (PR) by
   - Add UT/IT Automation
   - Make the code around the changes bit more Readable

### Testing Guidelines

Automated Unit Tests, Integration Tests, System Tests (End to End Tests) for all the features of Telemetry.

It is hard to cover all the corner cases in the IT and E2E Test, which is where UT shines. Can achieve ~100% Branch coverage. Mock can be leveraged here.
Why Unit testing and the testing pyramid → [Pyramid SmartDev article](https://wiki.cisco.com/display/SMARTDEV/Testing+Pyramid)
- [[Testing Pyramid]]
- [[Test Driven Dev]]

#### Behavior testing to improve [[State Coverage]]
1. Improve Unit test
2. Bring in the Behavior tests
   - On device
   - Off device
3. Prioritize Black box testing.
4. For every PR make sure there is some sort of Automated testing attached to the code that is being changed.
