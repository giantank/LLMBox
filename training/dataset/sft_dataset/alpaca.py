from .sftdataset import SFTDataset


class AlpacaDataset(SFTDataset):
    """
    Stanford alpaca's dataset is a 52K instruction-following demonstrations generated from OpenAI’s text-davinci-003.
    """
    
    def process(self,tokenizer):
        """Process the dataset and return input_ids and labels."""
        input_ids = []
        labels = []
        list_data_dict = self.load_data()
        for example in list_data_dict:
            s = tokenizer.apply_chat_template([{'role':'user','content':example['instruction']+example['input']}],tokenize=False)
            t = tokenizer.apply_chat_template([{'role':'assistant','content':example['output']}],tokenize=False)
            input_id, label = self.encode_src_tgt(s, t, tokenizer)
            input_ids.append(input_id)
            labels.append(label)
        return input_ids, labels
    
