provider "aws" {
  access_key = "AKIA357JAUIJ3UKPGNP7"
  secret_key = "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"
  region     = "eu_central-1"
}
resource "aws_instance" "my_test_ubuntu" {
  ami           = ""
  instance_type = ""
}
