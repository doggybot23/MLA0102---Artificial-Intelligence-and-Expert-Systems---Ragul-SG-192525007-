symptom(ravi, fever).
symptom(ravi, cough).
symptom(ravi, body_pain).

disease(Person, flu) :-
    symptom(Person, fever),
    symptom(Person, cough),
    symptom(Person, body_pain).

disease(Person, cold) :-
    symptom(Person, cough),
    symptom(Person, sneezing).

disease(Person, malaria) :-
    symptom(Person, fever),
    symptom(Person, chills).

diagnose(Person) :-
    disease(Person, Disease),
    write('Possible Disease: '),
    write(Disease).