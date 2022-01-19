
## Provision an EC2 server with a webserver (+index.html), ssh access using Terrafom

You can provision/destroy an EC2 easily with the provided files



>#### Prerequisites
>
> - SSH Key name for the ssh access (you could easily update the script so it is created but I already have one ready)
>
> - AWS key pair to use AWS API
>
> - Having the web page inside an S3 bucket

#### Before running Terraform

- in main.tf put your access keys an region for the server creation

- in hosts.tf put your ssh key name in key_name

- in hosts.tf put your S3 path for the index file



###### To setup terraform using brew
```sh
brew tap hashicorp/tap
brew install hashicorp/tap/terraform

```
For other system get the Hashicorp documentation to install [here](https://learn.hashicorp.com/tutorials/terraform/install-cli)

###### Create the plan to validate your syntax
```sh
terraform plan -out=terraform.plan
```
###### Provision the server
```sh
terraform apply "terraform.plan"
```
You will get the public IPV4 address as an output

###### To release the provisioned server
```sh
terraform destroy
```
