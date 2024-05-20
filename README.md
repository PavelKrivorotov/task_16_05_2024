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
