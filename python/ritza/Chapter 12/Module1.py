question = "What is the meaning of Life, the Universe, and Everything?"
answer = 42
print('the value of __name__ is:', __name__)
print('this script executed in:', __name__, 'when you import the module')

if __name__ == '__main__':
    print('''this line only execute in this file/module.
    when we try to import this file as module, this line will not execute.
    because the condition of global namespace "__name__" is not equal to "__main__"''')
    
