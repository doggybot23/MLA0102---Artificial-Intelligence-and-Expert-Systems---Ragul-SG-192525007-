% Available Time Slots
slot(t1).
slot(t2).
slot(t3).

% Subjects
subject(math).
subject(physics).
subject(chemistry).
subject(english).

% Conflicting Subjects
conflict(math, physics).
conflict(physics, math).

conflict(math, chemistry).
conflict(chemistry, math).

conflict(physics, english).
conflict(english, physics).

% Assign time slots
schedule(M, P, C, E) :-
    slot(M),
    slot(P),
    slot(C),
    slot(E),

    M \= P,
    M \= C,
    P \= E.

% Display timetable
timetable :-
    schedule(M, P, C, E),
    write('Math      : '), write(M), nl,
    write('Physics   : '), write(P), nl,
    write('Chemistry : '), write(C), nl,
    write('English   : '), write(E), nl.