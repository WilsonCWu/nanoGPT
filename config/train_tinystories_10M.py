# Based of train_chakespeare_char

out_dir = 'out-tinystories'
eval_interval = 1000
eval_iters = 200
log_interval = 10

always_save_checkpoint = True

wandb_log = True # override via command line if you like
wandb_project = 'tinystories'
wandb_run_name = 'tinystories-10M'

dataset = 'tinystories'
# total batch size ~0.5M??? assuming that's a good number based on train_gpt2
gradient_accumulation_steps = 30 
batch_size = 64
block_size = 256 # context of up to 256 previous characters

# baby GPT model :)
n_layer = 6
n_head = 6
n_embd = 384
dropout = 0.2

learning_rate = 1e-3 # with baby networks can afford to go a bit higher
max_iters = 5000
lr_decay_iters = 5000 # make equal to max_iters usually
min_lr = 1e-4 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

warmup_iters = 100 # not super necessary potentially

# on macbook also add
# device = 'cpu'  # run on cpu only
# compile = False # do not torch compile the model
