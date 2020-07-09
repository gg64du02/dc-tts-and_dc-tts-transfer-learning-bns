#from tensorflow.python.summary import event_accumulator
from tensorboard.backend.event_processing import event_accumulator


#ea = event_accumulator.EventAccumulator('events.out.tfevents.x.ip-x-x-x-x', 
ea = event_accumulator.EventAccumulator('./logdir/new_hand_cleaned/LJ01-2/events.out.tfevents.1594247561.SHADOW-TA0HD7L3', 
size_guidance={ # see below regarding this argument 
event_accumulator.COMPRESSED_HISTOGRAMS: 500, 
event_accumulator.IMAGES: 4, 
event_accumulator.AUDIO: 4, 
event_accumulator.SCALARS: 0, 
event_accumulator.HISTOGRAMS: 1, 
}) 
    
print(ea.Reload())

#print( ea.Tags() )

#'train/loss_mags', 'train/loss_bd2', 'lr'], 'distributions': [],
# 'tensors': [], 'graph': True, 'meta_graph': True, 'run_metadata': []}

#print( ea.Scalars('train/loss_mags') )
#print( ea.Scalars('train/loss_bd2') )
#print( ea.Scalars('lr') )
LRs = ea.Scalars('lr')
LRlist = []
loss_magss = ea.Scalars('train/loss_mags')
loss_magsList = []
loss_bd2s = ea.Scalars('train/loss_bd2') 
loss_bd2List = []
for lr in LRs:
    LRlist.append(lr.value)
for loss_mags in loss_magss:
    loss_magsList.append(loss_mags.value)
for loss_bd2 in loss_bd2s:
    loss_bd2List.append(loss_bd2.value)
    
    
import matplotlib.pyplot as plt
#plt.plot([1, 2, 3, 4])
#plt.plot(LRlist)
#plt.ylabel('LRlist')
#plt.show()


ax1 = plt.subplot(311)
plt.plot(LRlist)
ax2 = plt.subplot(312)
plt.plot(loss_magsList)
ax3 = plt.subplot(313)
plt.plot(loss_bd2List)
plt.show()