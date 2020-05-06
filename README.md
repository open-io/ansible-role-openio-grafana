[![Build Status](https://travis-ci.org/open-io/ansible-role-openio-grafana.svg?branch=master)](https://travis-ci.org/open-io/ansible-role-openio-grafana)
# Ansible role `grafana`

An Ansible role for install grafana. Specifically, the responsibilities of this role are to:

- install and configure grafana

## Requirements

- Ansible 2.9+

## Role Variables

| Variable   | Default | Comments (type)  |
| :---       | :---    | :---             |
| `openio_grafana_namespace` | `"{{ namespace \| d('OPENIO') }}"` | OpenIO Namespace|
| `openio_grafana_maintenance_mode` | `"{{ openio_maintenance_mode \| d(false) }}"` | Maintenance mode |
| `openio_grafana_bind_address` | `"{{ openio_mgmt_bind_address \| d(ansible_default_ipv4.address) }}"` | Binding IP address |
| `openio_grafana_bind_port` | `6910` | Binding port |
| `openio_grafana_ext_bind_address` | `"{{ openio_grafana_bind_address }}"` | |
| `openio_grafana_ext_bind_port` | `"{{ openio_grafana_bind_port }}"` | |
| `openio_grafana_url` | `"http://{{ openio_grafana_bind_address }}:{{ openio_grafana_bind_port}}"` | URL to access grafana |
| `openio_grafana_path_data` | `"{{ openio_service_volume }}/data"` | Where the data is stored |
| `openio_grafana_path_plugins` | `"{{ openio_service_volume }}/plugins"` | Where the plugins are stored |
| `openio_grafana_path_provisioning` | `"{{ openio_service_conf_dir }}/provisioning"` | Where to find provisionnized dashboards and datasources |
| `openio_grafana_temp_data_lifetime` | `"24h"` | Lifetime of temporary files |
| `openio_grafana_user` | `"admin"` | Admin username |
| `openio_grafana_password` | `"admin"` | Admin password |
| `openio_grafana_secret_key` | `59b579be5dfcfd1d4cc56a8c52d8d700` | Admin password hash |
| `openio_grafana_theme` | `light` | Theme to use |
| `openio_grafana_prometheus_group` | `"prometheus"` | The name of the prometheus group in the inventory |
| `openio_grafana_prometheus_bind_port` | `6900` | Port to use if `openio_prometheus_bind_port` is not set for the target |
| `openio_grafana_loki_group` | `"loki"` | The name of the loki group in the inventory |
| `openio_grafana_loki_bind_port` | `6902` | Port to use if `openio_loki_bind_port` is not set for the target |
| `openio_grafana_elasticsearch_group` | `"elasticsearch"` | The name of the elasticsearch group in the inventory |
| `openio_grafana_elasticsearch_bind_port` | `6904` | Port to use if `openio_elasticsearch_bind_port` is not set for the target |

## Dependencies
- https://github.com/open-io/ansible-role-openio-service

## Example Playbook

```yaml
- hosts: all
  gather_facts: true
  become: true

  tasks:
    - include_role:
        name: grafana
```

## Update provisioning dashboards
When updating provisioned dashboards, use the `retrive_dashboards.yml`
playbook which will download the dashboards from grafana. This way to update
a provisioned dashboard, please follow the following procedure:
- log in grafana
- make changes in the dashboard(s) and save them
- run the `retrive_dashboards.yml` playbook
- commit your changes and PR

To retrieve: 
- all dashbaords, use: `ansible-playbook roles/grafana/tools/retrieve_dashboards.yml`
- one dashboard, use: `ansible-playbook roles/grafana/tools/retrieve_dashboards.yml -e dashboard=%uid%`

**CAUTION**: this will erase the corresponding file(s) in `templates/provisioning/dashboards/openio/`

## Contributing

Issues, feature requests, ideas are appreciated and can be posted in the Issues section.

Pull requests are also very welcome.
The best way to submit a PR is by first creating a fork of this Github project, then creating a topic branch for the suggested change and pushing that branch to your own fork.
Github can then easily create a PR based on that branch.

## License
Copyright (C) 2015-2020 OpenIO SAS
