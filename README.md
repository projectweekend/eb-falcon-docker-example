### Elastic Beanstalk Deployment

Assuming [eb-cli](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html) is installed:


#### Initialize the app

```
eb init
```

You will be prompted to:

* Select a default region
* Enter an application name
* Choose a platform (Docker will be detected)
* Enable SSH for EC2 instances (optional)


#### Create the environment

```
eb create
```

You will be prompted to:

* Enter an environment name
* Enter a DNS CNAME prefix


#### Open in browser

```
eb open
```


#### Open Beanstalk Console

```
eb console
```
