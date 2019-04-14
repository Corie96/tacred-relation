"""
Define common constants.
"""
# TRAIN_JSON = 'train.json'
# DEV_JSON = 'dev.json'
# TEST_JSON = 'test.json'

# GLOVE_DIR = 'dataset/glove'

EMB_INIT_RANGE = 1.0
MAX_LEN = 100

# vocab
PAD_TOKEN = '<PAD>'
PAD_ID = 0
UNK_TOKEN = '<UNK>'
UNK_ID = 1

INFINITY_NUMBER = 1e12

VOCAB_PREFIX = [PAD_TOKEN, UNK_TOKEN]

# DEPREL_TO_ID = {PAD_TOKEN: 0, UNK_TOKEN: 1, 'punct': 2, 'compound': 3, 'case': 4, 'nmod': 5, 'det': 6, 'nsubj': 7, 'amod': 8, 'conj': 9, 'dobj': 10, 'ROOT': 11, 'cc': 12, 'nmod:poss': 13, 'mark': 14, 'advmod': 15, 'appos': 16, 'nummod': 17, 'dep': 18, 'ccomp': 19, 'aux': 20, 'advcl': 21, 'acl:relcl': 22, 'xcomp': 23, 'cop': 24, 'acl': 25, 'auxpass': 26, 'nsubjpass': 27, 'nmod:tmod': 28, 'neg': 29, 'compound:prt': 30, 'mwe': 31, 'parataxis': 32, 'root': 33, 'nmod:npmod': 34, 'expl': 35, 'csubj': 36, 'cc:preconj': 37, 'iobj': 38, 'det:predet': 39, 'discourse': 40, 'csubjpass': 41}

# hard-coded mappings from fields to ids

SUBJ_NER_TO_ID = {PAD_TOKEN: 0, UNK_TOKEN: 1, 'SET': 2, 'TITLE': 3, 'COUNTRY': 4, 'MONEY': 5, 'STATE_OR_PROVINCE': 6, 'RELIGION': 7, 'NATIONALITY': 8, 'LOCATION': 9, 'MISC': 10, 'CRIMINAL_CHARGE': 11, 'PERSON': 12, 'CAUSE_OF_DEATH': 13, 'O': 14, 'ORGANIZATION': 15, 'IDEOLOGY': 16, 'NUMBER': 17, 'TIME': 18, 'DATE': 19, 'DURATION': 20}

OBJ_NER_TO_ID = {PAD_TOKEN: 0, UNK_TOKEN: 1, 'PERSON': 2, 'ORGANIZATION': 3, 'DATE': 4, 'NUMBER': 5, 'TITLE': 6, 'COUNTRY': 7, 'LOCATION': 8, 'CITY': 9, 'MISC': 10, 'STATE_OR_PROVINCE': 11, 'DURATION': 12, 'NATIONALITY': 13, 'CAUSE_OF_DEATH': 14, 'CRIMINAL_CHARGE': 15, 'RELIGION': 16, 'URL': 17, 'IDEOLOGY': 18, 'SET': 19, 'O': 20, 'ORDINAL': 21, 'TIME': 21}

NER_TO_ID = {PAD_TOKEN: 0, UNK_TOKEN: 1, 'O': 2, 'PERSON': 3, 'ORGANIZATION': 4, 'LOCATION': 5, 'DATE': 6, 'NUMBER': 7, 'MISC': 8, 'DURATION': 9, 'MONEY': 10, 'PERCENT': 11, 'ORDINAL': 12, 'TIME': 13, 'SET': 14}

POS_TO_ID = {PAD_TOKEN: 0, UNK_TOKEN: 1, 'NNP': 2, 'NN': 3, 'IN': 4, 'DT': 5, ',': 6, 'JJ': 7, 'NNS': 8, 'VBD': 9, 'CD': 10, 'CC': 11, '.': 12, 'RB': 13, 'VBN': 14, 'PRP': 15, 'TO': 16, 'VB': 17, 'VBG': 18, 'VBZ': 19, 'PRP$': 20, ':': 21, 'POS': 22, '\'\'': 23, '``': 24, '-RRB-': 25, '-LRB-': 26, 'VBP': 27, 'MD': 28, 'NNPS': 29, 'WP': 30, 'WDT': 31, 'WRB': 32, 'RP': 33, 'JJR': 34, 'JJS': 35, '$': 36, 'FW': 37, 'RBR': 38, 'SYM': 39, 'EX': 40, 'RBS': 41, 'WP$': 42, 'PDT': 43, 'LS': 44, 'UH': 45, '#': 46}

