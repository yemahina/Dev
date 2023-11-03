  GNU nano 7.2                                                                                                                          ec2.tf                                                                                                                                    

provider "aws" {
  region = "us-east-2"
}


resource "aws_instance" "my_instance2" {
  ami           = "ami-0e83be366243f524a"
  instance_type = "t2.micro"
  key_name      = "yema"
  tags = {
    Name = "yema_Instance"
  }

  security_groups = [aws_security_group.my_security_group2.id]
  subnet_id = "subnet-04ce466f"
}

output "My_ip"{
        value = aws_instance.my_instance2.public_ip
}

resource "aws_security_group" "my_security_group2" {
  name        = "my_security_group2"
  description = "Security group for SSH and HTTP access"
  vpc_id = "vpc-c2c3a2a9"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }


  lifecycle {
    create_before_destroy = true
  }
}

