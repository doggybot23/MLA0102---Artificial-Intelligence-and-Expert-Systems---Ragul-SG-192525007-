% Fruit facts
color(apple, red).
color(banana, yellow).
color(orange, orange).
color(grape, purple).
color(watermelon, green).

% Production rules
fruit_type(Fruit, 'Red Fruit') :-
    color(Fruit, red).

fruit_type(Fruit, 'Yellow Fruit') :-
    color(Fruit, yellow).

fruit_type(Fruit, 'Orange Fruit') :-
    color(Fruit, orange).

fruit_type(Fruit, 'Purple Fruit') :-
    color(Fruit, purple).

fruit_type(Fruit, 'Green Fruit') :-
    color(Fruit, green).