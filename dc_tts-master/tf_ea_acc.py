#thanks to https://stackoverrun.com/fr/q/11306923
# from tensorflow.python.summary import event_accumulator
from tensorboard.backend.event_processing import event_accumulator

# ea = event_accumulator.EventAccumulator('events.out.tfevents.x.ip-x-x-x-x',
ea = event_accumulator.EventAccumulator(
    './logdir/new_hand_cleaned/LJ01-2/events.out.tfevents.1594247561.SHADOW-TA0HD7L3',
    size_guidance={  # see below regarding this argument
        event_accumulator.COMPRESSED_HISTOGRAMS: 500,
        event_accumulator.IMAGES: 4,
        event_accumulator.AUDIO: 4,
        event_accumulator.SCALARS: 0,
        event_accumulator.HISTOGRAMS: 1,
    })

print(ea.Reload())

print(ea.Tags())

# print( ea.Scalars('Loss') )
# 'train/loss_mags', 'train/loss_bd2', 'lr'], 'distributions': [],
# 'tensors': [], 'graph': True, 'meta_graph': True, 'run_metadata': []}
print(ea.Scalars('train/loss_mags'))
print(ea.Scalars('train/loss_bd2'))
print(ea.Scalars('lr'))

