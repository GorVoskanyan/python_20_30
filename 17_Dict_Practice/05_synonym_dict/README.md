# Հոմանիշների Բառարանի Ծրագիր

## Նկարագրություն

Այս ծրագիրը նախատեսված է հոմանիշների բառարան ստեղծելու և օգտվողի մուտքագրած բառի հոմանիշը գտնելու համար։ Օգտատերը մուտքագրում է N զույգ բառեր, որտեղ յուրաքանչյուր բառ հոմանիշ է իր զույգին։ Այնուհետև, օգտատերը կարող է մուտքագրել բառ, և ծրագիրը ցույց կտա այդ բառի հոմանիշը։

## Օգտագործման քայլեր

1. Օգտատերը մուտքագրում է զույգերի քանակը (`N`)։
2. Հետո օգտատերը մուտքագրում է `N` զույգ բառեր, որտեղ յուրաքանչյուր զույգը բաժանվում է `—` նշանով։
3. Այնուհետև օգտատերը կարող է մուտքագրել ցանկացած բառ՝ իմանալու դրա հոմանիշը։ Ծրագիրը ցույց կտա հոմանիշը կամ ծանուցում կտա, եթե այդպիսի բառ չկա բառարանում։

## Օգտագործման օրինակ

Օգտատերը մուտքագրում է զույգերի քանակը և յուրաքանչյուր զույգի բառերը՝

```
Մուտքագրեք զույգերի քանակը: 3
1-րդ զույգը: Բարև — Ողջույն
2-րդ զույգը: Տխուր — Դժգոհ
3-րդ զույգը: Ուրախ — Զվարթ
```

Հետո օգտատերը մուտքագրում է բառ՝ ստանալու դրա հոմանիշը՝

```
Մուտքագրեք բառ: ողջույն
Հոմանիշը: Բարև
```

Եթե մուտքագրված բառը չկա բառարանում՝

```
Մուտքագրեք բառ: հետաքրքիր
Այդպիսի բառ բառարանում չկա։
```

## Պահանջներ

1. Ծրագիրը պետք է ճիշտ կերպով ստեղծի հոմանիշների բառարանը՝ օգտատիրոջ մուտքագրած զույգերից։
2. Ծրագիրը պետք է հստակ ներկայացնի հոմանիշը կամ ծանուցում տա, եթե այդպիսի բառ չկա բառարանում։
3. Ծրագիրը պետք է ապահովի մեծատառ/փոքրատառ անտեսումը՝ անկախ այն բանից, թե ինչպես է մուտքագրվել բառը։