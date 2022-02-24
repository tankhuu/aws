# AWS Automation powered by AWS CDK TF(Terraform)

- [QuickStarted Guide](https://learn.hashicorp.com/tutorials/terraform/cdktf?in=terraform/cdktf)

## Prerequisites

- [cdktf](https://learn.hashicorp.com/tutorials/terraform/cdktf-install?in=terraform/cdktf)
- [node](https://nodejs.org/en/download/)
- [terraform](https://learn.hashicorp.com/tutorials/terraform/cdktf-install?in=terraform/cdktf)

## Init

```
cd cdktf/automation
cdktf init --template=typescript --local
```

## Get packages

```
# in cdktf/automationa
npm install @cdktf/provider-aws
cdktf get
```