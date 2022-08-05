import boto3

def create_ec2_instance():
        print("creating ec2 instance")
        resource_ec2 = boto3.client("ec2")
        #create the ec2 instance
        resource_ec2.run_instances(
            ImageId = "ami-090fa75af13c156b4",
            #imageid is the AMI ID
            MinCount = 1,
            MaxCount = 1,
            #set the min and max counts of the instances we want to create 
            InstanceType = "t2.micro",
            #set instance type
            KeyName = "ec2-key"
    )

def describe_ec2_instance():
    try:
        print("describing ec2 instance")
        resource_ec2 = boto3.client("ec2")
        #create the ec2 instance
        print(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
        return str(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
    except Exception as e:
        print(e)

def reboot_ec2_instance():
    try:
        print("reboot ec2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.reboot_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)

def stop_ec2_instance():
    try:
        print("stopping ec2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.stop_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)

def start_ec2_instance():
    try:
        print("Start ec2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.start_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)

def terminate_ec2_instance():
    try:
        print("Terminate ec2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.terminate_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)

#create_ec2_instance()
#describe_ec2_instance()
#reboot_ec2_instance()
#stop_ec2_instance()
#start_ec2_instance()
terminate_ec2_instance()
