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


Tools - Sanitize
-----

This role is outfitted with a sanitization tool to update dashboards. In order to update a dashboard you need to:

- Head to grafana dashboard, and modify it using the Web Interface (Make it editable first in the gear menu)
- In the gear menu, click View JSON, and copy the json to a file (e.g. `files/dashboard`)
- Run the sanitization script: `tools/sanitize.py files/dashboard`
- Update the dashboard with the sanitized one: `mv files/dashboard files/openio.json`
- Remove (or keep) the backup file (`files/dashboard.old`), you don't need to commit it
- Commit the changes and push to remote


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
