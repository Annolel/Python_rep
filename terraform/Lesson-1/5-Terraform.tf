provider "aws" {
  access_key = "AKIA357JAUIJQFKG6J5D"
  secret_key = "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"
  region     = "eu-central-1"
}
resource "aws_instance" "my_test_ubuntu" {
  ami           = "ami-04932daa2567651e7"
  instance_type = "t3.micro"
}
