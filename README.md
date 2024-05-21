## Installation

1) Clone this repository
  ```bash
  git clone https://github.com/PavelKrivorotov/task_16_05_2024.git
  ```

## Usage

1) Build and run containers in work directory:
 ```bash
 docker compose up
 ```

2) Open app container terminal
```bash
docker compose app exec sh
```

3) Call app with optional parameters (in container terminal)
```bash
/app # python manage.py COMMAND [OPTIONAL ARGS]
```

4) Open database container terminal (for details information about database changes)
```bash
docker compose exec psql -U postgres
```
```bash
postgres=# \c task_16_05_2024
```

## Example

1) `Command 1`: Initialize table `users` with columns `id`, `fio` (Surname, Name, Patronymic), `dob` (Date of birthday), `sex` (Male or Female)
```bash
/app # python manage.py 1
```

2) `Command 2`: Add new object in `users` table
```bash
/app # python manage.py 2 'Ivanov Ivan Ivanovich' 2000-01-01 Male
```

3) `Command 3`: Select all objects in table `users` where columns `fio` and `dob` is unique
```bash
/app # python manage.py 3
```

```bash
Out:
1, Ivanov Ivan Ivanovich, 2000-01-01, Male, 24
```

4) `Command 4`: Add `1,000,000` new objects in `users` table
```bash
/app # python manage.py 4
```

5) `Command 4`: Add `100` new objects with `fio` startswith `F` and `sex` = `Male` in `users` table
```bash
/app # python manage.py 4 --only-100-males-with-fio-startswith-f
```

6) `Command 5`: Select all users where `fio` startswith `F` and `sex` = `Male`
```bash
/app # python manage.py 5
```

```bash
Out:
Time query:  401.2895753631592  ms
```

7) `Command 6`: Select all users where `fio` startswith `F` and `sex` = `Male`. Change table users (add new column `fio_first_word`) and query
```bash
/app # python manage.py 6
```

```bash
Out:
Time query:  385.9735753631592  ms
```

8) `Command 7`: Clear database
```bash
/app # python manage.py 7
```

## Detailed analysis

`Command 5 (Query-1)`
```sql
SELECT * FROM users WHERE fio LIKE 'F%' AND sex = 'Male';
```

`Command 6 (Query-2)`
```sql
SELECT * FROM users WHERE fio_first_word = 'F' AND sex = 'Male';
```

<table>
  <thead>
    <tr>
      <th rowspan="2">Query</th>
      <th colspan="2">Mashine</th>
      <th colspan="2">Docker</th>
    </tr>
    <tr>
      <th>app time (ORM)</th>
      <th>explain analyse</th>
      <th>app time (ORM)</th>
      <th>explain analyse</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Query-1</td>
      <td>670 ms</td>
      <td>186 ms</td>
      <td>597 ms</td>
      <td>159 ms</td>
    </tr>
    <tr>
      <td>Query-2</td>
      <td>578 ms</td>
      <td>56 ms</td>
      <td>527 ms</td>
      <td>56 ms</td>
    </tr>
  </tbody>
</table>

The results are nothing more than the average time of `10` requests for each test. It is also worth saying that tests for `Mashine`
and `Docker` were carried out on various random samples containing `1,000,000` rows

1) Why the time difference between `App time (ORM)` and `Explain analyse` different by 10 times?
   
   **Answer: Since the `Query-1` finds about `40,000` records that satisfy the condition, it turns out that all of these records
   need to be sent over the network between the `Database` and `ORM`. This is where this difference comes from (overhead for data
   transfer between services)**
