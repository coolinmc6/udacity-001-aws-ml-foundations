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

[Code for the lesson](https://github.com/udacity/DSND_Term2/tree/master/lessons/ObjectOrientedProgramming)

- Objects have characteristics and can perform actions
- An object is a specific instance of something whereas a class is the generic
version of the object, or blueprint of it
- Here are some terms worth knowing:
  - class - a blueprint consisting of methods and attributes
  - object - an instance of a class. It can help to think of objects as something 
  in the real world like a yellow pencil, a small dog, a blue shirt, etc. However, 
  as you'll see later in the lesson, objects can be more abstract.
  - attribute - a descriptor or characteristic. Examples would be color, length, 
  size, etc. These attributes can take on specific values like blue, 3 inches, 
  large, etc.
  - method - an action that a class or object could take
  - OOP - a commonly used abbreviation for object-oriented programming
  - encapsulation - one of the fundamental ideas behind object-oriented programming 
  is called encapsulation: you can combine functions and data all into a single 
  entity. In object-oriented programming, this single entity is called a class. 
  Encapsulation allows you to hide implementation details much like how the 
  scikit-learn package hides the implementation of machine learning algorithms.
- **method** vs **function**:
  - a *method* is a function inside a class while a *function* is outside of a
  class
- when writing class methods, notice how you don't have to pass *self* in as an
argument; it is passed implicitly
- If you saved your Shirt class in a file called `shirt.py`, you would import
it by doing the following:

```py
from shirt import Shirt
```
- this assumes that your class is named "Shirt" (with a capital "S")
- There are a number of drawbacks of accessing object properties directly vs.
using getter and setter methods. Python is looser than other OO languages

### Gaussian Package

- Gaussian (normal distribution) calculator: http://onlinestatbook.com/2/calculators/normal_dist.html
- Binomial Distribution calculator: http://onlinestatbook.com/2/calculators/binomial_dist.html

- The exercise on magic methods was interesting. Notice in the `magic_methods.py`
file there is an `__add__` method. I'm overwriting Python's normal add method
so that when I do the following I don't get an error:

```py
gaussian_one = Gaussian(25, 3)
gaussian_two = Gaussian(30, 4)
gaussian_sum = gaussian_one + gaussian_two # __add__ magic method
```

**Inheritance**

- Inheritance is pretty self-explanatory in Python. Here is an example of the
Shirt class that inherits from Clothing:

```py
class Clothing:

    def __init__(self, color, size, style, price):
        self.color = color
        self.size = size
        self.style = style
        self.price = price
        
    def change_price(self, price):
        self.price = price
        
    def calculate_discount(self, discount):
        return self.price * (1 - discount)
    
    def calculate_shipping(self, weight, rate):
        return weight * rate
        
class Shirt(Clothing):
    
    def __init__(self, color, size, style, price, long_or_short):
        
        Clothing.__init__(self, color, size, style, price)
        self.long_or_short = long_or_short
    
    def double_price(self):
        self.price = 2*self.price
```
- `Clothing` is pretty normal, nothing exciting there
- `Shirt` first has `(Clothing)` on the class defintion line
- Notice the `__init__` method; it's a normal `__init__` method except you first
call the Clothing class and then set any properties for your Shirt class

**Advanced OOP Topics**

Here are some Python-focused OOP articles and concepts:
- [class methods, instance methods, and static methods](https://realpython.com/instance-class-and-static-methods-demystified/):
these are different types of methods that can be accessed at the class or object level
- [class attributes vs instance attributes](https://www.python-course.eu/python3_class_and_instance_attributes.php):
you can also define attributes at the class level or at the instance level
- [multiple inheritance, mixins](https://easyaspython.com/mixins-for-fun-and-profit-cb9962760556): 
A class can inherit from multiple parent classes
- [Python decorators](https://realpython.com/primer-on-python-decorators/): 
Decorators are a short-hand way for using functions inside other functions

**Making a package**

- I won't go through everything here are the basics. You can see what's really 
happening in the folder in this repo: *3a_python_package*


- my_python_package (**package_root**)
  - `setup.py` (sets up package)
  - distributions (**code for my package**)
    - `__init__`: the init code for my package
    - `Generaldistribution.py`: the parent class for my Gaussian distribution class
    - `Gaussiandistribution.py`: Gaussian distribution class
- To use it, I could go to that folder and do

```sh
pip install .
```
- this will install it. And then do `python` in the Terminal to bring up the
interpreter:

```py
from distributions import Gaussian
gaussian_one = Gaussian(25, 2)
gaussian_one.mean
gaussian_one + gaussian_one
```
- good overview of how to contribute to a GitHub project: 
[https://github.com/MarcDiethelm/contributing/blob/master/README.md](https://github.com/MarcDiethelm/contributing/blob/master/README.md) or
[https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/)

**Uploading Package to PyPi**

```sh
cd binomial_package_files
python setup.py sdist
pip install twine

# commands to upload to the pypi test repository
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
pip install --index-url https://test.pypi.org/simple/ dsnd-probability

# command to upload to the pypi repository
twine upload dist/*
pip install dsnd-probability
```
- tutorial on creating packages: [https://packaging.python.org/tutorials/packaging-projects/](https://packaging.python.org/tutorials/packaging-projects/)

## Lesson 5: Machine Learning with AWS DeepComposer

### ML Techniques and Generative AI

- Types of ML Techniques
  - Supervised Learning
    - every training example has a corresponding label
  - Unsupervised Learning
    - No labels for training data
    - Most Generative AI is unsupervised learning
  - Reinforcement Learning
    - learns through consequences of action in specific environment
- Generative AI is one of the most promising new technologies
- Generative AI pits two different neural networks against each other to produce
new and original digital works based on sample inputs

**their notes:**
Machine Learning Techniques

**Supervised Learning:** Models are presented wit input data and the desired results. The model will then attempt to learn rules that map the input data to the desired results.

**Unsupervised Learning:** Models are presented with datasets that have no labels or predefined patterns, and the model will attempt to infer the underlying structures from the dataset. Generative AI is a type of unsupervised learning.

**Reinforcement learning:** The model or agent will interact with a dynamic world to achieve a certain goal. The dynamic world will reward or punish the agent based on its actions. Overtime, the agent will learn to navigate the dynamic world and accomplish its goal(s) based on the rewards and punishments that it has received.

### AWS DeepComposer

- AWS DeepComposer is how Amazon is teaching developers how to use GAN (Generative
Adversarial Networks) to generate music
- GANs pit 2 networks, a generator and a discriminator, against each other to generate new content.
  - generator: creates new output
  - discriminator: evaluates the quality of output AND provides feedback


## Lesson 6: Dive Deeper into Machine Learning

## 
