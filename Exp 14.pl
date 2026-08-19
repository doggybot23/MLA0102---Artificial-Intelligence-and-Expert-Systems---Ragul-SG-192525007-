diet(underweight, "High calorie diet").
diet(normal, "Balanced diet").
diet(overweight, "Low calorie diet").
diet(diabetes, "Low sugar diet").
diet(heart, "Low fat diet").

recommend(BMI, diabetes, "Low sugar diet") :-
    BMI = overweight.

recommend(BMI, heart, "Low fat diet") :-
    BMI = overweight.

recommend(BMI, normal, Diet) :-
    diet(BMI, Diet).

recommend(BMI, none, Diet) :-
    diet(BMI, Diet).