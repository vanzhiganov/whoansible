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
    sa_inv = Inventory(loader=loader, variable_manager=variable_manager, host_list='%s/hosts' % app.config['ansible_path'])
    # print sa_inv.serialize()
    if request.args.get('group'):
        hosts = sa_inv.get_hosts(request.args.get('group'))
    else:
        hosts = sa_inv.get_hosts()

    return render_template('inventory.html', groups=sa_inv.get_groups(), hosts=hosts)
