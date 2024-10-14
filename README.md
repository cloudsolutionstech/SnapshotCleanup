## Automating EBS Snapshot Deletion with AWS Lambda

## Project Overview
This project demonstrates how to use AWS Lambda to automate the deletion of unused or orphaned Amazon Elastic Block Store (EBS) snapshots. The goal is to reduce storage costs and optimize AWS resource management by identifying and removing snapshots that are no longer associated with active EC2 instances. This solution enables you to maintain an efficient and cost-effective AWS cloud environment with minimal manual intervention.

## Table of Contents
- Project Overview
- Architecture
- Why This Project is Important
- AWS Services Used
- Pre-requisities
- Project Setup
01. Creating the Lamdba Function
02. IAM Role Setup
03. Configuring CloudWatch Event
- Monitoring the Lambda Function
- Testing the Lambda Function
- License

## Architecture
The architecture for this project is simple yet powerful:
- Lambda Function: Identifies and deletes EBS snapshots that are no longer associated with active EC2 instances.
- CloudWatch Events: Triggers the Lambda function on a set schedule (e.g., daily or weekly).
- IAM Roles: Provides the Lambda function with the required permissions to interact with EC2 and EBS resources.

## Why This Project is Important
AWS storage costs can escalate quickly if resources like EBS snapshots are not actively managed. Unused snapshots, especially those no longer associated with EC2 instances, can accumulate over time, leading to unnecessary overhead and increased expenses. This project automates the identification and deletion of these snapshots, ensuring that only the necessary resources are retained.

By implementing this solution, you can expect:

- Cost Optimization: Eliminate storage costs for unused EBS snapshots.
- Operational Efficiency: Automate manual snapshot management tasks, allowing your team to focus on more critical activities.
- Scalability: Easily scale this solution across multiple regions or accounts, ensuring continuous cost savings.

AWS Services Used
This project leverages the following AWS services:

01. AWS Lambda: The serverless compute service that executes the snapshot deletion logic.
02. Amazon EC2: The service providing the EBS snapshots and active instances.
03. Amazon Elastic Block Store (EBS): Provides the snapshots that are identified and deleted.
04. Amazon CloudWatch Events: Triggers the Lambda function on a scheduled basis (e.g., daily or weekly).
05. Amazon CloudWatch Logs: Logs all events and activities related to the Lambda function's execution.
06. IAM (Identity and Access Management): Manages the permissions required for the Lambda function.

## Pre-requisites
Before you begin, ensure you have the following:

01. AWS Account: You must have an AWS account with appropriate permissions to manage EC2, EBS, Lambda, and CloudWatch.
02. IAM Role with Necessary Permissions: An IAM Role that grants Lambda access to describe and delete EBS snapshots, and describe EC2 instances.
03. AWS CLI or Console Access: You should be able to deploy Lambda functions and manage AWS services through the AWS Management Console or CLI.
04. Python Knowledge: Basic understanding of Python for modifying the Lambda function if needed.

## Project Setup
Step 1: Creating the Lambda Function
1. Navigate to the AWS Lambda Console.
2. Click Create Function.
3. Select Author from scratch and give your function a name like ebs-snapshot-cleanup.
4. Choose the Python 3.x runtime.
5. Assign the appropriate execution role (IAM Role with EC2 and EBS permissions).
6. Copy and paste the Python code from this repository into the Lambda function editor. Ensure it matches your use case, especially if you're running it in multiple regions.
7. Save the function.

Step 2: IAM Role Setup
1. Go to the IAM Console and create a new role (if not done already).
2. Attach the following policies:
     - AmazonEC2ReadOnlyAccess: Allows Lambda to describe EC2 instances and volumes.
     - AmazonEBSFullAccess: Allows Lambda to manage and delete EBS snapshots.
3. Attach the role to your Lambda function under the Execution Role section.

Step 3: Configuring CloudWatch Event
1. Go to the Amazon CloudWatch Console.
2. In the navigation pane, select Rules and click Create Rule.
3. Choose Event Source > Schedule and set the desired frequency (e.g., daily, weekly).
4. Select Add Target and choose Lambda Function.
5. Select your Lambda function (ebs-snapshot-cleanup).
6. Save the rule.

## Monitoring the Lambda Function
1. Go to Amazon CloudWatch Logs.
2. You can monitor the Lambda execution logs under the log group for your Lambda function.
3. Logs will show detailed information about deleted snapshots, any errors encountered, and overall execution status.

## Testing the Lambda Function
1. In the AWS Lambda Console, create a Test Event for the function.
2. Run the function manually by invoking the test event.
3. Verify the results by checking CloudWatch Logs and ensuring that any disassociated snapshots are deleted.
4. Check your EBS Snapshot section in the EC2 Console to confirm that unused snapshots have been removed.

## License
This project is licensed under the MIT License - see the [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) for details.

## Contact
For any questions or inquiries, feel free to reach out:
- Email: info@cloudsolutionstech.com
- YouTube: [YouTube Channel](http://www.youtube.com/@cloudsolutionsIT)

## Additional Resources
- Blog Post: [Latest Tech News](https://cloudsolutionstech.com/news/)


This is the end of this project, You have done a great job !!!


