Midterm Exam  (3/6) - COGS 501/Spring 2024
------------------------------------

**No supplementary material is allowed in this exam.**


1. **[30/100]** Here is a game (or experiment) played by a fair coin. The coin will be tossed 4 times in a row. For the first H you get 1 credit, all the Hs after this first H earns you 2 credits.

   a. What is the size of the sample space (= the set of possible outcomes) of this experiment?
   b. What is the expected credit you would get from this experiment?

   -----------
   **Solution**

   The size of your sample space is $2^4=16$.

   Let $X$ be the random variable that computes the credit you earn given the
   sequence of tosses.

   $p(X=1) = \binom{4}{1}/2^4 = 4/16$  
   $p(X=3) = \binom{4}{2}/2^4 = 6/16$   
   $p(X=5) = \binom{4}{3}/2^4 = 4/16$  
   $p(X=7) = \binom{4}{4}/2^4 = 1/16$  

    $E(X)= 1\cdot \frac{4}{16} + 3\cdot\frac{6}{16} + 5\cdot\frac{4}{16} + 7\cdot\frac{1}{16} = \frac{49}{16} = 3.0625$

   -----------

1. **[30/100]** How many functions $f: \{1,2,3,4,5\}\mapsto \{a,b,c,d,e\}$ are onto (surjective)? A function is onto if no element in its range goes unassigned (that is, its range and its codomain are identical).

    --------------
    **Solution**

    See the solution to Example 1.6.9(b) of Levin.

    --------------

1. **[30/100]** Suppose that we have found that the word "Rolex" occurs in 250 of 2000 messages known to be spam and in 5 of 1000 messages known not to be spam. Estimate the probability that an incoming message containing the word "Rolex" is spam, assuming that it is equally likely that an incoming message is spam or not spam. If our threshold for rejecting a message as spam is 0.9, will we reject such messages? 

    --------------
    **Solution**

    See the solution to Example 3 on page 499, Rosen 8th edition.

    --------------

1. **[10/100]** You are given a biased coin with a probability $p\neq 0.5$ of heads. Describe a process which makes use of this biased coin and simulates a fair coin toss.
    
    -----------
    **Solution**
    
    Observe that $p(HT)=p(TH)$ even for a biased coin. You define a function
    $X$ which applies to sequences of two tosses, and which maps $HT$ to $T$, $TH$ to $H$, and in all other inputs it asks for a new toss.

    -----------
