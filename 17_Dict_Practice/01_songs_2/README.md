# Songs Duration Calculator

## Նկարագրություն
Այս ծրագիրը նախատեսված է օգտատիրոջ ընտրած երգերի ընդհանուր տևողությունը հաշվելու համար։ Օգտագործողի կողմից տրվում են երգերի անվանումները, և ծրագիրը հաշվարկում է դրանց ընդհանուր տևողությունը։

## Օգտագործված տվյալներ
Ծրագրում օգտագործվում է երգերի բառարան `violator_songs`, որը պարունակում է հետևյալ երգերի անվանումները և դրանց տևողությունը րոպեներով․

```python
violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
```

## Օգտագործման օրինակ
Օգտատերը մուտքագրում է, թե քանի երգ է ցանկանում ընտրել, ապա հաջորդաբար մուտքագրում է այդ երգերի անունները։ Ծրագիրը հաշվում է և արտածում ընդհանուր տևողությունը։

Օրինակ՝

```
Քանի երգ ընտրել? 3
1-րդ երգի անունը: Halo
2-րդ երգի անունը: Enjoy the Silence
3-րդ երգի անունը: Clean

Երգերի ընդհանուր տևողությունը: 14.93 րոպե
```

## Պահանջներ
1. Ծրագիրը պետք է ճիշտ կերպով հաշվի երգերի ընդհանուր տևողությունը։
2. Ծրագիրը պետք է առաջարկի օգտատիրոջը մուտքագրել երգերի անվանումները և ցույց տա սխալ, եթե երգը ցուցակում չէ։
3. Տեքստերը պետք է լինեն հայերեն՝ օգտագործողի համար առավել հարմարավետ դարձնելու համար։
