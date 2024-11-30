# SQL Chestsheet
## Functions
- `CHAR(int1, int2, int3, int4, ...)`: Used to create a string from ASCII values
```sql
$ CHAR(65, 67.3, 69.3)
ADE
```


- `CONCAT(string1, string2, ...)`: Joins two columns/strings
```sql
$ SELECT CONCAT(ename, grade) FROM employees;
RaviE4
AkashA1
NeelaB2
...
```


- `POWER(number, exponent)`/`POW(number, exponent)`: Power a number to another number
```sql
$ SELECT POWER(5, 3);
125
```


- `SQRT(number)`: Find square root of values
```sql
$ SELECT SQRT(POWER(500, 2));
500
```


- `ABS()`: Give the absolute value, i.e. modulus
```sql
$ SELECT ABS(34.9293);
34.9293

$ SELECT ABS(-34.9293);
34.9293

$ SELECT ABS("-34.9293");
34.9293
```


- `MOD()`: Used to select the remainder when a number is divided by another number, i.e. divisor
```sql
$ SELECT MOD(200,19);
10

$ SELECT 200 MOD 19;
10

$ SELECT 200 % 19;
10

$ SELECT MOD(34.5, 100);
34.5
```


- `SIGN()`: Returns the sign of the argment. i.e. if the number is positive, it will return 1, and if it is negative, it will return -1
```sql
$ SELECT SIGN(93420);
1

$ SELECT SIGN(-83289);
-1
```


- `ROUND()`: Returns the rounded value of the given integer
```sql
$ SELECT ROUND(1029.2931, 1)
$ SELECT ROUND(1029.2931, 1)
$ SELECT ROUND(1029.2931, 1)
```