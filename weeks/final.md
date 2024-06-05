Final Exam  (3/6) - COGS 501/Spring 2024
----------------------------------------

**No supplementary material is allowed in this exam.**

1. **[20/100]** Are the events E, that a family with three children has children of both sexes, and F, that this family has at most one boy, independent? Assume that the eight ways a family can have three children are equally likely.

    -------------
    **Solution**

    If they were independent, then we would have $p(E\cap F) = p(E)p(F)$.
    $p(E) = 3/4$, $p(F) = 1/2$, $p(E\cap F) = 3/8$. Therefore, the events are indpendent.

    -------------


1. **[20/100]** A palindrome is a string of zero or more symbols that you cannot change by reversing. How many palindromes of length 5 or less can be made by using the symbols $a,b,c$? 

    -------------
    **Solution**

    $3\cdot3\cdot3\cdot 1\cdot 1 + 3\cdot3\cdot 1\cdot 1 + 3\cdot 3\cdot 1 + 3\cdot 1 + 3 + 1 = 52$

    -------------

1. **[20/100]** A computer genarates random bit strings of length 10. What is the expected weight? (The weight of a bit string is the number of 1s in it.)

    -------------
    **Solution**

    Here is the time to make use of the linearity of expected values. We define 10 random variables $X_1,\ldots ,X_{10}$, such that, given a bit string $\alpha=x_1\ldots x_{10}$,  $X_i(\alpha)$ is 1 if the bit $x_i$ is 1, and 0 otherwise. It is obvious that $X(\alpha) = X_i(\alpha)+\ldots+X_{10}$ for a given bit string $\alpha$. By the linearity of expected values, $E(X)=E(X_1)+\ldots+E(X_{10})$. Observe that, for any $X_i$, $E(X_i) = p(X_1=1)\cdot 1 = 0.5$. Therefore $E(X)= 10\cdot 0.5 = 5$.

    -------------
    

1. **[20/100]** How many 7 digit phone numbers are there in which the digits are non-increasing? That is, every digit is less than or equal to the previous one. Digits can be repeated.

    -------------
    **Solution**

    This is selection of 7 numbers out of 10 where repetitions are allowed. This
    can be thought as solving the equation $x_1 + \ldots + x_{10} = 7$ or some
    other equivalent form. In any case, the answer is
    $\binom{16}{7}=\binom{16}{9}$.

    -------------


1. **[20/100]** There is a set $A$ with $|A|=n$. A computer program randomly generates relations $R_i \subseteq  A\times A$. What is the probability that a relation generated as such is a function?

    -------------
    **Solution**
    What is the number of possible relations?

    Given that any subset of $A\times A$ is a relation and $|A\times A|=n^2$, the total
    number of relations is $2^{n^2}$.

    What is the number of possible functions?

    Each and every element of $A$ must be mapped to some element in $A$. For any
$x\in A$ there are $n$ possibilities for its image. Therefore, the total number
of functions from $A$ to $A$ is $n^n$.

    The answer to the question, therefore, is $\frac{n^n}{2^{n^2}}$


    -------------
