f = open("pwlTest.p", "r")
P0f = open("DDSMDataP0.txt", "w")
P1f = open("DDSMDataP1.txt", "w")
P2f = open("DDSMDataP2.txt", "w")
P3f = open("DDSMDataP3.txt", "w")
P4f = open("DDSMDataP4.txt", "w")
Pass1f = open("DDSMDataPass1f.txt", "w")
Pass2f = open("DDSMDataPass2f.txt", "w")

flines = f.readlines()

Tref = 10e-9
N = 16

for i in range(0,len(flines)):
    line = flines[i].split()
    line[0] = float(line[0])*10*Tref
    sum = int(float(line[1]) + N)
    line[1] = '{0:05b}'.format(sum)
    
    #0 is MSB, 4 is LSB
    newlineP0f = str(line[0]) + " " + str(line[1][4]) + "\n"
    P0f.write(newlineP0f)
    newlineP0f = str(line[0] + Tref - 1e-10) + " " + str(line[1][4]) + "\n"
    P0f.write(newlineP0f)

    newlineP1f = str(line[0]) + " " + str(line[1][3]) + "\n"
    P1f.write(newlineP1f)
    newlineP1f = str(line[0] + Tref - 1e-10) + " " + str(line[1][3]) + "\n"
    P1f.write(newlineP1f)

    newlineP2f = str(line[0]) + " " + str(line[1][2]) + "\n"
    P2f.write(newlineP2f)
    newlineP2f = str(line[0] + Tref - 1e-10) + " " + str(line[1][2]) + "\n"
    P2f.write(newlineP2f)

    newlineP3f = str(line[0]) + " " + str(line[1][1]) + "\n"
    P3f.write(newlineP3f)
    newlineP3f = str(line[0] + Tref - 1e-10) + " " + str(line[1][1]) + "\n"
    P3f.write(newlineP3f)

    newlineP4f = str(line[0]) + " " + str(line[1][0]) + "\n"
    P4f.write(newlineP4f)
    newlineP4f = str(line[0] + Tref - 1e-10) + " " + str(line[1][0]) + "\n"
    P4f.write(newlineP4f)

    if sum > 31:
        newlinePass1f = str(line[0]) + " " + str(0) + "\n"
        Pass1f.write(newlinePass1f)
        newlinePass1f = str(line[0] + Tref - 1e-10) + " " + str(0) + "\n"
        Pass1f.write(newlinePass1f)

        newlinePass2f = str(line[0]) + " " + str(0) + "\n"
        Pass2f.write(newlinePass2f)
        newlinePass2f = str(line[0] + Tref - 1e-10) + " " + str(0) + "\n"
        Pass2f.write(newlinePass2f)
    elif sum > 15:
        newlinePass1f = str(line[0]) + " " + str(1) + "\n"
        Pass1f.write(newlinePass1f)
        newlinePass1f = str(line[0] + Tref - 1e-10) + " " + str(1) + "\n"
        Pass1f.write(newlinePass1f)

        newlinePass2f = str(line[0]) + " " + str(0) + "\n"
        Pass2f.write(newlinePass2f)
        newlinePass2f = str(line[0] + Tref - 1e-10) + " " + str(0) + "\n"
        Pass2f.write(newlinePass2f)
    else:
        newlinePass1f = str(line[0]) + " " + str(1) + "\n"
        Pass1f.write(newlinePass1f)
        newlinePass1f = str(line[0] + Tref - 1e-10) + " " + str(1) + "\n"
        Pass1f.write(newlinePass1f)

        newlinePass2f = str(line[0]) + " " + str(1) + "\n"
        Pass2f.write(newlinePass2f)
        newlinePass2f = str(line[0] + Tref - 1e-10) + " " + str(1) + "\n"
        Pass2f.write(newlinePass2f)