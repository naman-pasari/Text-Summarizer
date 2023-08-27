from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
from src.TextSummarizer.entity import ModelTrainerConfig
import torch
import os


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config


    
    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(device)
        os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:512"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_bart = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_colator = DataCollatorForSeq2Seq(
            tokenizer,
            model=model_bart,
        )
        
        #loading data 
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        #trainer_args = TrainingArguments(
            #output_dir=self.config.root_dir, num_train_epochs=self.config.num_train_epochs, warmup_steps=self.config.warmup_steps,
            #per_device_train_batch_size=self.config.per_device_train_batch_size, per_device_eval_batch_size=self.config.per_device_train_batch_size,
            #weight_decay=self.config.weight_decay, logging_steps=self.config.logging_steps,
            #evaluation_strategy=self.config.evaluation_strategy, eval_steps=self.config.eval_steps, save_steps=self.config.save_steps,
            #gradient_accumulation_steps=self.config.gradient_accumulation_steps
    #)
        
        trainer_args = TrainingArguments(
                output_dir=self.config.root_dir, num_train_epochs=5, warmup_steps=500,
                per_device_train_batch_size=1, per_device_eval_batch_size=1,
                weight_decay=0.01, logging_steps=10,
                evaluation_strategy='steps', eval_steps=1000, save_steps=1e6,
                gradient_accumulation_steps=1
            )

        trainer = Trainer(model=model_bart, args=trainer_args,
                  tokenizer=tokenizer, data_collator=seq2seq_data_colator,
                  train_dataset=dataset_samsum_pt["train"], 
                  eval_dataset=dataset_samsum_pt["validation"])
        torch.cuda.empty_cache()
        os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:512"
        trainer.train()

        ## Save model
        model_bart.save_pretrained(os.path.join(self.config.root_dir,"bart-samsum-model"))
        ## Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))