TACRED_LABEL_TO_ID = {'no_relation': 0, 'per:title': 1, 'org:top_members/employees': 2, 'per:employee_of': 3, 'org:alternate_names': 4, 'org:country_of_headquarters': 5, 'per:countries_of_residence': 6, 'org:city_of_headquarters': 7, 'per:cities_of_residence': 8, 'per:age': 9, 'per:stateorprovinces_of_residence': 10, 'per:origin': 11, 'org:subsidiaries': 12, 'org:parents': 13, 'per:spouse': 14, 'org:stateorprovince_of_headquarters': 15, 'per:children': 16, 'per:other_family': 17, 'per:alternate_names': 18, 'org:members': 19, 'per:siblings': 20, 'per:schools_attended': 21, 'per:parents': 22, 'per:date_of_death': 23, 'org:member_of': 24, 'org:founded_by': 25, 'org:website': 26, 'per:cause_of_death': 27, 'org:political/religious_affiliation': 28, 'org:founded': 29, 'per:city_of_death': 30, 'org:shareholders': 31, 'org:number_of_employees/members': 32, 'per:date_of_birth': 33, 'per:city_of_birth': 34, 'per:charges': 35, 'per:stateorprovince_of_death': 36, 'per:religion': 37, 'per:stateorprovince_of_birth': 38, 'per:country_of_birth': 39, 'org:dissolved': 40, 'per:country_of_death': 41}
TACRED_LABEL_TO_PROB = {'no_relation': 0.8018494583538754, 'per:title': 0.03641620807738944, 'org:top_members/employees': 0.028488054471078893, 'per:employee_of': 0.024477341470239444, 'org:alternate_names': 0.011898892723420698, 'org:country_of_headquarters': 0.007195299071273435, 'per:countries_of_residence': 0.006635664699063279, 'org:city_of_headquarters': 0.0058228623965675755, 'per:cities_of_residence': 0.005609668350011326, 'per:age': 0.005543045210462498, 'per:stateorprovinces_of_residence': 0.004983410838252341, 'per:origin': 0.004970086210342576, 'org:subsidiaries': 0.004343828698583592, 'org:parents': 0.004423776466042186, 'per:spouse': 0.004143959279937107, 'org:stateorprovince_of_headquarters': 0.003544351023997655, 'per:children': 0.0031312875587949205, 'per:other_family': 0.0031046383029753894, 'per:alternate_names': 0.0014790336979839838, 'org:members': 0.0025849778144945304, 'per:siblings': 0.0023717837679382804, 'per:schools_attended': 0.0023717837679382804, 'per:parents': 0.002185238977201562, 'per:date_of_death': 0.0020120188143746085, 'org:member_of': 0.001958720302735546, 'org:founded_by': 0.001932071046916015, 'org:website': 0.0017721755119988274, 'per:cause_of_death': 0.0016922277445402336, 'org:political/religious_affiliation': 0.001572306093352343, 'org:founded': 0.0013724366747058588, 'per:city_of_death': 0.0013591120467960933, 'org:shareholders': 0.001159242628149609, 'org:number_of_employees/members': 0.001159242628149609, 'per:date_of_birth': 0.0010393209769617184, 'per:city_of_birth': 0.0010259963490519526, 'per:charges': 0.0010259963490519526, 'per:stateorprovince_of_death': 0.0008661008141347653, 'per:religion': 0.0008128023024957028, 'per:stateorprovince_of_birth': 0.0006262575117589841, 'per:country_of_birth': 0.0005196604884808592, 'org:dissolved': 0.00038641420938320296, 'per:country_of_death': 0.0001332462790976562}
TACRED_LABEL_TO_LOG_PROB = {'no_relation': -0.22083439652311956, 'per:title': -3.312741326594402, 'org:top_members/employees': -3.55827042093748, 'per:employee_of': -3.7100074273073447, 'org:alternate_names': -4.431309931645972, 'org:country_of_headquarters': -4.93432737296415, 'per:countries_of_residence': -5.015296435497818, 'org:city_of_headquarters': -5.14596331742688, 'per:cities_of_residence': -5.183263678840089, 'per:age': -5.195211252261207, 'per:stateorprovinces_of_residence': -5.301640715107938, 'per:origin': -5.304318092878654, 'org:subsidiaries': -5.438999131155763, 'org:parents': -5.420761543605982, 'per:spouse': -5.486103600343236, 'org:stateorprovince_of_headquarters': -5.642400203740771, 'per:children': -5.766310998378311, 'per:other_family': -5.77485805895677, 'per:alternate_names': -6.516366311210136, 'org:members': -5.958038353459142, 'per:siblings': -6.044112962230385, 'per:schools_attended': -6.044112962230385, 'per:parents': -6.126030084698272, 'per:date_of_death': -6.208616675707546, 'org:member_of': -6.235463925743734, 'org:founded_by': -6.249162770101896, 'org:website': -6.335547384300717, 'per:cause_of_death': -6.381709426063879, 'org:political/religious_affiliation': -6.455211888056805, 'org:founded': -6.5911675242928345, 'per:city_of_death': -6.600923699238199, 'org:shareholders': -6.759988393867887, 'org:number_of_employees/members': -6.759988393867887, 'per:date_of_birth': -6.869187685832879, 'per:city_of_birth': -6.882091090668786, 'per:charges': -6.882091090668786, 'per:stateorprovince_of_death': -7.0515092426268335, 'per:religion': -7.115022648349159, 'per:stateorprovince_of_birth': -7.375748910812412, 'per:country_of_birth': -7.562334866392824, 'org:dissolved': -7.858600682535997, 'per:country_of_death': -8.923311419528424}

