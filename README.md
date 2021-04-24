# AWS ENEM API

## :wrench: Setup

To start developing, you must have Python 3.8 preinstalled.
We recommend using a version manager, like **pip**.

1. Install [Python 3.8](https://www.python.org/downloads/) and Serverless Framework (https://www.serverless.com/framework/docs/providers/aws/guide/installation/)
2. Clone this project `git clone https://github.com/AWS-EDU/aws-edu-enem-api.git`

3. Enter the directory and start VSCode (or your desired IDE) with `cd aws-edu-enem-api; code .`

4. Enter the service directory `cd dashboard_service`

5. Create a virtual environmnet with `virtualenv venv`.
6. Install the dependencies with `pip install -r requirements.txt`.

## :computer: Testing Local

```
cd services/<SERVICE NAME>

docker build -t <SERVICE NAME>:latest .

docker run -e AWS_ACCESS_KEY_ID=<ACCESS KEY> -e AWS_SECRET_ACCESS_KEY=<SECRET KEY> -e AWS_DEFAULT_REGION=<REGION> -p 9000:8080 <SERVICE NAME>:latest <FUNCTION>.lambda_handler

curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```

## :cloud: Deploying on AWS

```
sls package

sls deploy
```

## :lock: Security

See [CONTRIBUTING](/CONTRIBUTING.md#security-issue-notifications) for more information.

## :scroll: License

This project is licensed under the MIT-0 License.
See the [LICENSE](/LICENSE) file.
