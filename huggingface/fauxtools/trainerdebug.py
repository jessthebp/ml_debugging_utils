from typing import Union, Iterable

class FauxTrainer:
    def __init__(self, train_dataset, eval_dataset, data_collator):
        self.train_dataset = train_dataset
        self.eval_dataset = eval_dataset
        self.data_collator = data_collator

    def _check_valid_index_key(self, key: Union[int, slice, range, Iterable], size: int) -> None:
        print(f"Checking key: {key} for dataset size: {size}")  # Console log the key and dataset size

        if isinstance(key, int):
            if (key < 0 and key + size < 0) or (key >= size):
                raise IndexError(f"Invalid key: {key} is out of bounds for size {size}")
            return
        elif isinstance(key, slice):
            pass
        elif isinstance(key, range):
            if len(key) > 0:
                self._check_valid_index_key(max(key), size=size)
                self._check_valid_index_key(min(key), size=size)
        elif isinstance(key, Iterable):
            if len(key) > 0:
                self._check_valid_index_key(int(max(key)), size=size)
                self._check_valid_index_key(int(min(key)), size=size)
        else:
            raise ValueError(f"Invalid key type: {type(key)}")

    def train(self):
        # Simulate training by iterating over the train_dataset
        for i, data in enumerate(self.train_dataset):
            # Check if the index is valid
            self._check_valid_index_key(i, len(self.train_dataset))
            
            processed_data = self.data_collator([data])
            print(f"Batch {i}:")
            print(processed_data)
            print("------")

    def evaluate(self):
        # Simulate evaluation by iterating over the eval_dataset
        for i, data in enumerate(self.eval_dataset):
            # Check if the index is valid
            self._check_valid_index_key(i, len(self.eval_dataset))
            
            processed_data = self.data_collator([data])
            print(f"Batch {i}:")
            print(processed_data)
            print("------")

# Instantiate the FauxTrainer
faux_trainer = FauxTrainer(
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    data_collator=lambda data: custom_collate_fn(data, tokenizer=tokenizer)
)

# Call the train method to inspect the batches
faux_trainer.train()

# Call the evaluate method to inspect the batches
faux_trainer.evaluate()
