# Install CDK TF CLI

## Prerequisites

```
terraform -version
-----
Terraform v1.1.6
on darwin_amd64
-----

node --version
-----
v16.14.0
-----

yarn --version
-----
1.22.11
-----
```

### Install prerequisites [optional]

```
# Terraform
brew tap hashicorp/tap
brew install hashicorp/tap/terraform

# NodeJS
https://nodejs.org/en/
## Install latest stable version
## Install n or nvm (package manager) as needed
## Install node with necessary version
sudo n v16.14.20

# yarn
sudo npm install --global yarn
```

## Install CDK TF CLI

```
npm install --global cdktf-cli@next
```