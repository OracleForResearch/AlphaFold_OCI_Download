# AlphaFold OCI Download

Use these scripts to download data from Oracle Open Data platform to use with AlphaFold.

## Prerequisites:

### Install rclone 

__On Oracle Linux 7.9__

```{bash} 
sudo yum install rclone -y
```
__On Ubuntu__

```{bash}
sudo apt install rclone -y
```

### Configure rclone

```{bash}
vim ~/.config/rclone/rclone.conf
```
If the __~/.config/rclone__ folder is not exsisting, please create it.

and paste the following lines into the rclone.conf file

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

## How to use the script

Execute the download_all_data.sh by typing

```{bash}
./download_all_data.sh /path/to/download/directory
```
__NOTE :__

Consider running the script using screen 

