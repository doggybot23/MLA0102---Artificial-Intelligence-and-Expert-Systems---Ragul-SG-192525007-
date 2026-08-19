vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).

check_vowels([]).

check_vowels([H|T]) :-
    vowel(H),
    write(H),
    write(' is a vowel'), nl,
    check_vowels(T).

check_vowels([H|T]) :-
    \+ vowel(H),
    check_vowels(T).