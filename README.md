[![Build Status](https://travis-ci.org/open-io/ansible-role-openio-grafana.svg?branch=master)](https://travis-ci.org/open-io/ansible-role-openio-grafana)
ansible-role-grafana
=========

This role will deploy Grafana and provision a dashboard onto it

Requirements
------------

None

Role Variables
--------------

| Variable name          | Description                                     | Type    |
| ---------------------- | ----------------------------------------------- | ------- |
| grafana_version        | Version of grafana to use                       | String  |
| grafana_paths          | Configuration paths used by grafana-server      | Object  |
| grafana_http           | Host/Port on which grafana listens              | Object  |
| grafana_auth           | Grafana credentials                             | Object  |
| grafana_thene          | Theme (dark or light) used by grafana           | String  |
| grafana_oiofs_enabled  | Provision dashboard for filesystem connector    | Boolean |
| grafana_bind_interface | Grafana Network interface to run checks against | String  |
| grafana_bind_address   | Grafana Network address to run checks against   | Boolean |
| prometheus_host        | Host on which prometheus source is configured   | String  |
| prometheus_port        | Port on which prometheus source is configured   | Integer |


Tools - Dashboard retriever
-----

### Description:

This role is outfitted with a tool that updates provisioned dashboards. In order to update a dashboard you need to:

### Requirements:

- python3
- python-requests

### How to use

- Head to grafana dashboards, and modify them using the Web Interface (Make it editable first in the gear menu)
- Once done, run the tool: `python3 tools/retriever.py HOST:PORT USER PASSWORD ./files [STRICT]` where:
    - HOST:PORT is the IP/PORT of your Grafana
    - USER: is the Grafana user
    - PASSWORD: is the Grafana password
    - STRICT will fail on warnings
- If you have added a new dashboard, make sure you add it to vars/main.yml (grafana_dashboards)
- Your provisioned dashboards are now updated and are ready to be committed

Dependencies
------------

None

Example Playbook
----------------

See docker-tests branch

License
-------

GNU AFFERO GENERAL PUBLIC LICENSE, Version 3

Author Information
------------------

- [Cedric DELGEHIER](https://github.com/cdelgehier) (maintainer)
- [Romain ACCIARI](https://github.com/racciari) (maintainer)
- [Vladimir DOMBROVSKI](https://github.com/vdombrovski) (maintainer)
