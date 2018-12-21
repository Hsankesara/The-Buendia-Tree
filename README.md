# The Buendia Tree
** What is Buendia Tree**
The Buendia Tree is the implementation of extended Kinship domain problem using **First Order Logic**. Kinship domain is a set of logical rules which represents family relationships or kinships. The Buendia family has seven generations. It is inspired from the book *One Hundred Years of Solitude*.  It is not like a normal family and sometimes has pretty messed up relationships (You'd know if you read the book). The family tree looks like this
![Buendia Family Tree]('./oyos_characters_tree_420.jpg')
Now you might be wondering what is **First Order Logic**

## First Order Logic
In formal terms First Order Logic is defined as a set of logical rules which are explicitly defined to describe a problem. Every problem is operated under some set of rules which are intrinsic part of the problem. It is the way to exploit those rules and define objects and individuals, as well as their properties and the relationships between them. Sounds Confusing? Let's take an example in kinship domain.

In a big family there are many relationships. These relationships are operated under set of rules. For Instance "Your **grandfather** is a **male** who is also **parent** of your **father**". In this case an individual is your grandather if it is **male** **parent** of your **father**. Now you can derive your grandfather if you know your father and his parents and can find the male one from them. hence you can write it : 
**grandfather(X, Y) => father(Z, Y) & parent(W, Z) & gender(W, "male")**
The above rule states that X is grandfather of Y if  Z is father of Y and W is parent of Z and gender of W is male.
This is how rules are described in **First Order Logic**.

### Syntax And Semantics
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

## Inference
** Explain **
### Unification
** Explain Unification **
### Forward Chaining
** Explain and Forward Chaining **
## Application of First Order Logic

## The Buendia Domain
** Explain what you did here ** 
### Data
** Write About input data **
### Logic
** Tell the logic **

## Final Note

