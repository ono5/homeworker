# ● Outline

The homeowrk application helps us to solve the various home work chores.

such as ...

* Check household account book
* Create Todo List

# ● Dev Environment
* Mac on PC
* Docker version 18.09.1
* docker-compose version 1.23.2
* Python3
* Django
* Postgres
* redis

# ● Set up  My App on your environment

```bash
1. make test
2. make release
```

# ● About Email Setting
I set email settings for my app to send email when user have been forgotten password.

To send email, you need the below settins.

1. Create user_info.py under the setting folder.
2. Set email to your account

In addition, you need gmail account because this app is specified with gmail server to send email.

# ● Let's Browsing Test!
You can test for browsing test with selenium (ZALENIUM) easily.

First, you open browser at 'http://localhost:4444/grid/admin/live'.  
Second, you type the below command.

```bash
make test
exit  
make release
```

Finally, you type the below command.

```bash
make ft
```