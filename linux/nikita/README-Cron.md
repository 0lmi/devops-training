# Cron
----
### Task:
Teach a linux command tool *Cron*, why did we need it, how it works, give example of basic commands.

### Why did we need Crone?
---
The cron command-line utility is a job scheduler on Unix-like operating systems.
Users who set up and maintain software environments use cron to schedule jobs.
Cron can start periodically on user set fixed time or periods.

### How it works?
---
Schedulering time will be specified with 5 columns of *
|*|*|*|*|*|
|---------|
|Minutes|Hours|Day|Month|Day of the week|
The actions of cron are driven by a crontab (cron table) file, a configuration file that specifies shell commands to run periodically on a given schedule.
The crontab files are stored where the lists of jobs and other instructions to the cron daemon are kept.

### Basic commands
---
```crontab -l```
*-l for list*
Shows your already created jobs for cron, if you dont have any jobs its says no crontab for $USER.
If you already have atleast 1 job, it shows your simple overview about doing the jobs with crone, and on the bottom shows your job shedulering time and your command.

```crontab -e```
*-e for edit*
First its asking to select a editor for you.
When you picked the needable editor, you already started editing cron-task file which path was. /tmp/crontab.***/crontab.
After all comments start writting needable time and which command/script you prefer to start on your planed time.5 9 * * * echo "hello world" - Every day job starts at 9:05 am.

```crontab -u $USER -e```
*-u for user*
When you creating task you can specify user which complete this tasks.
Example, after starting apache server automatically creating www-data user.
This user can only have much less permissions, note same for yuor or root user.
For script starting you should give full path where this script are actually are.

---
#### Other triggering actions
@reboot - Action which trigger after rebooting system.
@hourly - Each new hour trigger cron.
