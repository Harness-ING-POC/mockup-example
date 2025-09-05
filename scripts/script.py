import os
import yaml

# Set your desired output directory here
output_dir = "/Users/kq76cv/Documents/work/povs/harnes/mockup-example/.harness/orgs/ing175org/projects/ing175ip1/services"
os.makedirs(output_dir, exist_ok=True)

# Base template
base_service = {
    "service": {
        "serviceDefinition": {
            "type": "NativeHelm",
            "spec": {
                "manifests": [
                    {
                        "manifest": {
                            "type": "HelmChart",
                            "spec": {
                                "store": {
                                    "type": "Github",
                                    "spec": {
                                        "connectorRef": "githubaccount",
                                        "gitFetchType": "Branch",
                                        "folderPath": "helmcharts/transaction-db",
                                        "branch": "main"
                                    }
                                },
                                "subChartPath": "",
                                "valuesPaths": [
                                    "helmcharts/transaction-db/values.yaml"
                                ],
                                "skipResourceVersioning": False,
                                "enableDeclarativeRollback": False,
                                "helmVersion": "V3",
                                "fetchHelmChartMetadata": False
                            },
                            "identifier": ""
                        }
                    }
                ]
            }
        },
        "name": "",
        "identifier": "",
        "gitOpsEnabled": False,
        "orgIdentifier": "ing175org",
        "projectIdentifier": "ing175ip1"
    }
}

# Generate 500 services
for i in range(1, 501):
    suffix = f"{i:03}"
    name = f"transaction-db-{suffix}"
    identifier = f"transactiondb{suffix}"

    service = base_service.copy()
    service["service"]["name"] = name
    service["service"]["identifier"] = identifier
    service["service"]["serviceDefinition"]["spec"]["manifests"][0]["manifest"]["identifier"] = identifier

    # Save to file
    file_path = os.path.join(output_dir, f"{name}.yaml")
    with open(file_path, "w") as f:
        yaml.dump(service, f, sort_keys=False)
