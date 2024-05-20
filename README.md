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
