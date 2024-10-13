# Cron ##
The cron command-line utility is a job scheduler on Unix-like operating systems. Users who set up and maintain software environments use cron to schedule jobs

The actions of cron are driven by a crontab (cron table) file, a configuration file that specifies shell commands to run periodically on a given schedule. The crontab files are stored where the lists of jobs and other instructions to the cron daemon are kept. Users can have their own individual crontab files and often there is a system-wide crontab file (usually in /etc or a subdirectory of /etc e.g. /etc/cron.d) that only system administrators can edit.
___

## Exemple ##

```
  * * * * * <command to execute>
  | | | | |
  | | | | day of the week (0–6) (Sunday to Saturday; 
  | | | month (1–12)             7 is also Sunday on some systems)
  | | day of the month (1–31)
  | hour (0–23)
  minute (0–59)
```
This example runs a shell program called export_dump.sh at 23:45 (11:45 PM) every Saturday.
```
45 23 * * 6 /home/oracle/scripts/export_dump.sh
```
**Note**: On some systems it is also possible to specify ```*/n``` to run for every n-th interval of time.
Also, specifying multiple specific time intervals can be done with commas (e.g., 1,2,3). The line below would output "hello world" to the command line every 5th minute of every first, second and third hour (i.e., 01:00, 01:05, 01:10, up until 03:55).
```commandline
*/5 1,2,3 * * * echo hello world
```
The configuration file for a user can be edited by calling ``crontab -e`` regardless of where the actual implementation stores this file
___

## Time zone handling ##

Most cron implementations simply interpret crontab entries in the system time zone setting that the cron daemon runs under.
This can be a source of dispute if a large multi-user machine has users in several time zones, especially if the system default time zone includes the potentially confusing DST.
Thus, a cron implementation may as a special case recognize lines of the form **"CRON_TZ=\<time zone\>"** in user crontabs, interpreting subsequent crontab entries relative to that time zone.
___

## Basic comands ##
1. Open the crontab configuration file for the current user by entering the following command:
```crontab -e```

> If this is your first time accessing the crontab, the system creates a new file. In Ubuntu 22.04, users are prompted to select a preferred text editor. Enter the corresponding number, for example, 1 for nano, to open the crontab file.

2. To schedule a job for a different user, add the -u option and the username:
```crontab -u [username] -e```

3. Enter the following command to list all cron jobs on your system without opening the crontab configuration file:
```crontab -l```

