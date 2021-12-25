# Lambda

This project is responsible for the setup.leadsigma.com onboarding

## Requirements

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

- SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- [Python 3 installed](https://www.python.org/downloads/)
  - NOTE: If you have a Mac, you may have to link 3.8 as your running python version `brew link --overwrite python@3.8`
- Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

## Running Locally

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build --use-container
```

Run functions locally and invoke them with the `sam local invoke` command.

```bash
sam local invoke SetupFunction --event events/event.json --env-vars=env.json -d 5890
```

The SAM CLI can also emulate your application's API. Use the `sam local start-api` to run the API locally on port 3000.

```bash
sam local start-api
```

You can override the OS envvars used with the env.json file in the root directory

```
{
    "SetupFunction": {
        "EX_URL": "https://aws.amazon.com",
        ...
}
```

## Debugging

Debugging through Lambda is a little hairy. We use [ptsvd](https://github.com/microsoft/ptvsd) with python attached deuggers. Currently to debug we paste the following lines of code in and build the container again. After the container is built pass the -d 5890 parameter in.

```
import ptvsd

# Enable ptvsd on 0.0.0.0 address and on port 5890 that we'll connect later with our IDE
ptvsd.enable_attach(address=('0.0.0.0', 5890), redirect_output=True)
ptvsd.wait_for_attach()
breakpoint()
```

Inside VSCODE use the python debugging functionality setup inside .vscode/launch.json

Execute the following code and then use the VSCode debugger to step through your breakpoints

```
sam local invoke ExFunction --event events/events.json --env-vars=env.json -d 5890
```

```

## Deploying

There are two config files, one for staging and one for prod

```

sam deploy
sam deploy --config-file=samconfig-prod.toml

```

## Tests

```

pip3 install pytest
pytest

```

## Resourcesa

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)
```