SEMEVAL_LABEL_TO_ID = {'no_relation': 0, 'Entity-Destination(e1,e2)': 1, 'Cause-Effect(e2,e1)': 2, 'Member-Collection(e2,e1)': 3, 'Entity-Origin(e1,e2)': 4, 'Message-Topic(e1,e2)': 5, 'Component-Whole(e2,e1)': 6, 'Component-Whole(e1,e2)': 7, 'Instrument-Agency(e2,e1)': 8, 'Product-Producer(e2,e1)': 9, 'Content-Container(e1,e2)': 10, 'Cause-Effect(e1,e2)': 11, 'Product-Producer(e1,e2)': 12, 'Content-Container(e2,e1)': 13, 'Entity-Origin(e2,e1)': 14, 'Message-Topic(e2,e1)': 15, 'Instrument-Agency(e1,e2)': 16, 'Member-Collection(e1,e2)': 17, 'Entity-Destination(e2,e1)': 18}
SEMEVAL_LABEL_TO_PROB = {'no_relation': 0.17446867620502848, 'Entity-Destination(e1,e2)': 0.10529240172246146, 'Cause-Effect(e2,e1)': 0.08278927628837339, 'Member-Collection(e2,e1)': 0.07584386720377831, 'Entity-Origin(e1,e2)': 0.07042644811779414, 'Message-Topic(e1,e2)': 0.06098069176274482, 'Component-Whole(e2,e1)': 0.059035977219058206, 'Component-Whole(e1,e2)': 0.0586192526739825, 'Instrument-Agency(e2,e1)': 0.051812751771079316, 'Product-Producer(e2,e1)': 0.049729129045700794, 'Content-Container(e1,e2)': 0.04778441450201417, 'Cause-Effect(e1,e2)': 0.04292262814279761, 'Product-Producer(e1,e2)': 0.04056118905403528, 'Content-Container(e2,e1)': 0.020558410890401446, 'Entity-Origin(e2,e1)': 0.018613696346714823, 'Message-Topic(e2,e1)': 0.018613696346714823, 'Instrument-Agency(e1,e2)': 0.011946103625503543, 'Member-Collection(e1,e2)': 0.010001389081816919, 'Entity-Destination(e2,e1)': 0.0}
SEMEVAL_LABEL_TO_LOG_PROB = {'no_relation': -1.746010059441159, 'Entity-Destination(e1,e2)': -2.2510140208269314, 'Cause-Effect(e2,e1)': -2.491456739403953, 'Member-Collection(e2,e1)': -2.579078430724398, 'Entity-Origin(e1,e2)': -2.6531864028781196, 'Message-Topic(e1,e2)': -2.7971979933941316, 'Component-Whole(e2,e1)': -2.829608237544886, 'Component-Whole(e1,e2)': -2.836692092433291, 'Instrument-Agency(e2,e1)': -2.9601189868254876, 'Product-Producer(e2,e1)': -3.0011644200686027, 'Content-Container(e1,e2)': -3.0410557490959045, 'Cause-Effect(e1,e2)': -3.1483561295715576, 'Product-Producer(e1,e2)': -3.2049436042010213, 'Content-Container(e2,e1)': -3.884485132705188, 'Entity-Origin(e2,e1)': -3.9838576065183915, 'Message-Topic(e2,e1)': -3.9838576065183915, 'Instrument-Agency(e1,e2)': -4.427350110215795, 'Member-Collection(e1,e2)': -4.605031287453247, 'Entity-Destination(e2,e1)': -27.631021115928547}

# SPECIFY THE DATASET HERE
DATASET = 'SEMEVAL'

if DATASET == 'TACRED':
    LABEL_TO_ID = TACRED_LABEL_TO_ID
    LABEL_TO_PROB = TACRED_LABEL_TO_PROB
    LABEL_TO_LOG_PROB = TACRED_LABEL_TO_LOG_PROB
elif DATASET == 'SEMEVAL':
    LABEL_TO_ID = SEMEVAL_LABEL_TO_ID
    LABEL_TO_PROB = SEMEVAL_LABEL_TO_PROB
    LABEL_TO_LOG_PROB = SEMEVAL_LABEL_TO_LOG_PROB