# Password manager app with crud functionality using AES encryption


## List of commands you can use 

### CREATE
```
    python main.py create -n <name> -c <description> -key <key> -exp <expiration_time>

    eg.

    python main.py create -n portal -c my student portal key -key 1234 -exp 300
```
### UPDATE
```
    python main.py update <name> -key <key>

    eg.

    python main.py update portal -key 54321
```

### DELETE
```
    python main.py delete <name>

    eg.

    python main.py delete portal
```
### READ
```
    python main.py read <name>

    eg.

    python main.py read portal
```
### LIST
```
    python main.py list

    eg.

    python main.py list
```

### REM
```
    python main.py rem <name>

    eg.

    python main.py rem portal
```
