# whoansible

Ansible Manager


## TODO

- [x] See host and groups
- [ ] Manage host and groups
- [ ] Inventory
- [ ] Create role
- [ ] Deploy role to groups, hosts


## Install & run

Off course, in first time you need to clone WhoAnsible from repo.

```
git clone ssh://git@git.org.ru/whoansible.git
```

```
cd ./whoansible
```

Create virtual environment in `.env` (don't worry, this directory in `.gitignore`)

```
virtualenv .env
```

```
source .env/bin/activate
```

After that you need to install requirements that specified in `requirements.txt` (yours captain obvious)

```
pip install -r requirements.txt
```

*Create default ansible dir structure*

```
mkdir -p ansible/{facts,group_vars,host_vars}
```

```
touch ansible/hosts
```

*Run babe, run*

Let's see this Indian movie :)

```
python run_server.py
```
