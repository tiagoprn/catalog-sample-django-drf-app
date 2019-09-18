# SETUP:

To setup a container ready to be run by the app, you must run this command:

```
$ make setupdb
```

It will create the database according to the parameter on the `postgres.env` file.
After finished, it will automatically start the container for it to be ready to be used
by the `catalog` Django Project.


# SOME OTHER NOTES:

- The container is called `postgres-catalog`. Edit it to your wish.

- `postgres.env` contains the credentials to create the database.

- `utils/` contains scripts to dump and restore the database, with some
  environment variables hardcoded there also.

- According to
  https://stackoverflow.com/questions/19674456/run-postgresql-queries-from-the-command-line,
if you set the enviroment variable PGPASSWORD you do not need to inform your
password.

