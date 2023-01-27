# Testing Pyramid

Hey there, welcome to Agile in a Nutshell I’m your host Jonathan Rasmusson. One framework that is very handy for teams when they first get into automated testing is the testing pyramid.

The testing pyramid is great because helps get teams on the same page around how they’d like tackle automated testing for their project.

It can help by

Giving them a common language
Sharing rules of thumb around where and when to use different types of tests
And just generally save teams a lot of time and effort by being clear about what kinds of tests they want to write, and when.
In this episode we are going to look at:

What the test pyramid is
The three kinds of tests that make it up
Along with some rules of thumb around when to use each kind of test
Let’s get started.

![](literature-notes/assets/test%20pyramid.png)

- [Article](http://www.agilenutshell.com/episodes/41-testing-pyramid)

The testing pyramid is a key concept in the software industry, describing the different levels at which tests can be written - end-to-end (E2E) testing, Integration testing (IT) and unit testing (UT) - and providing guidance on how much of each type of testing should be done. Here are two videos providing an introduction to this topic, covering the pros and cons of testing at east phase as well as the pitfalls of repeating the same testing at multiple levels. The youtube video on the right uses a web example while the XR Tech Talk linked below shows how the concepts are applied in the context of XR development.

Layers of the Testing Pyramid

The test pyramid breaks testing down into 3 types - end-to-end tests, integration tests and unit tests. This is really a spectrum with the boundaries between these typees being quite blurred. However in XR there is a relatively hard divide between tests that require a booted router or sim (including moonshine) and those that are isolated and run in the workspace with just a basic container.

Integration testing can be done in either environment so we've divided it into Broad and Narrow IT to indicate which one we mean.

Every type of testing has its pros and cons, and every level is important. But, as suggested by the shape of the pyramid, the goal is to create a large base of fast unit tests and do as much testing as possible at that stage, where the area under test is small and tests are quick to run and easy to debug.

The unit testing and integration testing phases are typically comprised of tests which run in seconds, meaning the relevant unit or integration tests could be run on each build, giving near-immediate feedback on the correctness of the changeset. UI and Manual tests typically require a full router or simulation environment, which takes far longer to build and boot.

Anyone starting new development today is recommended to develop two suites of tests:

a suite of unit and narrow integration tests using the cmocka framework that aims to test all the internal logic including mainline and error paths.
a suite of router-based tests using the CAFY framework to ensure that the feature works with its peers and dependencies. This may be further divided into a suite of end-to-end tests that can run on any image and a suite of broad integration tests that need a custom image with test code compiled in.
The next section looks at all the types of tests in more detail.
