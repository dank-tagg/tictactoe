from bke import *
import random



class Bot(MLAgent):

    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward


random.seed(1)

bot = Bot()


choices = ['Play against friend', 'Play against good bot', 'Play against noob bot']


for i, choice in enumerate(choices):
    print(f'{i}. {choice}')

ans = input('Please select mode:\n')


def start(selection: int):
    if selection == 0:
        # play against friend
        pass

    elif selection == 1 or selection == 2:
        # play against bot
        pass

    elif selection == 3:
        # train bot
        pass

    else:
        print('Not a valid choice, please check your answer and run again.')
        exit()

start(int(ans))
