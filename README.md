# Pystfix-Log-Gen
This is a python script and targeted postfix configuration designed to create postfix log data that is close to real world mail load. It has only been tested on CentOS 7 but should be very portable across distros.

One difference is that the extended delivery status info usually seen after 'status=<status>' is not there, as messages are discareded to avoid actually delivery attempts from being made.

From and to addresses are randomly generated before the @domain.com part of the address to allow unique to/from parsing of logs via queries if needed.

#Log Example:
Apr  1 15:32:46 localhost  postfix/discard[23132]: 9FA7140BE989: to=<HDYAVORGEDQZ@source.com>, relay=none, delay=0.02, delays=0.02/0/0/0, dsn=2.0.0, status=sent (source.com)
Apr  1 15:32:51 localhost postfix/error[23106]: 5D02540BE988: to=<MVVMZFTSJUBG@deferred.com>, relay=none, delay=0.02, delays=0.01/0/0/0.01, dsn=4.3.0, status=deferred (mail transport unavailable)
Apr  1 15:32:56 localhost postfix/error[23054]: 88B2D40BE989: to=<NVJUEPFETBBU@bounced.com>, relay=none, delay=0.04, delays=0.03/0/0/0, dsn=5.0.0, status=bounced (mail for bounced.com is not deliverable)
Apr  1 15:32:56 localhost postfix/discard[23132]: 8FA2940BE98C: to=<OTVHVBYSSFBS@source.com>, relay=none, delay=0.02, delays=0.02/0/0/0, dsn=2.0.0, status=sent (source.com)
Apr  1 15:33:01 localhost postfix/discard[23132]: 5DFC040BE989: to=<UYSLCXUJNXED@sent.com>, relay=none, delay=0.01, delays=0.01/0/0/0, dsn=2.0.0, status=sent (sent.com)
Apr  1 15:33:06 localhost postfix/error[23106]: 5D36740BE989: to=<RSZNUCTBVDPD@deferred.com>, relay=none, delay=0.05, delays=0.04/0/0/0.01, dsn=4.3.0, status=deferred (mail transport unavailable)

#Quick Start
copy the main.cf and transport_maps file into /etc/postfix
execute the 'postmap transport_maps' command
execute the 'postfix reload' command
#postfix shuld now be configured to properly handle the domains used by the script
place the script in the location you will run it from. Currently I run this from /root/bin but you can run de-elevated if you like. 
Call script into the background via 'nohup ./postfix_loadgen.py &'

watch the /var/log/maillog files to ensure there are no issues.
