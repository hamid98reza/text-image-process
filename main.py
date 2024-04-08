import sys
from src.tasks import Tasks

tsk = Tasks()
# tsk.process_english(no_num=True,
#                     multi_space=False,
#                     rm_dupl_words=True,
#                     meanless_words=False,
#                     rm_single_char=True)
tsk.process_farsi(rm_sign_num=True,
                  rm_dupl = True,
                  no_multispace=True)
