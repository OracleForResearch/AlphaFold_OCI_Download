# AlphaFold OCI Download

Use these scripts to download data from Oracle Open Data platform to use with AlphaFold.

## Prerequisites:

### Installing Aria2: 

__On Oracle Linux 7.9:__

```{bash}
sudo yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm -y 
sudo yum install aria2 -y
```

__On Ubuntu:__

```{bash}
sudo apt install aria2
```

### Install rclone 

__On Oracle Linux 7.9:__

```{bash} 
sudo yum install rclone -y
```
__On Ubuntu:__

```{bash}
sudo apt install rclone -y
```

### Configure rclone

```{bash}
vim ~/.config/rclone/rclone.conf
```
If the __~/.config/rclone__ folder is not existing, please create it. Then paste the following lines into the rclone.conf file

```{bash}
[oss]
type = s3
provider = Other
env_auth = false
access_key_id = 
secret_access_key = 
endpoint = https://idcxvbiyd8fn.compat.objectstorage.us-ashburn-1.oraclecloud.com
region = us-ashburn-1
```

## Make files executable 

```{bash}
chmod 777 *.sh *.py
```

## How to download data using the script

To download all the databases, execute the __download_all_data.sh__ by typing

```{bash}
./download_all_data.sh /path/to/download/directory
```
__NOTE :__

* Consider running the script using screen.

