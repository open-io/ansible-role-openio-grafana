ansible-role-grafana
=========

This role will deploy Grafana and provision a dashboard onto it

Requirements
------------

None

Role Variables
--------------

| Variable name   | Description                                   | Type    |
| --------------- | --------------------------------------------- | ------- |
| grafana_version | Version of grafana to use                     | String  |
| grafana_paths   | Configuration paths used by grafana-server    | Object  |
| grafana_http    | Host/Port on which grafana listens            | Object  |
| grafana_auth    | Grafana credentials                           | Object  |
| grafana_thene   | Theme (dark or light) used by grafana         | String  |
| prometheus_host | Host on which prometheus source is configured | String  |
| prometheus_port | Port on which prometheus source is configured | Integer |


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

https://github.com/vdombrovski/ansible-openio-monitoring

License
-------

Apache v2.0

Author Information
------------------

Vladimir DOMBROVSKI (maintainer)
Cedric Delgehier (contributor)
Romain Acciari (contributor)
