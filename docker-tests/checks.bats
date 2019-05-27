#! /usr/bin/env bats

# Variable SUT_IP should be set outside this script and should contain the IP
# address of the System Under Test.

# Tests

@test 'Grafana listens 3000' {
  run bash -c "curl http://${SUT_IP}:3000"
  echo "output: "$output
  echo "status: "$status
  [[ "${status}" -eq "0" ]]
}

@test 'Grafana dashboards are provisioned' {
  run bash -c "docker exec -ti ${SUT_ID} ls -l /etc/grafana/provisioning/dashboards/ | grep '.json'"
  echo "output: "$output
  [[ "${status}" -eq "0" ]]
}
