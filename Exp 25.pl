% Graph
edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(e, g).
edge(f, g).

% Heuristic values
h(a, 6).
h(b, 4).
h(c, 5).
h(d, 3).
h(e, 2).
h(f, 4).
h(g, 0).

% Best First Search
best_first(Start, Goal, Path) :-
    search([node(Start, [Start])], Goal, Path).

search([node(Goal, Path)|_], Goal, Path).

search([node(Current, Path)|Rest], Goal, FinalPath) :-
    findall(
        node(Next, [Next|Path]),
        (edge(Current, Next), \+ member(Next, Path)),
        Children
    ),
    append(Rest, Children, NewList),
    sort_by_heuristic(NewList, SortedList),
    search(SortedList, Goal, FinalPath).

sort_by_heuristic(Nodes, Sorted) :-
    map_list_to_pairs(node_heuristic, Nodes, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, Sorted).

node_heuristic(node(Node, _), H) :-
    h(Node, H).