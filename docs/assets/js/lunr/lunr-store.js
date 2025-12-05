var store = [{
        "title": "`collatz`",
        "excerpt":"View / copy raw utils.py 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 from funcutils import proc_seq def collatz(n): \"\"\"The...","categories": [],
        "tags": [],
        "url": "/cogs501/code/python/modules/collatz/",
        "teaser": null
      },{
        "title": "`funcutils`",
        "excerpt":"View / copy raw utils.py 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 def proc_seq(n, seq, alive, update, init): \"\"\"Process a sequence of items. n: seed seq: function that produces the next item in the sequence alive: function...","categories": [],
        "tags": [],
        "url": "/cogs501/code/python/modules/funcutils/",
        "teaser": null
      },{
        "title": "A sequence processor",
        "excerpt":"def proc_seq(n, sequencer, alive, update, init): \"\"\"Process a sequence of items. sequencer: function that produces the next item in the sequence alive: function that tests whether to continue processing update: function that updates the state init: initial state &gt;&gt;&gt; def sequencer(n): return n - 1 &gt;&gt;&gt; def alive(n): return n...","categories": [],
        "tags": [],
        "url": "/cogs501/code/python/snippets/proc_seq/",
        "teaser": null
      },{
        "title": "Higher-order functions",
        "excerpt":"Define a function apply_twice that takes a function f and a value x, and returns the result of applying f to x two times. def sqr(x): return x * x def apply_twice(f, x): \"\"\"apply f to x twice. &gt;&gt;&gt; apply_twice(sqr, 3) 81 \"\"\" Define a function applier that applies a...","categories": [],
        "tags": ["func-prog","python"],
        "url": "/cogs501/exercises/higher-order-functions/",
        "teaser": null
      },{
        "title": "Iteration",
        "excerpt":"The factorial function is defined over the non-negative integers as:1 \\[n! = \\begin{cases} 1, &amp; \\text{if } n = 0;\\\\ n \\times (n - 1)!, &amp; \\text{if } n &gt; 0. \\end{cases}\\] Define a function that computes the factorial of a given non-negative integer \\(n\\) using iteration by while. def...","categories": [],
        "tags": ["python","iteration","while","programming"],
        "url": "/cogs501/exercises/iteration/",
        "teaser": null
      },{
        "title": "Basic number theory",
        "excerpt":"Prove the following: Theorem (Some properties of divisibility) Let \\(a,b,c \\in \\mathbb{Z}\\) and \\(a \\neq 0\\). Then: i. if \\(a \\mid b\\) and \\(a \\mid c\\), then \\(a \\mid (b+c)\\); ii. if \\(a \\mid b\\), then \\(a \\mid kb\\) for any integer \\(k\\); iii. if \\(a \\mid b\\) and \\(b...","categories": [],
        "tags": ["math","discrete","proof","number thoery"],
        "url": "/cogs501/exercises/numbers/",
        "teaser": null
      },{
        "title": "Iteration by `while`",
        "excerpt":"Let’s start with a simple function defined over integers called the Collatz function \\(C\\). \\[C(n) = \\begin{cases} \\frac{n}{2} &amp; \\text{if } n \\text{ is even}\\\\ 3n + 1 &amp; \\text{if } n \\text{ is odd} \\end{cases}\\] Collatz’ conjecture states that for any positive integer \\(n\\), repeated application of \\(C\\) will...","categories": ["course"],
        "tags": ["programming","iteration","while loop","cogs501"],
        "url": "/cogs501/posts/course/iteration-by-while/",
        "teaser": null
      },{
        "title": "Higher order functions",
        "excerpt":"Remember our earlier discussion of Collatz function and sequences. Here is our task: Task: Given a positive integer \\(n\\), find the largest integer in the Collatz sequence seeded by \\(n\\).1 By now, the task should be a piece of cake for you. Is it? Try and see before proceeding. Here...","categories": ["course"],
        "tags": ["programming","functional programming","cogs501"],
        "url": "/cogs501/posts/course/higher-order-functions/",
        "teaser": null
      },{
        "title": "Euclid's Algorithm",
        "excerpt":"Check: Make sure you are fine with very basic number theory. Definition (greatest common divisor) Given two integers \\(a\\) and \\(b\\), the greatest common divisor (GCD) of \\(a\\) and \\(b\\), denoted by \\(\\gcd(a,b)\\), is the largest integer that divides both \\(a\\) and \\(b\\). Euclid’s algorithm (300 BC) which computes the...","categories": ["course"],
        "tags": ["algorithms","iteration","proof","discrete","cogs501","number theory"],
        "url": "/cogs501/posts/course/euclids-algorithm/",
        "teaser": null
      },{
        "title": "Very basic number theory",
        "excerpt":"This is a healthy minimum dose of number theory to make you feel comfortable with the concepts we will be using in this course. We do not start from the absolute beginning. We take for granted integers and arithmetic operations. We start by some terminology. The set of integers, denoted...","categories": ["course"],
        "tags": ["cogs501","discrete","proof","number theory"],
        "url": "/cogs501/posts/course/intro-number-theory/",
        "teaser": null
      },{
    "title": "Page Not Found",
    "excerpt":"Sorry, but the page you were trying to view does not exist.  ","url": "http://localhost:4000/cogs501/404.html"
  },{
    "title": "About",
    "excerpt":"Tempor velit sint sunt ipsum tempor enim ad qui ullamco. Est dolore anim ad velit duis dolore minim sunt aliquip amet commodo labore. Ut eu pariatur aute ea aute excepteur laborum. Esse ea esse excepteur minim mollit qui cillum excepteur ex dolore magna. Labore deserunt fugiat incididunt incididunt sint ea....","url": "http://localhost:4000/cogs501/sbout/"
  },{
    "title": "Posts by Category",
    "excerpt":" ","url": "http://localhost:4000/cogs501/categories/"
  },{
    "title": "Code browser",
    "excerpt":"        Language:            Any       Python       Racket       Haskell                        Kind:            Any       Module       Snippet                                                      collatz                                      python        · module            Various goodies related to Collatz conjecture.                                                   funcutils                                      python        · module            A utility module for functional abstractions.                                                   A sequence processor                                      python        · snippet            A generic function to process sequences based on user-defined behavior.                  ","url": "http://localhost:4000/cogs501/code/browser/"
  },{
    "title": "Code",
    "excerpt":" ","url": "http://localhost:4000/cogs501/code/"
  },{
    "title": "Exercises",
    "excerpt":"    python    iteration    func-prog    while    math    discrete    proof                                                 Higher-order functions                                A set of programming exercises to practice higher-order functions.                                                     Iteration                                A set of programming exercises to practice iteration using while loops.                                                     Basic number theory                                Mainly proof questions based on basic number theory.               ","url": "http://localhost:4000/cogs501/exercise/browser/"
  },{
    "title": "Exercises",
    "excerpt":" ","url": "http://localhost:4000/cogs501/exercises/"
  },{
    "title": "Modules",
    "excerpt":"                         `collatz`                                   Various goodies related to Collatz conjecture.                                              `funcutils`                                   A utility module for functional abstractions.                            ","url": "http://localhost:4000/cogs501/code/python/modules/"
  },{
    "title": "Snippets",
    "excerpt":"                         A sequence processor                                   A generic function to process sequences based on user-defined behavior.                           ","url": "http://localhost:4000/cogs501/code/python/snippets/"
  },{
    "title": "COGS 501 Quiz",
    "excerpt":"[2pts*] Translate the following into first order logic: i. Every student in this class has submitted at least one assignment. - S(x): “x is a student in this class” - A(x, y): “x has submitted assignment y” \\[\\forall x (S(x) \\to \\exists y A(x,y))\\] ii. There is a professor who...","url": "http://localhost:4000/cogs501/q06s/"
  },{
    "title": "COGS 501 Quiz",
    "excerpt":"Define a function that takes a positive integer and returns the sum of its digits. Two mathematical operations that might be useful here are modulo and division. You get 2pts bonus credit if you solve the problem using proc_seq. Save the definition of proc_seq from here in a file named...","url": "http://localhost:4000/cogs501/q09s/"
  },{
    "title": "COGS 501 Quiz",
    "excerpt":"[1pt] Prove that the product of an even integer with an odd integer is even. Let \\(m\\) be an even integer and \\(n\\) be an odd integer. By definition of even numbers, there exists an integer \\(k\\) such that \\(m = 2k\\). By definition of odd numbers, there exists an...","url": "http://localhost:4000/cogs501/q10s/"
  },{
    "title": "Schedule",
    "excerpt":"Week Reading Exercises Posts Quiz :calendar:2/10         :calendar:9/10         :calendar:23/10         :calendar:30/10         :calendar:6/11       quiz :calendar:13/11 CP 1.5, Epp 3, sections on Prolog can be omitted. 1-5 of Iteration Iteration by while no need for...","url": "http://localhost:4000/cogs501/schedule/"
  },{
    "title": "Snippets",
    "excerpt":"                         A sequence processor                                   A generic function to process sequences based on user-defined behavior.                           ","url": "http://localhost:4000/cogs501/code/snippets/"
  },{
    "title": "Syllabus",
    "excerpt":"Prerequisites The course is open, without any prerequisites, to any graduate student, with Cogsci first, Informatics second, and the rest third priority. Material Composing Programs Epp, Susanna S. (2018). Discrete Mathematics with Applications. 5th ed., Cengage Learning. Everything that is discussed in the class. Requirements Weekly quizzes Midterm exam Final...","url": "http://localhost:4000/cogs501/syllabus/"
  },{
    "title": "Posts by Tag",
    "excerpt":" ","url": "http://localhost:4000/cogs501/tags/"
  },{
    "title": "Posts by Year",
    "excerpt":" ","url": "http://localhost:4000/cogs501/posts/"
  }]
