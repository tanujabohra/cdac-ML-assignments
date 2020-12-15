from nltk.chat.util import Chat, reflections

pairs = [
    ['(hi|hello|hey)', ['Hey there !', 'Hi there !', 'Hey !']],
    ['what is your name ?', ['My name is mini']],
    ['what do you do ?', ['We provide a platform for tech enthusiasts, a wide range of options !']],
    ['who created you ?', ['Tanuja created me using python and NLTK']]
]

chat = Chat(pairs, reflections)
chat.converse()

