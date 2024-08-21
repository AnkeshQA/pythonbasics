# if condition is not met than it will not go inside the loop
# if the condition is met then it will keep on executing until condition mismatches
# continue keyword will skip iteration steps and it will start from next iteration steps
# break keyword will skip mentioned value and stop iteration

demo = 10
while demo >= 1:
    if demo == 9: # 9 wont be printed
        demo = demo-1
        continue
    if demo == 3: # 3 will be skipped and iteration will be stopped
        break
    print(demo)
    demo = demo-1