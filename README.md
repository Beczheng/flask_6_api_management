# flask_6_api_management

### Assignment:
- Course: HHA 504
- Homework assignment #6: Develop and document APIs using Flask, and manage them with Azure API Management.

### Flask API
- For more information, click [here](https://github.com/Beczheng/flask_6_api_management/blob/main/flask/app_flasgger.py).

### Azure Function API 
- For more information, click [here](https://github.com/Beczheng/flask_6_api_management/blob/main/LocalFunctionProj/function_app.py).

### Azure Deployment
- In your Cloud Shell terminal, type `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`. This will install the Azure CLI.
- Type `az` to check if Azure CLI is installed.
- Type `az login --use-device-code`. A link with a code will appear. Click on the link and enter the code. Then, login to your Microsoft Azure account. This will give Cloud Shell permission to access your Azure account.
- Type `sudo apt-get install azure-functions-core-tools-4`. This will install Azure Functions Core Tools for Linux.
- Type `func init <folder name> --python -m V2`. This will create an Azure Functions project folder. Then, inside the folder, open the `local.settings.json` file. Verify that the `AzureWebJobsFeatureFlags` has a value of `EnableWorkerIndexing`.
- In your Azure account, create a storage account. Then, go to the home page and click on your new storage account. Next, click `access keys` in the navigation bar. Copy the connection string under key. Lastly, replace the connection string with the content for `AzureWebJobsStorage`.
- In your Cloud Shell, type `func start`. This will check if your app is running locally.
- Type `az functionapp create --resource-group <resource group name> --consumption-plan-location eastus --runtime python --runtime-version 3.9 --functions-version 4 --name <app name> --os-type linux --storage-account <storage account name>`. This will create the Azure Function API in Azure.
- Type `func azure functionapp publish <app name>`. This will publish the Azure Function API.

