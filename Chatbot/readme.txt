## Question 1
Imputed the facts as single description elements e.g. cheese(feta). This allowed me to
simplify the nature of using the fact based as well as categorizing them without having to
have a highly variable fact fields. This would lead to duplication of fields if I wanted to add
more attributes to the fact base for certain items.


## Question 2
I decided to ask for certain features is a given order based mostly on when they are necessary to ask as I determined.
For example, for custom pizzas, I ask for size then crust then sauce then cheese then veggie toppings then if they want
a veggie pizza then for meat toppings if they don't decline. If I were to use backward chaining the main difference
would be the formatting as the dependencies would still be the same. I would still be building cheese pizza by
building a pizza with sauce.

## Question 3

Relations direct the flow of the python as it executes. This was done as it is easy to track the order in the python
code than the fact base. In essence the python adds facts to the fact to let the rules base know where it is and the
rules bases in turn calls python function with certain arguments to move the process along. Once the rules base calls
the python code and no new facts are added that progress the chain, then python code stack completes and returns
to the runchatbot for final processing and printing.


## Question 4

The only thing that I have to do is simply add CoolTopping to the fact base (fact.kfb) with the appropriate tag e.g.
meat_toppings(CoolTopping). If the topping tag does not exist then there would need to be an additional python method
to handle when this topping could be added.

## Question 5

Adding a food takes considerably more effort. One would need first add the food to the fact base (fact.kfb)
e.g. food(soup).
Then you would need to create a chain of rules in the rules base to handle the sequential questioning (relation.krb)
e.g. ask_for_soup.
Then you would need to modify the kb2text.py file, specifically the activate_pizzabot method in order to handle the
new answer and asserting the new facts into the fact base to trigger the new rules.
Then simply add the soup(your_opinion_here) to the fact base.

NOTES:
This program does not use pizzabot.py. It simply runs the runchatbot.py and kb2text.py takes it from there,
relying more on the ask_tty module in pyke to handle user interaction. The kb2text use the fact and rules bases
to guide the execution of code and the kb2text is primarily there to ask for and handle user responses.
Unfortunately, in this case, even though it was working initially working with switching between soup and pizza,
for whatever reason it is now no longer recognizing the new fact inserted and simply exiting the chat.