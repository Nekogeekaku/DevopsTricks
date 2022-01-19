resource "aws_instance" "MyServer" {
  ami = "ami-0ed9277fb7eb570c9"
  instance_type = "t2.micro"
  key_name = "name of my ssh keys"
  tags = {
    Name = "My server"
  }
  security_groups = ["${aws_security_group.sg_ssh.name}"]
  user_data = "#!/bin/bash\nyum update -y\nyum install -y httpd\nsystemctl start httpd\nsystemctl enable httpd\nsudo aws s3 cp s3://bucketname/ami-test.txt /var/www/html/index.html --no-sign-request\n"
}

output "instance_ip_addr" {
  value = aws_instance.MyServer.public_ip
  description = "Public IPV4 address of the new server."

}
