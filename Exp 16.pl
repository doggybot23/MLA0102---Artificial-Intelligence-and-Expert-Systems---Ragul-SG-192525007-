% Facts
bird(eagle).
bird(sparrow).
bird(penguin).

% Rule: Penguin cannot fly
fly(penguin) :-
    !,
    fail.

% Rule: Other birds can fly
fly(X) :-
    bird(X).