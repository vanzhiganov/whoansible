# coding: utf-8

import os
from flask import Flask, render_template, jsonify, request
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory

app = Flask(__name__)
app.config.from_pyfile(os.getenv('WHOANSIBLE_CONFIG', 'config_default.py'))


@app.route('/')
def index_html():
    return render_template('index.html')


@app.route('/inventory.html')
def inventory_html():
    loader = DataLoader()
    variable_manager = VariableManager()
    sa_inv = Inventory(loader=loader, variable_manager=variable_manager, host_list='%s/hosts' % app.config.get('ANSIBLE_PATH'))
    # print sa_inv.serialize()
    if request.args.get('group'):
        hosts = sa_inv.get_hosts(request.args.get('group'))
        group_vars = sa_inv.get_group_variables(groupname=request.args.get('group'))
    else:
        hosts = sa_inv.get_hosts()
        group_vars = None

    if request.args.get('host'):
        host_vars = sa_inv.get_host_vars(host=sa_inv.get_host(request.args.get('host')))
    else:
        host_vars = None

    return render_template(
        'inventory.html',
        group=request.args.get('group'),
        host=request.args.get('host'),
        groups=sa_inv.get_groups(), hosts=hosts,
        group_vars=group_vars, host_vars=host_vars
    )


@app.route('/roles.html')
def roles_html():
    return render_template('roles.html')
