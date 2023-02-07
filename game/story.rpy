label story:
scene bg club_day
$ s_name = "sayori"
show sayori 2 zorder 2 at t11
s "hi mc"
mc "hello"
hide sayori
$ i_name = "ironmouse"
show ironmouse girl4
i "hi friend can i show you my poem"
mc "sure"
call showpoem(poem_i1, img = "ironmouse girl4", music = True)
mc "wow"
return