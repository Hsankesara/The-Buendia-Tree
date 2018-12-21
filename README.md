# The Buendia Tree
The Buendia Tree is the implementation of extended Kinship domain problem using **First Order Logic**. Kinship domain problem is a task to find out relationship or kinship between family members. In this repository, relationship between members of Buendia family has been described using First Order Logic. It is taken from the book *One Hundred Years of Solitude* and it has seven generations. It is not like a normal family and sometimes has pretty messed up relationships (You'd know if you read the book). The family tree looks like this

![Buendia Family Tree](/oyos_characters_tree_420.jpg)


## First Order Logic
In formal terms First Order Logic is defined as a set of logical rules which are explicitly defined to describe a problem. Every problem is operated under some set of rules which are intrinsic part of the problem. It is the way to exploit those rules and define objects and individuals, as well as their properties and the relationships between them. Sounds Confusing? Let's take an example in kinship domain.

In a family there are many relationships. These relationships are operated under set of rules. For Instance "Your **grandfather** is a **male** who is also **parent** of your **father**". In this case an individual is your grandather if it is **male** **parent** of your **father**. Now you can derive your grandfather if you know your father and his parents and can find the male one from them. hence you can write it : 
**grandfather(X, Y) => father(Z, Y) & parent(W, Z) & gender(W, "male")**
The above rule states that X is grandfather of Y if  Z is father of Y and W is parent of Z and gender of W is male.
This is how rules are described in **First Order Logic**.

### Syntax And Semantics
Logic in first order is made of following entities:

1. **Functions**
A function takes multiple arguments as input and returns a single object.
For Example : **mul(x,y)**
2. **Predicates**
A predicate takes a single argument and returns binary value.
For Example : **even(x)**
3. **Relations**
A relation takes multiple arguments and returns binary value.
For Example : **divides(x,y)**
4. **Quantifiers**
What makes first-order logic powerful is that it allows us to make general assertions using quantifiers. The universal quantifier ∀ followed by a variable x is meant to represent the phrase "for every x."
Dual to the universal quantifier is the existential quantifier, ∃, which is used to express assertions such as "some number is even," or, "between any two even numbers there is an odd number."
5. **Connectives**
Symbols which connect the clauses.
For Example : not (~), and (^), or (v), implies (=>), if and only if (<=>)

## Inference
Inferences are made when a person (or machine) goes beyond available evidence to form a conclusion. With a deductive inference, this conclusion always follows the stated premises. In other words, if the premises are true, then the conclusion is valid. First Order Logic in deductive inference involves conditional reasoning problems which follow the "if A, then B" format i.e. the process of deriving new relation using set of logical rules is known as inference.
The Inference can be derived by following processes:
### Unification
Unification in logic is a kind of logical substitution. For instance it is given that **Knows(John, Jane)** and we have to find **Knows(John,x)** i.e. person who knows John so We can unify both of them and say that Jane knows John. It is a basic building block of Inference model.
Formally Unnification procedure can be defined as:
*Unify(P,Q)* takes two atomic(i.e. single predicates) sentences P and Q and returns a substitution that makes P and Q identical.

### Forward Chaining
Forward chaining starts with the available data and uses inference rules to extract more data (from an end user, for example) until a goal is reached. An inference engine using forward chaining searches the inference rules until it finds one where the antecedent (If clause) is known to be true. When such a rule is found, the engine can conclude, or infer, the consequent (Then clause), resulting in the addition of new information to its data. To understand it better let us take a classical example:
Given that:*The law says that it is a crime for an American to sell weapons to hostile nations. The country Nono, an enemy of America, has some missiles, and all of its missiles were sold to it by Colonel West, who is American.*.

Step 1: West is an American(Given) |  Nono owns missiles(Given) | Nono is an enemy of America(Given)

Step 2: Missile is a Weapon (Given) | West sold missiles to Nono(Since Nono owns missiles) | Nono is  hostile(Since Nono is an enemy of America)

Step 3: West is a criminal(Since West is american who sold weapon to hostile country)


![Forward Chaining](/forward_chaining_example.png)

But this method would take exponential time in a well defined world. There are many advanced inference algorithms are available such as *Backward Chaining*, *Resolution Refutation Procedure* and  *lifted inference*. You can read  about them [here](http://pages.cs.wisc.edu/~dyer/cs540/notes/fopc.html)  

## Application of First Order Logic
First order logic is a deterministic model and that is why alone it has very few advantages. Since the uprising of AI, It became an intrinsic part of it. AI usually works on system and that system has to follow some rules therefore First Order  Logic became the most expressive as well as simplest way to represent those rules.
Alongside this, It is also a basic block of Markov Logic Networks which has a potential to revolutionalize artificial intelligence.
## The Buendia Domain
Let's come to Buendia tree again. Now as we know First order logic is dependent on two entities data and Logic.
### Data
In this domain, the only input data used is marriage between two individuals, the parent-child relationship and gender of the individuals. Everything else is derived using logical rules.
### Logic
You can checkout all the logical rules [here](/logic.py)
### Test
To run test file
```bash
python3 -m unittest test.py
```

## References
1. [First Order Logic](https://leanprover.github.io/logic_and_proof/first_order_logic.html)
2. [Inference](http://www.cs.cornell.edu/courses/cs4700/2011fa/lectures/16_FirstOrderLogic.pdf)
3.  [AI and First Order Logic](https://ipvs.informatik.uni-stuttgart.de/mlr/marc/teaching/15-ArtificialIntelligence/10-firstOrderLogic.pdf)
4. [First Order Logic with Examples](https://formal.iti.kit.edu/~beckert/teaching/Einfuehrung-KI-WS0304/08FirstOrderLogic.pdf)