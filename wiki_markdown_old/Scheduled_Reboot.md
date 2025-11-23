Most dedicated administrators are determined to keep their server
running at its full potential. One way to help do this is rebooting the
system. Personally, I like to reboot my system every morning.

## Scheduling

As I stated before, I like to reboot my system at least once per day.
However, what if I\'m not at home? What if I\'m going to be gone for
days? A timer object would be very useful here.

`<spherescript>`{=html}\[ITEMDEF i_reboot_system_obj\] ID=i_crystal_ball
NAME=Reboot \[DO NOT REMOVE\] WEIGHT=200 TYPE=t_eq_script

ON=@Create

`   ATTR=attr_decay`\
`   TIMER=60`

ON=@Timer

`   LOCAL.HOUR = <SERV.RTIME.FORMAT %H>`\
`   IF (<LOCAL.HOUR> == 06)`\
`       SERV.SAVESTATICS`\
`       SERV.SAVE`\
`       SERV.SHUTDOWN 1`\
`       LOCAL.SPAWN = <SYSSPAWN C:\Windows\System32\shutdown.exe -r -t 120>`\
`   ENDIF`\
`   TIMER = 60`\
`   RETURN 1``</spherescript>`{=html}

Fortunately for us, there is an internal FORMAT function that extends
RTIME to return more specific information. It just so happens that the
argument %H will return the hour, so we can take advantage of this. If
you\'ll look at the IF statement, you\'ll notice that I\'m looking for
hour 06. At this point, we\'ll announce the daily reboot, perform a save
on the statics, as well as a world save. Finally, we\'ll use SYSSPAWN to
call the external program.

## Restarting Sphere {#restarting_sphere}

I bet now you\'re thinking, \"OK, so he figured out how to reboot, but
how the heck is he going to start the server again?\" There are quite a
few ways to approach this:

1.  Use the Startup folder.
2.  Run Sphere as a service.

I\'ve never tried running Sphere as a service, so we\'ll use the first
method. Follow these directions:

1.  Open your Sphere folder.
2.  Create a shortcut from SphereSvr.exe (right-click \> Create
    Shortcut).
3.  Single-click the shortcut, then Cut (Ctrl+X).

Now you need to navigate to your Startup folder (*C:\\Documents and
Settings\\`<USER_NAME>`{=html}\\Start Menu\\Programs\\Startup or Start
\> All Programs \> Startup*). Paste the shortcut into this folder
(Ctrl+V). You\'re done! Sphere should now start on every boot.

[Category:Articles](Category:Articles "wikilink")
