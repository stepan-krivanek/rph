import os

class MyFilter:
    def __init__(self):
        self.decisions = {
            False : ' OK\n',
            True : ' SPAM\n'
            }

        self.spam_key_words = {}
        self.ham_key_words = {}

    def train(self, train_dir):
        truth_dict = self.read_classification_from_file(os.path.join(train_dir, '!truth.txt'))
        spam_files = 0
        ham_files = 0

        for file_name, state in truth_dict.items():
            
            try:
                email = open(os.path.join(train_dir, file_name), 'r', encoding = 'utf-8')
                key_words = self.get_key_words(email)
                email.close()
            except:
                continue
            
            if state == 'SPAM':
                spam_files += 1
            else:
                ham_files += 1

            for word, abundance in key_words.items():
                if state == 'SPAM':
                    if word in self.spam_key_words.keys():
                        self.spam_key_words[word] += 1
                    else:
                        self.spam_key_words[word] = 1
                else:
                    if word in self.ham_key_words.keys():
                        self.ham_key_words[word] += 1
                    else:
                        self.ham_key_words[word] = 1

        for word, abundance in self.spam_key_words.items():
            if spam_files > 0:
                self.spam_key_words[word] = abundance/spam_files

        for word, abundance in self.ham_key_words.items():
            if ham_files > 0:
                self.ham_key_words[word] = abundance/ham_files

    def test(self, test_dir):
        prediction_file = open(os.path.join(test_dir, '!prediction.txt'), 'w+', encoding = 'utf-8')

        for file_name in os.listdir(test_dir):
            if file_name[0] == "!": continue
            
            try:
                email = open(os.path.join(test_dir, file_name), 'r', encoding = 'utf-8')
                key_words = self.get_key_words(email)
                email.close()
            except:
                continue

            decision = self.decisions[self.check_spam(key_words)]
            prediction_file.write(file_name + decision)

        prediction_file.close()

    def check_spam(self, key_words):     
        p1 = 1
        p2 = 1
        ret = False

        for word, abundance in key_words.items():
            if word in self.spam_key_words.keys():
                spam_appearance = self.spam_key_words[word]
            else:
                spam_appearance = 0

            if word in self.ham_key_words.keys():
                ham_appearance = self.ham_key_words[word]
            else:
                ham_appearance = 0
            
            word_appearance = spam_appearance + ham_appearance

            if word_appearance > 0:
                word_spam_prob = spam_appearance/word_appearance

                if word_spam_prob > 0.49 and word_spam_prob < 0.60:
                    continue
                else:
                    p1 = p1*(word_spam_prob)
                    p2 = p2*(1-word_spam_prob)
        
        if p1+p2 == 0:
            self.compress_dictionary(key_words, 10)
            ret = self.check_spam(key_words)
        else:
            spam_probability = p1/(p1+p2)
            if spam_probability > 0.5:
                ret = True

        return ret
    
    def compress_dictionary(self, dictionary, reduction):
        compression = len(dictionary)//reduction

        while len(dictionary) > compression:
            del dictionary[min(dictionary, key=dictionary.get)]

    def get_key_words(self, email):
        key_words = {}

        for word in email.read().split():
            if word in key_words.keys():
                key_words[word] += 1
            else:
                key_words[word] = 1

        return key_words

    def read_classification_from_file(self, file_name):
        f = open(file_name, 'r', encoding = 'utf-8')
        dictionary = {}

        for line in f:
            name, state = line.split()
            dictionary[name] = state

        f.close()
        return dictionary