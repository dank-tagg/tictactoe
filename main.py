from bke import MLAgent, is_winner, start, load, opponent, RandomAgent, train_and_plot
import random
import os
'''
Wat zijn hyperparameters?

Een hyperparameter is een parameter waarvan de waarde de computer stuurt bij het leerproces.
De andere parameters worden van de training afgeleid.
In deze programma zijn de hyperparameters alpha en epsilon:
    alpha: hoe hoger dit getal, hoe geneigd de agent zal zijn om nieuwe kennis te testen.
    epsilon: hoe hoger dit getal, hoe vaker de agent een nieuwe zet probeert i.p.v. de beste zet. Dus meer ruimte om nieuwe kennis te ontdekken.
'''


class MyAgent(MLAgent):

    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward


random.seed(1)

choices = [
    'Play against friend',
    'Play against good bot',
    'Play against noob bot',
    'Train and validate bot'
]

print('Play a game of tictactoe!')
for i, choice in enumerate(choices):
    print(f'{i}. {choice}')

ans = input('Please select mode:\n')


def play(selection: int):
    os.system('clear')
    if selection == 0:
        # play against friend
        start()

    elif selection == 1:
        # play against good bot
        bot = load('MyAgent_30000')
        players = [bot, None]
        start(player_x=players[0], player_o=players[1])

    elif selection == 2:
        # play against bad bot
        players = [RandomAgent(), None]
        random.shuffle(players)
        start(player_x=players[0], player_o=players[1])

    elif selection == 3:
        # train, validate, plot
        trainings = int(input('How many trainings?\n'))
        train_and_plot(
            agent=load('MyAgent_30000'),
            validation_agent=RandomAgent(),
            iterations=trainings,
            trainings=trainings,
            validations=1000
        )

    else:
        print('Not a valid choice, please check your answer and run again.')
        exit()


play(int(ans))