# Testing Principles

## Principles

1. ALWAYS write code that you can test.
2. Prioritize Readability over clever or concise code
3. ALWAYS prioritize writing "Clean Code" over completing the task FAST
    1. Ask yourself
        1. is it more readable
        2. can you make it more readable and maintainable
4. ALWAYS Document the process
    1. Readme
    2. Meaning full Commit messages
5. Quality metrics are just side effect of a "Good Code-base"

To Achieve:

1. Code base which is
   1. Readable
   2. Easy to Change/Extend
   3. Maintainable
   4. Modular
   5. Testable (UT/IT)
2. Operational state
   1. Bug turn around time is less
   2. Any change could be tested by Automated Test suites (including Unit and Module testing)
   3. Team can spend more time in building New Features
   4. Most of the Bugs are caught in Automation runs (pre-commit, nightly)
3. Achieve 100% "State Coverage"
   1. As a side effect Line and Branch coverage will be up

- [TBD]

## Dev Workflows

1. Automate workflows
    1. Add Linters and Static code analyzers
    2. Add Automated Code formatters
    3. Automated testing UT, IT
    4. Automate your deployments

### PR Guidelines

#### Accountability on Peer Reviews

1. With every PR, Add Automated UT for the changes done in the PR
2. If Automation is present,
   1. Attach Automation
   2. Why the Automation Didn't catch this issues
   3. [if needed] Fix the Automation
3. Improve the quality of the code by 1% by each commit (PR) by
   1. Add UT/IT Automation
   2. Make it code around the changes bit more Readable

### Testing Guidelines

- Automated Unit Tests, Integration Tests, System Tests(End to End Tests) for all the features of Telemetry
- It is hard to to cover all the corner cases in the IT and E2E Test, which is where UT shines. Can achieve ~100% Branch coverage. Mock can be leveraged here.
- Why Unit testing and the testing pyramid are covered in this Testing [Pyramid SmartDev article](https://wiki.cisco.com/display/SMARTDEV/Testing+Pyramid)
  - [[Testing Pyramid]]

#### Behavior testing to improve [[State Coverage]]

1. Improve Unit test
2. Bring in the Behavior tests
   1. On device
   2. Off device
3. Prioritize Black box testing.
4. For every PR make sure there is some sort of Automated testing attached to the code that is being changed.
