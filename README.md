to use this project, open it in vs and run it, paste your code, and hit enter.


example code (fibbonachi)

	mov r1,1
	fibbonachi_loop_label: ;comments look like this
	add r2 r1 r2
	add r1 r2 r1
	jmp fibbonachi_loop_label
