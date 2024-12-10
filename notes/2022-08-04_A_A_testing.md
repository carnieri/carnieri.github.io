## A/A testing

2022-08-04

After reading "Online controlled experiments and A/B testing" by Ron Kohavi and Roger Longbotham:

Besides A/B testing, you should also run "A/A" tests, where A and B user populations receive identical experiences. This is useful for debugging, checking that instrumentation is working, checking that normality assumption holds, etc.

A common example is refactoring. When I refactor a code base, I usually strive to maintain the system's behavior, so I can test if behavior before refactoring equals behavior after refactoring.

I realized I've been doing something similar to A/A testing when checking and debugging ML systems.

