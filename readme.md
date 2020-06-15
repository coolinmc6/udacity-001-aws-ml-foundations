[Back to All Courses](https://github.com/coolinmc6/CS-concepts)

# AWS Machine Learning Foundations Course

Link: [AWS Machine Learning Foundations Course](https://www.udacity.com/course/aws-machine-learning-foundations--ud090)

## Lesson 2: Software Engineering Practices Part 1
- "using vectorized operations and more efficient data structures can optimize 
your code" - what are *vectorized operations*?

**Links**

- [How to version control your production machine learning models](https://algorithmia.com/blog/how-to-version-control-your-production-machine-learning-models)
- [https://github.com/ShuaiW/data-science-question-answer](https://github.com/ShuaiW/data-science-question-answer)
  - cool repo, some good stuff

## Lesson 3: Lesson 2: Software Engineering Practices Part 1

- TDD: Test Driven Development: write tests before the code
- unit tests: a test that covers a small unit of code

- install pytest:

```sh
pip install -U pytest
```

- You need your test files to start with the word "test" as in `test_nearest.py`
and each test function must start with "test" as in `def test_nearest_square_5():`
- You then just type `pytest` in the terminal to run the tests

### Questions to Ask Yourself When Conducting a Code Review

**Is the code clean and modular?**
- Can I understand the code easily?
- Does it use meaningful names and whitespace?
- Is there duplicated code?
- Can you provide another layer of abstraction?
- Is each function and module necessary?
- Is each function or module too long?

**Is the code efficient?**
- Are there loops or other steps we can vectorize?
- Can we use better data structures to optimize any steps?
- Can we shorten the number of calculations needed for any steps?
- Can we use generators or multiprocessing to optimize any steps?

**Is documentation effective?**
- Are in-line comments concise and meaningful?
- Is there complex code that's missing documentation?
- Do function use effective docstrings?
- Is the necessary project documentation provided?

**Is the code well tested?**
- Does the code high test coverage?
- Do tests check for interesting cases?
- Are the tests readable?
- Can the tests be made more efficient?

**Is the logging effective?**
- Are log messages clear, concise, and professional?
- Do they include all relevant and useful information?
- Do they use the appropriate logging level?

- Use a linter like [pylint](https://www.pylint.org/#install)

**Links**

- [https://www.linkedin.com/pulse/data-science-test-driven-development-sam-savage/](https://www.linkedin.com/pulse/data-science-test-driven-development-sam-savage/)
- [https://engineering.pivotal.io/post/test-driven-development-for-data-science/](https://engineering.pivotal.io/post/test-driven-development-for-data-science/)
- https://medium.com/uk-hydrographic-office/test-driven-development-is-essential-for-good-data-science-heres-why-db7975a03a44
- https://docs.python-guide.org/writing/tests/
- Code Reviews
  - https://github.com/lyst/MakingLyst/tree/master/code-reviews
  - https://www.kevinlondon.com/2015/05/05/code-review-best-practices.html

## Lesson 4: Introduction to Object-Oriented Programming

## Lesson 5: Machine Learning with AWS DeepComposer

## Lesson 6: Dive Deeper into Machine Learning

## 
