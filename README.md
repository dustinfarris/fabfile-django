fabfile-django
==============

A collection of Fabric commands for working with a Django project and a remote server.

## Installation

Add the fabfile module to your project's root directory:

```console
wget https://github.com/dustinfarris/fabfile-django/archive/master.zip && unzip master.zip && mv fabfile-django-master fabfile && rm master.zip
```

## Configuration

Edit `fabfile/__init__.py` to reflect your Django project.  At a minimum you'll need to add your git repo URL and server
IP addresses.

## Usage

The built-in commands should work right out of the box after you have configured `__init__.py`

### Deploy

Deploy your project to a remote server.  You should specify 'production' or 'staging':

```console
fab production deploy
```

Optionally you can do a "quick" deploy that just git pulls your changes and runs migrations:

```console
fab staging deploy.quick
```

### Refresh

Pulls SQL and media backups down from the server.  Again, specify 'production' or 'staging':

```console
fab production refresh
```

### Restart

Restarts Apache, NGINX, and Memcached.  Specify 'production' or 'staging':

```console
fab production restart
```

### Stage

Merges your working branch into your staging branch.

```console
fab stage
```

### Sync

Merges your production branch into your working branch.

```console
fab sync
```

### Topic

Creates a new branch.

```console
fab topic
```

You can optionally provide the branch name inline with the command:

```console
fab topic:ISSUE-149
```

## Customization

You can add your own commands pretty easily.  The pattern is obvious and the [Fabric documentation][] is good.


[Fabric documentation]: http://docs.fabfile.org/en/1.8/

