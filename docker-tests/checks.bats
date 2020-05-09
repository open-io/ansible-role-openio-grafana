#! /usr/bin/env bats

# Variable SUT_IP should be set outside this script and should contain the IP
# address of the System Under Test.

# Tests

@test 'Grafana listens 6910' {
  run bash -c "curl http://${SUT_IP}:6910/api/health"
  echo "output: "$output
  echo "status: "$status
  [[ "${status}" -eq "0" ]]
}

@test 'Grafana got openio folder' {
  run bash -c "curl http://admin:admin@${SUT_IP}:6910/api/folders/openio"
  echo "output: "$output
  echo "status: "$status
  [[ "${status}" -eq "0" ]]
}

@test 'Grafana dashboards are provisioned' {
  #run bash -c "curl 'http://admin:admin@${SUT_IP}:6910/api/search?type=dash-db&folderIds=1'"
  run bash -c "curl -qs 'http://admin:admin@${SUT_IP}:6910/api/search?type=dash-db&folderIds=1' | jq '. | length'"
  echo "output: "$output
  [[ "${status}" -eq "0" && "$output" == "11" ]]
}
