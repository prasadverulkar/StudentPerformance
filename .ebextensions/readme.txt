# AWS - Elastic Beanstalk

AWS Elastic Beanstalk is a Platform as a Service (PaaS) offered by Amazon Web Services (AWS) that makes it easy to deploy, manage, and scale web applications and services.

✅ Key Features of Elastic Beanstalk:
1. Simplified Deployment: You only need to upload your code; Elastic Beanstalk handles provisioning, load balancing, scaling, and monitoring.
2. Supported Platforms: Supports Python, Java, Node.js, Ruby, PHP, .NET, Docker, and Go.
3. Infrastructure Management: Automatically manages underlying infrastructure, including EC2 instances, RDS, S3, and more.
4. Autoscaling: Automatically scales up or down depending on traffic.
5. Monitoring and Logs: Integrated with CloudWatch for real-time performance monitoring.
6. Customization: You can modify EC2 instance types, environment variables, and more.

🏆 Why Use Elastic Beanstalk for ML Models?
1. You can deploy machine learning models as a REST API.
2. Handles infrastructure and scaling so you can focus on the model.
3. Supports Docker, allowing you to package and deploy any ML model.

Requirements:
1) .ebextenstions which contains python.config file
The python.config file is used to configure the Elastic Beanstalk environment for a Python-based application. 
It specifies how Elastic Beanstalk should run and serve your Python application.
The python.config file is typically placed in a .ebextensions folder in the root directory of your project

Key components in python.config file:

1) option_settings

- The option_settings section is used to define configuration options for Elastic Beanstalk.
- Settings are defined in key-value pairs under specific namespaces.

2) "aws.elasticbeanstalk:container:python"

- This is a namespace for Python container configuration in Elastic Beanstalk.
- Tells Elastic Beanstalk that the app is a Python-based project.

3) WSGIPath

- Stands for Web Server Gateway Interface.
- Specifies the Python module and application object that Elastic Beanstalk should use to serve the app.
- Format is give as --> module_name:application_object
- module_name = Name of the Python file (File name without .py extension), 
  application_object = Name of the Flask or Django app object inside that file


If while creating an environment in elastic beanstalk, following error arises then follow instructions given in link
"The instance profile aws-elasticbeanstalk-ec2-role associated with the environment does not exist"
"https://www.reddit.com/r/aws/comments/13f2jdg/error_the_instance_profile/?rdt=34213"

Youtube reference video to create an application on aws beanstalk
https://www.youtube.com/watch?v=rVYFZ_gCYqw