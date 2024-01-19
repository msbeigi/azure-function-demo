
[![Build and deploy Python project to Azure Function App - city-app-demo](https://github.com/msbeigi/azure-function-demo/actions/workflows/main_city-app-demo.yml/badge.svg)](https://github.com/msbeigi/azure-function-demo/actions/workflows/main_city-app-demo.yml)

[![Microsoft Documentation](https://img.shields.io/badge/Microsoft-Documentation-blue?style=flat&logo=microsoft)](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=windows%2Cbash%2Cazure-cli&pivots=python-mode-decorators)


# azure-function-storage-processor

```
npm install -g npm@10.3.0
npm install -g azure-functions-core-tools@3 --unsafe-perm true

```

[Documentation](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=windows%2Cbash%2Cazure-cli&pivots=python-mode-decorators)

``` bash
python -m venv .venv
source .venv/bin/activate
sudo apt-get install python3-venv
func init --python
func new --name HttpSampleProcessor --template "HTTP trigger" --authlevel "anonymous"
# with the ANONYMOUS option
# in  the local.settings.json project file, the AzureWebJobsFeatureFlags setting should have a value of "EnableWorkerIndexing" and with "AzureWebJobsStorage": "UseDevelopmentStorage=true".
.venv/bin/python -m pip install -r requirements.txt
func start  # azure function is up & running (func host start --port 7072)
```

```
curl http://localhost:7071/api/HttpSampleProcessor
curl "http://localhost:7071/api/HttpSampleProcessor?name=John"


```


After Sychronizing the repo with the azureFunctionApp, .ymal file will be created