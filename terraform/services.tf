data "harness_platform_organization" "org" {
  identifier = "ing175org"
}

data "harness_platform_project" "prj" {
  name = "ing175ip1"
  org_id = "${data.harness_platform_organization.org.identifier}"
}

variable "itterator" {
  type    = list(string)
  default = ["0", "1", "2"]
}

resource "harness_platform_service" "simple_service" {
  count       = length(var.itterator)
  name        = "transaction-ingestor-${var.itterator[count.index]}"
  identifier  = "transactioningestor${var.itterator[count.index]}"
  description = "Minimal service without connectors"
  org_id      = "ing175org"
  project_id  = "ing175ip1"
  yaml = <<-EOT
      service:
        name: transaction-ingestor-${var.itterator[count.index]}
        identifier: transactioningestor${var.itterator[count.index]}
        serviceDefinition:
          type: NativeHelm
          spec:
            manifests:
              - manifest:
                  identifier: transactioningestor${var.itterator[count.index]}
                  type: HelmChart
                  spec:
                    store:
                      type: Github
                      spec:
                        connectorRef: githubaccount
                        gitFetchType: Branch
                        folderPath: helmcharts/transaction-ingestor
                        branch: main
                    subChartPath: ""
                    valuesPaths:
                      - helmcharts/transaction-ingestor/values.yaml
                    skipResourceVersioning: false
                    enableDeclarativeRollback: false
                    helmVersion: V3
                    fetchHelmChartMetadata: false
        gitOpsEnabled: false
        orgIdentifier: ing175org
        projectIdentifier: ing175ip1
  EOT
}
