from pathy import dataclass
from summarizer import Summarizer,TransformerSummarizer

dummy_text = '''Scientists say they have discovered a new species of orangutans on Indonesia’s island of Sumatra.
The population differs in several ways from the two existing orangutan species found in Sumatra and the neighboring island of Borneo.
The orangutans were found inside North Sumatra’s Batang Toru forest, the science publication Current Biology reported.
Researchers named the new species the Tapanuli orangutan. They say the animals are considered a new species because of genetic, skeletal and tooth differences.
Michael Kruetzen is a geneticist with the University of Zurich who has studied the orangutans for several years. He said he was excited to be part of the unusual discovery of a new great ape in the present day. He noted that most great apes are currently considered endangered or severely endangered.
Gorillas, chimpanzees and bonobos also belong to the great ape species. Orangutan – which means person of the forest in the Indonesian and Malay languages - is the world’s biggest tree-living mammal. The orange-haired animals can move easily among the trees because their arms are longer than their legs. They live more lonely lives than other great apes, spending a lot of time sleeping and eating fruit in the forest.
The new study said fewer than 800 of the newly-described orangutans exist. Their low numbers make the group the most endangered of all the great ape species.
They live within an area covering about 1,000 square kilometers. The population is considered highly vulnerable. That is because the environment which they depend on is greatly threatened by development.
Researchers say if steps are not taken quickly to reduce the current and future threats, the new species could become extinct “within our lifetime.”
Research into the new species began in 2013, when an orangutan protection group in Sumatra found an injured orangutan in an area far away from the other species. The adult male orangutan had been beaten by local villagers and died of his injuries. The complete skull was examined by researchers.
Among the physical differences of the new species are a notably smaller head and frizzier hair. The Tapanuli orangutans also have a different diet and are found only in higher forest areas.
There is no unified international system for recognizing new species. But to be considered, discovery claims at least require publication in a major scientific publication.
Russell Mittermeier is head of the primate specialist group at the International Union for the Conservation of Nature. He called the finding a “remarkable discovery.” He said it puts responsibility on the Indonesian government to help the species survive.
Matthew Nowak is one of the writers of the study. He told the Associated Press that there are three groups of the Tapanuli orangutans that are separated by non-protected land.He said forest land needs to connect the separated groups.
In addition, the writers of the study are recommending that plans for a hydropower center in the area be stopped by the government.
It also recommended that remaining forest in the Sumatran area where the orangutans live be protected.
I’m Bryan Lynn. '''

import re

def data_clean(body):

    body = body.encode('ascii', 'ignore').decode()
    sentence = re.sub(r"â\s+", "", body)
    sentence = re.sub(r'\r\n+', "", sentence)
    
    print(sentence)
    return sentence


def BERTSummarizer(body):
    print('len body:', len(body))
    model = Summarizer()    
    data = data_clean(body)
    result = ''.join(model(data, min_length=50))
    print('len BERT summary:', len(result))
    #print(result)
    return result

def GPTSummarizer(body):

    print('len body:', len(body))
    GPT2_model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2-medium")
    data = data_clean(body)
    full = ''.join(GPT2_model(data, min_length=60))
    print('len GPT summary:', len(full))
    #print(full)
    return full

#BERTSummarizer(body)
#GPTSummarizer(body)

'''
len BERT summary: 539
Scientists say they have discovered a new species of orangutans on Indonesia’s island of Sumatra. 
Researchers named the new species the Tapanuli orangutan. Orangutan – which means person of the forest in the 
Indonesian and Malay languages - is the world’s biggest tree-living mammal. Their low numbers make the group the most 
endangered of all the great ape species. There is no unified international system for recognizing new species. 
It also recommended that remaining forest in the Sumatran area where the orangutans live be protected.

len GPT summary: 621
Scientists say they have discovered a new species of orangutans on Indonesia’s island of Sumatra. 
The population differs in several ways from the two existing orangutan species found in Sumatra and the neighboring 
island of Borneo. They say the animals are considered a new species because of genetic, skeletal and tooth differences. 
They live within an area covering about 1,000 square kilometers. That is because the environment which they depend on
is greatly threatened by development. In addition, the writers of the study are recommending that plans for a 
hydropower center in the area be stopped by the government.

'''