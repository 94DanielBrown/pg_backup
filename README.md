pgbackup
========

CLI for backing up remote PostgreSQL databases locally or to AWS S3.

REQUIREMENTS
========

Python3 and required libraries as installed from 'requirements.txt'

aws cli for backing up to s3

USAGE
========
Pass in a full database URL(or ip), the storage driver, and destination.

S3 Example w/ bucket name:

    $ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups

Local Example w/ local path:

    $ pgbackup postgres://bob@example.com:5432/db_one --driver local /var/local/db_one/backups

