import sys


class ProgressBar:
    def __init__(self, goal, progress=0, name=None):
        assert goal != progress
        self.__goal = goal
        self.__progress = progress
        self.__initial_progress = progress
        if name is None:
            self.__progress_name = ''
        else:
            self.__progress_name = ' ' + name + ':'

    def make_step(self, step=1):
        new_progress = self.__progress + step
        if new_progress <= self.__goal:
            self.__progress = new_progress

    def printout(self, inline=False, counter=True, extra=None):
        progress_string = self.__build_bar_string()

        if counter:
            progress_string += self.__progress_name + ' ' + self.__build_details_string()

        if extra is not None:
            progress_string += ' ' + extra

        if inline:
            sys.stdout.write('\r'+progress_string)
            sys.stdout.flush()
        else:
            sys.stdout.write('\r'+progress_string+'\n')
            sys.stdout.flush()
            
    def reset(self, progress=0):
        self.__progress = progress

    def __build_bar_string(self, length=25):
        full_bar_length = length - 3
        progress_bar_length = int(full_bar_length * abs(float(self.__progress)/self.__goal-self.__initial_progress))
        empty_bar_length = full_bar_length - progress_bar_length
        return '[{}>{}]'.format('='*progress_bar_length, (' ' * empty_bar_length))

    def __build_details_string(self):
        return '{}/{}'.format(self.__progress, self.__goal)
