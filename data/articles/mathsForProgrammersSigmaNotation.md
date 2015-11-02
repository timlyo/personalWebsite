{
    "title": "Maths For Programmers - Sigma Notation",
    "outline": "Sigma Notation for Programmers",
    "date": "2015/10/26",
    "tags": ["maths"]
}
---

# Sigma Notation

> $\Sigma$ based on a nominalization of a verb σίζω (sízō, from earlier *sig-jō, meaning 'I hiss')

Sometimes Wikipedia just sums it up best, Sigma notation does make me want to hiss and boo. Yet I can't escape it. Everywhere I encounter some sort of summation, it's there. Starting at me amidst far more sensible glyphs. Urging me to google the syntax just that one more time. Fervently hoping that maybe, just maybe, I'll remember it. At least if the link is on on my own site I wont have to google for it right?


Sigma, or sum notation, is used for summations. In other words, it's a way for mathematicians to confuse mortals when they want to add some things together. For example $ \sum\limits_{i=1}^4 i $ has a much simpler form in C++:

```cpp
int sum = 0;
for(int i = 1; i <= 4; i++){
    sum += i;
}
```

Or a more complicated one $ \sum\limits_{i=1}^4 i^2 $

```cpp
int sum = 0;
for(int i = 1; i <= 4; i++){
    sum += std::pow(i, 2);
}
```

And another $ \sum\limits_{i=1}^4 i(i^2 + 2) $

```cpp
int sum = 0;
for(int i = 1; i <= 4; i++){
    sum += i * (std::pow(i, 2) + 2);
}
```

Which could also be shown as

```cpp
int calculate(int i, const int max){
    int result = i * (std::pow(i, 2) + 2);
    if(i == max)
        return result;
    else
        return result + calculate(i+1, max);
}
```

Ok, maybe sigma notation does have it's benefits, a standardised format, less verbose. Starting to sound like python to me.
