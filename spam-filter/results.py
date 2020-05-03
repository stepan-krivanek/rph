f = open("./tests/!prediction.txt", 'r', encoding='utf-8')

tp = 0
tn = 0
fp = 0
fn = 0
for line in f:
    if line[-5:-1] == "SPAM":
        if line[-14:-10] == "spam":
            tp += 1
        else:
            fp += 1
    elif line[-3:-1] == "OK":
        if line[-11:-8] == "ham":
            tn += 1
        else:
            fn += 1

print("tp: %d tn: %d fp: %d fn: %d" %(tp, tn, fp, fn))     
f.close()