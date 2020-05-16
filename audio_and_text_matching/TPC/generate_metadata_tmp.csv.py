
f = open("metadata_tmp.csv","w+")
for i in range(6726):
    tmpPathName = "samples/thepoetscorner_{:05}.wav|".format(i)
    f.write(tmpPathName+'\n')
f.close()
